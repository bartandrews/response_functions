import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import random
import csv
import heapq
import glob
from matplotlib.ticker import FormatStrFormatter


# Coulomb and Laughlin tests ###########################################################################################

def plot_3d_q(name, numb_qy, omega_min, omega_max, filename):

    ax = plt.subplot(111, projection='3d')

    qy = []
    omega = []
    SR = []

    for qy_value in range(numb_qy):
        file = f"fermions_torus_spec_resp_kysym_{name}_n_6_2s_{numb_qy}_ratio_1.000000_qy_{qy_value}" \
               f".omega_{omega_min}-{omega_max}_eps_0.0001.sr.cut"
        with open('stripped_files/' + file, 'r') as csvfile:
            plots = csv.reader(csvfile, delimiter=' ')
            for row in plots:
                qy.append(qy_value)
                omega.append(float(row[0]))
                SR.append(float(row[1]))

    ax.scatter(qy, omega, SR, s=1, c=qy, cmap='brg')

    ax.set_xlabel('$q_y$')
    ax.set_ylabel('$\\omega$')
    ax.set_zlabel('$S$')

    ax.set_xticks(np.arange(0, numb_qy, 2))

    # Get rid of colored axes planes
    # First remove fill
    ax.xaxis.pane.fill = False
    ax.yaxis.pane.fill = False
    ax.zaxis.pane.fill = False

    # Now set color to white (or whatever is "invisible")
    ax.xaxis.pane.set_edgecolor('w')
    ax.yaxis.pane.set_edgecolor('w')
    ax.zaxis.pane.set_edgecolor('w')

    # Bonus: To get rid of the grid as well:
    ax.grid(False)

    plt.subplots_adjust(top=1.22, bottom=0.01, right=1, left=-0.15, hspace=0, wspace=0)

    plt.savefig("/home/bart/Documents/papers/SR/notes/figures/" + filename, dpi=300)
    plt.show()


def plot_laughlin_res_3d(numb_qy, omega_min, omega_max, filename):

    ax = plt.subplot(111, projection='3d')

    qy = []
    omega = []
    SR = []

    for qy_value in range(numb_qy):
        file = f"fermions_torus_spec_resp_kysym_V1_n_6_2s_{numb_qy}_ratio_1.000000_qy_{qy_value}" \
               f".omega_{omega_min}-{omega_max}_eps_1e-06.sr.cut"
        with open('stripped_files/' + file, 'r') as csvfile:
            plots = csv.reader(csvfile, delimiter=' ')
            for row in plots:
                qy.append(qy_value)
                omega.append(float(row[0]))
                SR.append(float(row[1]))

    ax.scatter(qy, omega, SR, s=1, c=qy, cmap='brg')

    ax.set_xlabel('$q_y$')
    ax.set_ylabel('$\\omega$')
    ax.set_zlabel('$S$')

    ax.set_xticks(np.arange(0, numb_qy, 2))

    # Get rid of colored axes planes
    # First remove fill
    ax.xaxis.pane.fill = False
    ax.yaxis.pane.fill = False
    ax.zaxis.pane.fill = False

    # Now set color to white (or whatever is "invisible")
    ax.xaxis.pane.set_edgecolor('w')
    ax.yaxis.pane.set_edgecolor('w')
    ax.zaxis.pane.set_edgecolor('w')

    # Bonus: To get rid of the grid as well:
    ax.grid(False)

    plt.subplots_adjust(top=1.22, bottom=0.01, right=1, left=-0.15, hspace=0, wspace=0)

    plt.savefig("/home/bart/Documents/papers/SR/notes/figures/" + filename, dpi=300)
    plt.show()


