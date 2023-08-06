=============================
Spherical harmonic transforms
=============================

Spherical harmonic transforms for MW and symmetric MW samplings are created via the
factory function :py:class:`~tensossht.harmonic_transform`. The factory function takes
at least one parameter, ``lmax``.

.. code-block:: python

    from tensossht import harmonic_transform
    transform = harmonic_transform(lmax=8, spin=0, dtype=tf.float64)

Optionally, we can also specify ``lmin``, ``mmin``, and ``mmax``, though little testing
has been done apart from ``mmin=0``. Finally, the spin can be specified either with
``spin=0`` for single-spin transforms, or with ``smin=-1`` and ``smax=1`` for multi-spin
transforms. The latter case is another way to create a transform for real image-space
signals.  for this specific case:

.. code-block:: python

    rtransform = harmonic_transform(lmax=8, mmin=0, spin=0, dtype=tf.float64)

The underlying floating point can be specified via the ``dtype`` keyword argument. It
defaults to ``tf.float32`` (just like any other tensorflow operation). Furthermore, the
image-space sampling scheme can be specified via the ``sampling`` keyword. It defaults
to "MW".

MW Sampling in harmonic-space and image-space
=============================================

The transform works on a fixed basis in harmonic space, fully specifid by ``lmax``,
``lmin``, ``mmax``, ``mmin``. The order of the basis functions can be assessed via the
two properties:

>>> transform.llabels
<tf.Tensor: shape=(64,), dtype=int32, numpy=
array([0, 1, 1, 1, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 3, 3, 4, 4, 4, 4, 4, 4,
       4, 4, 4, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 6, 6, 6, 6, 6, 6, 6, 6,
       6, 6, 6, 6, 6, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7],
      dtype=int32)>

>>> transform.mlabels
<tf.Tensor: shape=(64,), dtype=int32, numpy=
array([ 0, -1,  0,  1, -2, -1,  0,  1,  2, -3, -2, -1,  0,  1,  2,  3, -4,
       -3, -2, -1,  0,  1,  2,  3,  4, -5, -4, -3, -2, -1,  0,  1,  2,  3,
        4,  5, -6, -5, -4, -3, -2, -1,  0,  1,  2,  3,  4,  5,  6, -7, -6,
       -5, -4, -3, -2, -1,  0,  1,  2,  3,  4,  5,  6,  7], dtype=int32)>

The transform for real signals only contains :math:`m \geq 0` components:

>>> rtransform.mlabels
<tf.Tensor: shape=(36,), dtype=int32, numpy=
array([0, 0, 1, 0, 1, 2, 0, 1, 2, 3, 0, 1, 2, 3, 4, 0, 1, 2, 3, 4, 5, 0,
       1, 2, 3, 4, 5, 6, 0, 1, 2, 3, 4, 5, 6, 7], dtype=int32)>

The sampling can be queried for :math:`\theta` and :math:`\phi`:

>>> transform.thetas.numpy().round(3)
array([0.209, 0.628, 1.047, 1.466, 1.885, 2.304, 2.723, 3.142])

>>> transform.phis.numpy().round(3)
array([0.   , 0.419, 0.838, 1.257, 1.676, 2.094, 2.513, 2.932, 3.351,
       3.77 , 4.189, 4.608, 5.027, 5.445, 5.864])

A :math:`\theta` by :math:`\phi` grid is also provided for convenience:

>>> transform.grid.shape
TensorShape([2, 8, 15])

As well as list of :math:`(\theta, \phi)` points:

>>> transform.points.shape
TensorShape([120, 2])

Forward and Inverse Transforms with MW Sampling
===============================================

The transforms themselves are called via
:py:meth:`~tensossht.transforms.mw.MWTransform.forward` and
:py:meth:`~tensossht.transforms.mw.MWTransform.inverse`. For instance, we can create a
set of two random images and transform them back and forth.

.. code-block:: python

    from pytest import approx
    nthetas = transform.lmax
    nphis = 2 * transform.lmax - 1
    assert (int(nthetas), int(nphis)) == transform.sampling.grid.shape[1:]
    images = tf.complex(
        tf.random.uniform((2, nthetas, nphis), dtype=transform.real_dtype),
        tf.random.uniform((2, nthetas, nphis), dtype=transform.real_dtype),
    )
    representable_images = transform.inverse(transform.forward(images))
    assert tf.reduce_any(representable_images != 0)

A first back-and-forth removes from the images components that cannot be represented
with the transform's harmonic-space basis. The second back-and-forth, however, should
yield exactly the same result as the first, except for numerical noise.

.. code-block:: python

    toandfro = transform.inverse(transform.forward(representable_images))
    assert toandfro.numpy() == approx(representable_images.numpy())

Similarly, for a real image-space signal:

.. code-block:: python

    images = tf.random.uniform((2, nthetas, nphis), dtype=transform.real_dtype)
    representable_images = rtransform.inverse(rtransform.forward(images))
    toandfro = rtransform.inverse(rtransform.forward(representable_images))
    assert toandfro.numpy() == approx(representable_images.numpy())

