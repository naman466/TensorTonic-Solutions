import numpy as np

def maxpool_forward(X, pool_size, stride):
    """
    Compute the forward pass of 2D max pooling.
    """
    X = np.array(X)
    H, W = X.shape

    H_out = (H - pool_size) // stride + 1
    W_out = (W - pool_size) // stride + 1

    # shape of windowed view
    shape = (H_out, W_out, pool_size, pool_size)

    # strides for sliding window
    strides = (
        X.strides[0] * stride,
        X.strides[1] * stride,
        X.strides[0],
        X.strides[1],
    )

    windows = np.lib.stride_tricks.as_strided(X, shape=shape, strides=strides)

    # Ttke max over pool, window
    out = windows.max(axis=(2, 3))

    return out.tolist()