def plot_3d_coulomb_conv(numb_qy, omega_min, omega_max, filename):

    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    omega = []
    SR = []

    for name in ["coulomb_nbr_eig_30", "coulomb_nbr_eig_40", "coulomb_nbr_eig_50",
                 "coulomb_nbr_eig_60", "coulomb_nbr_eig_70", "coulomb_nbr_eig_80",
                 "coulomb_nbr_eig_90", "coulomb_nbr_eig_100"]:
        file = f"fermions_torus_spec_resp_kysym_{name}_n_6_2s_{numb_qy}_ratio_1.000000_qy_0" \
               f".omega_{omega_min}-{omega_max}_eps_0.0001.sr.cut"
        with open('stripped_files/' + file, 'r') as csvfile:
            plots = csv.reader(csvfile, delimiter=' ')
            for row in plots:
                omega.append(float(row[0]))
                SR.append(float(row[1]))

    nbr_eig = [30]*10000 + [40]*10000 + [50]*10000 + [60]*10000 + [70]*10000 + [80]*10000 + [90]*10000 + [100]*10000
    ax.scatter(nbr_eig, omega, SR, s=2, c=nbr_eig, cmap='brg')

    ax.set_xlabel('nbr_eig')
    ax.xaxis.set_major_formatter(FormatStrFormatter('%.3g'))
    ax.set_ylabel('$\\omega$')
    ax.set_zlabel('$S$')

    #ax.set_xticks(np.arange(0, 1.05, 0.1))

    # Get rid of colored axes planes
    # First remove fill
    ax.xaxis.pane.fill = False
    ax.yaxis.pane.fill = False
    ax.zaxis.pane.fill = False

    # Now set color to white (or whatever is "invisible")
    ax.xaxis.pane.set_edgecolor('w')
    ax.yaxis.pane.set_edgecolor('w')
    ax.zaxis.pane.set_edgecolor('w')

    # Bonus: To get rid of the grid as well:
    ax.grid(False)

    fig.subplots_adjust(top=1.2, bottom=0, right=1, left=-0.1, hspace=0, wspace=0)

    plt.savefig("/home/bart/Documents/papers/SR/notes/figures/" + filename, dpi=300)
    plt.show()


# Laughlin perturbed by Coulomb ########################################################################################

def plot_3d_lpc(numb_qy, omega_min, omega_max, filename):

    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    omega = []
    SR = []

    for name in ["coulomb_0.0001_plus_V1", "coulomb_0.000316_plus_V1", "coulomb_0.001_plus_V1", "coulomb_0.00316_plus_V1", "coulomb_0.01_plus_V1", "coulomb_0.0316_plus_V1", "coulomb_0.1_plus_V1", "coulomb_0.316_plus_V1", "coulomb_plus_V1"]:
        file = f"fermions_torus_spec_resp_kysym_{name}_n_6_2s_{numb_qy}_ratio_1.000000_qy_0" \
               f".omega_{omega_min}-{omega_max}_eps_0.0001.sr.cut"
        with open('stripped_files/' + file, 'r') as csvfile:
            plots = csv.reader(csvfile, delimiter=' ')
            for row in plots:
                omega.append(float(row[0]))
                SR.append(float(row[1]))

    log_alpha = [-4]*10000 + [-3.5]*10000 + [-3]*10000 + [-2.5]*10000 + [-2]*10000 + [-1.5]*10000 + [-1]*10000 + [-0.5]*10000 + [0]*10000
    ax.scatter(log_alpha, omega, SR, s=2, c=log_alpha, cmap='brg')

    ax.set_xlabel('$\log \\alpha$')
    ax.xaxis.set_major_formatter(FormatStrFormatter('%.2g'))
    ax.set_ylabel('$\\omega$')
    ax.set_zlabel('$S$')

    #ax.set_xticks(np.arange(0, 1.05, 0.1))

    # Get rid of colored axes planes
    # First remove fill
    ax.xaxis.pane.fill = False
    ax.yaxis.pane.fill = False
    ax.zaxis.pane.fill = False

    # Now set color to white (or whatever is "invisible")
    ax.xaxis.pane.set_edgecolor('w')
    ax.yaxis.pane.set_edgecolor('w')
    ax.zaxis.pane.set_edgecolor('w')

    # Bonus: To get rid of the grid as well:
    ax.grid(False)

    fig.subplots_adjust(top=1.2, bottom=0, right=1, left=-0.1, hspace=0, wspace=0)

    plt.savefig("/home/bart/Documents/papers/SR/notes/figures/" + filename, dpi=300)
    plt.show()


