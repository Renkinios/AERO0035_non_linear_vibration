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