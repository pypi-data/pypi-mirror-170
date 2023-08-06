Forward Harmonic Transoform Layers
==================================

Forward Single Spin Layer
-------------------------

The forward layer is parameterized according to the image-space sampling, whether the
image is real or complex, and on the underlying floating point size. The order of the
dimensions can also be given as input.

The layers can be created using the so-called *functional* style. :math:`l_\mathrm{max}` is
determined during the functional call from the size of the input images. For instance:

.. code-block:: python

    from tensossht import ForwardLayer
    from tensossht.sampling import MW

    lmax = 10
    dtype = tf.float64
    sampling = MW(lmax)
    inputs = tf.keras.layers.Input(sampling.shape, dtype=dtype)
    ssht = ForwardLayer(is_real=True, sampling=sampling, dtype=dtype)(inputs)

The layers also accept the `spin` and the indices of the :math:`\theta`, :math:`\phi`,
and coeffficient dimensions as input. The `spin` is zero by default. Only one spin is
computed at a time. We can verify the layer works by creating a model from this single
layer and calling it on the spherical harmonics:

.. code-block:: python

    from pytest import approx
    from tensossht import spherical_harmonics, legendre_labels

    model = tf.keras.models.Model(inputs=inputs, outputs=ssht)

    labels = legendre_labels(lmax, mmin=0)
    sph = tf.math.real(
        spherical_harmonics(sampling.grid[0], sampling.grid[1], labels=labels)
    )
    y = model(tf.transpose(sph, [2, 0, 1]))
    expected = tf.eye(sph.shape[-1], dtype=tf.int32) / tf.where(labels[1] == 0, 1, 2)
    assert y.numpy() == approx(expected.numpy(), abs=1e-7)

The model can be saved and reloaded, as illustrated here:

.. code-block:: python

    from tempfile import TemporaryDirectory
    from pathlib import Path

    with TemporaryDirectory() as directory:
        model.save(str(Path(directory) / "model"))
        reloaded = tf.keras.models.load_model(str(Path(directory) / "model"))

We can verify the reloaded model works by applying it to the spherical harmonics:

.. code-block:: python

    y = reloaded(tf.transpose(sph, [2, 0, 1]))
    assert y.numpy() == approx(expected.numpy(), abs=1e-7)


Forward Multi-Spin Layer
------------------------

The multi-spin layer expects as input a stack of images. The size of the stack should be
odd. It determines the range of spins over which the transform will proceed:

.. code-block:: python

    from tensossht import ForwardSpinLayer
    from tensossht.sampling import MW

    lmax, nspins = 4, 5
    dtype = tf.complex128
    sampling = MW(lmax)
    inputs = tf.keras.layers.Input((nspins, *sampling.shape), dtype=dtype)
    ssht = ForwardSpinLayer(sampling=sampling, dtype=dtype)(inputs)

The layer accepts the same parameters as :py:class:`~tensossht.layers.ForwardLayer` as
well as the index of the spin axis in the images and the index of the spin axis for the
harmonic-coefficients. We can verify the layer works by creating a model from this
single layer and calling it on the spin spherical harmonics:


.. code-block:: python

    from pytest import approx
    from tensossht.specialfunctions.naive import spin_spherical_harmonics
    from tensossht.sampling import MW

    model = tf.keras.models.Model(inputs=inputs, outputs=ssht)

    grid = MW(lmax, dtype=tf.math.real(tf.zeros(0, dtype)).dtype).grid
    sph = spin_spherical_harmonics(
        grid[0],
        grid[1],
        lmax=lmax,
        mmin=None,
        smin=-(nspins - 1) // 2,
        smax=(nspins - 1) // 2,
        compact_spin=False
    )
    sph = tf.reshape(sph, (sph.shape[0], sph.shape[1], nspins, -1))
    y = model(tf.transpose(sph, [3, 2, 0, 1])).numpy()

Since spins are represented by a separate dimension, some rows in the tensor are empty.
They correspond for instance to ``spin == 1`` and ``l == 0``:

