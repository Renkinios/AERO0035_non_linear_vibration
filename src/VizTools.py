import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import pandas as pd
import identification.characteristics_functions as CF

# Définition globale des paramètres de police et de taille pour tous les graphiques
plt.rc('font', family='serif')  # Police avec empattements, comme Times
plt.rc('text', usetex=True)  # Utiliser LaTeX pour le texte dans les figures
plt.rcParams.update({
    'font.size': 14,       # Taille de police générale
    'legend.fontsize': 15, # Taille de police pour les légendes
    'axes.labelsize': 18,  # Taille de police pour les étiquettes des axes
})

def viz_displacement_LinearVSstudied(data_NI2D, data_exp):
    start_freq      = data_exp["ext_force"][0][2][0]      # Hz
    sweep_rate_freq = (data_exp["ext_force"][0][4][0])/60 # s
    freq            = start_freq + sweep_rate_freq * data_exp['t'][0]
    displacement_2  = data_exp['x'][1]
    limMin_y = np.min(displacement_2) - 0.02
    limMax_y = np.max(displacement_2) + 0.02
    plt.figure(figsize=(10, 4))
    plt.vlines(27.57, limMin_y, limMax_y, colors='black', linestyles='dashdot')
    plt.vlines(30.85, limMin_y, limMax_y, colors='black', linestyles='dashdot')
    plt.hlines(-0.0240, start_freq, max(freq), colors='black', linestyles='dashdot')
    plt.hlines(0.0286, start_freq, max(freq), colors='black', linestyles='dashdot')
    plt.plot(freq, displacement_2, label=r"Studied structure")
    plt.plot(data_NI2D["Frequency (Hz)"], data_NI2D["Amplitude (m)"], label=r"Linear structure")
    plt.xticks([5, 10, 15, 20, 25, 27.57, 30.85])
    plt.yticks([-0.1,-0.05, -0.0240, 0, 0.0286, 0.05, 0.1])

    plt.xlabel(r"Sweep frequency [Hz]")  
    plt.ylabel(r"Amplitude [m]")  
    plt.legend(loc="upper right")
    plt.xlim(start_freq, max(freq))
    plt.ylim(limMin_y, limMax_y)
    plt.savefig("../figures/identification/detection/LinearVSstudied.pdf", format='pdf', dpi=1200, bbox_inches='tight')
    # plt.show()
    plt.close()

def viz_true_sin(data_exp, data_NI2D, name_fig):
    limMin_y = np.min(data_exp['x'][0]) - 0.002
    limMax_y = np.max(data_exp['x'][0]) + 0.002
    # plt.figure(figsize=(10, 4))
    plt.plot(data_exp['t'][0], data_exp['x'][0], label=r"Experimental")
    plt.plot(data_NI2D["Frequency (Hz)"], data_NI2D["Amplitude (m)"], label=r"Simulations",linestyle='dashdot')
    plt.xlabel(r"Times [s]")  
    plt.ylabel(r"Amplitude [m]")  
    plt.legend(loc="upper right")
    plt.xlim(0, 1)
    plt.ylim(limMin_y, limMax_y)
    plt.savefig("../figures/identification/"+name_fig+".pdf", format='pdf', dpi=1200, bbox_inches='tight')
    plt.close()

def viz_true_sinesweep(data_exp, data_NI2D) :
    start_freq      = data_exp["ext_force"][0][2][0]      # Hz
    sweep_rate_freq = (data_exp["ext_force"][0][4][0])/60 # s
    freq            = start_freq + sweep_rate_freq * data_exp['t'][0]
    displacement_2  = data_exp['x'][1]
    limMin_y = np.min(displacement_2) - 0.02
    limMax_y = np.max(displacement_2) + 0.02
    plt.figure(figsize=(10, 4))
    plt.plot(freq, displacement_2, label=r"Experimental")
    plt.plot(data_NI2D["Frequency (Hz)"], data_NI2D["Amplitude (m)"], label=r"Simulations")
    plt.legend()
    plt.show()

