***************
Theta Extension
***************

This module provides functionality to extends functions over theta from :math:`[0,
\pi[`  to :math:`[0, 2pi[`.

This is one of the operations for the foward harmonic transforms. The details differ
depending on whether the image-space signal is real or complex, as well as on its
image-space sampling and on the spin number of the transform.

This module only exports a general function
:py:func:`~tensossht.theta_extension.theta_extension`. However, tensorflow functions are
available for each case. They are not exported since these functions do not perform
error checking.

The main function accepts four kind of signals:

#. complex image-space signals with MW sampling
#. complex image-space signals with MWSS sampling
#. real image-space signals with MW sampling
#. real image-space signals with MWSS sampling

Lets first create a complex MW signal:

>>> from tensossht.transforms.theta_extension import theta_extension
>>> from tensossht.sampling import ImageAxes
>>> lmax = 4
>>> functions = tf.range(2 * lmax - 1)[None] * tf.range(lmax)[:, None]
>>> functions
<tf.Tensor: shape=(4, 7), dtype=int32, numpy=
array([[ 0,  0,  0,  0,  0,  0,  0],
       [ 0,  1,  2,  3,  4,  5,  6],
       [ 0,  2,  4,  6,  8, 10, 12],
       [ 0,  3,  6,  9, 12, 15, 18]], dtype=int32)>

>>> theta_extension(functions, ImageAxes(theta=0, phi=1))
<tf.Tensor: shape=(7, 7), dtype=int32, numpy=
array([[  0,   0,   0,   0,   0,   0,   0],
       [  0,   1,   2,   3,   4,   5,   6],
       [  0,   2,   4,   6,   8,  10,  12],
       [  0,   3,   6,   9,  12,  15,  18],
       [  0,  -2,   4,  -6,  -8,  10, -12],
       [  0,  -1,   2,  -3,  -4,   5,  -6],
       [  0,   0,   0,   0,   0,   0,   0]], dtype=int32)>

A complex MWSS signal would be processed as follows:

>>> functions = tf.range(2 * lmax)[None] * tf.range(lmax + 1)[:, None]
>>> theta_extension(functions, ImageAxes(theta=0, phi=1), sampling="mwss")
<tf.Tensor: shape=(8, 8), dtype=int32, numpy=
array([[  0,   0,   0,   0,   0,   0,   0,   0],
       [  0,   1,   2,   3,   4,   5,   6,   7],
       [  0,   2,   4,   6,   8,  10,  12,  14],
       [  0,   3,   6,   9,  12,  15,  18,  21],
       [  0,   4,   8,  12,  16,  20,  24,  28],
       [  0,  -3,   6,  -9,  12, -15,  18, -21],
       [  0,  -2,   4,  -6,   8, -10,  12, -14],
       [  0,  -1,   2,  -3,   4,  -5,   6,  -7]], dtype=int32)>

A real MW signal is extended as follows:

>>> functions = tf.range(lmax)[None] * tf.range(lmax)[:, None]
>>> axes = ImageAxes(theta=0, phi=1)
>>> theta_extension(functions, axes, sampling="mw", is_complex=False)
<tf.Tensor: shape=(7, 4), dtype=int32, numpy=
array([[ 0,  0,  0,  0],
       [ 0,  1,  2,  3],
       [ 0,  2,  4,  6],
       [ 0,  3,  6,  9],
       [ 0, -2,  4, -6],
       [ 0, -1,  2, -3],
       [ 0,  0,  0,  0]], dtype=int32)>


A real MWSS signal is extended as follows:

>>> functions = tf.range(lmax + 1)[None] * tf.range(lmax + 1)[:, None]
>>> theta_extension(functions, axes, sampling="mwss", is_complex=False)
<tf.Tensor: shape=(8, 5), dtype=int32, numpy=
array([[ 0,  0,  0,  0,  0],
       [ 0,  1,  2,  3,  4],
       [ 0,  2,  4,  6,  8],
       [ 0,  3,  6,  9, 12],
       [ 0,  4,  8, 12, 16],
       [ 0, -3,  6, -9, 12],
       [ 0, -2,  4, -6,  8],
       [ 0, -1,  2, -3,  4]], dtype=int32)>


Theta extension for spin simply adds an extra sign factor depending on the parity of the
spin. We can repeat the extension for complex MW signals and check the parity
explicitly.

.. code-block:: python

    from pytest import approx
    nspin = 4
    functions = (
        tf.range(2 * lmax - 1)[None, None, :]
        * tf.range(lmax)[None, :, None]
        * tf.ones((nspin, 1, 1), dtype=tf.int32)
    )
    spinless = theta_extension(
        functions[0], ImageAxes(theta=0, phi=1), sampling="mw", is_complex=True
    )
    spin = theta_extension(
        functions, ImageAxes(theta=1, phi=2, spin=0), sampling="mw", is_complex=True
    )
    assert spin[0].numpy() == approx(spinless.numpy())
    assert spin[1, :lmax].numpy() == approx(spinless[:lmax].numpy())
    assert spin[1, lmax:].numpy() == approx(-spinless[lmax:].numpy())
    assert spin[2].numpy() == approx(spinless.numpy())
    assert spin[3, :lmax].numpy() == approx(spinless[:lmax].numpy())
    assert spin[3, lmax:].numpy() == approx(-spinless[lmax:].numpy())