def plot_3d_lpc_linear(numb_qy, omega_min, omega_max, filename):

    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    omega = []
    SR = []
    alpha = []

    for name in ["coulomb_0.01_plus_V1", "coulomb_0.02_plus_V1", "coulomb_0.03_plus_V1", "coulomb_0.04_plus_V1",
                 "coulomb_0.05_plus_V1", "coulomb_0.06_plus_V1", "coulomb_0.07_plus_V1", "coulomb_0.08_plus_V1",
                 "coulomb_0.09_plus_V1", "coulomb_0.1_plus_V1"]:
        file = f"fermions_torus_spec_resp_kysym_{name}_n_6_2s_{numb_qy}_ratio_1.000000_qy_0" \
               f".omega_{omega_min}-{omega_max}_eps_0.0001.sr.cut"
        with open('stripped_files/' + file, 'r') as csvfile:
            plots = csv.reader(csvfile, delimiter=' ')
            for row in plots:
                omega.append(float(row[0]))
                SR.append(float(row[1]))

    for i in range(10):
        alpha += [0.01+0.01*i]*10000

    ax.scatter(alpha, omega, SR, s=2, c=alpha, cmap='brg')

    ax.set_xlabel('$\\alpha$')
    ax.xaxis.set_major_formatter(FormatStrFormatter('%.2g'))
    ax.set_ylabel('$\\omega$')
    ax.set_zlabel('$S$')

    #ax.set_xticks(np.arange(0, 1.05, 0.1))

    # Get rid of colored axes planes
    # First remove fill
    ax.xaxis.pane.fill = False
    ax.yaxis.pane.fill = False
    ax.zaxis.pane.fill = False

    # Now set color to white (or whatever is "invisible")
    ax.xaxis.pane.set_edgecolor('w')
    ax.yaxis.pane.set_edgecolor('w')
    ax.zaxis.pane.set_edgecolor('w')

    # Bonus: To get rid of the grid as well:
    ax.grid(False)

    fig.subplots_adjust(top=1.2, bottom=0, right=1, left=-0.1, hspace=0, wspace=0)

    plt.savefig("/home/bart/Documents/papers/SR/notes/figures/" + filename, dpi=300)
    plt.show()


# Laughlin tune to Coulomb #############################################################################################

def plot_3d_ltc(numb_qy, omega_min, omega_max, filename):

    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    omega = []
    SR = []

    for name in ["coulomb_0.0001_plus_V1_scale_0.9999", "coulomb_0.000316_plus_V1_scale_0.999684",
                 "coulomb_0.001_plus_V1_scale_0.999", "coulomb_0.00316_plus_V1_scale_0.99684",
                 "coulomb_0.01_plus_V1_scale_0.99", "coulomb_0.0316_plus_V1_scale_0.9684",
                 "coulomb_0.1_plus_V1_scale_0.9", "coulomb_0.316_plus_V1_scale_0.684", "coulomb"]:
        file = f"fermions_torus_spec_resp_kysym_{name}_n_6_2s_{numb_qy}_ratio_1.000000_qy_0" \
               f".omega_{omega_min}-{omega_max}_eps_0.0001.sr.cut"
        with open('stripped_files/' + file, 'r') as csvfile:
            plots = csv.reader(csvfile, delimiter=' ')
            for row in plots:
                omega.append(float(row[0])+10)
                SR.append(float(row[1]))

    V3 = [-4]*10000 + [-3.5]*10000 + [-3]*10000 + [-2.5]*10000 + [-2]*10000 + [-1.5]*10000 + [-1]*10000 + [-0.5]*10000 + [0]*10000
    ax.scatter(V3, omega, SR, s=2, c=V3, cmap='brg')

    ax.set_xlabel('$\log \\alpha$')
    ax.xaxis.set_major_formatter(FormatStrFormatter('%.2g'))
    ax.set_ylabel('$\\omega$')
    ax.set_zlabel('$S$')
    ax.set_zlim(0)

    #ax.set_xticks(np.arange(0, 1.05, 0.1))

    # Get rid of colored axes planes
    # First remove fill
    ax.xaxis.pane.fill = False
    ax.yaxis.pane.fill = False
    ax.zaxis.pane.fill = False

    # Now set color to white (or whatever is "invisible")
    ax.xaxis.pane.set_edgecolor('w')
    ax.yaxis.pane.set_edgecolor('w')
    ax.zaxis.pane.set_edgecolor('w')

    # Bonus: To get rid of the grid as well:
    ax.grid(False)

    fig.subplots_adjust(top=1.2, bottom=0, right=1, left=-0.1, hspace=0, wspace=0)

    plt.savefig("/home/bart/Documents/papers/SR/notes/figures/" + filename, dpi=300)
    plt.show()