Note that both
:py:meth:`~tensossht.transforms.mw.MWTransform.forward` and
:py:meth:`~tensossht.transforms.mw.MWTransform.inverse` accept
keywords specifying which dimension corresponds to :math:`\theta`,
:math:`\phi` and to the harmonic space coefficients. By default, and to avoid
extra transpose operations, :math:`\theta` and the harmonic-space coefficients
should be stored along the last dimension, and :math:`\phi` on the penultimate.


Forward and Inverse Transforms with MWSS Sampling
=================================================

MW symmetric sampling is a more widespread sampling for 360 images. It requires slightly
more memory and the transforms require slightly more compute. However, both samplings
are quite similar. A transform with MWSS sampling can be created as follows:

.. code-block:: python

    from tensossht import harmonic_transform
    transform = harmonic_transform(lmax=5, spin=0, sampling="MWSS", dtype=tf.float64)

The sampling scheme is available through the transform:

>>> transform.sampling.thetas.numpy().round(3)
array([0.   , 0.628, 1.257, 1.885, 2.513, 3.142])

>>> transform.sampling.phis.numpy().round(3)
array([0.   , 0.628, 1.257, 1.885, 2.513, 3.142, 3.77 , 4.398, 5.027,
       5.655])

Let's create a full set of spherical harmonics with MWSS sampling. For illustration
purposes, the :math:`\phi` and :math:`\theta` dimensions are ordered in a less orthodox
(and less efficient) manner:

.. code-block:: python

    from tensossht import spherical_harmonics
    grid = transform.sampling.grid
    sph = spherical_harmonics(grid[0], grid[1], lmax=transform.lmax)

``sph`` is a three-dimensional array with the first dimension refering to :math:`theta`,
the second to :math:`phi`, and the second dimension to the spherical harmonics with
:math:`l \leq 4`.

>>> sph.shape
TensorShape([6, 10, 25])

In spherical-harmonic space, we expect the set of images to be transformed to the
identity matrix, since each image is a single spherical harmonic:

.. code-block:: python

    from pytest import approx
    sph_space = transform.forward(sph, theta_dim=0, phi_dim=1).numpy()
    assert sph_space == approx(tf.eye(sph.shape[-1]).numpy(), abs=1e-7)

Similarly, for a real image-space signal:

.. code-block:: python

    rsph = tf.math.real(sph)
    rtransform = transform.real
    rsph_space = rtransform.forward(rsph, theta_dim=0, phi_dim=1)
    as_complex = transform.forward(
        tf.complex(rsph, tf.constant(0, rtransform.real_dtype)),
        theta_dim=0,
        phi_dim=1,
    )
    as_complex = tf.transpose(
        tf.boolean_mask(tf.transpose(as_complex), transform.mlabels >= 0)
    )
    assert rsph_space.numpy() == approx(as_complex.numpy())


We can try the same operations for inverse transforms. If we feed the inverse transform
an identity matrix, it should spew out the spherical harmonics under the MWSS sampling
scheme:

.. code-block:: python

    coefficients = tf.eye(
        transform.lmax * transform.lmax, dtype=transform.complex_dtype
    )
    real_space = transform.inverse(coefficients, phi_dim=1, theta_dim=0)
    assert real_space.numpy() == approx(sph.numpy(), abs=1e-6)


Similarly for real-space signals:

.. code-block:: python

    coefficients = (
        tf.eye(rtransform.labels.shape[1], dtype=rtransform.complex_dtype)
        * tf.cast(
            tf.where(rtransform.mlabels == 0, 1.0, 0.5),
            dtype=rtransform.complex_dtype
        )
    )
    real_space = rtransform.inverse(coefficients, phi_dim=1, theta_dim=0)
    rsph = spherical_harmonics(grid[0], grid[1], lmax=rtransform.lmax, mmin=0)
    assert real_space.numpy() == approx(tf.math.real(rsph).numpy(), abs=1e-5, rel=1e-5)

API
===

.. autoclass:: tensossht.transforms.transforms.HarmonicTransform
    :members:
    :undoc-members:

    .. method:: forward(images: tf.Tensor, theta_dim: int = -2, phi_dim: int = -1, coeff_dim: int = -1) -> tf.Tensor

        Transform from image to harmonic space. The image axes ``theta_dim`` and
        ``phi_dim``, as well as the harmonic-coefficient axis ``coeff_dim`` can be
        specified on input. They default to the innermost axes (.i.e. :math:`\phi` is
        contiguous in memory).

    .. method:: inverse(images: tf.Tensor, theta_dim: int = -2, phi_dim: int = -1, coeff_dim: int = -1) -> tf.Tensor

        Transform from harmonic to image space. The image axes ``theta_dim`` and
        ``phi_dim``, as well as the harmonic-coefficient axis ``coeff_dim`` can be
        specified on input. They default to the innermost axes (.i.e. :math:`\phi` is
        contiguous in memory).

.. autoclass:: tensossht.transforms.forward.ForwardTransform
    :members: __call__
    :undoc-members:


.. autoclass:: tensossht.transforms.inverse.InverseTransform
    :members: __call__
    :undoc-members:
