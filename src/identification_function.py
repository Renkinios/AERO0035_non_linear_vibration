import numpy as np

def get_RFS(data_exp) :
    start_freq      = data_exp["ext_force"][0][2][0]      # Hz
    sweep_rate_freq = (data_exp["ext_force"][0][4][0])/60 # s
    freq            = start_freq + sweep_rate_freq * data_exp['t'][0]
    # Selection of the second pick of the displacement
    idx    = (freq >= 24) & (freq <= 35)
    x1     = data_exp['x'][0][idx]
    x2     = data_exp['x'][1][idx]
    v1     = data_exp['xd'][0][idx]
    v2     = data_exp['xd'][1][idx]
    a1     = data_exp['xdd'][0][idx]
    a2     = data_exp['xdd'][1][idx]
    force1 = data_exp['ext_force'][0][idx]
    force2 = data_exp['ext_force'][1][idx]

    fext = [force1, force2]
    q    = [x1, x2]
    qd   = [v1, v2]
    qdd  = [a1, a2] 
    

    return 0