def viz_sinwesweepupVSsinwesweepdown(data_exp_up, data_exp_down):
    start_freq_up        = data_exp_up["ext_force"][0][2][0]      # Hz
    sweep_rate_freq_up   = (data_exp_up["ext_force"][0][4][0])/60 # s
    freq_up              = start_freq_up + sweep_rate_freq_up * data_exp_up['t'][0]
    displacement_2_up    = data_exp_up['x'][1]
    start_freq_down      = data_exp_down["ext_force"][0][2][0]      # Hz
    sweep_rate_freq_down = (data_exp_down["ext_force"][0][4][0])/60 # s
    freq_down            = start_freq_down + sweep_rate_freq_down * data_exp_down['t'][0]
    displacement_2_up_down  = data_exp_down['x'][1]
    limMin_y = np.min(displacement_2_up) - 0.02
    limMax_y = np.max(displacement_2_up) + 0.02
    plt.figure(figsize=(10, 4))
    plt.vlines(29, limMin_y, limMax_y, colors='black', linestyles='dashdot')
    plt.vlines(30.88, limMin_y, limMax_y, colors='black', linestyles='dashdot')
    plt.hlines(-0.0240, start_freq_up, max(freq_up), colors='black', linestyles='dashdot')
    plt.hlines(0.0286, start_freq_up, max(freq_up), colors='black', linestyles='dashdot')
    plt.plot(freq_up, displacement_2_up, label=r"Sine sweep up excitation")
    plt.plot(freq_down, displacement_2_up_down, label=r"Sine sweep down excitation")
    plt.xlim(start_freq_up, max(freq_up))
    plt.ylim(limMin_y, limMax_y)
    plt.xticks([5, 10, 15, 20, 25, 29, 30.88])
    plt.yticks([-0.1,-0.05, -0.0240, 0, 0.0286, 0.05, 0.1])
    plt.xlabel(r"Sweep frequency [Hz]")  
    plt.ylabel(r"Amplitude [m]")  
    plt.legend(loc="upper right")
    plt.savefig("../figures/identification/detection/sinwesweepupVSsinwesweepdown.pdf", format='pdf', dpi=1200, bbox_inches='tight')
    # plt.show()
    plt.close()

def viz_sinesweep40NVSsinesweep30N(data_exp_50N, data_exp_40N, data_exp_30N):
    start_freq_50N      = data_exp_50N["ext_force"][0][2][0]      # Hz
    sweep_rate_freq_50N = (data_exp_50N["ext_force"][0][4][0])/60 # s
    freq_50N            = start_freq_50N + sweep_rate_freq_50N * data_exp_50N['t'][0]
    displacement_2_50N  = data_exp_50N['x'][1]
    limMin_y = np.min(displacement_2_50N) - 0.02
    limMax_y = np.max(displacement_2_50N) + 0.02

    start_freq_40N      = data_exp_40N["ext_force"][0][2][0]      # Hz
    sweep_rate_freq_40N = (data_exp_40N["ext_force"][0][4][0])/60 # s
    freq_40N            = start_freq_40N + sweep_rate_freq_40N * data_exp_40N['t'][0]
    displacement_2_40N  = data_exp_40N['x'][1]

    start_freq_30N      = data_exp_30N["ext_force"][0][2][0]      # Hz
    sweep_rate_freq_30N = (data_exp_30N["ext_force"][0][4][0])/60 # s
    freq_30N            = start_freq_30N + sweep_rate_freq_30N * data_exp_30N['t'][0]
    displacement_2_30N  = data_exp_30N['x'][1]
    plt.figure(figsize=(10, 4))
    plt.plot(freq_50N, displacement_2_50N, label=r"Sine sweep 50N")
    plt.plot(freq_40N, displacement_2_40N, label=r"Sine sweep 40N")
    plt.plot(freq_30N, displacement_2_30N, label=r"Sine sweep 30N")
    plt.vlines(30, limMin_y, limMax_y, colors='black', linestyles='dashdot')
    plt.vlines(30.9, limMin_y, limMax_y, colors='black', linestyles='dashdot')
    plt.vlines(31.1, limMin_y, limMax_y, colors='black', linestyles='dashdot')
    plt.text(30.1 - 2.2, -0.1, r'$30.1$', fontsize=15)
    plt.text(31.1 + 0.5, -0.1, r'$31.1$', fontsize=15)

    plt.xticks([5, 10, 15, 20, 25, 30.9])

    plt.xlim(start_freq_40N, max(freq_40N))
    plt.xlabel(r"Sweep frequency [Hz]")  
    plt.ylabel(r"Amplitude [m]")  
    plt.ylim(limMin_y, limMax_y)
    plt.legend(loc="upper right")
    plt.savefig("../figures/identification/detection/sinesweep40NVSsinesweep30N.pdf", format='pdf', dpi=1200, bbox_inches='tight')
    # plt.show()
    plt.close()

