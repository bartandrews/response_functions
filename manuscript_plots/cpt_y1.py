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


def plot_2d_cpt_variable_full(axis, numb_qy, omega_min, omega_max):

    marker = itertools.cycle(('1', '2', '3', '4', ',', '+', '.', 'o', '*', '^', 'v', '>', '<', 'X', '_', 'd', '|', 'H'))

    name_list = []
    lbl = []

    for i in range(2, 100, 2):
        name_list += [f"coulomb_0_plus_YukawaPlaneL1_trunc_{i}"]
        lbl += [i]
    name_list += ["coulomb_0_plus_YukawaPlaneL1"]
    lbl += [100]

    for i, name in enumerate(name_list):
        omega = []
        SR = []
        file = f"fermions_torus_spec_resp_kysym_{name}_n_{int(numb_qy/3)}_2s_{numb_qy}_ratio_1.000000_qy_0" \
               f".omega_{omega_min}-{omega_max}_eps_0.0001.sr.cut"
        with open('/home/bart/PycharmProjects/response_functions/FQHETorusSpectralResponse/stripped_files/' + file, 'r') as csvfile:
            plots = csv.reader(csvfile, delimiter=' ')
            for row in plots:
                omega.append(float(row[0])+10)
                SR.append(float(row[1])/1000)
        if lbl[i] % 10 == 0:
            axis.scatter(omega, SR, s=1, label=f"${lbl[i] / 10:g}$", marker=next(marker))


    axis.set_xlabel('$\omega$')
    axis.set_ylabel('$S/10^3$')
    axis.yaxis.set_major_formatter(FormatStrFormatter('$%g$'))
    axis.set_ylim(0)
    axis.legend(loc='upper right', handletextpad=0, borderpad=0.2, framealpha=1,
                edgecolor=None, markerscale=4,
                fontsize=10, ncol=5, labelspacing=0, columnspacing=0, bbox_to_anchor=(1.01, 1.4), title='$\\beta/10$')


def plot_3d_cpt_variable_full(axis, numb_qy, omega_min, omega_max):

    omega = []
    SR = []

    name_list = []
    lbl = []

    for i in range(2, 100, 2):
        name_list += [f"coulomb_0_plus_YukawaPlaneL1_trunc_{i}"]
    name_list += ["coulomb_0_plus_YukawaPlaneL1"]

    for i, name in enumerate(name_list):
        file = f"fermions_torus_spec_resp_kysym_{name}_n_{int(numb_qy/3)}_2s_{numb_qy}_ratio_1.000000_qy_0" \
               f".omega_{omega_min}-{omega_max}_eps_0.0001.sr.cut"
        with open('/home/bart/PycharmProjects/response_functions/FQHETorusSpectralResponse/stripped_files/' + file, 'r') as csvfile:
            plots = csv.reader(csvfile, delimiter=' ')
            for row in plots:
                omega.append(float(row[0])+10)
                SR.append(float(row[1])/1000)
                lbl += [2*i+2]

    axis.scatter(lbl, omega, SR, s=0.1, c=lbl, cmap='brg')

    axis.set_xlabel('$\\beta$')
    axis.xaxis.set_major_formatter(FormatStrFormatter('$%g$'))
    # axis.set_xticks(np.arange(1, 100, 2))
    axis.yaxis.set_major_formatter(FormatStrFormatter('$%g$'))
    axis.set_ylabel('$\\omega$')
    axis.set_zlabel('$S/10^3$')
    axis.set_position(Bbox.from_bounds(0.48, 0.52, 0.44, 0.48))
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

    for i in range(2, 100, 2):  # 40
        name_list += [f"coulomb_0_plus_YukawaPlaneL1_trunc_{i}"]
        lbl += [i]
    name_list += ["coulomb_0_plus_YukawaPlaneL1"]
    lbl += [100]

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

    props = dict(markerfacecolor='b', marker='x', markersize=0.1)
    bp_dict = axis.boxplot(data_to_plot, positions=lbl, flierprops=props, whiskerprops={"linewidth": 0.5}, boxprops={"linewidth": 0.5}, capprops={"linewidth": 0.5}, medianprops={"linewidth": 0.5}, widths=1)

    print(bp_dict['medians'][0].get_ydata()[0])
    print([item.get_ydata() for item in bp_dict['medians']])

    axis.set_xlabel('$\\beta$')
    axis.set_xlim([2, 100])
    axis.set_ylabel('$\omega$')

    # axis.axhline(2.206245, c='r', ls='--', zorder=-10, lw=1)
    # axis.axhspan(1.4377775, 2.7400525, alpha=0.1, color='red')
    #
    # x = np.linspace(0, 100, 256, endpoint = True)
    # ax.plot(x, np.sqrt(np.pi*x)-10, label="$\omega=\sqrt{\pi \\beta}-10$")
    # axis.plot(x, np.sqrt(x)/(2**(-1.25 + 0.25*np.cos(2*x*np.pi))*np.pi**(0.5*np.sin(np.pi*x)**2)), label="asymptotic behaviour of $1/V_m^{(0)}$", lw=0.5, zorder=5)

    pos = np.arange(0, 100.1, 20)
    posy = np.arange(0, 100.1, 20)
    axis.set(xticks=pos, xticklabels=posy)
    axis.xaxis.set_major_formatter(ticker.FormatStrFormatter('$%g$'))
    axis.yaxis.set_major_formatter(ticker.FormatStrFormatter('$%g$'))

    # axis.legend(loc='upper left')


