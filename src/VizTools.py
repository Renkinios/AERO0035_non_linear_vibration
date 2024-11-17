import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import pandas as pd
import characteristics_functions as CF

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
    plt.vlines(28.1, limMin_y, limMax_y, colors='black', linestyles='dashdot')
    plt.vlines(30.85, limMin_y, limMax_y, colors='black', linestyles='dashdot')
    plt.hlines(-0.0240, start_freq, max(freq), colors='black', linestyles='dashdot')
    plt.hlines(0.0286, start_freq, max(freq), colors='black', linestyles='dashdot')
    plt.plot(freq, displacement_2, label=r"Studied structure")
    plt.plot(data_NI2D["Frequency (Hz)"], data_NI2D["Amplitude (m)"], label=r"Linear structure")
    plt.xticks([5, 10, 15, 20, 25, 28.1, 30.85])
    plt.yticks([-0.1,-0.05, -0.0240, 0, 0.0286, 0.05, 0.1])

    plt.xlabel(r"Sweep frequency [Hz]")  
    plt.ylabel(r"Amplitude [m]")  
    plt.legend()
    plt.xlim(start_freq, max(freq))
    plt.ylim(limMin_y, limMax_y)
    plt.savefig("../figures/detection/LinearVSstudied.pdf", format='pdf', dpi=1200, bbox_inches='tight')
    # plt.show()
    plt.close()

def viz_sinwesweepupVSsinwesweepdown(data_exp_up, data_exp_up_down):
    start_freq_up      = data_exp_up["ext_force"][0][2][0]      # Hz
    sweep_rate_freq_up = (data_exp_up["ext_force"][0][4][0])/60 # s
    freq_up            = start_freq_up + sweep_rate_freq_up * data_exp_up['t'][0]
    displacement_2_up  = data_exp_up['x'][1]
    start_freq_up_down      = data_exp_up_down["ext_force"][0][2][0]      # Hz
    sweep_rate_freq_up_down = (data_exp_up_down["ext_force"][0][4][0])/60 # s
    freq_up_down            = start_freq_up_down + sweep_rate_freq_up_down * data_exp_up_down['t'][0]
    displacement_2_up_down  = data_exp_up_down['x'][1]
    limMin_y = np.min(displacement_2_up) - 0.02
    limMax_y = np.max(displacement_2_up) + 0.02
    plt.figure(figsize=(10, 4))
    plt.vlines(29, limMin_y, limMax_y, colors='black', linestyles='dashdot')
    plt.vlines(30.88, limMin_y, limMax_y, colors='black', linestyles='dashdot')
    plt.hlines(-0.0240, start_freq_up, max(freq_up), colors='black', linestyles='dashdot')
    plt.hlines(0.0286, start_freq_up, max(freq_up), colors='black', linestyles='dashdot')
    plt.plot(freq_up, displacement_2_up, label=r"Sine sweep up excitation")
    plt.plot(freq_up_down, displacement_2_up_down, label=r"Sine sweep down excitation")
    plt.xlim(start_freq_up, max(freq_up))
    plt.ylim(limMin_y, limMax_y)
    plt.xticks([5, 10, 15, 20, 25, 29, 30.88])
    plt.yticks([-0.1,-0.05, -0.0240, 0, 0.0286, 0.05, 0.1])
    plt.xlabel(r"Sweep frequency [Hz]")  
    plt.ylabel(r"Amplitude [m]")  
    plt.legend()
    plt.savefig("../figures/detection/sinwesweepupVSsinwesweepdown.pdf", format='pdf', dpi=1200, bbox_inches='tight')
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
    plt.legend()
    plt.savefig("../figures/detection/sinesweep40NVSsinesweep30N.pdf", format='pdf', dpi=1200, bbox_inches='tight')
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
    plt.show()  
    # plt.savefig("../figures/detection/displacement.pdf", format='pdf', dpi=1200, bbox_inches='tight')
    plt.close()


def VizASM(relative_displacement, relative_speed, acceleration) : 
    taille_point = 20
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.plot3D(relative_speed, relative_displacement, acceleration)
    ax.set_xlabel(r'Rel. vel [m]')
    ax.set_ylabel(r'Rel. disp [m/s]')
    ax.set_zlabel(r'-Acc.$[\mathrm{m}/\mathrm{s}^2]$')
    ax.yaxis.labelpad=10
    ax.grid(False) 
    # ax.xaxis.pane.fill = False
    # ax.yaxis.pane.fill = False
    # ax.zaxis.pane.fill = False
    ax.xaxis.pane.set_edgecolor('w')
    ax.yaxis.pane.set_edgecolor('w')
    ax.zaxis.pane.set_edgecolor('w')
    ax.set_box_aspect([1,2,1])
    acc0speed, rel_disp0speed = CF.get_stiffness_curve_speed0(acceleration, relative_displacement, relative_speed)
    ax.scatter(0, rel_disp0speed, acc0speed, color='#800020', s=taille_point, marker='x')
    acc0disp, rel_speed0disp = CF.get_damping_curve_disp0(acceleration, relative_displacement, relative_speed, tol=1e-5)
    ax.scatter(rel_speed0disp, 0, acc0disp, color='#006400', s=taille_point, marker='x')
    plt.savefig("../figures/characteristique/ASM_3D.pdf", format='pdf', dpi=300, bbox_inches='tight')
    # plt.show()
    plt.close()
    plt.figure()
    plt.scatter(rel_disp0speed, acc0speed, color='#800020', s=taille_point, marker='x')
    plt.xlabel(r'Rel. displ [m]',fontdict={'fontsize': 20})
    plt.ylabel(r'-Acc.$[\mathrm{m}/\mathrm{s}^2]$', fontdict={'fontsize': 20})
    plt.savefig("../figures/characteristique/ASM_stifness.pdf", format='pdf', dpi=300, bbox_inches='tight')
    plt.close()
    plt.figure()
    plt.scatter(rel_speed0disp, acc0disp, color ='#006400', s=taille_point,marker='x')
    plt.xlabel(r'Rel. vel [m/s]',fontdict={'fontsize': 20})
    plt.ylabel(r'-Acc.$[\mathrm{m}/\mathrm{s}^2]$',fontdict={'fontsize': 20})
    # plt.savefig("../figures/characteristique/ASM_damping.pdf", format='pdf', dpi=300, bbox_inches='tight')
    plt.show()
    plt.close()


    