def viz_displacement(data):
    start_freq      = data["ext_force"][0][2][0]      # Hz
    sweep_rate_freq = (data["ext_force"][0][4][0])/60 # s
    freq            = start_freq + sweep_rate_freq * data['t'][0]
    displacement_2  = data['x'][1]
    plt.figure(figsize=(10, 5))
    plt.plot(freq, displacement_2)
    plt.xlabel(r"Sweep frequency [Hz]")  
    plt.ylabel(r"Amplitude [m]")  
    # plt.show()  
    plt.savefig("../figures/identification/detection/displacement.pdf", format='pdf', dpi=1200, bbox_inches='tight')
    plt.close()


def VizASM(relative_displacement, relative_speed, acceleration):
    taille_point = 20
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    
    ax.plot3D(relative_speed, relative_displacement, acceleration, color='royalblue')
    
    ax.set_xlabel(r'Rel. vel [m]')
    ax.set_ylabel(r'Rel. disp [m/s]')
    ax.set_zlabel(r'-Acc.$[\mathrm{m}/\mathrm{s}^2]$')
    
    ax.yaxis.labelpad = 10
    
    ax.grid(False)
    
    ax.xaxis.pane.fill = False
    ax.yaxis.pane.fill = False
    ax.zaxis.pane.fill = False
    fig.patch.set_facecolor('white')
    ax.set_box_aspect([1, 1, 1])
    
    acc0speed, rel_disp0speed = CF.get_stiffness_curve_speed0(acceleration, relative_displacement, relative_speed)
    ax.scatter(0, rel_disp0speed, acc0speed, color='#800020', s=taille_point, marker='x')
    
    acc0disp, rel_speed0disp = CF.get_damping_curve_disp0(acceleration, relative_displacement, relative_speed, tol=1e-5)
    ax.scatter(rel_speed0disp, 0, acc0disp, color='#006400', s=taille_point, marker='x')
    
    # plt.savefig("../figures/identification/characteristique/ASM_3D.pdf", format='pdf', dpi=300, bbox_inches='tight')
    plt.show()
    plt.close()
    plt.figure()
    plt.scatter(rel_disp0speed, acc0speed, color='#800020', s=taille_point, marker='x')
    plt.xlabel(r'Rel. displ [m]',fontdict={'fontsize': 20})
    plt.ylabel(r'-Acc.$[\mathrm{m}/\mathrm{s}^2]$', fontdict={'fontsize': 20})
    plt.savefig("../figures/identification/characteristique/ASM_stifness.pdf", format='pdf', dpi=300, bbox_inches='tight')
    plt.close()
    plt.figure()
    plt.scatter(rel_speed0disp, acc0disp, color ='#006400', s=taille_point,marker='x')
    plt.xlabel(r'Rel. vel [m/s]',fontdict={'fontsize': 20})
    plt.ylabel(r'-Acc.$[\mathrm{m}/\mathrm{s}^2]$',fontdict={'fontsize': 20})
    plt.savefig("../figures/identification/characteristique/ASM_damping.pdf", format='pdf', dpi=300, bbox_inches='tight')
    plt.close()