def plot_2d_cpt_variable_full_hist(axis, numb_qy, omega_min, omega_max):

    omega = []
    SR = []

    name_list = []
    lbl = []

    for i in range(2, 100, 2):
        name_list += [f"coulomb_0_plus_YukawaPlaneL1_trunc_{i}"]
    name_list += ["coulomb_0_plus_YukawaPlaneL1"]

    for i, name in enumerate(name_list):
        file = f"fermions_torus_spec_resp_kysym_{name}_n_{int(numb_qy/3)}_2s_{numb_qy}_ratio_1.000000_qy_0" \
               f".omega_{omega_min}-{omega_max}_eps_0.0001.sr.cut"
        with open('/home/bart/PycharmProjects/response_functions/FQHETorusSpectralResponse/stripped_files/' + file, 'r') as csvfile:
            plots = csv.reader(csvfile, delimiter=' ')
            for row in plots:
                omega.append(float(row[0])+10)
                SR.append(float(row[1]))
                lbl += [2*i+2]

    counts, xedges, yedges, im = axis.hist2d(lbl, omega, bins=(19, 50), range=[[1, 101], None], cmap=plt.cm.inferno)
    cb = fig.colorbar(im, ax=axis, format=ticker.FuncFormatter(lambda x, pos: '${0:g}$'.format(x/100)), pad=0.02)
    cb.set_label("percentage of $S$ values", labelpad=5)

    axis.set_xlabel('$\\beta$')
    axis.xaxis.set_major_formatter(FormatStrFormatter('$%g$'))
    axis.set_ylabel('$\\omega$')
    axis.yaxis.set_major_formatter(FormatStrFormatter('$%g$'))

    axis.set_xticks(np.arange(0, 100.1, 20))


if __name__ == "__main__":

    fig = plt.figure(figsize=(6, 5))
    gs = gridspec.GridSpec(2, 2, hspace=0.4, wspace=0.4)

    ax0 = plt.subplot(gs[0])
    plot_2d_cpt_variable_full(ax0, 18, omega_min=-100, omega_max=100)
    ax1 = plt.subplot(gs[1], projection='3d')
    plot_3d_cpt_variable_full(ax1, 18, omega_min=-100, omega_max=100)
    ax2 = plt.subplot(gs[2])
    plot_2d_cpt_variable_full_box(ax2, 18, omega_min=-100, omega_max=100)
    ax3 = plt.subplot(gs[3])
    plot_2d_cpt_variable_full_hist(ax3, 18, omega_min=-100, omega_max=100)

    fig.text(0.02, 0.9, "(a)", fontsize=12)
    fig.text(0.49, 0.9, "(b)", fontsize=12)
    fig.text(0.02, 0.42, "(c)", fontsize=12)
    fig.text(0.49, 0.42, "(d)", fontsize=12)

    plt.savefig("/home/bart/Documents/papers/SR/cpt_y1.png", bbox_inches='tight', dpi=300)
    plt.show()
