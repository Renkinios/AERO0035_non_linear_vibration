import numpy as np


def get_ASM(data_exp) :
    start_freq      = data_exp["ext_force"][0][2][0]      # Hz
    sweep_rate_freq = (data_exp["ext_force"][0][4][0])/60 # s
    freq            = start_freq + sweep_rate_freq * data_exp['t'][0]
    # Selection of the second pick of the displacement
    idx                   = (freq >= 24) & (freq <= 35)
    relative_displacement = (data_exp['x'][1][idx] - data_exp['x'][0][idx])
    relative_speed        = (data_exp['xd'][1][idx] - data_exp['xd'][0][idx])
    neg_acceleration      = - (data_exp['xdd'][1])[idx]
    return relative_displacement, relative_speed, neg_acceleration

def get_stiffness_curve_speed0(acceleration,rel_disp, rel_speed,tol=1e-4) :
    idx_zero_speed = np.isclose(rel_speed, 0, atol=tol)
    acc0speed      = acceleration[idx_zero_speed]
    rel_disp0speed = rel_disp[idx_zero_speed]
    return acc0speed, rel_disp0speed

def get_stiffness_curve_disp0(acceleration,rel_disp, rel_speed,tol=1e-4) :
    idx_zero_disp = np.isclose(rel_disp, 0, atol=tol)
    acc0disp      = acceleration[idx_zero_disp]
    rel_speed0disp = rel_speed[idx_zero_disp]
    return acc0disp, rel_speed0disp
