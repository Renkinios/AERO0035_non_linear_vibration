import numpy as np
import VibLinSpace as VLS
import VizTools as VT
import DataPull as DP
import matplotlib.pyplot as plt
import identification.characteristics_functions as CF
import identification.estimation_parameter as IF
import simulate.shooting_method as SM
from simulate.NLFR import get_NFLR
from simulate.NNN import get_NNN

# matrice of the linear system at the begining 
M = np.array([[1, 0], [0, 1]])
C = np.array([[3, -1], [-1, 3]])
K = 10**4 * np.array([[2, -1], [-1, 2]])
system = {'M': M, 'C': C, 'K': K}

# freq, mode = VLS.get_mode_freq_lin(M, K)
# First see the up and down about the sin sweep
lab_linear_sin_sweep_40N_up             = DP.extract_data("../data/first_lab/group3_test1_1.mat")
# V2ID_true     = DP.extract_data_NI2D("../data/first_lab/coorect_model.csv")

lab_linear_sin_sweep_40N_down           = DP.extract_data("../data/first_lab/group3_test1_2.mat")

# # Second experimental see the differnce with the amplitude of the force
# lab_linear_sin_sweep_50N_up             =  DP.extract_data("../data/sec_lab/group3_test2_1.mat")
# lab_linear_sin_sweep_30N_up             =  DP.extract_data("../data/sec_lab/group3_test2_3.mat")

# # For the comapraison with the experimental data
# V2ID_data_linear_sin_sweep_up_40N       = DP.extract_data_NI2D("../data/first_lab/model_project_Displacement_sin_sweep40.csv")
# VT.viz_displacement_LinearVSstudied(V2ID_true, lab_linear_sin_sweep_40N_up)

# VT.viz_displacement_LinearVSstudied(V2ID_data_linear_sin_sweep_up_40N, lab_linear_sin_sweep_40N_up)
# VT.viz_sinwesweepupVSsinwesweepdown(lab_linear_sin_sweep_40N_up, lab_linear_sin_sweep_40N_down)
# VT.viz_sinesweep40NVSsinesweep30N(lab_linear_sin_sweep_50N_up, lab_linear_sin_sweep_40N_up, lab_linear_sin_sweep_30N_up)
# VT.viz_displacement(lab_linear_sin_sweep_40N_up)
# relative_displacement, relative_speed, neg_acceleration= CF.get_ASM(lab_linear_sin_sweep_40N_up)
# VT.VizASM(relative_displacement, relative_speed, neg_acceleration)

# alpha, degree_pole, right_term, estimate_fext, data_RFS =  IF.get_RFS(lab_linear_sin_sweep_40N_up, system)
# VT.viz_identification(right_term, estimate_fext, data_RFS)

def f_nl(q, qd):
    return np.array([-2.1e+10 * (q[1] - q[0])**7 + 5.3e+07 * (q[1] - q[0])**4 - 2.5e+06 * (q[1] - q[0])**3, 
                     2.1e+10 * (q[1] - q[0])**7 - 5.3e+07 * (q[1] - q[0])**4 + 2.5e+06 * (q[1] - q[0])**3])

system['f_nl'] = f_nl



# Testing the shooting method with the linear model
# def f_nl(q, qd):
#     return np.array([0,0])

# system['f_nl'] = f_nl
# freq = np.linspace(10, 30, 800)
# omega = 2*np.pi*freq
# y_guess = np.array([0.002, -0.001, 0.002, -0.001])
# matrix_absolute_value = get_NFLR(system, omega, y_guess)
# print("matrix_absolute_value",matrix_absolute_value)
# print("matrix_absolute_value",len(matrix_absolute_value[1]))
# print("matrix_absolute_value",len(matrix_absolute_value))

# plt.figure()
# plt.plot(freq, matrix_absolute_value[1], label='q1')
# plt.show()


# The shooting method with the vibration model for differnt amplitude
# def f_ext_50(t, omega):
#     return np.array([50*np.sin(omega*t), 0])
# system['f_ext'] = f_ext_50
# freq = np.linspace(10, 35, 800)
# omega = 2*np.pi*freq
# y_guess = np.array([0.002, -0.001, 0.002, -0.001])
# dic_NLFR50 = get_NFLR(system, omega, y_guess)

# def f_ext_30(t, omega):
#     return np.array([30*np.sin(omega*t), 0])
# system['f_ext'] = f_ext_30
# dic_NLFR30 = get_NFLR(system, omega, y_guess)

# def f_ext_10(t, omega):
#     return np.array([10*np.sin(omega*t), 0])
# system['f_ext'] = f_ext_10
# dic_NLFR10 = get_NFLR(system, omega, y_guess)

# VT.viz_NLFR(dic_NLFR50, dic_NLFR30, dic_NLFR10)


# Validation of the NLFRs with the sin up and down 
# def f_ext_40(t, omega):
#     return np.array([40*np.sin(omega*t), 0])
# system['f_ext'] = f_ext_40
# freq = np.linspace(10, 35, 800)
# omega = 2*np.pi*freq
# y_guess = np.array([0.002, -0.001, 0.002, -0.001])
# dic_NLFR40 = get_NFLR(system, omega, y_guess)
# VT.viz_confirm_NLFR_up_down(lab_linear_sin_sweep_40N_up, lab_linear_sin_sweep_40N_down, dic_NLFR40)

# NNN modal, backbone curve
# nDof = len(system['M'])
# def f_ext(t, omega):
#     return np.array([0, 0])
# system['f_ext'] = f_ext
# system['C']     = np.zeros((nDof, nDof))
# freq = np.linspace(28, 30.64, 10)
# omega = 2*np.pi*freq
# # y_guess = 1.0e-04 * np.array([-0.0001, 0.0001, -0.1159, 0.1159])
# y_guess = np.array([0.01, -0.01, 0, 0])
# mat_absVal_without_bif = get_NNN(system, omega, y_guess)
# print( mat_absVal_without_bif[1])

# VT.viz_backbonecurve(mat_absVal_without_bif[i],freq)
# VT.viz_NLFR(dic_NLFR50, dic_NLFR30, dic_NLFR10, backboneBOOL= True, backbone=mat_absVal_without_bif, freq= freq)