def viz_identification(measurement, prediction, data_RFS,tol=1e-3) :
    measurement = measurement[1::2] # Selecting the second dof
    prediction  = prediction[1::2] # Selecting the second dof
    
    indices_d       = np.argsort(data_RFS['rel_d']) 
    rel_disp_sorted = data_RFS['rel_d'][indices_d]  
    f_nl_2          = prediction[indices_d]        

    arg_0speed         = np.isclose(data_RFS['rel_v'], 0, atol=tol)
    real_disp_0speed   = data_RFS['rel_d'][arg_0speed]
    measurement_0speed = measurement[arg_0speed]

    arg_sorted_disp    = np.argsort(real_disp_0speed)
    real_disp_0speed   = real_disp_0speed[arg_sorted_disp]
    measurement_0speed = measurement_0speed[arg_sorted_disp]

    # like in relative speed = 0 no the g_nl = 0 for 0 displacement
    f_nl_speed = np.zeros(len(data_RFS['rel_v']))
    arg_0speed = np.isclose(data_RFS['rel_d'], 0, atol=1e-5)
    real_speed_0disp = data_RFS['rel_v'][arg_0speed]
    measurement_speed = measurement[arg_0speed]

    plt.figure()
    plt.scatter(real_speed_0disp, measurement_speed, s=20, marker='x',label=r'Measured')
    plt.plot(data_RFS['rel_v'], f_nl_speed, label=r'Estimated', color='#800020')
    plt.xlabel(r'Rel. vel [m/s]')
    plt.ylabel(r'$f_{nl}(0, \dot{x_2} - \dot{x_1})$ [N]')
    plt.legend(loc ='lower right')
    plt.savefig("../figures/identification/estimation/Identification_speed.pdf", format='pdf', dpi=300, bbox_inches='tight')
    plt.close()
    plt.figure()
    plt.plot(rel_disp_sorted, f_nl_2, label=r'Measured')
    plt.plot(real_disp_0speed, measurement_0speed, label=r'Estimated', alpha=0.5)
    plt.xlabel(r'Rel. disp [m]')
    plt.ylabel(r'$f_{nl}(x_2 - x_1, 0)$ [N]')
    plt.legend(loc ='lower right')
    plt.savefig("../figures/identification/estimation/Identification_displacement.pdf", format='pdf', dpi=300, bbox_inches='tight')
    plt.close()

