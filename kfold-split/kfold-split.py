import numpy as np

def kfold_split(N, k, shuffle=True, rng=None):
    """
    Returns: list of length k with tuples (train_idx, val_idx)
    """
    idx = np.arange(N)

    if shuffle:
        if rng is not None:
            idx = rng.permutation(idx)
        else:
            np.random.shuffle(idx)

    fold_sizes = np.full(k, N // k, dtype=int)
    fold_sizes[: N % k] += 1  # first folds get the extra samples

    splits = []
    start = 0

    for size in fold_sizes:
        val_idx = idx[start:start + size]
        train_idx = np.concatenate((idx[:start], idx[start + size:]))
        splits.append((train_idx, val_idx))
        start += size

    return splits







