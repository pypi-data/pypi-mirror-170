Packing and Unpacking Layers
============================

By default, the transforms work with coefficients layed out in compressed form along a
single dimension, e.g. :math:`(l, m) \rightarrow (0, 0), (1, 0), (1, 1), (2, 0), \dots`.
However, some users would rather work with a more convernient two dimension :math:`(l,
m)` matrix, even though it is less memory efficient. :py:mod:`tensossht` provides a
packing layer :py:class:`~tensossht.layers.PackingLayer` and an unpacking layer
:py:class:`~tensossht.layers.UnpackingLayer` to mediate between the two formats. The
packing layer should be used *before* the inverse transform layer. The unpacking layer
should be used *after* the forward transform layer.

To illustrate their use, we will first pack the labels :math:`(l, m)` themselves. And
then unpack them in due course.

Using a fill-value of 100, the unpacked :math:`(l, m)` labels can be constructed as:

.. code-block:: python

    lmax, mmin = 5, 0
    coefficients = tf.constant(
        [
            [
                [order if order >= abs(m) else 100 for m in range(mmin, lmax)]
                for order in range(lmax)
            ],
            [
                [m if order >= abs(m) else 100 for m in range(mmin, lmax)]
                for order in range(lmax)
            ],
        ]
    )

>>> coefficients
<tf.Tensor: shape=(2, 5, 5), dtype=int32, numpy=
array([[[  0, 100, 100, 100, 100],
        [  1,   1, 100, 100, 100],
        [  2,   2,   2, 100, 100],
        [  3,   3,   3,   3, 100],
        [  4,   4,   4,   4,   4]],
<BLANKLINE>
       [[  0, 100, 100, 100, 100],
        [  0,   1, 100, 100, 100],
        [  0,   1,   2, 100, 100],
        [  0,   1,   2,   3, 100],
        [  0,   1,   2,   3,   4]]], dtype=int32)>


The first 2-matrix contains :math:`l`, and the second contains :math:`m`.

We now create the layer and attendant model:

.. code-block:: python

    from tensossht import PackingLayer

    inputs = tf.keras.layers.Input(coefficients.shape[1:], dtype=coefficients.dtype)
    packing = PackingLayer(is_real=True, dtype=coefficients.dtype)(inputs)
    packing_model = tf.keras.models.Model(inputs=inputs, outputs=packing)

We can verify that applying the layer to the coefficients :math:`(l, m)` returns the
packed labels computed by :py:func:`~tensossht.specialfunctions.legendre_labels`:

.. code-block:: python

    from pytest import approx
    from tensossht import legendre_labels

    y = packing_model(coefficients)
    labels = legendre_labels(lmax=lmax, mmin=mmin)
    assert y.shape == (2, ((lmax * (lmax + 1)) // 2))
    assert y.numpy() == approx(labels.numpy())

The unpacking layer :py:class:`~tensossht.layers.Unpacking` takes the journeyback from
the :math:`(l, m)` matrix to the compressed coefficient form:

.. code-block:: python

    from tensossht import UnpackingLayer
    inputs = tf.keras.layers.Input(labels.shape[1:], dtype=labels.dtype)
    unpacking = UnpackingLayer(
        is_real=True, dtype=labels.dtype, fill_value=100, l_dim=-2, m_dim=-1
    )(inputs)
    unpacking_model = tf.keras.models.Model(inputs=inputs, outputs=unpacking)

    y = unpacking_model(labels)
    assert y.shape == (2, lmax, lmax - mmin)
    assert y.numpy() == approx(np.array(coefficients))


Both layers can be serialized:

.. code-block:: python

    from pathlib import Path
    from tempfile import TemporaryDirectory

    with TemporaryDirectory() as directory:
        packing_model.save(str(Path(directory) / "packing"))
        pckmod = tf.keras.models.load_model(str(Path(directory) / "packing"))

        unpacking_model.save(str(Path(directory) / "unpacking"))
        upckmod = tf.keras.models.load_model(str(Path(directory) / "unpacking"))

    assert pckmod(coefficients).numpy() == approx(labels.numpy())
    assert upckmod(labels).numpy() == approx(coefficients.numpy())