# Coulomb pseudopotentials #############################################################################################

def plot_3d_cpt_fixed(numb_qy, omega_min, omega_max, filename):

    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    omega = []
    SR = []

    for name in ["coulomb_0_plus_CoulombPlane_trunc_2", "coulomb_0_plus_CoulombPlane_trunc_4",
                 "coulomb_0_plus_CoulombPlane_trunc_6", "coulomb_0_plus_CoulombPlane_trunc_8",
                 "coulomb_0_plus_CoulombPlane_trunc_10"]:
        file = f"fermions_torus_spec_resp_kysym_{name}_n_6_2s_{numb_qy}_ratio_1.000000_qy_0" \
               f".omega_{omega_min}-{omega_max}_eps_0.0001.sr.cut"
        with open('stripped_files/' + file, 'r') as csvfile:
            plots = csv.reader(csvfile, delimiter=' ')
            for row in plots:
                omega.append(float(row[0]))
                SR.append(float(row[1]))

    trunc = [2]*10000 + [4]*10000 + [6]*10000 + [8]*10000 + [10]*10000
    ax.scatter(trunc, omega, SR, s=2, c=trunc, cmap='brg')

    ax.set_xlabel('$\\alpha$')
    ax.xaxis.set_major_formatter(FormatStrFormatter('%.2g'))
    ax.set_ylabel('$\\omega$')
    ax.set_zlabel('$S$')

    #ax.set_xticks(np.arange(0, 1.05, 0.1))

    # Get rid of colored axes planes
    # First remove fill
    ax.xaxis.pane.fill = False
    ax.yaxis.pane.fill = False
    ax.zaxis.pane.fill = False

    # Now set color to white (or whatever is "invisible")
    ax.xaxis.pane.set_edgecolor('w')
    ax.yaxis.pane.set_edgecolor('w')
    ax.zaxis.pane.set_edgecolor('w')

    # Bonus: To get rid of the grid as well:
    ax.grid(False)

    fig.subplots_adjust(top=1.2, bottom=0, right=1, left=-0.1, hspace=0, wspace=0)

    plt.savefig("/home/bart/Documents/papers/SR/notes/figures/" + filename, dpi=300)
    plt.show()


def plot_3d_cpt_fixed_full(numb_qy, omega_min, omega_max, filename):

    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    omega = []
    SR = []

    name_list = []
    lbl = []

    for i in range(2, 40, 2):
        name_list += [f"coulomb_0_plus_CoulombPlane_trunc_{i}"]

    for i, name in enumerate(name_list):
        file = f"fermions_torus_spec_resp_kysym_{name}_n_6_2s_{numb_qy}_ratio_1.000000_qy_0" \
               f".omega_{omega_min}-{omega_max}_eps_0.0001.sr.cut"
        with open('stripped_files/' + file, 'r') as csvfile:
            plots = csv.reader(csvfile, delimiter=' ')
            for row in plots:
                omega.append(float(row[0]))
                SR.append(float(row[1]))
                lbl += [2*i+2]

    ax.scatter(lbl, omega, SR, s=2, c=lbl, cmap='brg')

    ax.set_xlabel('$\\alpha$')
    ax.xaxis.set_major_formatter(FormatStrFormatter('%.2g'))
    ax.set_ylabel('$\\omega$')
    ax.set_zlabel('$S$')

    #ax.set_xticks(np.arange(0, 1.05, 0.1))

    # Get rid of colored axes planes
    # First remove fill
    ax.xaxis.pane.fill = False
    ax.yaxis.pane.fill = False
    ax.zaxis.pane.fill = False

    # Now set color to white (or whatever is "invisible")
    ax.xaxis.pane.set_edgecolor('w')
    ax.yaxis.pane.set_edgecolor('w')
    ax.zaxis.pane.set_edgecolor('w')

    # Bonus: To get rid of the grid as well:
    ax.grid(False)

    fig.subplots_adjust(top=1.2, bottom=0, right=1, left=-0.1, hspace=0, wspace=0)

    plt.savefig("/home/bart/Documents/papers/SR/notes/figures/" + filename, dpi=300)
    plt.show()


