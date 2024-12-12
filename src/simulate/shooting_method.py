import numpy as np
from scipy.integrate import solve_ivp
from scipy.optimize import fsolve

def equation_shooting(y_0, sys, t_end, omega) :
    q_sol = ODE_shot(y_0, sys, t_end, omega)
    q_end = q_sol.y[:,-1]
    h = q_sol.y[:, -1] - q_sol.y[:, 0]
    return h

def compute_shooting_method(sys, T, omega, y_guess) :
    t_end = T
    nDof = len(sys['M'])
    equation_shooting_omega = lambda y_0 : equation_shooting(y_0, sys, t_end, omega)
    options = {'xtol': 5e-5, 'maxfev': 1000}  
    y_sol, _, ier, _ = fsolve(equation_shooting_omega, y_guess, full_output=True, **options) #solve the shooting quation

    x_0_sol = y_sol[:nDof]
    xdot_0_sol = y_sol[nDof:]
    return x_0_sol, xdot_0_sol, ier

def ODE_shot(y_0, sys, t_end, omega) :
    nDof = len(sys['M'])
    M_inv = np.linalg.inv(sys['M'])
    L = np.block([
        [np.zeros((nDof, nDof)), np.eye(nDof)],
        [-M_inv @ sys['K'], -M_inv @ sys['C']]
    ])
    def g_nl(q, qd):
        return np.concatenate((np.zeros(nDof), M_inv @ sys['f_nl'](q, qd)))

    def g_ext(t):
        return np.concatenate((np.zeros(nDof), M_inv @ sys['f_ext'](t, omega)))
    
    def ODE_shoting(t, y) :
        q, qd = y[:nDof], y[nDof:]
        return L @ y - g_nl(q, qd) + g_ext(t)
    
    q_sol = solve_ivp(ODE_shoting,[0, t_end], y_0, method='RK45', rtol=1e-12, atol=1e-11) 
    return q_sol

def result_ODE(sys, T, omega, y_guess) :
    nDof = len(sys['M'])
    ODE_sol = ODE_shot(y_guess, sys, T, omega)
    q       = ODE_sol.y[:nDof] 
    return q , ODE_sol.t