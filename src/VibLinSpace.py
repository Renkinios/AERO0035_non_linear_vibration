import numpy as np
from scipy.linalg import eigh

def get_mode_freq_lin(M,K):
    omega_squared, modes = eigh(K, M)
    freq = np.sqrt(omega_squared) / (2 * np.pi)
    idx = np.argsort(freq)
    freq = freq[idx]
    modes = modes[:, idx]
    return freq, modes
