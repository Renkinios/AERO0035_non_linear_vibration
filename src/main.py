import numpy as np
import VibLinSpace as VLS
import VizTools as VT
import DataPull as DP
import matplotlib.pyplot as plt
import characteristics_functions as CF
import identification_function as IF

# matrice of the linear system at the begining 
M = np.array([[1, 0], [0, 1]])
C = np.array([[3, -1], [-1, 3]])
K = 10**4 * np.array([[2, -1], [-1, 2]])
system = {'M': M, 'C': C, 'K': K}

# freq, mode = VLS.get_mode_freq_lin(M, K)
# First see the up and down about the sin sweep
lab_linear_sin_sweep_40N_up             = DP.extract_data("../data/first_lab/group3_test1_1.mat")
# lab_linear_sin_sweep_40N_down           = DP.extract_data("../data/first_lab/group3_test1_2.mat")

# # Second experimental see the differnce with the amplitude of the force
# lab_linear_sin_sweep_50N_up             =  DP.extract_data("../data/sec_lab/group3_test2_1.mat")
# lab_linear_sin_sweep_30N_up             =  DP.extract_data("../data/sec_lab/group3_test2_3.mat")

# # For the comapraison with the experimental data
# V2ID_data_linear_sin_sweep_up_40N       = DP.extract_data_NI2D("../data/first_lab/model_project_Displacement_sin_sweep40.csv")

# VT.viz_displacement_LinearVSstudied(V2ID_data_linear_sin_sweep_up_40N, lab_linear_sin_sweep_40N_up)
# VT.viz_sinwesweepupVSsinwesweepdown(lab_linear_sin_sweep_40N_up, lab_linear_sin_sweep_40N_down)
# VT.viz_sinesweep40NVSsinesweep30N(lab_linear_sin_sweep_50N_up, lab_linear_sin_sweep_40N_up, lab_linear_sin_sweep_30N_up)
# VT.viz_displacement(lab_linear_sin_sweep_40N_up)
# relative_displacement, relative_speed, neg_acceleration= CF.get_ASM(lab_linear_sin_sweep_40N_up)
# VT.VizASM(relative_displacement, relative_speed, neg_acceleration)

alpha =  IF.get_RFS(lab_linear_sin_sweep_40N_up, system)
print(alpha)