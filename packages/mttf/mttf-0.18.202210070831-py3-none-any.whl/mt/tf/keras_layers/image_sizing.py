"""Module involves upsizing and downsizing images in each axis individually using convolutions of residuals."""

import typing as tp

import tensorflow as tf

from .var_regularizer import VarianceRegularizer


__all__ = [
    "Downsize2D",
    "Upsize2D",
    "Upsize2D_V2",
    "Downsize2D_V2",
]


class Downsize2D(tf.keras.layers.Layer):
    """Downsizing along the x-axis and the y-axis using convolutions of residuals.

    Downsizing means halving the width and the height and doubling the number of channels.

    Parameters
    ----------
    input_dim : int
        the dimensionality (number of channels) of each input pixel
    expanded_dim : float, optional
        the dimensionality of the expanded space. If not given, it is set to 4 times the input
        dimensionality.
    kernel_size : int or tuple or list
        An integer or tuple/list of 2 integers, specifying the height and width of the 2D
        convolution window. Can be a single integer to specify the same value for all spatial
        dimensions.
    kernel_initializer : object
        Initializer for the convolutional kernels.
    bias_initializer : object
        Initializer for the convolutional biases.
    kernel_regularizer : object
        Regularizer for the convolutional kernels.
    bias_regularizer : object
        Regularizer for the convolutional biases.
    kernel_constraint: object
        Contraint function applied to the convolutional layer kernels.
    bias_constraint: object
        Contraint function applied to the convolutional layer biases.
    tanh_reg_rate : float
        rate for the tanh activation regularizer. Only valid if negative.
    """

    def __init__(
        self,
        input_dim: int,
        expanded_dim: tp.Optional[int] = None,
        kernel_size: tp.Union[int, tuple, list] = 3,
        kernel_initializer="glorot_uniform",
        bias_initializer="zeros",
        kernel_regularizer=None,
        bias_regularizer=None,
        kernel_constraint=None,
        bias_constraint=None,
        tanh_reg_rate: float = 0.0,
        **kwargs
    ):
        super(Downsize2D, self).__init__(**kwargs)

        self._input_dim = input_dim
        self._expanded_dim = input_dim * 4 if expanded_dim is None else expanded_dim
        self._kernel_size = kernel_size
        self._kernel_initializer = tf.keras.initializers.get(kernel_initializer)
        self._bias_initializer = tf.keras.initializers.get(bias_initializer)
        self._kernel_regularizer = tf.keras.regularizers.get(kernel_regularizer)
        self._bias_regularizer = tf.keras.regularizers.get(bias_regularizer)
        self._kernel_constraint = tf.keras.constraints.get(kernel_constraint)
        self._bias_constraint = tf.keras.constraints.get(bias_constraint)
        self._tanh_reg_rate = tanh_reg_rate

        self.prenorm1_layer = tf.keras.layers.LayerNormalization(name="prenorm1")
        self.expansion_layer = tf.keras.layers.Conv2D(
            self._expanded_dim,
            self._kernel_size,
            padding="same",
            activation="swish",
            kernel_initializer=self._kernel_initializer,
            bias_initializer=self._bias_initializer,
            kernel_regularizer=self._kernel_regularizer,
            bias_regularizer=self._bias_regularizer,
            kernel_constraint=self._kernel_constraint,
            bias_constraint=self._bias_constraint,
            name="expand",
        )
        self.prenorm2_layer = tf.keras.layers.LayerNormalization(name="prenorm2")
        self.projection_layer = tf.keras.layers.Conv2D(
            self._input_dim,
            self._kernel_size,
            padding="same",
            activation="tanh",  # (-1, 1)
            kernel_initializer=self._kernel_initializer,
            bias_initializer=self._bias_initializer,
            kernel_regularizer=self._kernel_regularizer,
            bias_regularizer=self._bias_regularizer,
            kernel_constraint=self._kernel_constraint,
            bias_constraint=self._bias_constraint,
            name="project",
        )
        if tanh_reg_rate < 0:
            self.tanh_reg_layer = VarianceRegularizer(
                rate=tanh_reg_rate, l_axes=[0, 1, 2], name="tanh_reg"
            )
        else:
            self.tanh_reg_layer = None

    def call(self, x, training: bool = False):
        input_shape = tf.shape(x)
        x = tf.reshape(
            x,
            [
                input_shape[0],
                input_shape[1] // 2,
                2,
                input_shape[2] // 2,
                2,
                input_shape[3],
            ],
        )
        x = tf.transpose(x, perm=[0, 1, 3, 2, 4, 5])
        x_avg = tf.reduce_mean(x, axis=[3, 4], keepdims=True)
        x -= x_avg  # residuals
        x_avg = x_avg[:, :, :, 0, 0, :]  # means
        x = tf.reshape(
            x,
            [
                input_shape[0],
                input_shape[1] // 2,
                input_shape[2] // 2,
                input_shape[3] * 4,
            ],
        )
        x = self.prenorm1_layer(x, training=training)
        x = self.expansion_layer(x, training=training)
        x = self.prenorm2_layer(x, training=training)
        x = self.projection_layer(x, training=training)
        if self.tanh_reg_layer is not None:
            x = self.tanh_reg_layer(x, training=training)

        # mix x_avg (0., 1.) and x (-1., 1.)
        x_avg = x_avg * 0.5 + 0.25  # (0.25, 0.75)
        x = x * 0.25  # (-0.25, 0.25)
        x = tf.concat(
            [x_avg + x, x_avg - x], axis=3
        )  # to make the channels homogeneous

        return x

    call.__doc__ = tf.keras.layers.Layer.call.__doc__

    def compute_output_shape(self, input_shape):
        if len(input_shape) != 4:
            raise ValueError(
                "Expected input shape to be (B, H, W, C). Got: {}.".format(input_shape)
            )

        if input_shape[1] % 2 != 0:
            raise ValueError("The height must be even. Got {}.".format(input_shape[1]))

        if input_shape[2] % 2 != 0:
            raise ValueError("The width must be even. Got {}.".format(input_shape[2]))

        if input_shape[3] != self._input_dim:
            raise ValueError(
                "The input dim must be {}. Got {}.".format(
                    self._input_dim, input_shape[3]
                )
            )

        output_shape = (
            input_shape[0],
            input_shape[1] // 2,
            input_shape[2] // 2,
            self._input_dim * 2,
        )

        return output_shape

    compute_output_shape.__doc__ = tf.keras.layers.Layer.compute_output_shape.__doc__

    def get_config(self):
        config = {
            "input_dim": self._input_dim,
            "expanded_dim": self._expanded_dim,
            "kernel_size": self._kernel_size,
            "kernel_initializer": tf.keras.initializers.serialize(
                self._kernel_initializer
            ),
            "bias_initializer": tf.keras.initializers.serialize(self._bias_initializer),
            "kernel_regularizer": tf.keras.regularizers.serialize(
                self._kernel_regularizer
            ),
            "bias_regularizer": tf.keras.regularizers.serialize(self._bias_regularizer),
            "kernel_constraint": tf.keras.constraints.serialize(
                self._kernel_constraint
            ),
            "bias_constraint": tf.keras.constraints.serialize(self._bias_constraint),
            "tanh_reg_rate": self._tanh_reg_rate,
        }
        base_config = super(Downsize2D, self).get_config()
        return dict(list(base_config.items()) + list(config.items()))

    get_config.__doc__ = tf.keras.layers.Layer.get_config.__doc__