.. code-block:: python

    for s in tf.range(-(nspins - 1) // 2, (nspins + 1) // 2):
        expected = np.eye(y.shape[-1])
        expected[: s * s, : s * s] = 0
        assert y[:, s + (nspins - 1) // 2] == approx(expected, abs=1e-6, rel=1e-6)

Once again, the model can be saved and reloaded:

.. code-block:: python

    from tempfile import TemporaryDirectory
    from pathlib import Path

    with TemporaryDirectory() as directory:
        model.save(str(Path(directory) / "model"))
        reloaded = tf.keras.models.load_model(str(Path(directory) / "model"))

    yreloaded = reloaded(tf.transpose(sph, [3, 2, 0, 1])).numpy()
    assert yreloaded == approx(y)

Inverse Harmonic Transform Layers
=================================

Inverse Single Spin Layer
-------------------------

The inverser layer works in a similar fashion to the forward single-spin layer. It also
takse the same arguments as input:

.. code-block:: python

    from pytest import approx
    from tensossht import spherical_harmonics, legendre_labels, InverseLayer
    from tensossht.sampling import MW, image_sampling_scheme

    lmax = 10
    rdtype, cdtype = tf.float64, tf.complex128
    sampling = MW(lmax)
    inputs = tf.keras.layers.Input(lmax * lmax, dtype=cdtype)
    ssht = InverseLayer(is_real=False, sampling=sampling, dtype=cdtype)(inputs)
    model = tf.keras.models.Model(inputs=inputs, outputs=ssht)

    labels = legendre_labels(lmax, mmin=-lmax)
    grid = image_sampling_scheme(sampling).value(lmax, dtype=rdtype).grid
    sph = tf.transpose(spherical_harmonics(grid[0], grid[1], labels=labels), [2, 0, 1])

    coeffs = tf.eye(lmax * lmax, dtype=cdtype)
    model = tf.keras.models.Model(inputs=inputs, outputs=ssht)
    y = model(coeffs)
    assert y.dtype == cdtype
    assert y.numpy() == approx(sph.numpy(), abs=1e-6)

Once again, the model can be saved and reloaded:

.. code-block:: python

    from tempfile import TemporaryDirectory
    from pathlib import Path

    with TemporaryDirectory() as directory:
        model.save(str(Path(directory) / "model"))
        reloaded = tf.keras.models.load_model(str(Path(directory) / "model"))

    y = reloaded(coeffs)
    assert y.dtype == cdtype
    assert y.numpy() == approx(sph.numpy(), abs=1e-6)

Inverse Multi-Spin Layer
------------------------

Setting up a multi-spin layer should offer no surprises:

.. code-block:: python

    from pytest import approx
    from tensossht import InverseSpinLayer
    from tensossht.sampling import MW
    from tensossht.specialfunctions.naive import spin_spherical_harmonics

    lmax, nspins = 4, 5
    dtype = tf.complex128
    sampling = MW(lmax)
    inputs = tf.keras.layers.Input((nspins, lmax * lmax), dtype=dtype)
    ssht = InverseSpinLayer(sampling=sampling, dtype=dtype)(inputs)
    
    model = tf.keras.models.Model(inputs=inputs, outputs=ssht)

    grid = MW(lmax, dtype=tf.math.real(tf.zeros(0, dtype)).dtype).grid
    coeffs = tf.reshape(
        tf.eye(nspins * lmax * lmax, dtype=dtype),
        (nspins * lmax * lmax, nspins, lmax * lmax),
    )

    y = model(coeffs)
    y = tf.reshape(y, (nspins, lmax * lmax, *y.shape[1:]))

    for sin in range(-(nspins // 2), nspins // 2 + 1):
        for sout in range(-(nspins // 2), nspins // 2 + 1):
            element = y[sin + nspins // 2, :, sout + nspins // 2].numpy()
            if sin != sout:
                assert element == approx(0)
            else:
                sph = spin_spherical_harmonics(
                    grid[0],
                    grid[1],
                    lmax=lmax,
                    mmin=-lmax,
                    smin=sin,
                    smax=sin,
                    compact_spin=False,
                )
                sph = tf.transpose(sph, [2, 0, 1]).numpy()
                assert element == approx(sph, rel=1e-6, abs=1e-6)

Once again, the model can be saved and reloaded:

.. code-block:: python

    from tempfile import TemporaryDirectory
    from pathlib import Path

    with TemporaryDirectory() as directory:
        model.save(str(Path(directory) / "model"))
        reloaded = tf.keras.models.load_model(str(Path(directory) / "model"))

    assert reloaded(coeffs).numpy() == approx(model(coeffs).numpy())
