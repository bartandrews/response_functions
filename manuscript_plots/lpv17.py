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


def plot_2d_lpv17(axis, numb_qy, omega_min, omega_max):

    marker = itertools.cycle(('1', '2', '3', '4', ',', '+', '.', 'o', '*', '^', 'v', '>', '<', 'X', '_', 'd', '|', 'H'))

    for i, name in enumerate(["V1_V17_0.0001", "V1_V17_0.001", "V1_V17_0.01", "V1_V17_0.1", "V1_V17"]):
        omega = []
        SR = []
        file = f"fermions_torus_spec_resp_kysym_{name}_n_6_2s_{numb_qy}_ratio_1.000000_qy_0" \
               f".omega_{omega_min}-{omega_max}_eps_0.0001.sr.cut"
        with open('/home/bart/PycharmProjects/response_functions/FQHETorusSpectralResponse/stripped_files/' + file, 'r') as csvfile:
            plots = csv.reader(csvfile, delimiter=' ')
            for row in plots:
                omega.append(float(row[0])+10)
                SR.append(float(row[1])/1000)
        axis.scatter(omega, SR, s=2, label=f"${i-4}$", marker=next(marker))

    axis.set_xlabel('$\omega$')
    axis.xaxis.set_major_formatter(FormatStrFormatter('$%.3g$'))
    axis.set_ylabel('$S/10^3$')
    axis.legend(loc='upper right', handletextpad=0, borderpad=0.4, framealpha=1,
              edgecolor=None, markerscale=3,
              fontsize=10, ncol=1, labelspacing=0, columnspacing=0, title='$\log \\alpha$')

    fig.subplots_adjust(top=0.95, bottom=0.1, right=0.95, left=0.11)


def plot_3d_lpv17(axis, numb_qy, omega_min, omega_max):

    # omega = []
    # SR = []

    for i, name in enumerate(["V1_V17_0.0001", "V1_V17_0.001", "V1_V17_0.01", "V1_V17_0.1", "V1_V17"]):
        omega = []
        SR = []
        file = f"fermions_torus_spec_resp_kysym_{name}_n_6_2s_{numb_qy}_ratio_1.000000_qy_0" \
               f".omega_{omega_min}-{omega_max}_eps_0.0001.sr.cut"
        with open('/home/bart/PycharmProjects/response_functions/FQHETorusSpectralResponse/stripped_files/' + file, 'r') as csvfile:
            plots = csv.reader(csvfile, delimiter=' ')
            for row in plots:
                omega.append(float(row[0])+10)
                SR.append(float(row[1])/1000)

        V17 = [-4+i]*10000
        axis.plot(V17, omega, SR, '.', markersize=3, c=f"C{i}")

    axis.set_xlabel('$\log \\alpha$')
    axis.xaxis.set_major_formatter(FormatStrFormatter('$%.2g$'))
    axis.yaxis.set_major_formatter(FormatStrFormatter('$%.2g$'))
    axis.zaxis.set_major_formatter(FormatStrFormatter('$%.2g$'))
    axis.set_ylabel('$\\omega$')
    axis.set_zlabel('$S/10^3$')

    axis.set_yticks(np.arange(-0.1, 0.11, 0.1))

    # Get rid of colored axes planes
    # First remove fill
    axis.xaxis.pane.fill = False
    axis.yaxis.pane.fill = False
    axis.zaxis.pane.fill = False

    # Now set color to white (or whatever is "invisible")
    axis.xaxis.pane.set_edgecolor('w')
    axis.yaxis.pane.set_edgecolor('w')
    axis.zaxis.pane.set_edgecolor('w')

    # Bonus: To get rid of the grid as well:
    axis.grid(False)

    # fig.subplots_adjust(top=1.2, bottom=0, right=1, left=-0.1, hspace=0, wspace=0)
    axis.set_position(Bbox.from_bounds(0.47, 0.01, 0.45, 1.06))
    axis.tick_params(axis='both', which='major', pad=-2)
    axis.xaxis.labelpad = -1
    axis.yaxis.labelpad = -1
    axis.zaxis.labelpad = -4


if __name__ == "__main__":

    fig = plt.figure(figsize=(6, 2.5))
    gs = gridspec.GridSpec(1, 2, hspace=0.4, wspace=0.4)

    ax0 = plt.subplot(gs[0])
    plot_2d_lpv17(ax0, 18, omega_min=-100, omega_max=100)
    ax1 = plt.subplot(gs[1], projection='3d')
    plot_3d_lpv17(ax1, 18, omega_min=-100, omega_max=100)

    fig.text(0.03, 0.94, "(a)", fontsize=12)
    fig.text(0.51, 0.94, "(b)", fontsize=12)

    #fig.text(0.405, 0.8, "$V_1$", fontsize=11)
    #fig.text(0.79, 0.8, "Coulomb", fontsize=11)

    plt.savefig("/home/bart/Documents/papers/SR/lpv17.png", bbox_inches='tight', dpi=300)
    plt.show()
