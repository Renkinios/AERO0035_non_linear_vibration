import simulate.shooting_method as SM
import numpy as np


def get_NFLR(system, omega, y_firstguess):
    # This code is based on one mode that have some linearity is for that that we considere 
    # just one bifurcatoin possible
    nDof = len(system['M'])

    mat_absVal_without_bif = np.zeros((nDof, len(omega)))
    mat_absVal_bif = np.zeros((nDof, len(omega)))
    omega_without_bif = omega
    omega_bif = omega[::-1] # if have some bifurcation going to star t at the end and look to the first point.
    bifurcation = False
    y_guess = y_firstguess
    for i in range(len(omega)):
        T = (2 * np.pi) / omega[i]
        x_0_sol, xdot_0_sol, ier = SM.shooting_method(system, T, omega[i], y_guess)
        if ier != 1:
            print("bifurcation appear at omega = ", omega[i]/2/np.pi)
            bifurcation = True
            if i == 0:
                mat_absVal_without_bif = mat_absVal_without_bif[:, :i]
                omega_without_bif = omega_without_bif[:i]
                break
            else:
                mat_absVal_without_bif = mat_absVal_without_bif[:, :i -1]
                omega_without_bif = omega_without_bif[:i -1]
            break
        y_guess = np.concatenate([x_0_sol, xdot_0_sol])
        q, _ = SM.result_ODE(system, T, omega[i], y_guess)
        for j in range(nDof):
            mat_absVal_without_bif[j][i] = np.max(np.abs(q[j]))
    if bifurcation:
        y_guess = y_firstguess
        for i in range(len(omega_bif)):
            T = (2 * np.pi) / omega_bif[i]
            x_0_sol, xdot_0_sol, ier = SM.shooting_method(system, T, omega_bif[i], y_guess)
            if ier != 1:
                if i == 0:  
                    mat_absVal_bif = mat_absVal_bif[:, :i]
                    omega_bif = omega_bif[:i]
                else:
                    # print("Y_guess \t", y_guess)
                    mat_absVal_bif = mat_absVal_bif[:, :i -1]
                    omega_bif = omega_bif[:i -1] 
                break
            y_guess = np.concatenate([x_0_sol, xdot_0_sol])
            q, t = SM.result_ODE(system, T, omega_bif[i], y_guess)
            for j in range(nDof):
                mat_absVal_bif[j][i] = np.max(np.abs(q[j]))
    else:
        return {'bifurcation': bifurcation, 'mat_absVal_without_bif': mat_absVal_without_bif, 'omega_without_bif': omega_without_bif, 'mat_absVal_bif': None, 'omega_bif': None}
                
    return {'bifurcation': bifurcation, 'mat_absVal_without_bif': mat_absVal_without_bif, 'omega_without_bif': omega_without_bif, 'mat_absVal_bif': mat_absVal_bif, 'omega_bif': omega_bif}