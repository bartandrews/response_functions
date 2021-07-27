import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import random
import csv
import heapq
import glob
import itertools
import matplotlib.gridspec as gridspec
from matplotlib.ticker import FormatStrFormatter

def plot_2d_q(numb_qy, omega_min, omega_max, filename):

    fig = plt.figure(figsize=(8, 2.5))
    gs = gridspec.GridSpec(1, 2, width_ratios=[1, 1], wspace=0)
    ax = plt.subplot(gs[0])
    ax2 = plt.subplot(gs[1], sharey=ax)

    ax.grid(which='major', axis='y', zorder=-1)
    ax2.grid(which='major', axis='y', zorder=-1)
    ax.set_axisbelow(True)
    ax2.set_axisbelow(True)

    marker = itertools.cycle(('1', '2', '3', '4', ',', '+', '.', 'o', '*', '^', 'v', '>', '<', 'X', '_', 'd', '|', 'H'))

    for qy_value in range(numb_qy):
        omega = []
        SR = []
        file = f"fermions_torus_spec_resp_kysym_unknown_n_6_2s_{numb_qy}_ratio_1.000000_qy_{qy_value}" \
               f".omega_{omega_min}-{omega_max}_eps_0.0001.sr.cut"
        with open('stripped_files/' + file, 'r') as csvfile:
            plots = csv.reader(csvfile, delimiter=' ')
            for row in plots:
                omega.append(float(row[0]))
                SR.append(float(row[1]))
        ax.scatter([x + 30 for x in omega], [x / 1000 for x in SR], s=2, label=qy_value, marker=next(marker))

    for qy_value in range(numb_qy):
        omega = []
        SR = []
        file = f"fermions_torus_spec_resp_kysym_coulomb_0.0001_plus_V1_n_6_2s_{numb_qy}_ratio_1.000000_qy_{qy_value}" \
               f".omega_{omega_min}-{omega_max}_eps_0.0001.sr.cut"
        with open('stripped_files/' + file, 'r') as csvfile:
            plots = csv.reader(csvfile, delimiter=' ')
            for row in plots:
                omega.append(float(row[0]))
                SR.append(float(row[1]))
        ax2.scatter([x + 30 for x in omega], [x / 1000 for x in SR], s=2, label=qy_value, marker=next(marker))

    ax.set_xlabel('$\omega - \omega_0$', fontsize=16)
    ax.set_ylabel('$S / 10^3$', fontsize=16, labelpad=10)
    ax.yaxis.set_major_formatter(FormatStrFormatter('%.2g'))
    ax.set_ylim(bottom=0)
    #ax.text(10, 1000, "hello", fontsize=14)

    ax2.set_xlabel('$\omega - \omega_0$', fontsize=16)
    plt.setp(ax2.get_yticklabels(), visible=False)
    ax2.tick_params('y', direction='inout')

    ax.tick_params(axis='both', which='major', labelsize=14)
    ax2.tick_params(axis='both', which='major', labelsize=14)

    leg = ax2.legend(loc='upper center', bbox_to_anchor=(0, 1.55), handletextpad=0, borderpad=0.4, framealpha=1,
              edgecolor='k', markerscale=5,
              fontsize=14, ncol=9, labelspacing=0, columnspacing=0, title='$q_y$', title_fontsize=14)
    leg.get_frame().set_linewidth(0.5)

    plt.savefig("/home/bart/Documents/Berkeley/research_statement/figures/" + filename, bbox_inches='tight', dpi=300)
    plt.show()


def plot_2d_V3(omega_min, omega_max, filename):

    fig = plt.figure()
    ax = fig.add_subplot(111)

    marker = itertools.cycle(('1', '2', '3', '4', ',', '+', '.', 'o', '*', '^', 'v', '>', '<', 'X', '_', 'd', '|', 'H'))

    for V3 in [0, 0.001, 0.003, 0.01, 0.03, 0.1, 0.3, 1]:
        omega = []
        SR = []
        file = f"fermions_torus_spec_resp_kysym_unknown_n_6_2s_15_ratio_1.000000_qy_0" \
               f".omega_{omega_min}-{omega_max}_eps_0.0001.sr.V3_{V3}.cut"
        with open('stripped_files/' + file, 'r') as csvfile:
            plots = csv.reader(csvfile, delimiter=' ')
            for row in plots:
                omega.append(float(row[0]))
                SR.append(float(row[1]))
        ax.scatter(omega, SR, s=2, label=V3, marker=next(marker))

    ax.set_xlabel('$\omega$')
    ax.set_ylabel('$S$')
    ax.legend(loc='upper right', handletextpad=0, borderpad=0.4, framealpha=1,
              edgecolor='k', markerscale=3,
              fontsize=10, ncol=3, labelspacing=0, columnspacing=0, title='$V_3$')

    fig.subplots_adjust(top=0.95, bottom=0.1, right=0.95, left=0.11)

    plt.savefig("/home/bart/Documents/papers/SR2020/figures/" + filename, dpi=300)
    plt.show()


if __name__ == "__main__":

    plot_2d_q(numb_qy=18, omega_min=-100, omega_max=100, filename="combined_plot2d.png")
    # plot_2d_V3(omega_min=-100, omega_max=100, filename="Laughlin_plot2d_V3.png")