class Upsize2D(tf.keras.layers.Layer):
    """Upsizing along the x-axis and the y-axis using convolutions of residuals.

    Upsizing means doubling the width and the height and halving the number of channels.

    Parameters
    ----------
    input_dim : int
        the dimensionality of each input pixel. Must be even.
    expanded_dim : float, optional
        the dimensionality of the expanded space. If not given, it is set to 2 times the input
        dimensionality.
    kernel_size : int or tuple or list
        An integer or tuple/list of 2 integers, specifying the height and width of the 2D
        convolution window. Can be a single integer to specify the same value for all spatial
        dimensions.
    kernel_initializer : object
        Initializer for the convolutional kernels.
    bias_initializer : object
        Initializer for the convolutional biases.
    kernel_regularizer : object
        Regularizer for the convolutional kernels.
    bias_regularizer : object
        Regularizer for the convolutional biases.
    kernel_constraint: object
        Contraint function applied to the convolutional layer kernels.
    bias_constraint: object
        Contraint function applied to the convolutional layer biases.
    """

    def __init__(
        self,
        input_dim: int,
        expanded_dim: tp.Optional[int] = None,
        kernel_size: tp.Union[int, tuple, list] = 3,
        kernel_initializer="glorot_uniform",
        bias_initializer="zeros",
        kernel_regularizer=None,
        bias_regularizer=None,
        kernel_constraint=None,
        bias_constraint=None,
        **kwargs
    ):
        super(Upsize2D, self).__init__(**kwargs)

        if input_dim & 1 != 0:
            raise ValueError(
                "Input dimensionality must be even. Got {}.".format(input_dim)
            )

        self._input_dim = input_dim
        self._expanded_dim = input_dim * 2 if expanded_dim is None else expanded_dim
        self._kernel_size = kernel_size
        self._kernel_initializer = tf.keras.initializers.get(kernel_initializer)
        self._bias_initializer = tf.keras.initializers.get(bias_initializer)
        self._kernel_regularizer = tf.keras.regularizers.get(kernel_regularizer)
        self._bias_regularizer = tf.keras.regularizers.get(bias_regularizer)
        self._kernel_constraint = tf.keras.constraints.get(kernel_constraint)
        self._bias_constraint = tf.keras.constraints.get(bias_constraint)

        self.prenorm1_layer = tf.keras.layers.LayerNormalization(name="prenorm1")
        self.expansion_layer = tf.keras.layers.Conv2D(
            self._expanded_dim,
            self._kernel_size,
            padding="same",
            activation="swish",
            kernel_initializer=self._kernel_initializer,
            bias_initializer=self._bias_initializer,
            kernel_regularizer=self._kernel_regularizer,
            bias_regularizer=self._bias_regularizer,
            kernel_constraint=self._kernel_constraint,
            bias_constraint=self._bias_constraint,
            name="expand",
        )
        self.prenorm2_layer = tf.keras.layers.LayerNormalization(name="prenorm2")
        self.projection_layer = tf.keras.layers.Conv2D(
            self._input_dim * 2,
            self._kernel_size,
            padding="same",
            activation="tanh",  # (-1., 1.)
            kernel_initializer=self._kernel_initializer,
            bias_initializer=self._bias_initializer,
            kernel_regularizer=self._kernel_regularizer,
            bias_regularizer=self._bias_regularizer,
            kernel_constraint=self._kernel_constraint,
            bias_constraint=self._bias_constraint,
            name="project",
        )

    def call(self, x, training: bool = False):
        # unmix x_avg (0., 1.) and x (-1., 1.)
        x_plus = x[:, :, :, : self._input_dim // 2]
        x_minus = x[:, :, :, self._input_dim // 2 :]
        x_avg = x_plus + x_minus - 0.5  # means, (0., 1.)
        x_avg = x_avg[:, :, :, tf.newaxis, tf.newaxis, :]
        x = (x_plus - x_minus) * 2  # residuals, (-1., 1.)

        x = self.prenorm1_layer(x, training=training)
        x = self.expansion_layer(x, training=training)
        x = self.prenorm2_layer(x, training=training)
        x = self.projection_layer(x, training=training)
        input_shape = tf.shape(x)
        x = tf.reshape(
            x,
            [
                input_shape[0],
                input_shape[1],
                input_shape[2],
                2,
                2,
                self._input_dim // 2,
            ],
        )
        x += x_avg
        x = tf.transpose(x, perm=[0, 1, 3, 2, 4, 5])
        x = tf.reshape(
            x,
            [
                input_shape[0],
                input_shape[1] * 2,
                input_shape[2] * 2,
                self._input_dim // 2,
            ],
        )

        return x

    call.__doc__ = tf.keras.layers.Layer.call.__doc__

    def compute_output_shape(self, input_shape):
        if len(input_shape) != 4:
            raise ValueError(
                "Expected input shape to be (B, H, W, C). Got: {}.".format(input_shape)
            )

        if input_shape[3] != self._input_dim:
            raise ValueError(
                "The input dim must be {}. Got {}.".format(
                    self._input_dim, input_shape[3]
                )
            )

        output_shape = (
            input_shape[0],
            input_shape[1] * 2,
            input_shape[2] * 2,
            self._input_dim // 2,
        )
        return output_shape

    compute_output_shape.__doc__ = tf.keras.layers.Layer.compute_output_shape.__doc__

    def get_config(self):
        config = {
            "input_dim": self._input_dim,
            "expanded_dim": self._expanded_dim,
            "kernel_size": self._kernel_size,
            "kernel_initializer": tf.keras.initializers.serialize(
                self._kernel_initializer
            ),
            "bias_initializer": tf.keras.initializers.serialize(self._bias_initializer),
            "kernel_regularizer": tf.keras.regularizers.serialize(
                self._kernel_regularizer
            ),
            "bias_regularizer": tf.keras.regularizers.serialize(self._bias_regularizer),
            "kernel_constraint": tf.keras.constraints.serialize(
                self._kernel_constraint
            ),
            "bias_constraint": tf.keras.constraints.serialize(self._bias_constraint),
        }
        base_config = super(Upsize2D, self).get_config()
        return dict(list(base_config.items()) + list(config.items()))

    get_config.__doc__ = tf.keras.layers.Layer.get_config.__doc__


class Upsize2D_V2(tf.keras.layers.Layer):
    """Upsizing along the x-axis and the y-axis using convolutions of residuals.

    Upsizing means doubling the width and the height and halving the number of channels.

    This version is similar to Upsize2D. However, the pipeline is slightly different. Input at each
    grid cell is a pair of `(avg, res)` images at resolution `(H,W,C)`. The pair is transformed to
    `4*expansion_factor` hidden images and then 4 residual images `(res1, res2, res3, res4)`. Then,
    `avg` is added to the 4 residual images, forming at each cell a 2x2 block of images
    `(avg+res1, avg+res2, avg+res3, avg+res4)`. Finally, the new blocks across the whole tensor
    form a new grid, doubling the height and width. Note that each `avg+resK` image serves as a
    pair of average and residual images in the higher resolution.

    Parameters
    ----------
    input_dim : int
        the dimensionality of each input pixel. Must be even.
    expansion_factor : int
        the coefficient defining the number of hidden images per cell needed.
    kernel_size : int or tuple or list
        An integer or tuple/list of 2 integers, specifying the height and width of the 2D
        convolution window. Can be a single integer to specify the same value for all spatial
        dimensions.
    kernel_initializer : object
        Initializer for the convolutional kernels.
    bias_initializer : object
        Initializer for the convolutional biases.
    kernel_regularizer : object
        Regularizer for the convolutional kernels.
    bias_regularizer : object
        Regularizer for the convolutional biases.
    kernel_constraint: object
        Contraint function applied to the convolutional layer kernels.
    bias_constraint: object
        Contraint function applied to the convolutional layer biases.
    """

    def __init__(
        self,
        input_dim: int,
        expansion_factor: int = 2,
        kernel_size: tp.Union[int, tuple, list] = 3,
        kernel_initializer="glorot_uniform",
        bias_initializer="zeros",
        kernel_regularizer=None,
        bias_regularizer=None,
        kernel_constraint=None,
        bias_constraint=None,
        **kwargs
    ):
        super(Upsize2D_V2, self).__init__(**kwargs)

        if input_dim & 1 != 0:
            raise ValueError(
                "Input dimensionality must be even. Got {}.".format(input_dim)
            )

        self._input_dim = input_dim
        self._expansion_factor = expansion_factor
        self._kernel_size = kernel_size
        self._kernel_initializer = tf.keras.initializers.get(kernel_initializer)
        self._bias_initializer = tf.keras.initializers.get(bias_initializer)
        self._kernel_regularizer = tf.keras.regularizers.get(kernel_regularizer)
        self._bias_regularizer = tf.keras.regularizers.get(bias_regularizer)
        self._kernel_constraint = tf.keras.constraints.get(kernel_constraint)
        self._bias_constraint = tf.keras.constraints.get(bias_constraint)

        self.prenorm1_layer = tf.keras.layers.LayerNormalization(name="prenorm1")
        self.expansion_layer = tf.keras.layers.Conv2D(
            self._input_dim * 2 * expansion_factor,
            self._kernel_size,
            padding="same",
            activation="swish",
            kernel_initializer=self._kernel_initializer,
            bias_initializer=self._bias_initializer,
            kernel_regularizer=self._kernel_regularizer,
            bias_regularizer=self._bias_regularizer,
            kernel_constraint=self._kernel_constraint,
            bias_constraint=self._bias_constraint,
            name="expand",
        )
        self.prenorm2_layer = tf.keras.layers.LayerNormalization(name="prenorm2")
        self.projection_layer = tf.keras.layers.Conv2D(
            self._input_dim * 2,
            self._kernel_size,
            padding="same",
            activation="tanh",  # (-1., 1.)
            kernel_initializer=self._kernel_initializer,
            bias_initializer=self._bias_initializer,
            kernel_regularizer=self._kernel_regularizer,
            bias_regularizer=self._bias_regularizer,
            kernel_constraint=self._kernel_constraint,
            bias_constraint=self._bias_constraint,
            name="project",
        )

    def call(self, x, training: bool = False):
        x_avg = x[:, :, :, : self._input_dim // 2]

        # expand
        x = self.prenorm1_layer(x, training=training)
        x = self.expansion_layer(x, training=training)

        # project
        x = self.prenorm2_layer(x, training=training)
        x = self.projection_layer(x, training=training)

        # reshape
        input_shape = tf.shape(x)
        x = tf.reshape(
            x,
            [
                input_shape[0],
                input_shape[1],
                input_shape[2],
                2,
                2,
                self._input_dim // 2,
            ],
        )

        # add average
        x += x_avg[:, :, :, tf.newaxis, tf.newaxis, :]

        # make a new grid
        x = tf.transpose(x, perm=[0, 1, 3, 2, 4, 5])
        x = tf.reshape(
            x,
            [
                input_shape[0],
                input_shape[1] * 2,
                input_shape[2] * 2,
                self._input_dim // 2,
            ],
        )

        return x

    call.__doc__ = tf.keras.layers.Layer.call.__doc__

    def compute_output_shape(self, input_shape):
        if len(input_shape) != 4:
            raise ValueError(
                "Expected input shape to be (B, H, W, C). Got: {}.".format(input_shape)
            )

        if input_shape[3] != self._input_dim:
            raise ValueError(
                "The input dim must be {}. Got {}.".format(
                    self._input_dim, input_shape[3]
                )
            )

        output_shape = (
            input_shape[0],
            input_shape[1] * 2,
            input_shape[2] * 2,
            self._input_dim // 2,
        )
        return output_shape

    compute_output_shape.__doc__ = tf.keras.layers.Layer.compute_output_shape.__doc__

    def get_config(self):
        config = {
            "input_dim": self._input_dim,
            "expansion_factor": self._expansion_factor,
            "kernel_size": self._kernel_size,
            "kernel_initializer": tf.keras.initializers.serialize(
                self._kernel_initializer
            ),
            "bias_initializer": tf.keras.initializers.serialize(self._bias_initializer),
            "kernel_regularizer": tf.keras.regularizers.serialize(
                self._kernel_regularizer
            ),
            "bias_regularizer": tf.keras.regularizers.serialize(self._bias_regularizer),
            "kernel_constraint": tf.keras.constraints.serialize(
                self._kernel_constraint
            ),
            "bias_constraint": tf.keras.constraints.serialize(self._bias_constraint),
        }
        base_config = super(Upsize2D_V2, self).get_config()
        return dict(list(base_config.items()) + list(config.items()))

    get_config.__doc__ = tf.keras.layers.Layer.get_config.__doc__


class Downsize2D_V2(tf.keras.layers.Layer):
    """Downsizing along the x-axis and the y-axis using convolutions of residuals.

    Downsizing means halving the width and the height and doubling the number of channels.

    This layer is supposed to be nearly an inverse of the Upsize2D_V2 layer.

    Parameters
    ----------
    input_dim : int
        the dimensionality (number of channels) of each input pixel
    expansion_factor : int
        the coefficient defining the number of hidden images per cell needed.
    kernel_size : int or tuple or list
        An integer or tuple/list of 2 integers, specifying the height and width of the 2D
        convolution window. Can be a single integer to specify the same value for all spatial
        dimensions.
    kernel_initializer : object
        Initializer for the convolutional kernels.
    bias_initializer : object
        Initializer for the convolutional biases.
    kernel_regularizer : object
        Regularizer for the convolutional kernels.
    bias_regularizer : object
        Regularizer for the convolutional biases.
    kernel_constraint: object
        Contraint function applied to the convolutional layer kernels.
    bias_constraint: object
        Contraint function applied to the convolutional layer biases.
    """

    def __init__(
        self,
        input_dim: int,
        expansion_factor: int = 2,
        kernel_size: tp.Union[int, tuple, list] = 3,
        kernel_initializer="glorot_uniform",
        bias_initializer="zeros",
        kernel_regularizer=None,
        bias_regularizer=None,
        kernel_constraint=None,
        bias_constraint=None,
        **kwargs
    ):
        super(Downsize2D_V2, self).__init__(**kwargs)

        self._input_dim = input_dim
        self._expansion_factor = expansion_factor
        self._kernel_size = kernel_size
        self._kernel_initializer = tf.keras.initializers.get(kernel_initializer)
        self._bias_initializer = tf.keras.initializers.get(bias_initializer)
        self._kernel_regularizer = tf.keras.regularizers.get(kernel_regularizer)
        self._bias_regularizer = tf.keras.regularizers.get(bias_regularizer)
        self._kernel_constraint = tf.keras.constraints.get(kernel_constraint)
        self._bias_constraint = tf.keras.constraints.get(bias_constraint)

        self.prenorm1_layer = tf.keras.layers.LayerNormalization(name="prenorm1")
        self.expansion_layer = tf.keras.layers.Conv2D(
            self._input_dim * 4 * self._expansion_factor,
            self._kernel_size,
            padding="same",
            activation="swish",
            kernel_initializer=self._kernel_initializer,
            bias_initializer=self._bias_initializer,
            kernel_regularizer=self._kernel_regularizer,
            bias_regularizer=self._bias_regularizer,
            kernel_constraint=self._kernel_constraint,
            bias_constraint=self._bias_constraint,
            name="expand",
        )
        self.prenorm2_layer = tf.keras.layers.LayerNormalization(name="prenorm2")
        self.projection_layer = tf.keras.layers.Conv2D(
            self._input_dim,
            self._kernel_size,
            padding="same",
            activation="sigmoid",  # (0., 1.)
            kernel_initializer=self._kernel_initializer,
            bias_initializer=self._bias_initializer,
            kernel_regularizer=self._kernel_regularizer,
            bias_regularizer=self._bias_regularizer,
            kernel_constraint=self._kernel_constraint,
            bias_constraint=self._bias_constraint,
            name="project",
        )

    def call(self, x, training: bool = False):
        # reshape
        input_shape = tf.shape(x)
        x = tf.reshape(
            x,
            [
                input_shape[0],
                input_shape[1] // 2,
                2,
                input_shape[2] // 2,
                2,
                input_shape[3],
            ],
        )

        # extract average
        x_avg = tf.reduce_mean(x, axis=[2, 4], keepdims=True)
        x -= x_avg  # residuals
        x_avg = x_avg[:, :, 0, :, 0, :]  # means

        # make a new grid
        x = tf.transpose(x, perm=[0, 1, 3, 2, 4, 5])
        x = tf.reshape(
            x,
            [
                input_shape[0],
                input_shape[1] // 2,
                input_shape[2] // 2,
                input_shape[3] * 4,
            ],
        )

        # expand
        x = tf.concat([x_avg, x], axis=3)
        x = self.prenorm1_layer(x, training=training)
        x = self.expansion_layer(x, training=training)

        # project
        x = self.prenorm2_layer(x, training=training)
        x = self.projection_layer(x, training=training)

        # form output
        x = tf.concat([x_avg, x], axis=3)

        return x

    call.__doc__ = tf.keras.layers.Layer.call.__doc__

    def compute_output_shape(self, input_shape):
        if len(input_shape) != 4:
            raise ValueError(
                "Expected input shape to be (B, H, W, C). Got: {}.".format(input_shape)
            )

        if input_shape[1] % 2 != 0:
            raise ValueError("The height must be even. Got {}.".format(input_shape[1]))

        if input_shape[2] % 2 != 0:
            raise ValueError("The width must be even. Got {}.".format(input_shape[2]))

        if input_shape[3] != self._input_dim:
            raise ValueError(
                "The input dim must be {}. Got {}.".format(
                    self._input_dim, input_shape[3]
                )
            )

        output_shape = (
            input_shape[0],
            input_shape[1] // 2,
            input_shape[2] // 2,
            self._input_dim * 2,
        )

        return output_shape

    compute_output_shape.__doc__ = tf.keras.layers.Layer.compute_output_shape.__doc__

    def get_config(self):
        config = {
            "input_dim": self._input_dim,
            "expansion_factor": self._expansion_factor,
            "kernel_size": self._kernel_size,
            "kernel_initializer": tf.keras.initializers.serialize(
                self._kernel_initializer
            ),
            "bias_initializer": tf.keras.initializers.serialize(self._bias_initializer),
            "kernel_regularizer": tf.keras.regularizers.serialize(
                self._kernel_regularizer
            ),
            "bias_regularizer": tf.keras.regularizers.serialize(self._bias_regularizer),
            "kernel_constraint": tf.keras.constraints.serialize(
                self._kernel_constraint
            ),
            "bias_constraint": tf.keras.constraints.serialize(self._bias_constraint),
        }
        base_config = super(Downsize2D_V2, self).get_config()
        return dict(list(base_config.items()) + list(config.items()))

    get_config.__doc__ = tf.keras.layers.Layer.get_config.__doc__