def plot_3d_cpt_variable_full(numb_qy, omega_min, omega_max, filename):

    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    omega = []
    SR = []

    name_list = []
    lbl = []

    for i in range(2, 100, 2):
        name_list += [f"coulomb_0_plus_CoulombPlane_trunc_{i}"]
    name_list += ["coulomb_0_plus_CoulombPlane"]

    for i, name in enumerate(name_list):
        file = f"fermions_torus_spec_resp_kysym_{name}_n_6_2s_{numb_qy}_ratio_1.000000_qy_0" \
               f".omega_{omega_min}-{omega_max}_eps_0.0001.sr.cut"
        with open('stripped_files/' + file, 'r') as csvfile:
            plots = csv.reader(csvfile, delimiter=' ')
            for row in plots:
                omega.append(float(row[0]))
                SR.append(float(row[1]))
                lbl += [2*i+2]

    ax.scatter(lbl, omega, SR, s=2, c=lbl, cmap='brg')

    ax.set_xlabel('$\\alpha$')
    ax.xaxis.set_major_formatter(FormatStrFormatter('%.2g'))
    ax.set_ylabel('$\\omega$')
    ax.set_zlabel('$S$')

    #ax.set_xticks(np.arange(0, 1.05, 0.1))

    # Get rid of colored axes planes
    # First remove fill
    ax.xaxis.pane.fill = False
    ax.yaxis.pane.fill = False
    ax.zaxis.pane.fill = False

    # Now set color to white (or whatever is "invisible")
    ax.xaxis.pane.set_edgecolor('w')
    ax.yaxis.pane.set_edgecolor('w')
    ax.zaxis.pane.set_edgecolor('w')

    # Bonus: To get rid of the grid as well:
    ax.grid(False)

    fig.subplots_adjust(top=1.2, bottom=0, right=1, left=-0.1, hspace=0, wspace=0)

    plt.savefig("/home/bart/Documents/papers/SR/notes/figures/" + filename, dpi=300)
    plt.show()


def plot_3d_ypt_variable_full(numb_qy, omega_min, omega_max, filename):

    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    omega = []
    SR = []

    name_list = []
    lbl = []

    for i in range(2, 100, 2):  # 60
        name_list += [f"coulomb_0_plus_YukawaPlaneL100_trunc_{i}"]
    name_list += ["coulomb_0_plus_YukawaPlaneL100"]

    for i, name in enumerate(name_list):
        file = f"fermions_torus_spec_resp_kysym_{name}_n_6_2s_{numb_qy}_ratio_1.000000_qy_0" \
               f".omega_{omega_min}-{omega_max}_eps_0.0001.sr.cut"
        with open('stripped_files/' + file, 'r') as csvfile:
            plots = csv.reader(csvfile, delimiter=' ')
            for row in plots:
                omega.append(float(row[0]))
                SR.append(float(row[1]))
                lbl += [2*i+2]

    ax.scatter(lbl, omega, SR, s=2, c=lbl, cmap='brg')

    ax.set_xlabel('$\\alpha$')
    ax.xaxis.set_major_formatter(FormatStrFormatter('%.2g'))
    ax.set_ylabel('$\\omega$')
    ax.set_zlabel('$S$')

    #ax.set_xticks(np.arange(0, 1.05, 0.1))

    # Get rid of colored axes planes
    # First remove fill
    ax.xaxis.pane.fill = False
    ax.yaxis.pane.fill = False
    ax.zaxis.pane.fill = False

    # Now set color to white (or whatever is "invisible")
    ax.xaxis.pane.set_edgecolor('w')
    ax.yaxis.pane.set_edgecolor('w')
    ax.zaxis.pane.set_edgecolor('w')

    # Bonus: To get rid of the grid as well:
    ax.grid(False)

    fig.subplots_adjust(top=1.2, bottom=0, right=1, left=-0.1, hspace=0, wspace=0)

    plt.savefig("/home/bart/Documents/papers/SR/notes/figures/" + filename, dpi=300)
    plt.show()


# Short and long range interactions ####################################################################################

