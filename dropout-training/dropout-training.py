import numpy as np

def dropout(x, p=0.5, rng=None):
    """
    Apply dropout to input x with probability p.
    Return (output, dropout_pattern).
    """
    x = np.asarray(x)
    if not 0.0 <= p < 1.0:
        raise ValueError("p must satisfy 0.0 <= p < 1.0")

    if rng is None:
        rng = np.random

    if p == 0.0:
        pattern = np.ones_like(x)
        return x.copy(), pattern

    # use < (1 - p)
    keep = rng.random(x.shape) < (1.0 - p)

    scale = 1.0 / (1.0 - p)
    pattern = keep.astype(x.dtype) * scale

    output = x * pattern

    return output, pattern
