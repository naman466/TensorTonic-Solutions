import numpy as np

def positional_encoding(seq_length: int, d_model: int) -> np.ndarray:
    """
    Generate sinusoidal positional encodings.
    """
    positions = np.arange(seq_length)[:, np.newaxis]        
    dims = np.arange(d_model)[np.newaxis, :]               

    angle_rates = 1 / np.power(10000, (2 * (dims // 2)) / d_model)

    angle_rads = positions * angle_rates                  

    angle_rads[:, 0::2] = np.sin(angle_rads[:, 0::2])
    angle_rads[:, 1::2] = np.cos(angle_rads[:, 1::2])

    return angle_rads