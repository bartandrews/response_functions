import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import random
import csv
import heapq
import glob


def plot_3d_q(numb_qy, omega_min, omega_max, filename):

    fig = plt.figure(figsize=(5, 5))
    ax = fig.add_subplot(111, projection='3d')

    qy = []
    omega = []
    SR = []

    for qy_value in range(numb_qy):
        file = f"fermions_torus_spec_resp_kysym_coulomb_0.0001_plus_V1_n_6_2s_{numb_qy}_ratio_1.000000_qy_{qy_value}" \
               f".omega_{omega_min}-{omega_max}_eps_0.0001.sr.cut"
        with open('stripped_files/' + file, 'r') as csvfile:
            plots = csv.reader(csvfile, delimiter=' ')
            for row in plots:
                qy.append(qy_value)
                omega.append(float(row[0]))
                SR.append(float(row[1]))

    ax.scatter(qy, [x + 25 for x in omega], [x / 1000 for x in SR], s=2, c=qy, cmap='brg')

    ax.set_xlabel('$q_y$', fontsize=16, labelpad=6)
    ax.set_ylabel('$\\omega-\\omega_0$', fontsize=16, labelpad=10)
    ax.set_zlabel('$S / 10^{3}$', fontsize=16)

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

    fig.subplots_adjust(top=1.22, bottom=0.01, right=1, left=-0.15, hspace=0, wspace=0)

    ax.tick_params(axis='x', which='major', labelsize=14, pad=-0.5)
    ax.tick_params(axis='y', which='major', labelsize=14)
    ax.tick_params(axis='z', which='major', labelsize=14)

    plt.savefig("/home/bart/Documents/Berkeley/research_statement/figures/" + filename, dpi=300)
    plt.show()


def plot_3d_V3(omega_min, omega_max, filename):

    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    V3 = []
    omega = []
    SR = []

    for V3_value in [0, 0.001, 0.003, 0.01, 0.03, 0.1, 0.3, 1]:
        file = f"fermions_torus_spec_resp_kysym_unknown_n_6_2s_15_ratio_1.000000_qy_0" \
            f".omega_{omega_min}-{omega_max}_eps_0.0001.sr.V3_{V3_value}.cut"
        with open('stripped_files/' + file, 'r') as csvfile:
            plots = csv.reader(csvfile, delimiter=' ')
            for row in plots:
                V3.append(V3_value)
                omega.append(float(row[0]))
                SR.append(float(row[1]))

    ax.scatter(V3, omega, SR, s=2, c=V3, cmap='brg')

    ax.set_xlabel('$V_3$')
    ax.set_ylabel('$\\omega$')
    ax.set_zlabel('$S$')

    ax.set_xticks(np.arange(0, 1.05, 0.1))

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

    plt.savefig("/home/bart/Documents/SR2020/figures/" + filename, dpi=300)
    plt.show()


if __name__ == "__main__":

    plot_3d_q(numb_qy=18, omega_min=-100, omega_max=100, filename="Laughlin_plus_little_Coulomb_plot3d.png")
    # plot_3d_V3(omega_min=-100, omega_max=100, filename="Laughlin_plot3d_V3.png")
