import simulate.shooting_method as SM
import numpy as np


def get_NNN(system, omega, y_firstguess):
    # This code is based on one mode that have some linearity is for that that we considere 
    # just one bifurcatoin possible
    nDof = len(system['M'])
    def f_ext(t, omega):
        return np.array([0, 0])
    system['f_ext'] = f_ext
    system['C']     = np.zeros((nDof, nDof))
    y_guess = y_firstguess
    mat_absVal_without_bif = np.zeros((nDof, len(omega)))
    for i in range(len(omega)):
        T = (2 * np.pi) / omega[i]
        # print("y_guess",y_guess)
        
        x_0_sol, xdot_0_sol, ier = SM.shooting_method(system, T, omega[i], y_guess)
        if ier != 1:
            
            print("bifurcation appear at omega = ", omega[i]/2/np.pi)
            # bifurcation = True
            # mat_absVal_without_bif = mat_absVal_without_bif[:, :i -1]
            # omega_without_bif = omega_without_bif[:i -1]
            break
        # print("okok")
        y_guess = np.concatenate([x_0_sol, xdot_0_sol])
        q, _ = SM.result_ODE(system, T, omega[i], y_guess)
        for j in range(nDof):
            mat_absVal_without_bif[j][i] = np.max(np.abs(q[j]))
    return mat_absVal_without_bif