def viz_NLFR(dic_NLFR10, dic_NLFR30, dict_NLFR50, backboneBOOL = False, freq = [], backbone = []) :
    if backboneBOOL:
        plt.figure()
    else:
        plt.figure(figsize=(10, 4))
    if dic_NLFR10['bifurcation']:
        plt.plot(dic_NLFR10['omega_without_bif'] / 2 / np.pi, dic_NLFR10['mat_absVal_without_bif'][1], color='#1f77b4')  
        plt.plot(dic_NLFR10['omega_bif'] / 2 / np.pi, dic_NLFR10['mat_absVal_bif'][1], color='#1f77b4', label=r"$|F| = 10$ N")
    else:
        plt.plot(dic_NLFR10['omega_without_bif'] / 2 / np.pi, dic_NLFR10['mat_absVal_without_bif'][1], color='#1f77b4', label=r"$|F| = 10$ N")

    if dic_NLFR30['bifurcation']:
        plt.plot(dic_NLFR30['omega_without_bif'] / 2 / np.pi, dic_NLFR30['mat_absVal_without_bif'][1], color='#8b0000')
        plt.plot(dic_NLFR30['omega_bif'] / 2 / np.pi, dic_NLFR30['mat_absVal_bif'][1], color='#8b0000', label=r"$|F| = 30$ N")
    else:
        plt.plot(dic_NLFR30['omega_without_bif'] / 2 / np.pi, dic_NLFR30['mat_absVal_without_bif'][1], color='#8b0000', label=r"$|F| = 30$ N")

    if dict_NLFR50['bifurcation']:
        plt.plot(dict_NLFR50['omega_without_bif'] / 2 / np.pi, dict_NLFR50['mat_absVal_without_bif'][1], color='#228b22')
        plt.plot(dict_NLFR50['omega_bif'] / 2 / np.pi, dict_NLFR50['mat_absVal_bif'][1], color='#228b22', label=r"$|F| = 50$ N")
    else:
        plt.plot(dict_NLFR50['omega_without_bif'] / 2 / np.pi, dict_NLFR50['mat_absVal_without_bif'][1], color='#228b22', label=r"$|F| = 50$ N")
    if backboneBOOL:
        plt.plot(freq, backbone[1], color='#000000', label=r"Backbone curve")
    plt.xlabel(r"Frequency [Hz]")
    plt.ylabel(r"Amplitude [m]")
    plt.legend()
    if backboneBOOL:
        plt.xlim(25,33)
        plt.ylim(0,0.034)
        plt.savefig("../figures/simulation/NLFR_with_backbone.pdf", format='pdf', dpi=300, bbox_inches='tight')
    else:
        plt.xlim(np.min(dict_NLFR50['omega_without_bif'] / 2 / np.pi), np.max(dic_NLFR10['omega_bif'] / 2 / np.pi))
        plt.savefig("../figures/simulation/NLFR.pdf", format='pdf', dpi=300, bbox_inches='tight')

def viz_confirm_NLFR_up_down(data_exp_up, data_exp_down,dict_NLFR):
    start_freq_up        = data_exp_up["ext_force"][0][2][0]      # Hz
    sweep_rate_freq_up   = (data_exp_up["ext_force"][0][4][0])/60 # s
    freq_up              = start_freq_up + sweep_rate_freq_up * data_exp_up['t'][0]
    displacement_2_up    = data_exp_up['x'][1]
    start_freq_down      = data_exp_down["ext_force"][0][2][0]      # Hz
    sweep_rate_freq_down = (data_exp_down["ext_force"][0][4][0])/60 # s
    freq_down            = start_freq_down + sweep_rate_freq_down * data_exp_down['t'][0]
    displacement_2_up_down  = data_exp_down['x'][1]
    limMin_y = np.min(displacement_2_up) - 0.02
    limMax_y = np.max(displacement_2_up) + 0.02
    plt.figure(figsize=(10, 4))
    plt.plot(freq_up, displacement_2_up, label=r"Sine sweep up excitation")
    plt.plot(freq_down, displacement_2_up_down, label=r"Sine sweep down excitation")
    if dict_NLFR['bifurcation']:
        plt.plot(dict_NLFR['omega_without_bif'] / 2 / np.pi, dict_NLFR['mat_absVal_without_bif'][1], color='#009E73',linewidth=3)
        plt.plot(dict_NLFR['omega_bif'] / 2 / np.pi, dict_NLFR['mat_absVal_bif'][1], color='#009E73', label=r"NLFRs",linewidth=3)
    else:
        plt.plot(dict_NLFR['omega_without_bif'] / 2 / np.pi, dict_NLFR['mat_absVal_without_bif'][1], color='#009E73', label=r"NLFRs",linewidth=3)
    plt.xlim(start_freq_up, max(freq_up))
    plt.ylim(limMin_y, limMax_y)
    plt.xlabel(r"Sweep frequency [Hz]")  
    plt.ylabel(r"Amplitude [m]")  
    plt.legend()
    plt.savefig("../figures/simulation/confirm_NLFR_up_down.pdf", format='pdf', dpi=300, bbox_inches='tight')

