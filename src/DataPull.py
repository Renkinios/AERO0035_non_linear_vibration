import scipy.io
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


def extract_data(data_set) :
    # Charger le fichier .mat
    mat = scipy.io.loadmat(data_set)
    key_variables = {name: data for name, data in mat.items() if not name.startswith("__")}
    return key_variables

def extract_data_NI2D(data_set):
    # Charger le fichier CSV avec l'en-tête, en ignorant les colonnes vides
    data = pd.read_csv(data_set, skiprows=1, names=["Frequency (Hz)", "Amplitude (m)"])
    return data

def extract_particular_data(data_set, start_freq, end_freq = 0) :
    start_freq_create  = data_set["ext_force"][0][2][0]      # Hz
    sweep_rate_freq    = (data_set["ext_force"][0][4][0])/60 # s
    freq               = start_freq_create + sweep_rate_freq * data_set['t'][0]
    if end_freq != 0 :
        idx    = (freq >= start_freq) & (freq <= end_freq)
        
    else : 
        idx    = (freq >= start_freq)
    x1     = data_set['x'][0][idx]
    x2     = data_set['x'][1][idx]
    v1     = data_set['xd'][0][idx]
    v2     = data_set['xd'][1][idx]
    a1     = data_set['xdd'][0][idx]
    a2     = data_set['xdd'][1][idx]
    force1 = data_set['pex'][0][idx]
    force2 = data_set['pex'][1][idx]
    rel_d  = x2 - x1
    fext = np.array([force1, force2])
    q    = np.array([x1, x2])
    qd   = np.array([v1, v2])
    qdd  = np.array([a1, a2]) 
    # fext = np.concatenate((force1, force2))
    # q = np.concatenate((x1, x2))
    # qd = np.concatenate((v1, v2))
    # qdd = np.concatenate((a1, a2))
    return fext, q, qd, qdd, rel_d