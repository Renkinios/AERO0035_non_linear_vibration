import numpy as np
import DataPull as DP
from scipy.linalg import pinv

def get_RFS(data_exp, system) :
    data_RFS   = DP.extract_particular_data(data_exp, 24, 30)
    right_term = data_RFS['fext'] - system['M'] @ data_RFS['qdd'] - system['C'] @ data_RFS['qd'] - system['K'] @ data_RFS['q']
    right_term = right_term.flatten(order='F')

    degree_pol = [3,4,7]
    f = []
    for i in degree_pol :
        f.append(np.column_stack((-data_RFS['rel_d']**i,data_RFS['rel_d']**i)).flatten(order='C'))
    f = np.array(f).T

    alpha, _, _, _ =  np.linalg.lstsq(f,right_term, rcond=None)
    print("Alpha : \t",alpha)
    estimate_fext = f @ alpha
    sigma = np.var(right_term)
    sigma_tot = np.var(estimate_fext)
    MSE = (100 / (len(right_term) * sigma)) * np.sum((right_term - estimate_fext) ** 2)
    print("Mean square error : \t",MSE)
    significance_factor = np.zeros(len(alpha))
    for i in range(len(alpha)) :
        f_r = f.T[i] * alpha[i]
        sigma_pole = np.var(f_r)
        significance_factor[i] = 100 * sigma_pole / sigma_tot

    print("Significance factor : \t",significance_factor)

    return alpha, right_term, estimate_fext, data_RFS
