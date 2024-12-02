import simulate.shooting_method as SM
import numpy as np
from tqdm import tqdm 

def get_NFLR(system, omega, y_firstguess):

    nDof                   = len(system['M'])
    mat_absVal_without_bif = np.zeros((nDof, len(omega)))
    mat_absVal_bif         = np.zeros((nDof, len(omega)))
    omega_without_bif      = omega
    omega_bif              = omega[::-1]  # Inversion des fréquences pour le calcul avec bifurcation
    bifurcation            = False
    y_guess                = y_firstguess

    for i in tqdm(range(len(omega)), desc="Progression (without bifurcation)", unit="freq"):
        T = (2 * np.pi) / omega[i]
        x_0_sol, xdot_0_sol, ier = SM.shooting_method(system, T, omega[i], y_guess)
        if ier != 1:
            bifurcation = True
            if i == 0:
                mat_absVal_without_bif = mat_absVal_without_bif[:, :i]
                omega_without_bif      = omega_without_bif[:i]
            else:
                mat_absVal_without_bif = mat_absVal_without_bif[:, :i - 1]
                omega_without_bif      = omega_without_bif[:i - 1]
            break
        y_guess = np.concatenate([x_0_sol, xdot_0_sol])
        q, _ = SM.result_ODE(system, T, omega[i], y_guess)
        for j in range(nDof):
            mat_absVal_without_bif[j][i] = np.max(np.abs(q[j]))

    if bifurcation:
        print(f"Bifurcation détectée à omega = {omega[i] / (2 * np.pi):.3f} Hz")
        y_guess = y_firstguess
        for i in tqdm(range(len(omega_bif)), desc="Progression (with bifurcation)   ", unit="freq"):
            T = (2 * np.pi) / omega_bif[i]
            x_0_sol, xdot_0_sol, ier = SM.shooting_method(system, T, omega_bif[i], y_guess)
            if ier != 1:
                if i == 0:
                    mat_absVal_bif = mat_absVal_bif[:, :i]
                    omega_bif      = omega_bif[:i]
                else:
                    mat_absVal_bif = mat_absVal_bif[:, :i - 1]
                    omega_bif      = omega_bif[:i - 1]
                break
            y_guess = np.concatenate([x_0_sol, xdot_0_sol])
            q, t    = SM.result_ODE(system, T, omega_bif[i], y_guess)
            for j in range(nDof):
                mat_absVal_bif[j][i] = np.max(np.abs(q[j]))

    if not bifurcation:
        return {
            'bifurcation': bifurcation,
            'mat_absVal_without_bif': mat_absVal_without_bif,
            'omega_without_bif': omega_without_bif,
            'mat_absVal_bif': None,
            'omega_bif': None
        }

    return {
        'bifurcation': bifurcation,
        'mat_absVal_without_bif': mat_absVal_without_bif,
        'omega_without_bif': omega_without_bif,
        'mat_absVal_bif': mat_absVal_bif,
        'omega_bif': omega_bif
    }
