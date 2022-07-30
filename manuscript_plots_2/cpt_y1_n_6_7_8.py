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

gs_energies = [0, 0.8038915015368, 2.5450951336863, 3.5508171154871, 4.6025076304994, 5.4976061943948]
coulomb_gs_energy = -1.371144400495800


def plot_3d_cpt_variable_full(axis, numb_qy, omega_min, omega_max):

    omega = []
    SR = []

    name_list = []
    lbl = []

    if axis == ax0:
        for i in range(2, 9, 2):
            name_list += [f"coulomb_0_plus_YukawaPlaneL1_trunc_{i}"]
    else:
        for i in range(2, int(numb_qy/2)+2, 2):
            name_list += [f"coulomb_0_plus_YukawaPlaneL1_trunc_{i}"]

    for i, name in enumerate(name_list):
        file = f"fermions_torus_spec_resp_kysym_{name}_n_{int(numb_qy/3)}_2s_{numb_qy}_ratio_1.000000_qy_0" \
               f".omega_{omega_min}-{omega_max}_eps_0.0001.sr.cut"
        with open('/home/bart/PycharmProjects/response_functions/FQHETorusSpectralResponse/stripped_files/' + file, 'r') as csvfile:
            plots = csv.reader(csvfile, delimiter=' ')
            for row in plots:
                omega.append(float(row[0])+10)
                SR.append(float(row[1])/1000)
                lbl += [2*i+1]

    axis.scatter(lbl, omega, SR, s=0.1, c=lbl, cmap='brg')

    axis.set_xlabel('$\\beta$')
    axis.xaxis.set_major_formatter(FormatStrFormatter('$%g$'))
    if axis == ax0:
        axis.set_xticks(np.arange(1, 8, 2))
    else:
        axis.set_xticks(np.arange(1, int(numb_qy / 2) + 1, 2))
    axis.yaxis.set_major_formatter(FormatStrFormatter('$%g$'))
    axis.set_ylabel('$\\omega$')
    axis.zaxis.set_major_formatter(FormatStrFormatter('$%g$'))
    axis.set_zlabel('$I/10^3$')
    axis.set_facecolor((0, 0, 0, 0))
    if axis == ax0:  # N=6
        axis.set_position(Bbox.from_bounds(0, 0.64, 0.44, 0.28))
    elif axis == ax2:  # N=7
        axis.set_position(Bbox.from_bounds(0, 0.35, 0.44, 0.28))
    elif axis == ax4:  # N=8
        axis.set_position(Bbox.from_bounds(0, 0.07, 0.44, 0.28))
    axis.tick_params(axis='both', which='major', pad=0)
    axis.xaxis.labelpad = 0
    axis.yaxis.labelpad = 0
    axis.zaxis.labelpad = 0

    #ax.set_xticks(np.arange(0, 1.05, 0.1))

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


def plot_2d_cpt_variable_full_box(axis, numb_qy, omega_min, omega_max):

    name_list = []
    lbl = []
    data_to_plot = []

    for i in range(2, int(numb_qy/2)+2, 2):  # 40
        name_list += [f"coulomb_0_plus_YukawaPlaneL1_trunc_{i}"]
        lbl += [i-1]

    for i, name in enumerate(name_list):
        omega = []
        SR = []
        file = f"fermions_torus_spec_resp_kysym_{name}_n_{int(numb_qy/3)}_2s_{numb_qy}_ratio_1.000000_qy_0" \
               f".omega_{omega_min}-{omega_max}_eps_0.0001.sr.cut"
        with open('/home/bart/PycharmProjects/response_functions/FQHETorusSpectralResponse/stripped_files/' + file, 'r') as csvfile:
            plots = csv.reader(csvfile, delimiter=' ')
            for row in plots:
                omega.append(float(row[0])+10)
                SR.append(float(row[1]))
            data_to_plot += [omega]

    props = dict(markerfacecolor='b', marker='x', markersize=5, markeredgewidth=0.01)
    bp_dict = axis.boxplot(data_to_plot, positions=lbl, flierprops=props, whiskerprops={"linewidth": 0.5}, boxprops={"linewidth": 0.5}, capprops={"linewidth": 0.5}, medianprops={"linewidth": 0.5}, widths=1)

    print(bp_dict['medians'][0].get_ydata()[0])
    print([item.get_ydata() for item in bp_dict['medians']])

    axis.set_xlabel('$\\beta$')
    if axis == ax1:
        axis.set_xlim([0, 8])
    elif axis == ax3:
        axis.set_xlim([0, 10])
    elif axis == ax5:
        axis.set_xlim([0, 12])
    axis.set_ylabel('$\omega$')

    if axis == ax1:  # N=6
        axis.axhline(2.264645, c='r', ls='--', zorder=-10, lw=1)
        axis.axhspan(1.4346474999999996, 2.7407224999999995, alpha=0.1, color='red')
    elif axis == ax3:  # N=7
        axis.axhline(2.2973350206643, c='r', ls='--', zorder=-10, lw=1)
        axis.axhspan(1.8468075206813, 2.8201225206444995, alpha=0.1, color='red')
    elif axis == ax5:  # N=8
        axis.axhline(2.8096450206449, c='r', ls='--', zorder=-10, lw=1)
        axis.axhspan(2.3537575206621, 3.1959425206303003, alpha=0.1, color='red')

    axis.xaxis.set_major_formatter(ticker.FormatStrFormatter('$%g$'))
    axis.yaxis.set_major_formatter(ticker.FormatStrFormatter('$%g$'))


if __name__ == "__main__":

    fig = plt.figure(figsize=(6, 7.5))
    gs = gridspec.GridSpec(3, 2, hspace=0.4, wspace=0.4)

    ax0 = plt.subplot(gs[0], projection='3d')
    plot_3d_cpt_variable_full(ax0, 18, omega_min=-100, omega_max=100)
    ax1 = plt.subplot(gs[1])
    plot_2d_cpt_variable_full_box(ax1, 18, omega_min=-100, omega_max=100)
    ax2 = plt.subplot(gs[2], projection='3d')
    plot_3d_cpt_variable_full(ax2, 21, omega_min=-100, omega_max=100)
    ax3 = plt.subplot(gs[3])
    plot_2d_cpt_variable_full_box(ax3, 21, omega_min=-100, omega_max=100)
    ax4 = plt.subplot(gs[4], projection='3d')
    plot_3d_cpt_variable_full(ax4, 24, omega_min=-100, omega_max=100)
    ax5 = plt.subplot(gs[5])
    plot_2d_cpt_variable_full_box(ax5, 24, omega_min=-100, omega_max=100)

    fig.text(0.02, 0.875, "(a)", fontsize=12)
    fig.text(0.2, 0.845, "$N=6$", fontsize=12)
    fig.text(0.49, 0.875, "(b)", fontsize=12)

    fig.text(0.02, 0.59, "(c)", fontsize=12)
    fig.text(0.2, 0.556, "$N=7$", fontsize=12)
    fig.text(0.49, 0.59, "(d)", fontsize=12)

    fig.text(0.02, 0.31, "(e)", fontsize=12)
    fig.text(0.2, 0.275, "$N=8$", fontsize=12)
    fig.text(0.49, 0.31, "(f)", fontsize=12)

    plt.savefig("/home/bart/Documents/papers/SR/cpt_y1_n_6_7_8.png", bbox_inches='tight', dpi=300)
    plt.show()