def plot_3d_lpv3(numb_qy, omega_min, omega_max, filename):

    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    omega = []
    SR = []

    for name in ["V1_V3_0.0001", "V1_V3_0.001", "V1_V3_0.01", "V1_V3_0.1", "V1_V3"]:
        file = f"fermions_torus_spec_resp_kysym_{name}_n_6_2s_{numb_qy}_ratio_1.000000_qy_0" \
               f".omega_{omega_min}-{omega_max}_eps_0.0001.sr.cut"
        with open('stripped_files/' + file, 'r') as csvfile:
            plots = csv.reader(csvfile, delimiter=' ')
            for row in plots:
                omega.append(float(row[0]))
                SR.append(float(row[1]))

    V3 = [-4]*10000 + [-3]*10000 + [-2]*10000 + [-1]*10000 + [0]*10000
    ax.scatter(V3, omega, SR, s=2, c=V3, cmap='brg')

    ax.set_xlabel('$\log \\alpha$')
    ax.xaxis.set_major_formatter(FormatStrFormatter('%.2g'))
    ax.set_ylabel('$\\omega$')
    ax.set_zlabel('$S$')

    #ax.set_xticks(np.arange(0, 1.05, 0.1))

    # Get rid of colored axes planes
    # First remove fill
    ax.xaxis.pane.fill = False
    ax.yaxis.pane.fill = False
    ax.zaxis.pane.fill = False

    # Now set color to white (or whatever is "invisible")
    ax.xaxis.pane.set_edgecolor('w')
    ax.yaxis.pane.set_edgecolor('w')
    ax.zaxis.pane.set_edgecolor('w')

    # Bonus: To get rid of the grid as well:
    ax.grid(False)

    fig.subplots_adjust(top=1.2, bottom=0, right=1, left=-0.1, hspace=0, wspace=0)

    plt.savefig("/home/bart/Documents/papers/SR/notes/figures/" + filename, dpi=300)
    plt.show()


def plot_3d_lpv17(numb_qy, omega_min, omega_max, filename):

    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    omega = []
    SR = []

    for name in ["V1_V17_0.0001", "V1_V17_0.001", "V1_V17_0.01", "V1_V17_0.1", "V1_V17"]:
        file = f"fermions_torus_spec_resp_kysym_{name}_n_6_2s_{numb_qy}_ratio_1.000000_qy_0" \
               f".omega_{omega_min}-{omega_max}_eps_0.0001.sr.cut"
        with open('stripped_files/' + file, 'r') as csvfile:
            plots = csv.reader(csvfile, delimiter=' ')
            for row in plots:
                omega.append(float(row[0]))
                SR.append(float(row[1]))

    V17 = [-4]*10000 + [-3]*10000 + [-2]*10000 + [-1]*10000 + [0]*10000
    ax.scatter(V17, omega, SR, s=2, c=V17, cmap='brg')

    ax.set_xlabel('$\log \\alpha$')
    ax.xaxis.set_major_formatter(FormatStrFormatter('%.2g'))
    ax.set_ylabel('$\\omega$')
    ax.set_zlabel('$S$')

    #ax.set_xticks(np.arange(0, 1.05, 0.1))

    # Get rid of colored axes planes
    # First remove fill
    ax.xaxis.pane.fill = False
    ax.yaxis.pane.fill = False
    ax.zaxis.pane.fill = False

    # Now set color to white (or whatever is "invisible")
    ax.xaxis.pane.set_edgecolor('w')
    ax.yaxis.pane.set_edgecolor('w')
    ax.zaxis.pane.set_edgecolor('w')

    # Bonus: To get rid of the grid as well:
    ax.grid(False)

    fig.subplots_adjust(top=1.2, bottom=0, right=1, left=-0.1, hspace=0, wspace=0)

    plt.savefig("/home/bart/Documents/papers/SR/notes/figures/" + filename, dpi=300)
    plt.show()


