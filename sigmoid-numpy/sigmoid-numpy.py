import numpy as np

def sigmoid(x):
    x = np.asarray(x, dtype=np.float64)
    
    # create masks for positive and negative entries
    pos_mask = x >= 0
    neg_mask = ~pos_mask
    
    z = np.empty_like(x)
    
    # x >= 0 → 1 / (1 + exp(-x))
    z[pos_mask] = 1 / (1 + np.exp(-x[pos_mask]))
    
    # x < 0 → exp(x) / (1 + exp(x)) -> to avoid issues with neg exp
    exp_x = np.exp(x[neg_mask])
    z[neg_mask] = exp_x / (1 + exp_x)
    
    return z
