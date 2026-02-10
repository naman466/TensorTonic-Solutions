import numpy as np

def roc_curve(y_true, y_score):
    """
    Compute ROC curve from binary labels and scores.
    """
    y_true = np.asarray(y_true)
    y_score = np.asarray(y_score)

    order = np.argsort(-y_score)
    y_true = y_true[order]
    y_score = y_score[order]

    # total pos and neg 
    P = np.sum(y_true)
    N = len(y_true) - P

    tps = np.cumsum(y_true)
    fps = np.cumsum(1 - y_true)

    # fidn score change indices
    distinct_value_indices = np.where(np.diff(y_score))[0]
    threshold_idxs = np.r_[distinct_value_indices, len(y_score) - 1]

    # find tp and fp at threshold
    tps = tps[threshold_idxs]
    fps = fps[threshold_idxs]
    thresholds = y_score[threshold_idxs]

    # find rates
    tpr = tps / P if P > 0 else np.zeros_like(tps, dtype=float)
    fpr = fps / N if N > 0 else np.zeros_like(fps, dtype=float)

    tpr = np.r_[0.0, tpr]
    fpr = np.r_[0.0, fpr]
    thresholds = np.r_[np.inf, thresholds]

    return fpr, tpr, thresholds