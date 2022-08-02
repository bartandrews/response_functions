import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
from matplotlib.transforms import Bbox
from mpl_toolkits.mplot3d import Axes3D
import random
import csv
import heapq
import glob
import itertools
import matplotlib.gridspec as gridspec
from matplotlib.ticker import FormatStrFormatter
import matplotlib.ticker as ticker
import matplotlib.colors as colors
from scipy import stats
from scipy.special import hyperu
# from mpmath import sqrt, pi, gamma, hyperu, fac, fac2, exp
import mpmath as mp

plt.rc('text', usetex=True)
plt.rc('text.latex', preamble=r'\usepackage{amsmath}')


def plot_2d_q(axis, name, numb_qy, omega_min, omega_max, epsilon_list):

    marker = itertools.cycle(('1', '2', '3', '4', ',', '+', '.', 'o', '*', '^', 'v', '>', '<', 'X', '_', 'd', '|', 'H'))

    for i, epsilon in enumerate([epsilon_list]):
        omega = []
        SR = []
        file = f"fermions_torus_spec_resp_kysym_{name}_n_6_2s_{numb_qy}_ratio_1.000000_qy_0" \
               f".omega_{omega_min}-{omega_max}_eps_{epsilon}.sr"
        with open('/home/bart/PycharmProjects/response_functions/debug/test/FQHETorusSpectralResponse/laughlin/' + file, 'r') as csvfile:
            plots = csv.reader(csvfile, delimiter=' ')
            for row in plots:
                if name == "V1":
                    if float(row[0]) > -10.1:
                        omega.append(float(row[0]))
                elif name == "coulomb":
                    omega.append(float(row[0]))
                if float(row[0]) > -10.1:
                    SR.append(float(row[1]))
        axis.scatter(omega, SR, s=1, label=epsilon, marker=next(marker))

    axis.set_xlabel('$\omega$')
    axis.xaxis.set_major_formatter(FormatStrFormatter('$%g$'))
    axis.yaxis.set_major_formatter(FormatStrFormatter('$%g$'))
    axis.set_ylabel('$I$')

    leg = axis.legend(loc='upper right', handletextpad=0, borderpad=0.2, framealpha=1,
                      edgecolor=None, markerscale=5, ncol=10, labelspacing=0, columnspacing=0, title='$\\epsilon=\\Delta\\omega$')
    leg.get_frame().set_linewidth(0.5)


if __name__ == "__main__":

    fig = plt.figure(figsize=(6, 6))
    gs = gridspec.GridSpec(3, 2, hspace=0.4, wspace=0.4)

    ax0 = plt.subplot(gs[0])
    plot_2d_q(ax0, "V1", 18, omega_min=-10.1, omega_max=-9.9, epsilon_list="0.0001")
    ax1 = plt.subplot(gs[1])
    plot_2d_q(ax1, "V1", 18, omega_min=-10.1, omega_max=-9.9, epsilon_list="1e-05")
    ax2 = plt.subplot(gs[2])
    plot_2d_q(ax2, "V1", 18, omega_min=-10.1, omega_max=-9.9, epsilon_list="1e-06")
    ax3 = plt.subplot(gs[3])
    plot_2d_q(ax3, "V1", 18, omega_min=-10.1, omega_max=-9.9, epsilon_list="1e-07")
    ax4 = plt.subplot(gs[4])
    plot_2d_q(ax4, "V1", 18, omega_min=-10.1, omega_max=-9.9, epsilon_list="1e-08")

    plt.savefig("epsilon_test.png", bbox_inches='tight', dpi=300)
    plt.show()