def plot_3d_lpv17_res(numb_qy, omega_min, omega_max, filename):

    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    omega = []
    SR = []

    for name in ["V1_V17_0.0001", "V1_V17_0.001", "V1_V17_0.01", "V1_V17_0.1", "V1_V17"]:
        file = f"fermions_torus_spec_resp_kysym_{name}_n_6_2s_{numb_qy}_ratio_1.000000_qy_0" \
               f".omega_{omega_min}-{omega_max}_eps_1e-06.sr.cut"
        with open('stripped_files/' + file, 'r') as csvfile:
            plots = csv.reader(csvfile, delimiter=' ')
            for row in plots:
                omega.append(float(row[0]))
                SR.append(float(row[1]))

    V17 = [-4]*10000 + [-3]*10000 + [-2]*10000 + [-1]*10000 + [0]*10000
    ax.scatter(V17, omega, SR, s=2, c=V17, cmap='brg')

    ax.set_xlabel('$\log \\alpha$')
    ax.xaxis.set_major_formatter(FormatStrFormatter('%.2g'))
    ax.set_ylabel('$\\omega$')
    ax.set_zlabel('$S$')

    #ax.set_xticks(np.arange(0, 1.05, 0.1))

    # Get rid of colored axes planes
    # First remove fill
    ax.xaxis.pane.fill = False
    ax.yaxis.pane.fill = False
    ax.zaxis.pane.fill = False

    # Now set color to white (or whatever is "invisible")
    ax.xaxis.pane.set_edgecolor('w')
    ax.yaxis.pane.set_edgecolor('w')
    ax.zaxis.pane.set_edgecolor('w')

    # Bonus: To get rid of the grid as well:
    ax.grid(False)

    fig.subplots_adjust(top=1.2, bottom=0, right=1, left=-0.1, hspace=0, wspace=0)

    plt.savefig("/home/bart/Documents/papers/SR/notes/figures/" + filename, dpi=300)
    plt.show()


if __name__ == "__main__":

    # Coulomb and Laughlin tests #######################################################################################
    #
    # name = "coulomb"
    # plot_3d_q(name, 18, omega_min=-100, omega_max=100, filename=f"{name}_3d.png")
    # name = "coulomb_swap"
    # plot_3d_q(name, 18, omega_min=-100, omega_max=100, filename=f"{name}_3d.png")
    # name = "coulomb_plus_zero"
    # plot_3d_q(name, 18, omega_min=-100, omega_max=100, filename=f"{name}_3d.png")
    # name = "coulomb_plus_zero_swap"
    # plot_3d_q(name, 18, omega_min=-100, omega_max=100, filename=f"{name}_3d.png")
    # name = "coulomb_plus_V1_scale_0.0001"
    # plot_3d_q(name, 18, omega_min=-100, omega_max=100, filename=f"{name}_3d.png")
    # name = "V1"
    # plot_3d_q(name, 18, omega_min=-100, omega_max=100, filename=f"{name}_3d.png")
    # name = "coulomb_0_plus_V1"
    # plot_3d_q(name, 18, omega_min=-100, omega_max=100, filename=f"{name}_3d.png")
    # name = "coulomb_0.0001_plus_V1"
    # plot_3d_q(name, 18, omega_min=-100, omega_max=100, filename=f"{name}_3d.png")
    # plot_laughlin_res_3d(18, omega_min=-25, omega_max=5, filename=f"laughlin_res_3d.png")
    # plot_3d_coulomb_conv(18, omega_min=-100, omega_max=100, filename="coulomb_conv_3d.png")

    # Laughlin perturbed by Coulomb ####################################################################################
    #
    # plot_3d_lpc(18, omega_min=-100, omega_max=100, filename="lpc_3d.png")
    # plot_3d_lpc_linear(18, omega_min=-100, omega_max=100, filename="lpc_linear_3d.png")

    # Laughlin tune to Coulomb #########################################################################################
    #
    # plot_3d_ltc(18, omega_min=-100, omega_max=100, filename="ltc_3d.png")

    # Coulomb pseudopotentials #########################################################################################
    #
    # plot_3d_cpt_fixed(18, omega_min=-100, omega_max=100, filename="cpt_fixed_3d.png")
    # plot_3d_cpt_fixed_full(18, omega_min=-100, omega_max=100, filename="cpt_fixed_full_3d.png")
    plot_3d_cpt_variable_full(18, omega_min=-100, omega_max=100, filename="cpt_variable_full_3d.png")

    # Yukawa pseudopotentials ##########################################################################################
    #
    # plot_3d_ypt_variable_full(18, omega_min=-100, omega_max=100, filename="yptl100_variable_full_3d.png")

    # Short and long range interactions ################################################################################
    #
    # plot_3d_lpv3(18, omega_min=-100, omega_max=100, filename="lpv3_3d.png")
    # plot_3d_lpv17(18, omega_min=-100, omega_max=100, filename="lpv17_3d.png")
    # plot_3d_lpv17_res(18, omega_min=-11, omega_max=-9, filename="lpv17_res_3d.png")
