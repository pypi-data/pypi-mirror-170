Wigner Transform Layers
=======================

The forward and inverse transforms can be instanciated using the factory function
:py:func:`~tensossh.layers.wigner.wigner_layer` in :py:mod:`tensossht.layers`.
The implementation follows [McEwen2015]_ and is implemented via Fourier
transforms and a spin harmonic transforms.

.. code-block:: python

    from tensossht.layers import wigner_layer
    from tensossht.sampling import MW

    lmax, nspins = 7, 5
    sampling = MW(lmax)
    inputs = tf.keras.layers.Input((*sampling.shape, nspins), dtype=tf.complex128)
    forward = wigner_layer(is_forward=True, sampling="mw", dtype=tf.complex128)(inputs)

We can verify that the transform works correctly by applying it to the Wigner functions
themselves. First, we compute all the Wigner functions for the current harmonic-space
sampling.

.. code-block:: python

    from tensossht.sampling import harmonic_sampling_scheme
    from tensossht.specialfunctions import kostelec

    hsampling = harmonic_sampling_scheme(
        lmax=lmax, smin=-(nspins // 2), smax=nspins // 2, compact_spin=False
    )

    wignerd = tf.reshape(
        tf.cast(
            kostelec.wignerd(labels=hsampling.labels, beta=sampling.thetas),
            tf.complex128
        ),
        (-1, 1, 1, hsampling.ncoeffs)
    )
    gamma = MW(hsampling.smax + 1).phis
    gamma_exp = tf.exp(
        tf.complex(
            tf.constant(0, tf.float64),
            -gamma[None, None, :, None] * tf.cast(hsampling.slabels, tf.float64)
        )
    )
    phi_exp = tf.exp(
        tf.complex(
            tf.constant(0, tf.float64),
            -sampling.phis[None, :, None, None] * tf.cast(hsampling.mlabels, tf.float64)
        )
    )

    basis = tf.transpose(
        phi_exp * wignerd * gamma_exp
        * tf.cast(
            tf.cast(2 * hsampling.llabels + 1, dtype=tf.float64) / (8 * np.pi * np.pi),
            dtype=tf.complex128
        ),
        perm=[3, 0, 1, 2],
        conjugate=True
    )

Then, we create and apply the model:

.. code-block:: python

    model = tf.keras.models.Model(inputs=inputs, outputs=forward)
    y = model(basis)

We can test that the result is almost identity, expect where the triplet `(l, m, s)` is
not valid:

.. code-block:: python

    from pytest import approx

    for i, (l, m, s) in enumerate(hsampling.labels.numpy().T):
        if np.abs(m) > l or np.abs(s) > l:
            continue
            assert y[i].numpy() == approx(0)
        else:
            expected = tf.one_hot(i, hsampling.ncoeffs).numpy()
            assert y[i].numpy().flatten() == approx(expected, abs=1e-6)


The inverse layer can be instantiated and a model created as follows:

.. code-block:: python

    inv_inputs = tf.keras.layers.Input(y.shape[1:], dtype=tf.complex128)
    inverse = wigner_layer(is_forward=False, sampling="mw", dtype=tf.complex128)(
        inv_inputs
    )
    inv_model = tf.keras.models.Model(inputs=inv_inputs, outputs=inverse)
    inv_y = inv_model(y)

    assert inv_y.numpy() == approx(basis.numpy(), abs=1e-8, rel=1e-6)


Once again, the models can be saved and reloaded. Lets recreate the forward transform:

.. code-block:: python

    from tempfile import TemporaryDirectory
    from pathlib import Path

    with TemporaryDirectory() as directory:
        model.save(str(Path(directory) / "model"))
        reloaded = tf.keras.models.load_model(str(Path(directory) / "model"))

    yreloaded = reloaded(basis)
    assert y.numpy() == approx(yreloaded.numpy())

And the inverse transform:

.. code-block:: python

    with TemporaryDirectory() as directory:
        inv_model.save(str(Path(directory) / "inv_model"))
        inv_reloaded = tf.keras.models.load_model(str(Path(directory) / "inv_model"))

    inv_yreloaded = inv_reloaded(y)
    assert inv_y.numpy() == approx(inv_yreloaded.numpy())

Fourier Transform Layer
=======================

The Fourier transform performs two operations. It shifts the axis over which to perform
the FFT to last, and then it performs the forward or inverse FFT itself. Currently, only
complex transforms are implemented.

.. code-block:: python

    from tensossht.layers.wigner import FourierLayer

    shape = (5, 3)
    inputs = tf.keras.layers.Input(shape, dtype=tf.complex128)
    fft = FourierLayer(is_forward=True, axis=-2)(inputs)

The axis can be given relative to the last dimension, as a negative index. If given as a
positive index, one should not forget the batch dimension. We can verify the transform
operates as expected:

.. code-block:: python

    from pytest import approx

    model = tf.keras.models.Model(inputs=inputs, outputs=fft)
    data = tf.cast(tf.random.uniform((2, *shape)), dtype=tf.complex128)
    transformed = model(data)

    exponent = tf.cast(
        tf.range(shape[0])[:, None] * tf.range(shape[0])[None],
        tf.complex128
    ) * complex(0, -2 * np.pi / shape[0])
    handrolled = tf.reduce_sum(
        tf.transpose(data, perm=[0, 2, 1])[:, :, :, None] * tf.exp(exponent), axis=-2
    )

    assert transformed.numpy().round(4) == approx(handrolled.numpy().round(4))

The Fourier layer also accepts `is_real` as an argument, in which case it expects or
creates real-valued image-space signals. In that case, the inverse transform cannot
guess the size of the image-space signals from the size of the Fourier-space signals.
Hence, the layer also accepts a parameter `is_odd_spin` for signals where the length in
real space is odd.

.. [McEwen2015]
    McEwen JD, Büttner M, Leistedt B, Peiris HV, Wiaux Y. A 
    "A novel sampling theorem on the rotation group"
    IEEE Signal Processing Letters 22.12 (2015): 2425-2429
