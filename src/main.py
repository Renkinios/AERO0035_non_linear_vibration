import numpy as np
import VibLinSpace as VLS
import VizTools as VT
import DataPull as DP
import matplotlib.pyplot as plt
import identification.characteristics_functions as CF
import identification.estimation_parameter as IF
import simulate.shooting_method as SM

# matrice of the linear system at the begining 
M = np.array([[1, 0], [0, 1]])
C = np.array([[3, -1], [-1, 3]])
K = 10**4 * np.array([[2, -1], [-1, 2]])
system = {'M': M, 'C': C, 'K': K}

# freq, mode = VLS.get_mode_freq_lin(M, K)
# First see the up and down about the sin sweep
# lab_linear_sin_sweep_40N_up             = DP.extract_data("../data/first_lab/group3_test1_1.mat")
# V2ID_true     = DP.extract_data_NI2D("../data/first_lab/coorect_model.csv")

# lab_linear_sin_sweep_40N_down           = DP.extract_data("../data/first_lab/group3_test1_2.mat")

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
def f_ext(t, omega):
    return np.array([50*np.sin(omega*t), 0])

system['f_nl'] = f_nl
system['f_ext'] = f_ext

x_0 = np.array([0.002, -0.001]).T
xd_0 = np.array([0.002, -0.001]).T
y_guess = np.concatenate([x_0, xd_0])


f = 20
omega = 2*np.pi*f
T = 1/f
t_end = T

q, t = SM.result_ODE(system, T, omega, y_guess)
x_0_sol, xdot_0_sol, ier = SM.shooting_method(system, T, omega, y_guess)
y_true = np.concatenate([x_0_sol, xdot_0_sol])
print("y_true",y_true)
q_shot, t_shot = SM.result_ODE(system, T, omega, y_true)

plt.figure()
plt.plot(t, q[1], label='Initial guess')
plt.plot(t_shot, q_shot[1], label='Shooting method', alpha=0.5)
plt.plot([0, T], [x_0_sol[1], x_0_sol[1]], 'k--')
plt.plot
plt.legend()
plt.show()