def viz_backbonecurve(backbone, freq, backbone_NI2D):
    plt.figure(figsize=(8,7))
    plt.plot(freq, backbone[1], label=r"Backbone curve", linewidth=2)
    plt.plot(backbone_NI2D["Frequency (Hz)"], backbone_NI2D["Amplitude (m)"], label=r"Backbone curve NI2D", linewidth=1, linestyle='dashdot')
    plt.vlines(27.5664,0, 0.06, colors='black', linestyles='dashdot', label=r'Linear resonance frequency')
    plt.xlabel(r"Frequency [Hz]")
    plt.ylabel(r"Amplitude [m]")
    plt.xlim(27.2,31)
    plt.ylim(0,0.06)
    plt.legend()
    plt.savefig("../figures/simulation/backbone_curve.pdf", format='pdf', dpi=300, bbox_inches='tight')
    plt.close()
    

def viz_NLFR_confirm_NI2D(dic_NLFR10, dic_NLFR30, dict_NLFR50, NLFRs_NI2D_50, NLFRs_NI2D_30, NLFRs_NI2D_10):
    plt.figure(figsize=(10, 4))
    
    if dic_NLFR10['bifurcation']:
        plt.plot(dic_NLFR10['omega_without_bif'] / 2 / np.pi, dic_NLFR10['mat_absVal_without_bif'][1], 
                 color='#1f77b4', linewidth=2) 
        plt.plot(dic_NLFR10['omega_bif'] / 2 / np.pi, dic_NLFR10['mat_absVal_bif'][1], 
                 color='#1f77b4', linewidth=2, label=r"$|F| = 10$ N")  
    else:
        plt.plot(dic_NLFR10['omega_without_bif'] / 2 / np.pi, dic_NLFR10['mat_absVal_without_bif'][1], 
                 color='#1f77b4', linewidth=2, label=r"$|F| = 10$ N") 

    if dic_NLFR30['bifurcation']:
        plt.plot(dic_NLFR30['omega_without_bif'] / 2 / np.pi, dic_NLFR30['mat_absVal_without_bif'][1], 
                 color='#8b0000', linewidth=2)
        plt.plot(dic_NLFR30['omega_bif'] / 2 / np.pi, dic_NLFR30['mat_absVal_bif'][1], 
                 color='#8b0000', linewidth=2, label=r"$|F| = 30$ N")
    else:
        plt.plot(dic_NLFR30['omega_without_bif'] / 2 / np.pi, dic_NLFR30['mat_absVal_without_bif'][1], 
                 color='#8b0000', linewidth=2, label=r"$|F| = 30$ N")


    if dict_NLFR50['bifurcation']:
        plt.plot(dict_NLFR50['omega_without_bif'] / 2 / np.pi, dict_NLFR50['mat_absVal_without_bif'][1], 
                 color='#228b22', linewidth=2)
        plt.plot(dict_NLFR50['omega_bif'] / 2 / np.pi, dict_NLFR50['mat_absVal_bif'][1], 
                 color='#228b22', linewidth=2, label=r"$|F| = 50$ N")
    else:
        plt.plot(dict_NLFR50['omega_without_bif'] / 2 / np.pi, dict_NLFR50['mat_absVal_without_bif'][1], 
                 color='#228b22', linewidth=2, label=r"$|F| = 50$ N")

    plt.plot(NLFRs_NI2D_50["Frequency (Hz)"], NLFRs_NI2D_50["Amplitude (m)"], 
             color='black', alpha=0.7, linewidth=1.25)
    plt.plot(NLFRs_NI2D_30["Frequency (Hz)"], NLFRs_NI2D_30["Amplitude (m)"], 
             color='black', alpha=0.7, linewidth=1.25)
    plt.plot(NLFRs_NI2D_10["Frequency (Hz)"], NLFRs_NI2D_10["Amplitude (m)"], 
             color='black', label=r"NI2D Harmonic Balance Continuation", alpha=0.7, linewidth=1.5)

    plt.xlabel(r"Frequency [Hz]")
    plt.ylabel(r"Amplitude [m]")
    plt.legend()
    plt.xlim(10, 35)
    plt.savefig("../figures/simulation/NLFR_confirm_NI2D.pdf", format='pdf', dpi=300, bbox_inches='tight')
