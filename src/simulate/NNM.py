import simulate.shooting_method as SM
import numpy as np
from tqdm import tqdm 


def get_NNN(system, omega, y_firstguess):
    
    nDof  = len(system['M'])
    def f_ext(t, omega):
        return np.zeros(nDof)
    
    system['f_ext']        = f_ext
    system['C']            = np.zeros((nDof, nDof))
    y_guess                = y_firstguess
    mat_absVal_without_bif = np.zeros((nDof, len(omega)))
    omega_without_bif      = omega

    for i in tqdm(range(len(omega)), desc="Progression NNMs", unit="freq"):
        T = (2 * np.pi) / omega[i]
        x_0_sol, xdot_0_sol, ier = SM.compute_shooting_method(system, T, omega[i], y_guess)
        if ier != 1:
            bifurcation = True
            if i == 0:
                mat_absVal_without_bif = mat_absVal_without_bif[:, :i]
                omega_without_bif      = omega_without_bif[:i]
                break
            else:
                mat_absVal_without_bif = mat_absVal_without_bif[:, :i -1]
                omega_without_bif      = omega_without_bif[:i -1]
            break
        y_guess = np.concatenate([x_0_sol, xdot_0_sol])
        q, _    = SM.result_ODE(system, T, omega[i], y_guess)
        for j in range(nDof):
            mat_absVal_without_bif[j][i] = np.max(np.abs(q[j]))
    if bifurcation:
        print(f"Bifurcation détectée à omega = {omega[i] / (2 * np.pi):.3f} Hz")
    return mat_absVal_without_bif, omega_without_bif
