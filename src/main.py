import numpy as np
import matplotlib.pyplot as plt
import VizTools as VT
import DataPull as DP
import argparse

import identification.characteristics_functions as CF
import identification.estimation_parameter as IF
import simulate.shooting_method as SM
from   simulate.NLFR import get_NFLR
from   simulate.NNM import get_NNN



# matrice of the linear system at the begining 
M = np.array([[1, 0], [0, 1]])
C = np.array([[3, -1], [-1, 3]])
K = 10**4 * np.array([[2, -1], [-1, 2]])
system = {'M': M, 'C': C, 'K': K}
def run_identification():
    print("Running identification")
    # First see the up and down about the sin sweep
    lab_linear_sin_sweep_40N_up             = DP.extract_data("../data/first_lab/group3_test1_1.mat")
    lab_linear_sin_sweep_40N_down           = DP.extract_data("../data/first_lab/group3_test1_2.mat")

    lab_sin_40N_10_hz  = DP.extract_data("../data/third_lab/group3_test3_1.mat")
    lab_sin_40N_30_hz  = DP.extract_data("../data/third_lab/group3_test3_2.mat")
    V2ID_sin_40N_10_hz = DP.extract_data_NI2D("../data/NI2D/sin40N_1s_10HZ.csv")
    V2ID_sin_40N_30_hz = DP.extract_data_NI2D("../data/NI2D/sin40N_1s_30HZ.csv")
    VT.viz_true_sin(lab_sin_40N_10_hz, V2ID_sin_40N_10_hz, "verify_sin_10HZ")
    VT.viz_true_sin(lab_sin_40N_30_hz, V2ID_sin_40N_30_hz, "verify_sin_30HZ")

    # Second experimental see the differnce with the amplitude of the force
    lab_linear_sin_sweep_50N_up             =  DP.extract_data("../data/sec_lab/group3_test2_1.mat")
    lab_linear_sin_sweep_30N_up             =  DP.extract_data("../data/sec_lab/group3_test2_3.mat")

    # For the comapraison with the experimental data
    V2ID_data_linear_sin_sweep_up_40N       = DP.extract_data_NI2D("../data/NI2D/model_project_Displacement_sin_sweep40.csv")
    
    VT.viz_displacement_LinearVSstudied(V2ID_data_linear_sin_sweep_up_40N, lab_linear_sin_sweep_40N_up)
    VT.viz_sinwesweepupVSsinwesweepdown(lab_linear_sin_sweep_40N_up, lab_linear_sin_sweep_40N_down)
    VT.viz_sinesweep40NVSsinesweep30N(lab_linear_sin_sweep_50N_up, lab_linear_sin_sweep_40N_up, lab_linear_sin_sweep_30N_up)

    # characteristique method ASM
    relative_displacement, relative_speed, neg_acceleration= CF.get_ASM(lab_linear_sin_sweep_40N_up)
    VT.VizASM(relative_displacement, relative_speed, neg_acceleration)

    # Estimation of the parameter by RFS method
    alpha, degree_pole, right_term, estimate_fext, data_RFS =  IF.get_RFS(lab_linear_sin_sweep_40N_up, system)
    VT.viz_identification(right_term, estimate_fext, data_RFS)


def run_simulation():
    print("Running simulation")
    def f_nl(q, qd):
        rel_d = q[1] - q[0]
        rel_d3 = rel_d**3 
        rel_d4 = rel_d3 * rel_d
        rel_d7 = rel_d4 * rel_d3
        return np.array([-1.9e+10 * rel_d7 + 5.2e+07 * rel_d4 - 2.6e+06 * rel_d3,
                          1.9e+10 * rel_d7 - 5.2e+07 * rel_d4 + 2.6e+06 * rel_d3])

    system['f_nl'] = f_nl
    def f_ext_50(t, omega):
        return np.array([50*np.sin(omega*t), 0])
    system['f_ext'] = f_ext_50
    freq = np.linspace(10, 35, 700)
    omega = 2*np.pi*freq
    y_guess = np.array([0.002, -0.001, 0.002, -0.001])
    print("\nShooting method for force amplitude of F = 50N")
    dic_NLFR50 = get_NFLR(system, omega, y_guess)

    def f_ext_30(t, omega):
        return np.array([30*np.sin(omega*t), 0])
    system['f_ext'] = f_ext_30
    print("\nShooting method for force amplitude of F = 30N")
    dic_NLFR30 = get_NFLR(system, omega, y_guess)
    def f_ext_10(t, omega):
        return np.array([10*np.sin(omega*t), 0])
    system['f_ext'] = f_ext_10
    print("\nShooting method for force amplitude of F = 10N")
    dic_NLFR10 = get_NFLR(system, omega, y_guess)
    
    VT.viz_NLFR(dic_NLFR50, dic_NLFR30, dic_NLFR10)


    # Validation of the NLFRs with the sin up and down 
    def f_ext_40(t, omega):
        return np.array([40*np.sin(omega*t), 0])
    system['f_ext'] = f_ext_40
    freq = np.linspace(10, 35, 800)
    omega = 2*np.pi*freq
    y_guess = np.array([0.002, -0.001, 0.002, -0.001])
    dic_NLFR40 = get_NFLR(system, omega, y_guess)
    lab_linear_sin_sweep_40N_up             = DP.extract_data("../data/first_lab/group3_test1_1.mat")
    lab_linear_sin_sweep_40N_down           = DP.extract_data("../data/first_lab/group3_test1_2.mat")
    VT.viz_confirm_NLFR_up_down(lab_linear_sin_sweep_40N_up, lab_linear_sin_sweep_40N_down, dic_NLFR40)

    # NNN modal, backbone curve
    freq    = np.linspace(27.58, 33, 800)
    omega   = 2*np.pi*freq
    y_guess = np.array([0.009, -0.009, 0, 0]) *1e-1
    mat_absVal_without_bif, omega_without_bif = get_NNN(system, omega, y_guess)
    # backbone_NI2D = DP.extract_data_NI2D("../data/NI2D/backbone_curve.csv")
    VT.viz_backbonecurve(mat_absVal_without_bif, omega_without_bif/2/np.pi)
    # VT.viz_NLFR(dic_NLFR10, dic_NLFR30, dic_NLFR50, backboneBOOL= True, backbone=mat_absVal_without_bif, freq= omega_without_bif/2/np.pi)


    # Validation of the NLFRs wiith 
    NLFRs_50_NI2D = DP.extract_data_NI2D("../data/NI2D/NLFRs_50.csv")
    NLFRs_30_NI2D = DP.extract_data_NI2D("../data/NI2D/NLFRs_30.csv")
    NLFRs_10_NI2D = DP.extract_data_NI2D("../data/NI2D/NLFRs_10.csv")
    VT.viz_NLFR_confirm_NI2D(dic_NLFR10, dic_NLFR30, dic_NLFR50, NLFRs_50_NI2D, NLFRs_30_NI2D, NLFRs_10_NI2D)


def main():
    parser = argparse.ArgumentParser(description="Manage simulations and identifications.")
    parser.add_argument(
        '-s', '--simulation', action='store_true', help="Run only the simulation."
    )
    parser.add_argument(
        '-i', '--identification', action='store_true', help="Run only the identification."
    )

    args = parser.parse_args()

    # Run everything if no arguments are provided
    if not (args.simulation or args.identification):
        print("No arguments provided, running all tasks.")
        run_identification()
        run_simulation()
    else:
        if args.simulation:
            run_simulation()
        if args.identification:
            run_identification()

if __name__ == "__main__":
    main()
