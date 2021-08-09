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
import matplotlib.ticker as ticker
import matplotlib.colors as colors
from scipy import stats
from scipy.special import hyperu
# from mpmath import sqrt, pi, gamma, hyperu, fac, fac2, exp
import mpmath as mp


def line_of_best_fit(axis, x_list, y_list, xval=0.25, yval=1.2):

    parameters, cov = np.polyfit(x_list, y_list, 1, cov=True)
    _, _, r_value, _, _ = stats.linregress(x_list, y_list)
    m, m_err, c, c_err = parameters[0], np.sqrt(cov[0][0]), parameters[1], np.sqrt(cov[1][1])
    r2_value = r_value*r_value

    print("SvN = m*(Ly/lB) + c")
    print(f"(m, m_err, c, c_err) = ({m:.5f}, {m_err:.5f}, {c:.5f}, {c_err:.5f})")
    xvalues = np.linspace(min(x_list), max(x_list))
    axis.plot(xvalues, m * xvalues + c, '-', c='k', zorder=0)
    axis.text(xval, yval, "$y=({gradient:.5f}\pm{gradient_err:.5f})x+{intercept:.5f}$\n$R^2={rsquared:.5f}$".format(
        gradient=m, gradient_err=m_err, intercept=c, rsquared=r2_value, fontsize=10))

    return m, m_err, c, c_err, r2_value


# Coulomb and Laughlin tests ###########################################################################################

def plot_2d_q(name, numb_qy, omega_min, omega_max, filename):

    ax = plt.subplot(111)

    marker = itertools.cycle(('1', '2', '3', '4', ',', '+', '.', 'o', '*', '^', 'v', '>', '<', 'X', '_', 'd', '|', 'H'))

    for qy_value in range(numb_qy):
        omega = []
        SR = []
        file = f"fermions_torus_spec_resp_kysym_{name}_n_6_2s_{numb_qy}_ratio_1.000000_qy_{qy_value}" \
               f".omega_{omega_min}-{omega_max}_eps_0.0001.sr.cut"
        with open('stripped_files/' + file, 'r') as csvfile:
            plots = csv.reader(csvfile, delimiter=' ')
            for row in plots:
                omega.append(float(row[0]))
                SR.append(float(row[1]))
        ax.scatter(omega, SR, s=1, label=qy_value, marker=next(marker))

    ax.set_xlabel('$\omega$')
    ax.set_ylabel('$S$')
    ax.set_ylim(bottom=0)

    leg = ax.legend(loc='upper right', handletextpad=0, borderpad=0.4, framealpha=1,
                    edgecolor='k', markerscale=5, ncol=3, labelspacing=0, columnspacing=0, title='$q_y$')
    leg.get_frame().set_linewidth(0.5)

    plt.savefig("/home/bart/Documents/papers/SR/notes/figures/" + filename, bbox_inches='tight', dpi=300)
    plt.show()


def plot_laughlin_res_2d(numb_qy, omega_min, omega_max, filename):

    ax = plt.subplot(111)

    marker = itertools.cycle(('1', '2', '3', '4', ',', '+', '.', 'o', '*', '^', 'v', '>', '<', 'X', '_', 'd', '|', 'H'))

    for qy_value in range(numb_qy):
        omega = []
        SR = []
        file = f"fermions_torus_spec_resp_kysym_V1_n_6_2s_{numb_qy}_ratio_1.000000_qy_{qy_value}" \
               f".omega_{omega_min}-{omega_max}_eps_1e-06.sr.cut"
        with open('stripped_files/' + file, 'r') as csvfile:
            plots = csv.reader(csvfile, delimiter=' ')
            for row in plots:
                omega.append(float(row[0]))
                SR.append(float(row[1]))
        ax.scatter(omega, SR, s=1, label=qy_value, marker=next(marker))

    ax.set_xlabel('$\omega$')
    ax.set_ylabel('$S$')
    ax.set_ylim(bottom=0)

    leg = ax.legend(loc='upper right', handletextpad=0, borderpad=0.4, framealpha=1,
                    edgecolor='k', markerscale=5, ncol=3, labelspacing=0, columnspacing=0, title='$q_y$')
    leg.get_frame().set_linewidth(0.5)

    plt.savefig("/home/bart/Documents/papers/SR/notes/figures/" + filename, bbox_inches='tight', dpi=300)
    plt.show()


def plot_2d_coulomb_conv_box(numb_qy, omega_min, omega_max, filename):

    fig = plt.figure()
    ax = fig.add_subplot(111)

    name_list = []
    lbl = []
    data_to_plot = []

    for i in range(30, 110, 10):
        name_list += [f"coulomb_nbr_eig_{i}"]
        lbl += [i]

    for i, name in enumerate(name_list):
        omega = []
        SR = []
        file = f"fermions_torus_spec_resp_kysym_{name}_n_6_2s_{numb_qy}_ratio_1.000000_qy_0" \
               f".omega_{omega_min}-{omega_max}_eps_0.0001.sr.cut"
        with open('stripped_files/' + file, 'r') as csvfile:
            plots = csv.reader(csvfile, delimiter=' ')
            for row in plots:
                omega.append(float(row[0])+10)
                SR.append(float(row[1]))
            data_to_plot += [omega]

    props = dict(markerfacecolor='b', marker='x', markersize=5)
    bp_dict = ax.boxplot(data_to_plot, positions=lbl, flierprops=props, widths=5)

    print([item.get_ydata() for item in bp_dict['medians']])
    print([item.get_ydata() for item in bp_dict['boxes']])

    ax.set_xlabel('nbr_eig')
    ax.set_ylabel('$\omega$')

    fig.subplots_adjust(top=0.95, bottom=0.1, right=0.95, left=0.11)

    plt.savefig("/home/bart/Documents/papers/SR/notes/figures/" + filename, bbox_inches='tight', dpi=300)
    plt.show()


# Laughlin perturbed by Coulomb ########################################################################################

def plot_2d_lpc(numb_qy, omega_min, omega_max, filename):

    fig = plt.figure()
    ax = fig.add_subplot(111)

    marker = itertools.cycle(('1', '2', '3', '4', ',', '+', '.', 'o', '*', '^', 'v', '>', '<', 'X', '_', 'd', '|', 'H'))

    for i, name in enumerate(["coulomb_0.0001_plus_V1", "coulomb_0.000316_plus_V1", "coulomb_0.001_plus_V1",
                              "coulomb_0.00316_plus_V1", "coulomb_0.01_plus_V1", "coulomb_0.0316_plus_V1",
                              "coulomb_0.1_plus_V1", "coulomb_0.316_plus_V1", "coulomb_plus_V1"]):
        omega = []
        SR = []
        file = f"fermions_torus_spec_resp_kysym_{name}_n_6_2s_{numb_qy}_ratio_1.000000_qy_0" \
               f".omega_{omega_min}-{omega_max}_eps_0.0001.sr.cut"
        with open('stripped_files/' + file, 'r') as csvfile:
            plots = csv.reader(csvfile, delimiter=' ')
            for row in plots:
                omega.append(float(row[0]))
                SR.append(float(row[1]))
        ax.scatter(omega, SR, s=2, label=f"{i-(4+i/2):.2g}", marker=next(marker))

    ax.set_xlabel('$\omega$')
    ax.set_ylabel('$S$')
    ax.legend(loc='upper right', handletextpad=0, borderpad=0.4, framealpha=1,
              edgecolor='k', markerscale=3,
              fontsize=10, ncol=3, labelspacing=0, columnspacing=0, title='$\log \\alpha$')

    fig.subplots_adjust(top=0.95, bottom=0.1, right=0.95, left=0.11)

    plt.savefig("/home/bart/Documents/papers/SR/notes/figures/" + filename, bbox_inches='tight', dpi=300)
    plt.show()


def plot_2d_lpc_early(numb_qy, omega_min, omega_max, filename):

    fig = plt.figure()
    ax = fig.add_subplot(111)

    marker = itertools.cycle(('1', '2', '3', '4', ',', '+', '.', 'o', '*', '^', 'v', '>', '<', 'X', '_', 'd', '|', 'H'))

    for i, name in enumerate(["coulomb_0.0001_plus_V1", "coulomb_0.0002_plus_V1", "coulomb_0.0003_plus_V1",
                              "coulomb_0.0004_plus_V1", "coulomb_0.0005_plus_V1", "coulomb_0.0006_plus_V1",
                              "coulomb_0.0007_plus_V1", "coulomb_0.0008_plus_V1", "coulomb_0.0009_plus_V1",
                              "coulomb_0.001_plus_V1"]):
        omega = []
        SR = []
        file = f"fermions_torus_spec_resp_kysym_{name}_n_6_2s_{numb_qy}_ratio_1.000000_qy_0" \
               f".omega_{omega_min}-{omega_max}_eps_0.0001.sr.cut"
        with open('stripped_files/' + file, 'r') as csvfile:
            plots = csv.reader(csvfile, delimiter=' ')
            for row in plots:
                omega.append(float(row[0]))
                SR.append(float(row[1]))
        ax.scatter(omega, SR, s=2, label=f"{1*(i+1):.2g}", marker=next(marker))

    ax.set_xlabel('$\omega$')
    ax.set_ylabel('$S$')
    ax.legend(loc='upper right', handletextpad=0, borderpad=0.4, framealpha=1,
              edgecolor='k', markerscale=3,
              fontsize=10, ncol=3, labelspacing=0, columnspacing=0, title='$\\alpha / 10^{-4}$')
    ax.set_xlim([-10.005, -9.99])

    fig.subplots_adjust(top=0.95, bottom=0.1, right=0.95, left=0.11)

    plt.savefig("/home/bart/Documents/papers/SR/notes/figures/" + filename, bbox_inches='tight', dpi=300)
    plt.show()


def plot_2d_lpc_early_max(numb_qy, omega_min, omega_max, filename):

    fig = plt.figure()
    ax = fig.add_subplot(111)

    omega = []
    SR = []

    name_list = []
    lbl = []

    for i, name in enumerate(["coulomb_0.0001_plus_V1", "coulomb_0.0002_plus_V1", "coulomb_0.0003_plus_V1",
                              "coulomb_0.0004_plus_V1", "coulomb_0.0005_plus_V1", "coulomb_0.0006_plus_V1",
                              "coulomb_0.0007_plus_V1", "coulomb_0.0008_plus_V1", "coulomb_0.0009_plus_V1",
                              "coulomb_0.001_plus_V1"]):
        file = f"fermions_torus_spec_resp_kysym_{name}_n_6_2s_{numb_qy}_ratio_1.000000_qy_0" \
               f".omega_{omega_min}-{omega_max}_eps_0.0001.sr.cut"
        with open('stripped_files/' + file, 'r') as csvfile:
            plots = csv.reader(csvfile, delimiter=' ')
            for row in plots:
                omega.append(float(row[0]))
                SR.append(float(row[1]))
                lbl += [0.0001*(i+1)]

    print(np.shape(omega), np.shape(SR), np.shape(lbl))

    omega_max = []
    for i, entry in enumerate(omega):
        if SR[i] > SR[i-1] and SR[i] > SR[i+1] and omega[i] > -10:
            omega_max += [1]
        else:
            omega_max += [0]

    print(omega_max.count(1))

    lbl[:] = [x for i, x in enumerate(lbl) if omega_max[i] == 1]
    omega[:] = [x for i, x in enumerate(omega) if omega_max[i] == 1]

    ax.plot(lbl, omega, '.')

    ax.set_xlabel('$\\alpha$')
    ax.xaxis.set_major_formatter(FormatStrFormatter('%.2g'))
    ax.set_ylabel('$\\omega$')

    # ax.set_xticks(np.arange(2, 40, 2))

    fig.subplots_adjust(top=0.95, bottom=0.1, right=0.95, left=0.11)

    plt.savefig("/home/bart/Documents/papers/SR/notes/figures/" + filename, dpi=300)
    plt.show()


def plot_2d_lpc_linear(numb_qy, omega_min, omega_max, filename):

    fig = plt.figure()
    ax = fig.add_subplot(111)

    marker = itertools.cycle(('1', '2', '3', '4', ',', '+', '.', 'o', '*', '^', 'v', '>', '<', 'X', '_', 'd', '|', 'H'))

    for i, name in enumerate(["coulomb_0.01_plus_V1", "coulomb_0.02_plus_V1", "coulomb_0.03_plus_V1",
                              "coulomb_0.04_plus_V1", "coulomb_0.05_plus_V1", "coulomb_0.06_plus_V1",
                              "coulomb_0.07_plus_V1", "coulomb_0.08_plus_V1", "coulomb_0.09_plus_V1",
                              "coulomb_0.1_plus_V1"]):
        omega = []
        SR = []
        file = f"fermions_torus_spec_resp_kysym_{name}_n_6_2s_{numb_qy}_ratio_1.000000_qy_0" \
               f".omega_{omega_min}-{omega_max}_eps_0.0001.sr.cut"
        with open('stripped_files/' + file, 'r') as csvfile:
            plots = csv.reader(csvfile, delimiter=' ')
            for row in plots:
                omega.append(float(row[0]))
                SR.append(float(row[1]))
        ax.scatter(omega, SR, s=2, label=f"{0.01+0.01*i:.2g}", marker=next(marker))

    ax.set_xlabel('$\omega$')
    ax.set_ylabel('$S$')
    ax.legend(loc='upper right', handletextpad=0, borderpad=0.4, framealpha=1,
              edgecolor='k', markerscale=3,
              fontsize=10, ncol=3, labelspacing=0, columnspacing=0, title='$\\alpha$')

    fig.subplots_adjust(top=0.95, bottom=0.1, right=0.95, left=0.11)

    plt.savefig("/home/bart/Documents/papers/SR/notes/figures/" + filename, bbox_inches='tight', dpi=300)
    plt.show()


def plot_2d_lpc_linear_hist(numb_qy, omega_min, omega_max, filename):

    fig = plt.figure()
    ax = fig.add_subplot(111)

    omega = []
    SR = []

    name_list = []
    lbl = []

    for i, name in enumerate(["coulomb_0.01_plus_V1", "coulomb_0.02_plus_V1", "coulomb_0.03_plus_V1",
                              "coulomb_0.04_plus_V1", "coulomb_0.05_plus_V1", "coulomb_0.06_plus_V1",
                              "coulomb_0.07_plus_V1", "coulomb_0.08_plus_V1", "coulomb_0.09_plus_V1",
                              "coulomb_0.1_plus_V1"]):
        file = f"fermions_torus_spec_resp_kysym_{name}_n_6_2s_{numb_qy}_ratio_1.000000_qy_0" \
               f".omega_{omega_min}-{omega_max}_eps_0.0001.sr.cut"
        with open('stripped_files/' + file, 'r') as csvfile:
            plots = csv.reader(csvfile, delimiter=' ')
            for row in plots:
                omega.append(float(row[0]))
                SR.append(float(row[1]))
                lbl += [0.01*(i+1)]

    counts, xedges, yedges, im = ax.hist2d(lbl, omega, bins=(10, 50), range=[[0, 0.11], None], cmap=plt.cm.inferno)
    fig.colorbar(im, ax=ax, label='percentage of S values',
                 format=ticker.FuncFormatter(lambda x, pos: '{0:g}'.format(x/100)))

    ax.set_xlabel('$\\alpha$')
    ax.xaxis.set_major_formatter(FormatStrFormatter('%.2g'))
    ax.set_ylabel('$\\omega$')

    # ax.set_xticks(np.arange(2, 40, 2))

    fig.subplots_adjust(top=0.95, bottom=0.1, right=0.95, left=0.11)

    plt.savefig("/home/bart/Documents/papers/SR/notes/figures/" + filename, dpi=300)
    plt.show()


def plot_2d_lpc_linear_max(numb_qy, omega_min, omega_max, filename):

    fig = plt.figure()
    ax = fig.add_subplot(111)

    omega = []
    SR = []

    name_list = []
    lbl = []

    for i, name in enumerate(["coulomb_0.01_plus_V1", "coulomb_0.02_plus_V1", "coulomb_0.03_plus_V1",
                              "coulomb_0.04_plus_V1", "coulomb_0.05_plus_V1", "coulomb_0.06_plus_V1",
                              "coulomb_0.07_plus_V1", "coulomb_0.08_plus_V1", "coulomb_0.09_plus_V1",
                              "coulomb_0.1_plus_V1"]):
        file = f"fermions_torus_spec_resp_kysym_{name}_n_6_2s_{numb_qy}_ratio_1.000000_qy_0" \
               f".omega_{omega_min}-{omega_max}_eps_0.0001.sr.cut"
        with open('stripped_files/' + file, 'r') as csvfile:
            plots = csv.reader(csvfile, delimiter=' ')
            for row in plots:
                omega.append(float(row[0]))
                SR.append(float(row[1]))
                lbl += [0.01*(i+1)]

    omega_max = []
    for i, entry in enumerate(omega):
        if SR[i] > SR[i-1] and SR[i] > SR[i+1] and omega[i] > -10:
            omega_max += [1]
        else:
            omega_max += [0]

    lbl[:] = [x for i, x in enumerate(lbl) if omega_max[i] == 1]
    omega[:] = [x for i, x in enumerate(omega) if omega_max[i] == 1]

    ax.plot(lbl, omega, '.')

    ax.set_xlabel('$\\alpha$')
    ax.xaxis.set_major_formatter(FormatStrFormatter('%.2g'))
    ax.set_ylabel('$\\omega$')

    # ax.set_xticks(np.arange(2, 40, 2))

    fig.subplots_adjust(top=0.95, bottom=0.1, right=0.95, left=0.11)

    plt.savefig("/home/bart/Documents/papers/SR/notes/figures/" + filename, dpi=300)
    plt.show()


# Laughlin tune to Coulomb #############################################################################################

def plot_2d_ltc(numb_qy, omega_min, omega_max, filename):

    fig = plt.figure()
    ax = fig.add_subplot(111)

    marker = itertools.cycle(('1', '2', '3', '4', ',', '+', '.', 'o', '*', '^', 'v', '>', '<', 'X', '_', 'd', '|', 'H'))

    for i, name in enumerate(["coulomb_0.0001_plus_V1_scale_0.9999", "coulomb_0.000316_plus_V1_scale_0.999684",
                              "coulomb_0.001_plus_V1_scale_0.999", "coulomb_0.00316_plus_V1_scale_0.99684",
                              "coulomb_0.01_plus_V1_scale_0.99", "coulomb_0.0316_plus_V1_scale_0.9684",
                              "coulomb_0.1_plus_V1_scale_0.9", "coulomb_0.316_plus_V1_scale_0.684", "coulomb"]):
        omega = []
        SR = []
        file = f"fermions_torus_spec_resp_kysym_{name}_n_6_2s_{numb_qy}_ratio_1.000000_qy_0" \
               f".omega_{omega_min}-{omega_max}_eps_0.0001.sr.cut"
        with open('stripped_files/' + file, 'r') as csvfile:
            plots = csv.reader(csvfile, delimiter=' ')
            for row in plots:
                omega.append(float(row[0])+10)
                SR.append(float(row[1]))
        ax.scatter(omega, SR, s=2, label=f"{i-(4+i/2):.2g}", marker=next(marker))

    ax.set_xlabel('$\omega$')
    ax.set_ylabel('$S$')
    ax.set_ylim(0)
    ax.legend(loc='upper right', handletextpad=0, borderpad=0.4, framealpha=1,
              edgecolor='k', markerscale=3,
              fontsize=10, ncol=3, labelspacing=0, columnspacing=0, title='$\log \\alpha$')

    fig.subplots_adjust(top=0.95, bottom=0.1, right=0.95, left=0.11)

    plt.savefig("/home/bart/Documents/papers/SR/notes/figures/" + filename, bbox_inches='tight', dpi=300)
    plt.show()


def plot_2d_ltc_early(numb_qy, omega_min, omega_max, filename):

    fig = plt.figure()
    ax = fig.add_subplot(111)

    marker = itertools.cycle(('1', '2', '3', '4', ',', '+', '.', 'o', '*', '^', 'v', '>', '<', 'X', '_', 'd', '|', 'H'))

    for i, name in enumerate(["coulomb_0.0001_plus_V1_scale_0.9999", "coulomb_0.0002_plus_V1_scale_0.9998",
                              "coulomb_0.0003_plus_V1_scale_0.9997", "coulomb_0.0004_plus_V1_scale_0.9996",
                              "coulomb_0.0005_plus_V1_scale_0.9995", "coulomb_0.0006_plus_V1_scale_0.9994",
                              "coulomb_0.0007_plus_V1_scale_0.9993", "coulomb_0.0008_plus_V1_scale_0.9992",
                              "coulomb_0.0009_plus_V1_scale_0.9991", "coulomb_0.001_plus_V1_scale_0.999"]):
        omega = []
        SR = []
        file = f"fermions_torus_spec_resp_kysym_{name}_n_6_2s_{numb_qy}_ratio_1.000000_qy_0" \
               f".omega_{omega_min}-{omega_max}_eps_0.0001.sr.cut"
        with open('stripped_files/' + file, 'r') as csvfile:
            plots = csv.reader(csvfile, delimiter=' ')
            for row in plots:
                omega.append(float(row[0])+10)
                SR.append(float(row[1]))
        ax.scatter(omega, SR, s=2, label=f"{1*(i+1):.2g}", marker=next(marker))

    ax.set_xlabel('$\omega$')
    ax.set_ylabel('$S$')
    ax.set_ylim(0)
    ax.legend(loc='upper right', handletextpad=0, borderpad=0.4, framealpha=1,
              edgecolor='k', markerscale=3,
              fontsize=10, ncol=3, labelspacing=0, columnspacing=0, title='$\\alpha / 10^{-4}$')
    ax.set_xlim([10-10.005, 10-9.99])

    fig.subplots_adjust(top=0.95, bottom=0.1, right=0.95, left=0.11)

    plt.savefig("/home/bart/Documents/papers/SR/notes/figures/" + filename, bbox_inches='tight', dpi=300)
    plt.show()


def plot_2d_ltc_early_reorth(numb_qy, omega_min, omega_max, filename):

    fig = plt.figure()
    ax = fig.add_subplot(111)

    marker = itertools.cycle(('1', '2', '3', '4', ',', '+', '.', 'o', '*', '^', 'v', '>', '<', 'X', '_', 'd', '|', 'H'))

    for i, name in enumerate(["coulomb_0.0001_plus_V1_reorth_scale_0.9999", "coulomb_0.0002_plus_V1_reorth_scale_0.9998",
                              "coulomb_0.0003_plus_V1_reorth_scale_0.9997", "coulomb_0.0004_plus_V1_reorth_scale_0.9996",
                              "coulomb_0.0005_plus_V1_reorth_scale_0.9995", "coulomb_0.0006_plus_V1_reorth_scale_0.9994",
                              "coulomb_0.0007_plus_V1_reorth_scale_0.9993", "coulomb_0.0008_plus_V1_reorth_scale_0.9992",
                              "coulomb_0.0009_plus_V1_reorth_scale_0.9991", "coulomb_0.001_plus_V1_reorth_scale_0.999"]):
        omega = []
        SR = []
        file = f"fermions_torus_spec_resp_kysym_{name}_n_6_2s_{numb_qy}_ratio_1.000000_qy_0" \
               f".omega_{omega_min}-{omega_max}_eps_0.0001.sr.cut"
        with open('stripped_files/' + file, 'r') as csvfile:
            plots = csv.reader(csvfile, delimiter=' ')
            for row in plots:
                omega.append(float(row[0])+10)
                SR.append(float(row[1]))
        ax.scatter(omega, SR, s=2, label=f"{1*(i+1):.2g}", marker=next(marker))

    ax.set_xlabel('$\omega$')
    ax.set_ylabel('$S$')
    ax.set_ylim(0)
    ax.legend(loc='upper right', handletextpad=0, borderpad=0.4, framealpha=1,
              edgecolor='k', markerscale=3,
              fontsize=10, ncol=3, labelspacing=0, columnspacing=0, title='$\\alpha / 10^{-4}$')
    ax.set_xlim([10-10.005, 10-9.99])

    fig.subplots_adjust(top=0.95, bottom=0.1, right=0.95, left=0.11)

    plt.savefig("/home/bart/Documents/papers/SR/notes/figures/" + filename, bbox_inches='tight', dpi=300)
    plt.show()


def plot_2d_ltc_early_max(numb_qy, omega_min, omega_max, filename):

    fig = plt.figure()
    ax = fig.add_subplot(111)

    omega = []
    SR = []

    name_list = []
    lbl = []

    for i, name in enumerate(["coulomb_0.0001_plus_V1_scale_0.9999", "coulomb_0.0002_plus_V1_scale_0.9998",
                              "coulomb_0.0003_plus_V1_scale_0.9997", "coulomb_0.0004_plus_V1_scale_0.9996",
                              "coulomb_0.0005_plus_V1_scale_0.9995", "coulomb_0.0006_plus_V1_scale_0.9994",
                              "coulomb_0.0007_plus_V1_scale_0.9993", "coulomb_0.0008_plus_V1_scale_0.9992",
                              "coulomb_0.0009_plus_V1_scale_0.9991", "coulomb_0.001_plus_V1_scale_0.999"]):
        file = f"fermions_torus_spec_resp_kysym_{name}_n_6_2s_{numb_qy}_ratio_1.000000_qy_0" \
               f".omega_{omega_min}-{omega_max}_eps_0.0001.sr.cut"
        with open('stripped_files/' + file, 'r') as csvfile:
            plots = csv.reader(csvfile, delimiter=' ')
            for row in plots:
                omega.append(float(row[0])+10)
                SR.append(float(row[1]))
                lbl += [0.0001*(i+1)]

    print(np.shape(omega), np.shape(SR), np.shape(lbl))

    omega_max = []
    for i, entry in enumerate(omega):
        if SR[i] > SR[i-1] and SR[i] > SR[i+1] and omega[i] > -10:
            omega_max += [1]
        else:
            omega_max += [0]

    print(omega_max.count(1))

    lbl[:] = [x for i, x in enumerate(lbl) if omega_max[i] == 1]
    omega[:] = [x for i, x in enumerate(omega) if omega_max[i] == 1]

    ax.plot(lbl, omega, '.')

    ax.set_xlabel('$\\alpha$')
    ax.xaxis.set_major_formatter(FormatStrFormatter('%.2g'))
    ax.set_ylabel('$\\omega$')

    # ax.set_xticks(np.arange(2, 40, 2))

    fig.subplots_adjust(top=0.95, bottom=0.1, right=0.95, left=0.11)

    plt.savefig("/home/bart/Documents/papers/SR/notes/figures/" + filename, dpi=300)
    plt.show()


def plot_2d_ltc_early_reorth_max(numb_qy, omega_min, omega_max, filename):

    fig = plt.figure()
    ax = fig.add_subplot(111)

    omega = []
    SR = []

    name_list = []
    lbl = []

    for i, name in enumerate(["coulomb_0.0001_plus_V1_reorth_scale_0.9999", "coulomb_0.0002_plus_V1_reorth_scale_0.9998",
                              "coulomb_0.0003_plus_V1_reorth_scale_0.9997", "coulomb_0.0004_plus_V1_reorth_scale_0.9996",
                              "coulomb_0.0005_plus_V1_reorth_scale_0.9995", "coulomb_0.0006_plus_V1_reorth_scale_0.9994",
                              "coulomb_0.0007_plus_V1_reorth_scale_0.9993", "coulomb_0.0008_plus_V1_reorth_scale_0.9992",
                              "coulomb_0.0009_plus_V1_reorth_scale_0.9991", "coulomb_0.001_plus_V1_reorth_scale_0.999"]):
        file = f"fermions_torus_spec_resp_kysym_{name}_n_6_2s_{numb_qy}_ratio_1.000000_qy_0" \
               f".omega_{omega_min}-{omega_max}_eps_0.0001.sr.cut"
        with open('stripped_files/' + file, 'r') as csvfile:
            plots = csv.reader(csvfile, delimiter=' ')
            for row in plots:
                omega.append(float(row[0])+10)
                SR.append(float(row[1]))
                lbl += [0.0001*(i+1)]

    print(np.shape(omega), np.shape(SR), np.shape(lbl))

    omega_max = []
    for i, entry in enumerate(omega):
        if SR[i] > SR[i-1] and SR[i] > SR[i+1] and omega[i] > -10:
            omega_max += [1]
        else:
            omega_max += [0]

    print(omega_max.count(1))

    lbl[:] = [x for i, x in enumerate(lbl) if omega_max[i] == 1]
    omega[:] = [x for i, x in enumerate(omega) if omega_max[i] == 1]

    ax.plot(lbl, omega, '.')

    ax.set_xlabel('$\\alpha$')
    ax.xaxis.set_major_formatter(FormatStrFormatter('%.2g'))
    ax.set_ylabel('$\\omega$')

    # ax.set_xticks(np.arange(2, 40, 2))

    fig.subplots_adjust(top=0.95, bottom=0.1, right=0.95, left=0.11)

    plt.savefig("/home/bart/Documents/papers/SR/notes/figures/" + filename, dpi=300)
    plt.show()


def plot_2d_ltc_early_res(numb_qy, omega_min, omega_max, filename):

    fig = plt.figure()
    ax = fig.add_subplot(111)

    marker = itertools.cycle(('1', '2', '3', '4', ',', '+', '.', 'o', '*', '^', 'v', '>', '<', 'X', '_', 'd', '|', 'H'))

    for i, name in enumerate(["coulomb_0.0001_plus_V1_scale_0.9999", "coulomb_0.0002_plus_V1_scale_0.9998",
                              "coulomb_0.0003_plus_V1_scale_0.9997", "coulomb_0.0004_plus_V1_scale_0.9996",
                              "coulomb_0.0005_plus_V1_scale_0.9995", "coulomb_0.0006_plus_V1_scale_0.9994",
                              "coulomb_0.0007_plus_V1_scale_0.9993", "coulomb_0.0008_plus_V1_scale_0.9992",
                              "coulomb_0.0009_plus_V1_scale_0.9991", "coulomb_0.001_plus_V1_scale_0.999"]):
        omega = []
        SR = []
        file = f"fermions_torus_spec_resp_kysym_{name}_n_6_2s_{numb_qy}_ratio_1.000000_qy_0" \
               f".omega_{omega_min}-{omega_max}_eps_1e-06.sr.cut"
        with open('stripped_files/' + file, 'r') as csvfile:
            plots = csv.reader(csvfile, delimiter=' ')
            for row in plots:
                omega.append(float(row[0])+10)
                SR.append(float(row[1]))
        ax.scatter(omega, SR, s=2, label=f"{1*(i+1):.2g}", marker=next(marker))

    ax.set_xlabel('$\omega$')
    ax.set_xlim([10-10, 10-9.992])
    ax.set_ylabel('$S$')
    ax.set_ylim(0)
    ax.legend(loc='upper right', handletextpad=0, borderpad=0.4, framealpha=1,
              edgecolor='k', markerscale=3,
              fontsize=10, ncol=3, labelspacing=0, columnspacing=0, title='$\\alpha / 10^{-4}$')
    # ax.set_xlim([-10.005, -9.99])

    fig.subplots_adjust(top=0.95, bottom=0.1, right=0.95, left=0.11)

    plt.savefig("/home/bart/Documents/papers/SR/notes/figures/" + filename, bbox_inches='tight', dpi=300)
    plt.show()


def plot_2d_ltc_early_reorth_res(numb_qy, omega_min, omega_max, filename):

    fig = plt.figure()
    ax = fig.add_subplot(111)

    marker = itertools.cycle(('1', '2', '3', '4', ',', '+', '.', 'o', '*', '^', 'v', '>', '<', 'X', '_', 'd', '|', 'H'))

    for i, name in enumerate(["coulomb_0.0001_plus_V1_reorth_scale_0.9999", "coulomb_0.0002_plus_V1_reorth_scale_0.9998",
                              "coulomb_0.0003_plus_V1_reorth_scale_0.9997", "coulomb_0.0004_plus_V1_reorth_scale_0.9996",
                              "coulomb_0.0005_plus_V1_reorth_scale_0.9995", "coulomb_0.0006_plus_V1_reorth_scale_0.9994",
                              "coulomb_0.0007_plus_V1_reorth_scale_0.9993", "coulomb_0.0008_plus_V1_reorth_scale_0.9992",
                              "coulomb_0.0009_plus_V1_reorth_scale_0.9991", "coulomb_0.001_plus_V1_reorth_scale_0.999"]):
        omega = []
        SR = []
        file = f"fermions_torus_spec_resp_kysym_{name}_n_6_2s_{numb_qy}_ratio_1.000000_qy_0" \
               f".omega_{omega_min}-{omega_max}_eps_1e-06.sr.cut"
        with open('stripped_files/' + file, 'r') as csvfile:
            plots = csv.reader(csvfile, delimiter=' ')
            for row in plots:
                omega.append(float(row[0])+10)
                SR.append(float(row[1]))
        ax.scatter(omega, SR, s=2, label=f"{1*(i+1):.2g}", marker=next(marker))

    ax.set_xlabel('$\omega$')
    ax.set_xlim([10-10, 10-9.992])
    ax.set_ylabel('$S$')
    ax.set_ylim(0)
    ax.legend(loc='upper right', handletextpad=0, borderpad=0.4, framealpha=1,
              edgecolor='k', markerscale=3,
              fontsize=10, ncol=3, labelspacing=0, columnspacing=0, title='$\\alpha / 10^{-4}$')
    # ax.set_xlim([-10.005, -9.99])

    fig.subplots_adjust(top=0.95, bottom=0.1, right=0.95, left=0.11)

    plt.savefig("/home/bart/Documents/papers/SR/notes/figures/" + filename, bbox_inches='tight', dpi=300)
    plt.show()


def plot_2d_ltc_early_res_max(numb_qy, omega_min, omega_max, filename):

    fig = plt.figure()
    ax = fig.add_subplot(111)

    omega = []
    SR = []

    name_list = []
    lbl = []

    for i, name in enumerate(["coulomb_0.0001_plus_V1_scale_0.9999", "coulomb_0.0002_plus_V1_scale_0.9998",
                              "coulomb_0.0003_plus_V1_scale_0.9997", "coulomb_0.0004_plus_V1_scale_0.9996",
                              "coulomb_0.0005_plus_V1_scale_0.9995", "coulomb_0.0006_plus_V1_scale_0.9994",
                              "coulomb_0.0007_plus_V1_scale_0.9993", "coulomb_0.0008_plus_V1_scale_0.9992",
                              "coulomb_0.0009_plus_V1_scale_0.9991", "coulomb_0.001_plus_V1_scale_0.999"]):
        file = f"fermions_torus_spec_resp_kysym_{name}_n_6_2s_{numb_qy}_ratio_1.000000_qy_0" \
               f".omega_{omega_min}-{omega_max}_eps_1e-06.sr.cut"
        with open('stripped_files/' + file, 'r') as csvfile:
            plots = csv.reader(csvfile, delimiter=' ')
            for row in plots:
                omega.append(float(row[0])+10)
                SR.append(float(row[1]))
                lbl += [0.0001*(i+1)]

    print(np.shape(omega), np.shape(SR), np.shape(lbl))

    omega_max = []
    sr_max = []
    for i, entry in enumerate(omega):
        if SR[i] > SR[i-1] and SR[i] > SR[i+1] and omega[i] > -10:
            omega_max += [1]
            sr_max += [SR[i]]
        else:
            omega_max += [0]

    print(omega_max.count(1))

    lbl[:] = [x for i, x in enumerate(lbl) if omega_max[i] == 1]
    omega[:] = [x for i, x in enumerate(omega) if omega_max[i] == 1]

    # plot the large S points on top
    zipped = list(zip(lbl, omega, sr_max))
    zipped.sort(key=lambda pair: pair[2])
    lbl, omega, sr_max = zip(*zipped)

    im = ax.scatter(lbl, omega, c=sr_max, s=10, norm=colors.LogNorm(vmin=min(sr_max), vmax=max(sr_max)),
                    cmap=plt.cm.Reds)
    fig.colorbar(im, ax=ax, label='$S$')
    ax.set_xlim([0, 0.0011])
    ax.set_ylim([10-10, 10-9.992])

    ax.set_xlabel('$\\alpha$')
    ax.xaxis.set_major_formatter(FormatStrFormatter('%.2g'))
    ax.set_ylabel('$\\omega$')

    # ax.set_xticks(np.arange(2, 40, 2))

    fig.subplots_adjust(top=0.95, bottom=0.1, right=0.95, left=0.11)

    plt.savefig("/home/bart/Documents/papers/SR/notes/figures/" + filename, dpi=300)
    plt.show()


def plot_2d_ltc_early_reorth_res_max(numb_qy, omega_min, omega_max, filename):

    fig = plt.figure()
    ax = fig.add_subplot(111)

    omega = []
    SR = []

    name_list = []
    lbl = []

    for i, name in enumerate(["coulomb_0.0001_plus_V1_reorth_scale_0.9999", "coulomb_0.0002_plus_V1_reorth_scale_0.9998",
                              "coulomb_0.0003_plus_V1_reorth_scale_0.9997", "coulomb_0.0004_plus_V1_reorth_scale_0.9996",
                              "coulomb_0.0005_plus_V1_reorth_scale_0.9995", "coulomb_0.0006_plus_V1_reorth_scale_0.9994",
                              "coulomb_0.0007_plus_V1_reorth_scale_0.9993", "coulomb_0.0008_plus_V1_reorth_scale_0.9992",
                              "coulomb_0.0009_plus_V1_reorth_scale_0.9991", "coulomb_0.001_plus_V1_reorth_scale_0.999"]):
        file = f"fermions_torus_spec_resp_kysym_{name}_n_6_2s_{numb_qy}_ratio_1.000000_qy_0" \
               f".omega_{omega_min}-{omega_max}_eps_1e-06.sr.cut"
        with open('stripped_files/' + file, 'r') as csvfile:
            plots = csv.reader(csvfile, delimiter=' ')
            for row in plots:
                omega.append(float(row[0])+10)
                SR.append(float(row[1]))
                lbl += [0.0001*(i+1)]

    print(np.shape(omega), np.shape(SR), np.shape(lbl))

    omega_max = []
    sr_max = []
    for i, entry in enumerate(omega):
        if SR[i] > SR[i-1] and SR[i] > SR[i+1] and omega[i] > -10:
            omega_max += [1]
            sr_max += [SR[i]]
        else:
            omega_max += [0]

    print(omega_max.count(1))

    lbl[:] = [x for i, x in enumerate(lbl) if omega_max[i] == 1]
    omega[:] = [x for i, x in enumerate(omega) if omega_max[i] == 1]

    # plot the large S points on top
    zipped = list(zip(lbl, omega, sr_max))
    zipped.sort(key=lambda pair: pair[2])
    lbl, omega, sr_max = zip(*zipped)

    im = ax.scatter(lbl, omega, c=sr_max, s=10, norm=colors.LogNorm(vmin=min(sr_max), vmax=max(sr_max)),
                    cmap=plt.cm.Reds)
    fig.colorbar(im, ax=ax, label='$S$')
    ax.set_xlim([0, 0.0011])
    ax.set_ylim([10-10, 10-9.992])

    ax.set_xlabel('$\\alpha$')
    ax.xaxis.set_major_formatter(FormatStrFormatter('%.2g'))
    ax.set_ylabel('$\\omega$')

    # ax.set_xticks(np.arange(2, 40, 2))

    fig.subplots_adjust(top=0.95, bottom=0.1, right=0.95, left=0.11)

    plt.savefig("/home/bart/Documents/papers/SR/notes/figures/" + filename, dpi=300)
    plt.show()


def plot_2d_ltc_earlyish_res(numb_qy, omega_min, omega_max, filename):

    fig = plt.figure()
    ax = fig.add_subplot(111)

    marker = itertools.cycle(('1', '2', '3', '4', ',', '+', '.', 'o', '*', '^', 'v', '>', '<', 'X', '_', 'd', '|', 'H'))

    for i, name in enumerate(["coulomb_0.001_plus_V1_scale_0.999", "coulomb_0.002_plus_V1_scale_0.998",
                              "coulomb_0.003_plus_V1_scale_0.997", "coulomb_0.004_plus_V1_scale_0.996",
                              "coulomb_0.005_plus_V1_scale_0.995", "coulomb_0.006_plus_V1_scale_0.994",
                              "coulomb_0.007_plus_V1_scale_0.993", "coulomb_0.008_plus_V1_scale_0.992",
                              "coulomb_0.009_plus_V1_scale_0.991", "coulomb_0.01_plus_V1_scale_0.99"]):
        omega = []
        SR = []
        file = f"fermions_torus_spec_resp_kysym_{name}_n_6_2s_{numb_qy}_ratio_1.000000_qy_0" \
               f".omega_{omega_min}-{omega_max}_eps_1e-06.sr.cut"
        with open('stripped_files/' + file, 'r') as csvfile:
            plots = csv.reader(csvfile, delimiter=' ')
            for row in plots:
                omega.append(float(row[0])+10)
                SR.append(float(row[1]))
        ax.scatter(omega, SR, s=2, label=f"{1*(i+1):.2g}", marker=next(marker))

    ax.set_xlabel('$\omega$')
    ax.set_xlim([10-10, 10-9.92])
    ax.set_ylabel('$S$')
    ax.set_ylim(0)
    ax.legend(loc='upper right', handletextpad=0, borderpad=0.4, framealpha=1,
              edgecolor='k', markerscale=3,
              fontsize=10, ncol=3, labelspacing=0, columnspacing=0, title='$\\alpha / 10^{-3}$')
    # ax.set_xlim([-10, -9.9])

    fig.subplots_adjust(top=0.95, bottom=0.1, right=0.95, left=0.11)

    plt.savefig("/home/bart/Documents/papers/SR/notes/figures/" + filename, bbox_inches='tight', dpi=300)
    plt.show()


def plot_2d_ltc_earlyish_res_max(numb_qy, omega_min, omega_max, filename):

    fig = plt.figure()
    ax = fig.add_subplot(111)

    omega = []
    SR = []

    name_list = []
    lbl = []

    for i, name in enumerate(["coulomb_0.001_plus_V1_scale_0.999", "coulomb_0.002_plus_V1_scale_0.998",
                              "coulomb_0.003_plus_V1_scale_0.997", "coulomb_0.004_plus_V1_scale_0.996",
                              "coulomb_0.005_plus_V1_scale_0.995", "coulomb_0.006_plus_V1_scale_0.994",
                              "coulomb_0.007_plus_V1_scale_0.993", "coulomb_0.008_plus_V1_scale_0.992",
                              "coulomb_0.009_plus_V1_scale_0.991", "coulomb_0.01_plus_V1_scale_0.99"]):
        file = f"fermions_torus_spec_resp_kysym_{name}_n_6_2s_{numb_qy}_ratio_1.000000_qy_0" \
               f".omega_{omega_min}-{omega_max}_eps_1e-06.sr.cut"
        with open('stripped_files/' + file, 'r') as csvfile:
            plots = csv.reader(csvfile, delimiter=' ')
            for row in plots:
                omega.append(float(row[0])+10)
                SR.append(float(row[1]))
                lbl += [0.001*(i+1)]

    print(np.shape(omega), np.shape(SR), np.shape(lbl))

    omega_max = []
    sr_max = []
    for i, entry in enumerate(omega):
        if SR[i] > SR[i-1] and SR[i] > SR[i+1] and omega[i] > -10:
            omega_max += [1]
            sr_max += [SR[i]]
        else:
            omega_max += [0]

    print(omega_max.count(1))

    lbl[:] = [x for i, x in enumerate(lbl) if omega_max[i] == 1]
    omega[:] = [x for i, x in enumerate(omega) if omega_max[i] == 1]

    # plot the large S points on top
    zipped = list(zip(lbl, omega, sr_max))
    zipped.sort(key=lambda pair: pair[2])
    lbl, omega, sr_max = zip(*zipped)

    im = ax.scatter(lbl, omega, c=sr_max, s=10, norm=colors.LogNorm(vmin=min(sr_max), vmax=max(sr_max)),
                    cmap=plt.cm.Reds)
    fig.colorbar(im, ax=ax, label='$S$')
    ax.set_xlim([0, 0.011])
    ax.set_ylim([10-10, 10-9.92])

    ax.set_xlabel('$\\alpha$')
    ax.xaxis.set_major_formatter(FormatStrFormatter('%.2g'))
    ax.set_ylabel('$\\omega$')

    # ax.set_xticks(np.arange(2, 40, 2))

    fig.subplots_adjust(top=0.95, bottom=0.1, right=0.95, left=0.11)

    plt.savefig("/home/bart/Documents/papers/SR/notes/figures/" + filename, dpi=300)
    plt.show()


def plot_2d_ltc_latish_res(numb_qy, omega_min, omega_max, filename):

    fig = plt.figure()
    ax = fig.add_subplot(111)

    marker = itertools.cycle(('1', '2', '3', '4', ',', '+', '.', 'o', '*', '^', 'v', '>', '<', 'X', '_', 'd', '|', 'H'))

    for i, name in enumerate(["coulomb_0.01_plus_V1_scale_0.99", "coulomb_0.02_plus_V1_scale_0.98",
                              "coulomb_0.03_plus_V1_scale_0.97", "coulomb_0.04_plus_V1_scale_0.96",
                              "coulomb_0.05_plus_V1_scale_0.95", "coulomb_0.06_plus_V1_scale_0.94",
                              "coulomb_0.07_plus_V1_scale_0.93", "coulomb_0.08_plus_V1_scale_0.92",
                              "coulomb_0.09_plus_V1_scale_0.91", "coulomb_0.1_plus_V1_scale_0.9"]):
        omega = []
        SR = []
        file = f"fermions_torus_spec_resp_kysym_{name}_n_6_2s_{numb_qy}_ratio_1.000000_qy_0" \
               f".omega_{omega_min}-{omega_max}_eps_1e-06.sr.cut"
        with open('stripped_files/' + file, 'r') as csvfile:
            plots = csv.reader(csvfile, delimiter=' ')
            for row in plots:
                omega.append(float(row[0])+10)
                SR.append(float(row[1]))
        ax.scatter(omega, SR, s=2, label=f"{1*(i+1):.2g}", marker=next(marker))

    ax.set_xlabel('$\omega$')
    ax.set_xlim([10-10, 10-9.2])
    ax.set_ylabel('$S$')
    ax.set_ylim(0)
    ax.legend(loc='upper right', handletextpad=0, borderpad=0.4, framealpha=1,
              edgecolor='k', markerscale=3,
              fontsize=10, ncol=3, labelspacing=0, columnspacing=0, title='$\\alpha / 10^{-2}$')
    # ax.set_xlim([-10, -9])

    fig.subplots_adjust(top=0.95, bottom=0.1, right=0.95, left=0.11)

    plt.savefig("/home/bart/Documents/papers/SR/notes/figures/" + filename, bbox_inches='tight', dpi=300)
    plt.show()


def plot_2d_ltc_latish_res_max(numb_qy, omega_min, omega_max, filename):

    fig = plt.figure()
    ax = fig.add_subplot(111)

    omega = []
    SR = []

    name_list = []
    lbl = []

    for i, name in enumerate(["coulomb_0.01_plus_V1_scale_0.99", "coulomb_0.02_plus_V1_scale_0.98",
                              "coulomb_0.03_plus_V1_scale_0.97", "coulomb_0.04_plus_V1_scale_0.96",
                              "coulomb_0.05_plus_V1_scale_0.95", "coulomb_0.06_plus_V1_scale_0.94",
                              "coulomb_0.07_plus_V1_scale_0.93", "coulomb_0.08_plus_V1_scale_0.92",
                              "coulomb_0.09_plus_V1_scale_0.91", "coulomb_0.1_plus_V1_scale_0.9"]):
        file = f"fermions_torus_spec_resp_kysym_{name}_n_6_2s_{numb_qy}_ratio_1.000000_qy_0" \
               f".omega_{omega_min}-{omega_max}_eps_1e-06.sr.cut"
        with open('stripped_files/' + file, 'r') as csvfile:
            plots = csv.reader(csvfile, delimiter=' ')
            for row in plots:
                omega.append(float(row[0])+10)
                SR.append(float(row[1]))
                lbl += [0.01*(i+1)]

    print(np.shape(omega), np.shape(SR), np.shape(lbl))

    omega_max = []
    sr_max = []
    for i, entry in enumerate(omega):
        if SR[i] > SR[i-1] and SR[i] > SR[i+1] and omega[i] > -10:
            omega_max += [1]
            sr_max += [SR[i]]
        else:
            omega_max += [0]

    print(omega_max.count(1))

    lbl[:] = [x for i, x in enumerate(lbl) if omega_max[i] == 1]
    omega[:] = [x for i, x in enumerate(omega) if omega_max[i] == 1]

    # plot the large S points on top
    zipped = list(zip(lbl, omega, sr_max))
    zipped.sort(key=lambda pair: pair[2])
    lbl, omega, sr_max = zip(*zipped)

    im = ax.scatter(lbl, omega, c=sr_max, s=10, norm=colors.LogNorm(vmin=min(sr_max), vmax=max(sr_max)), cmap=plt.cm.Reds)
    fig.colorbar(im, ax=ax, label='$S$')
    ax.set_xlim([0, 0.11])
    ax.set_ylim([10-10, 10-9.2])

    ax.set_xlabel('$\\alpha$')
    ax.xaxis.set_major_formatter(FormatStrFormatter('%.2g'))
    ax.set_ylabel('$\\omega$')

    # ax.set_xticks(np.arange(2, 40, 2))

    fig.subplots_adjust(top=0.95, bottom=0.1, right=0.95, left=0.11)

    plt.savefig("/home/bart/Documents/papers/SR/notes/figures/" + filename, dpi=300)
    plt.show()


def plot_2d_ltc_late_res(numb_qy, omega_min, omega_max, filename):

    fig = plt.figure()
    ax = fig.add_subplot(111)

    marker = itertools.cycle(('1', '2', '3', '4', ',', '+', '.', 'o', '*', '^', 'v', '>', '<', 'X', '_', 'd', '|', 'H'))

    for i, name in enumerate(["coulomb_0.1_plus_V1_scale_0.9", "coulomb_0.2_plus_V1_scale_0.8",
                              "coulomb_0.3_plus_V1_scale_0.7", "coulomb_0.4_plus_V1_scale_0.6",
                              "coulomb_0.5_plus_V1_scale_0.5", "coulomb_0.6_plus_V1_scale_0.4",
                              "coulomb_0.7_plus_V1_scale_0.3", "coulomb_0.8_plus_V1_scale_0.2",
                              "coulomb_0.9_plus_V1_scale_0.1", "coulomb_plus_V1_scale_0"]):
        omega = []
        SR = []
        file = f"fermions_torus_spec_resp_kysym_{name}_n_6_2s_{numb_qy}_ratio_1.000000_qy_0" \
               f".omega_{omega_min}-{omega_max}_eps_1e-06.sr.cut"
        with open('stripped_files/' + file, 'r') as csvfile:
            plots = csv.reader(csvfile, delimiter=' ')
            for row in plots:
                omega.append(float(row[0])+10)
                SR.append(float(row[1]))
        ax.scatter(omega, SR, s=2, label=f"{1*(i+1):.2g}", marker=next(marker))

    ax.set_xlabel('$\omega$')
    ax.set_xlim([10-10, 10-2])
    ax.set_ylabel('$S$')
    ax.set_ylim(0)
    ax.legend(loc='upper right', handletextpad=0, borderpad=0.4, framealpha=1,
              edgecolor='k', markerscale=3,
              fontsize=10, ncol=3, labelspacing=0, columnspacing=0, title='$\\alpha / 10^{-1}$')
    # ax.set_xlim([-10, 0])

    fig.subplots_adjust(top=0.95, bottom=0.1, right=0.95, left=0.11)

    plt.savefig("/home/bart/Documents/papers/SR/notes/figures/" + filename, bbox_inches='tight', dpi=300)
    plt.show()


def plot_2d_ltc_late_res_max(numb_qy, omega_min, omega_max, filename):

    fig = plt.figure()
    ax = fig.add_subplot(111)

    omega = []
    SR = []

    name_list = []
    lbl = []

    for i, name in enumerate(["coulomb_0.1_plus_V1_scale_0.9", "coulomb_0.2_plus_V1_scale_0.8",
                              "coulomb_0.3_plus_V1_scale_0.7", "coulomb_0.4_plus_V1_scale_0.6",
                              "coulomb_0.5_plus_V1_scale_0.5", "coulomb_0.6_plus_V1_scale_0.4",
                              "coulomb_0.7_plus_V1_scale_0.3", "coulomb_0.8_plus_V1_scale_0.2",
                              "coulomb_0.9_plus_V1_scale_0.1", "coulomb_plus_V1_scale_0"]):
        file = f"fermions_torus_spec_resp_kysym_{name}_n_6_2s_{numb_qy}_ratio_1.000000_qy_0" \
               f".omega_{omega_min}-{omega_max}_eps_1e-06.sr.cut"
        with open('stripped_files/' + file, 'r') as csvfile:
            plots = csv.reader(csvfile, delimiter=' ')
            for row in plots:
                omega.append(float(row[0])+10)
                SR.append(float(row[1]))
                lbl += [0.1*(i+1)]

    print(np.shape(omega), np.shape(SR), np.shape(lbl))

    omega_max = []
    sr_max = []
    for i, entry in enumerate(omega):
        if SR[i] > SR[i-1] and SR[i] > SR[i+1] and omega[i] > -10:
            omega_max += [1]
            sr_max += [SR[i]]
        else:
            omega_max += [0]

    print(omega_max.count(1))

    lbl[:] = [x for i, x in enumerate(lbl) if omega_max[i] == 1]
    omega[:] = [x for i, x in enumerate(omega) if omega_max[i] == 1]

    # plot the large S points on top
    zipped = list(zip(lbl, omega, sr_max))
    zipped.sort(key=lambda pair: pair[2])
    lbl, omega, sr_max = zip(*zipped)

    im = ax.scatter(lbl, omega, c=sr_max, s=10, norm=colors.LogNorm(vmin=min(sr_max), vmax=max(sr_max)),
                    cmap=plt.cm.Reds)
    fig.colorbar(im, ax=ax, label='$S$')
    ax.set_xlim([0, 1.1])
    ax.set_ylim([10-10, 10-2])

    ax.set_xlabel('$\\alpha$')
    ax.xaxis.set_major_formatter(FormatStrFormatter('%.2g'))
    ax.set_ylabel('$\\omega$')

    # ax.set_xticks(np.arange(2, 40, 2))

    fig.subplots_adjust(top=0.95, bottom=0.1, right=0.95, left=0.11)

    plt.savefig("/home/bart/Documents/papers/SR/notes/figures/" + filename, dpi=300)
    plt.show()


def plot_2d_ltc_complete_res_max(numb_qy, filename):

    fig = plt.figure()
    ax = fig.add_subplot(111)

    omega = []
    SR = []

    name_list = []
    lbl = []

    for i, file in enumerate([f"fermions_torus_spec_resp_kysym_coulomb_0.0001_plus_V1_scale_0.9999_n_6_2s_{numb_qy}_ratio_1.000000_qy_0.omega_-10--9.992_eps_1e-06.sr.cut",
                              f"fermions_torus_spec_resp_kysym_coulomb_0.000126_plus_V1_scale_0.999874_n_6_2s_{numb_qy}_ratio_1.000000_qy_0.omega_-10--9.992_eps_1e-06.sr.cut",
                              f"fermions_torus_spec_resp_kysym_coulomb_0.000158_plus_V1_scale_0.999842_n_6_2s_{numb_qy}_ratio_1.000000_qy_0.omega_-10--9.992_eps_1e-06.sr.cut",
                              f"fermions_torus_spec_resp_kysym_coulomb_0.0002_plus_V1_scale_0.9998_n_6_2s_{numb_qy}_ratio_1.000000_qy_0.omega_-10--9.992_eps_1e-06.sr.cut",
                              f"fermions_torus_spec_resp_kysym_coulomb_0.000251_plus_V1_scale_0.999749_n_6_2s_{numb_qy}_ratio_1.000000_qy_0.omega_-10--9.992_eps_1e-06.sr.cut",
                              f"fermions_torus_spec_resp_kysym_coulomb_0.000316_plus_V1_scale_0.999684_n_6_2s_{numb_qy}_ratio_1.000000_qy_0.omega_-10--9.992_eps_1e-06.sr.cut",
                              f"fermions_torus_spec_resp_kysym_coulomb_0.000398_plus_V1_scale_0.999602_n_6_2s_{numb_qy}_ratio_1.000000_qy_0.omega_-10--9.992_eps_1e-06.sr.cut",
                              f"fermions_torus_spec_resp_kysym_coulomb_0.000501_plus_V1_scale_0.999499_n_6_2s_{numb_qy}_ratio_1.000000_qy_0.omega_-10--9.992_eps_1e-06.sr.cut",
                              f"fermions_torus_spec_resp_kysym_coulomb_0.000631_plus_V1_scale_0.999369_n_6_2s_{numb_qy}_ratio_1.000000_qy_0.omega_-10--9.992_eps_1e-06.sr.cut",
                              f"fermions_torus_spec_resp_kysym_coulomb_0.000794_plus_V1_scale_0.999206_n_6_2s_{numb_qy}_ratio_1.000000_qy_0.omega_-10--9.992_eps_1e-06.sr.cut",
                              f"fermions_torus_spec_resp_kysym_coulomb_0.001_plus_V1_scale_0.999_n_6_2s_{numb_qy}_ratio_1.000000_qy_0.omega_-10--9.9_eps_1e-06.sr.cut",
                              f"fermions_torus_spec_resp_kysym_coulomb_0.00126_plus_V1_scale_0.99874_n_6_2s_{numb_qy}_ratio_1.000000_qy_0.omega_-10--9.9_eps_1e-06.sr.cut",
                              f"fermions_torus_spec_resp_kysym_coulomb_0.00158_plus_V1_scale_0.99842_n_6_2s_{numb_qy}_ratio_1.000000_qy_0.omega_-10--9.9_eps_1e-06.sr.cut",
                              f"fermions_torus_spec_resp_kysym_coulomb_0.002_plus_V1_scale_0.998_n_6_2s_{numb_qy}_ratio_1.000000_qy_0.omega_-10--9.9_eps_1e-06.sr.cut",
                              f"fermions_torus_spec_resp_kysym_coulomb_0.00251_plus_V1_scale_0.99749_n_6_2s_{numb_qy}_ratio_1.000000_qy_0.omega_-10--9.9_eps_1e-06.sr.cut",
                              f"fermions_torus_spec_resp_kysym_coulomb_0.00316_plus_V1_scale_0.99684_n_6_2s_{numb_qy}_ratio_1.000000_qy_0.omega_-10--9.9_eps_1e-06.sr.cut",
                              f"fermions_torus_spec_resp_kysym_coulomb_0.00398_plus_V1_scale_0.99602_n_6_2s_{numb_qy}_ratio_1.000000_qy_0.omega_-10--9.9_eps_1e-06.sr.cut",
                              f"fermions_torus_spec_resp_kysym_coulomb_0.00501_plus_V1_scale_0.99499_n_6_2s_{numb_qy}_ratio_1.000000_qy_0.omega_-10--9.9_eps_1e-06.sr.cut",
                              f"fermions_torus_spec_resp_kysym_coulomb_0.00631_plus_V1_scale_0.99369_n_6_2s_{numb_qy}_ratio_1.000000_qy_0.omega_-10--9.9_eps_1e-06.sr.cut",
                              f"fermions_torus_spec_resp_kysym_coulomb_0.00794_plus_V1_scale_0.99206_n_6_2s_{numb_qy}_ratio_1.000000_qy_0.omega_-10--9.9_eps_1e-06.sr.cut",
                              f"fermions_torus_spec_resp_kysym_coulomb_0.01_plus_V1_scale_0.99_n_6_2s_{numb_qy}_ratio_1.000000_qy_0.omega_-10--9_eps_1e-06.sr.cut",
                              f"fermions_torus_spec_resp_kysym_coulomb_0.0126_plus_V1_scale_0.9874_n_6_2s_{numb_qy}_ratio_1.000000_qy_0.omega_-10--9_eps_1e-06.sr.cut",
                              f"fermions_torus_spec_resp_kysym_coulomb_0.0158_plus_V1_scale_0.9842_n_6_2s_{numb_qy}_ratio_1.000000_qy_0.omega_-10--9_eps_1e-06.sr.cut",
                              f"fermions_torus_spec_resp_kysym_coulomb_0.02_plus_V1_scale_0.98_n_6_2s_{numb_qy}_ratio_1.000000_qy_0.omega_-10--9_eps_1e-06.sr.cut",
                              f"fermions_torus_spec_resp_kysym_coulomb_0.0251_plus_V1_scale_0.9749_n_6_2s_{numb_qy}_ratio_1.000000_qy_0.omega_-10--9_eps_1e-06.sr.cut",
                              f"fermions_torus_spec_resp_kysym_coulomb_0.0316_plus_V1_scale_0.9684_n_6_2s_{numb_qy}_ratio_1.000000_qy_0.omega_-10--9_eps_1e-06.sr.cut",
                              f"fermions_torus_spec_resp_kysym_coulomb_0.0398_plus_V1_scale_0.9602_n_6_2s_{numb_qy}_ratio_1.000000_qy_0.omega_-10--9_eps_1e-06.sr.cut",
                              f"fermions_torus_spec_resp_kysym_coulomb_0.0501_plus_V1_scale_0.9499_n_6_2s_{numb_qy}_ratio_1.000000_qy_0.omega_-10--9_eps_1e-06.sr.cut",
                              f"fermions_torus_spec_resp_kysym_coulomb_0.0631_plus_V1_scale_0.9369_n_6_2s_{numb_qy}_ratio_1.000000_qy_0.omega_-10--9_eps_1e-06.sr.cut",
                              f"fermions_torus_spec_resp_kysym_coulomb_0.0794_plus_V1_scale_0.9206_n_6_2s_{numb_qy}_ratio_1.000000_qy_0.omega_-10--9_eps_1e-06.sr.cut",
                              f"fermions_torus_spec_resp_kysym_coulomb_0.1_plus_V1_scale_0.9_n_6_2s_{numb_qy}_ratio_1.000000_qy_0.omega_-10-0_eps_1e-06.sr.cut",
                              f"fermions_torus_spec_resp_kysym_coulomb_0.126_plus_V1_scale_0.874_n_6_2s_{numb_qy}_ratio_1.000000_qy_0.omega_-10-0_eps_1e-06.sr.cut",
                              f"fermions_torus_spec_resp_kysym_coulomb_0.158_plus_V1_scale_0.842_n_6_2s_{numb_qy}_ratio_1.000000_qy_0.omega_-10-0_eps_1e-06.sr.cut",
                              f"fermions_torus_spec_resp_kysym_coulomb_0.2_plus_V1_scale_0.8_n_6_2s_{numb_qy}_ratio_1.000000_qy_0.omega_-10-0_eps_1e-06.sr.cut",
                              f"fermions_torus_spec_resp_kysym_coulomb_0.251_plus_V1_scale_0.749_n_6_2s_{numb_qy}_ratio_1.000000_qy_0.omega_-10-0_eps_1e-06.sr.cut",
                              f"fermions_torus_spec_resp_kysym_coulomb_0.316_plus_V1_scale_0.684_n_6_2s_{numb_qy}_ratio_1.000000_qy_0.omega_-10-0_eps_1e-06.sr.cut",
                              f"fermions_torus_spec_resp_kysym_coulomb_0.398_plus_V1_scale_0.602_n_6_2s_{numb_qy}_ratio_1.000000_qy_0.omega_-10-0_eps_1e-06.sr.cut",
                              f"fermions_torus_spec_resp_kysym_coulomb_0.501_plus_V1_scale_0.499_n_6_2s_{numb_qy}_ratio_1.000000_qy_0.omega_-10-0_eps_1e-06.sr.cut",
                              f"fermions_torus_spec_resp_kysym_coulomb_0.631_plus_V1_scale_0.369_n_6_2s_{numb_qy}_ratio_1.000000_qy_0.omega_-10-0_eps_1e-06.sr.cut",
                              f"fermions_torus_spec_resp_kysym_coulomb_0.794_plus_V1_scale_0.206_n_6_2s_{numb_qy}_ratio_1.000000_qy_0.omega_-10-0_eps_1e-06.sr.cut",
                              f"fermions_torus_spec_resp_kysym_coulomb_plus_V1_scale_0_n_6_2s_{numb_qy}_ratio_1.000000_qy_0.omega_-10-0_eps_1e-06.sr.cut"]):

        with open('stripped_files/' + file, 'r') as csvfile:
            plots = csv.reader(csvfile, delimiter=' ')
            for row in plots:
                omega.append(float(row[0])+10)
                SR.append(float(row[1]))
                lbl += [10**(-4+i*0.1)]
                # if i < 10:
                #     lbl += [0.0001*(i+1)]
                # elif 10 <= i < 19:
                #     lbl += [0.001 * (i % 10 + 2)]
                # elif 19 <= i < 28:
                #     lbl += [0.01 * (i % 19 + 2)]
                # elif 28 <= i:
                #     lbl += [0.1 * (i % 28 + 2)]

    print(np.shape(omega), np.shape(SR), np.shape(lbl))

    omega_max = []
    sr_max = []
    for i, entry in enumerate(omega):
        if SR[i] > SR[i-1] and SR[i] > SR[i+1] and omega[i] > 0:
            omega_max += [1]
            sr_max += [SR[i]]
        else:
            omega_max += [0]

    print(omega_max.count(1))

    lbl[:] = [x for i, x in enumerate(lbl) if omega_max[i] == 1]
    omega[:] = [x for i, x in enumerate(omega) if omega_max[i] == 1]

    print(len(omega))

    # plot the large S points on top
    zipped = list(zip(lbl, omega, sr_max))
    zipped.sort(key=lambda pair: pair[2])
    lbl, omega, sr_max = zip(*zipped)

    im = ax.scatter(lbl, omega, c=sr_max, s=10, norm=colors.LogNorm(vmin=min(sr_max), vmax=max(sr_max)),
                    cmap=plt.cm.Reds)
    fig.colorbar(im, ax=ax, label='$S$')
    ax.set_xlim([0.00001, 10])
    ax.set_ylim([0.00001, 10])

    ax.set_xscale('log')
    ax.set_yscale('log')
    ax.set_xlabel('$\\alpha$')
    # ax.xaxis.set_major_formatter(FormatStrFormatter('%.2g'))
    ax.set_ylabel('$\\omega$')

    # ax.set_xticks(np.arange(2, 40, 2))

    fig.subplots_adjust(top=0.95, bottom=0.1, right=0.95, left=0.11)

    plt.savefig("/home/bart/Documents/papers/SR/notes/figures/" + filename, dpi=300)
    plt.show()


def plot_2d_ltc_slope_res_max(numb_qy, filename):

    fig = plt.figure()
    ax = fig.add_subplot(111)

    omega = []
    SR = []

    name_list = []
    lbl = []

    for i, file in enumerate([f"fermions_torus_spec_resp_kysym_coulomb_0.0001_plus_V1_scale_0.9999_n_6_2s_{numb_qy}_ratio_1.000000_qy_0.omega_-10--9.992_eps_1e-06.sr.cut",
                              f"fermions_torus_spec_resp_kysym_coulomb_0.000126_plus_V1_scale_0.999874_n_6_2s_{numb_qy}_ratio_1.000000_qy_0.omega_-10--9.992_eps_1e-06.sr.cut",
                              f"fermions_torus_spec_resp_kysym_coulomb_0.000158_plus_V1_scale_0.999842_n_6_2s_{numb_qy}_ratio_1.000000_qy_0.omega_-10--9.992_eps_1e-06.sr.cut",
                              f"fermions_torus_spec_resp_kysym_coulomb_0.0002_plus_V1_scale_0.9998_n_6_2s_{numb_qy}_ratio_1.000000_qy_0.omega_-10--9.992_eps_1e-06.sr.cut",
                              f"fermions_torus_spec_resp_kysym_coulomb_0.000251_plus_V1_scale_0.999749_n_6_2s_{numb_qy}_ratio_1.000000_qy_0.omega_-10--9.992_eps_1e-06.sr.cut",
                              f"fermions_torus_spec_resp_kysym_coulomb_0.000316_plus_V1_scale_0.999684_n_6_2s_{numb_qy}_ratio_1.000000_qy_0.omega_-10--9.992_eps_1e-06.sr.cut",
                              f"fermions_torus_spec_resp_kysym_coulomb_0.000398_plus_V1_scale_0.999602_n_6_2s_{numb_qy}_ratio_1.000000_qy_0.omega_-10--9.992_eps_1e-06.sr.cut",
                              f"fermions_torus_spec_resp_kysym_coulomb_0.000501_plus_V1_scale_0.999499_n_6_2s_{numb_qy}_ratio_1.000000_qy_0.omega_-10--9.992_eps_1e-06.sr.cut",
                              f"fermions_torus_spec_resp_kysym_coulomb_0.000631_plus_V1_scale_0.999369_n_6_2s_{numb_qy}_ratio_1.000000_qy_0.omega_-10--9.992_eps_1e-06.sr.cut",
                              f"fermions_torus_spec_resp_kysym_coulomb_0.000794_plus_V1_scale_0.999206_n_6_2s_{numb_qy}_ratio_1.000000_qy_0.omega_-10--9.992_eps_1e-06.sr.cut",
                              f"fermions_torus_spec_resp_kysym_coulomb_0.001_plus_V1_scale_0.999_n_6_2s_{numb_qy}_ratio_1.000000_qy_0.omega_-10--9.9_eps_1e-06.sr.cut",
                              f"fermions_torus_spec_resp_kysym_coulomb_0.00126_plus_V1_scale_0.99874_n_6_2s_{numb_qy}_ratio_1.000000_qy_0.omega_-10--9.9_eps_1e-06.sr.cut",
                              f"fermions_torus_spec_resp_kysym_coulomb_0.00158_plus_V1_scale_0.99842_n_6_2s_{numb_qy}_ratio_1.000000_qy_0.omega_-10--9.9_eps_1e-06.sr.cut",
                              f"fermions_torus_spec_resp_kysym_coulomb_0.002_plus_V1_scale_0.998_n_6_2s_{numb_qy}_ratio_1.000000_qy_0.omega_-10--9.9_eps_1e-06.sr.cut",
                              f"fermions_torus_spec_resp_kysym_coulomb_0.00251_plus_V1_scale_0.99749_n_6_2s_{numb_qy}_ratio_1.000000_qy_0.omega_-10--9.9_eps_1e-06.sr.cut",
                              f"fermions_torus_spec_resp_kysym_coulomb_0.00316_plus_V1_scale_0.99684_n_6_2s_{numb_qy}_ratio_1.000000_qy_0.omega_-10--9.9_eps_1e-06.sr.cut",
                              f"fermions_torus_spec_resp_kysym_coulomb_0.00398_plus_V1_scale_0.99602_n_6_2s_{numb_qy}_ratio_1.000000_qy_0.omega_-10--9.9_eps_1e-06.sr.cut",
                              f"fermions_torus_spec_resp_kysym_coulomb_0.00501_plus_V1_scale_0.99499_n_6_2s_{numb_qy}_ratio_1.000000_qy_0.omega_-10--9.9_eps_1e-06.sr.cut",
                              f"fermions_torus_spec_resp_kysym_coulomb_0.00631_plus_V1_scale_0.99369_n_6_2s_{numb_qy}_ratio_1.000000_qy_0.omega_-10--9.9_eps_1e-06.sr.cut",
                              f"fermions_torus_spec_resp_kysym_coulomb_0.00794_plus_V1_scale_0.99206_n_6_2s_{numb_qy}_ratio_1.000000_qy_0.omega_-10--9.9_eps_1e-06.sr.cut",
                              f"fermions_torus_spec_resp_kysym_coulomb_0.01_plus_V1_scale_0.99_n_6_2s_{numb_qy}_ratio_1.000000_qy_0.omega_-10--9_eps_1e-06.sr.cut",
                              f"fermions_torus_spec_resp_kysym_coulomb_0.0126_plus_V1_scale_0.9874_n_6_2s_{numb_qy}_ratio_1.000000_qy_0.omega_-10--9_eps_1e-06.sr.cut",
                              f"fermions_torus_spec_resp_kysym_coulomb_0.0158_plus_V1_scale_0.9842_n_6_2s_{numb_qy}_ratio_1.000000_qy_0.omega_-10--9_eps_1e-06.sr.cut",
                              f"fermions_torus_spec_resp_kysym_coulomb_0.02_plus_V1_scale_0.98_n_6_2s_{numb_qy}_ratio_1.000000_qy_0.omega_-10--9_eps_1e-06.sr.cut",
                              f"fermions_torus_spec_resp_kysym_coulomb_0.0251_plus_V1_scale_0.9749_n_6_2s_{numb_qy}_ratio_1.000000_qy_0.omega_-10--9_eps_1e-06.sr.cut",
                              f"fermions_torus_spec_resp_kysym_coulomb_0.0316_plus_V1_scale_0.9684_n_6_2s_{numb_qy}_ratio_1.000000_qy_0.omega_-10--9_eps_1e-06.sr.cut",
                              f"fermions_torus_spec_resp_kysym_coulomb_0.0398_plus_V1_scale_0.9602_n_6_2s_{numb_qy}_ratio_1.000000_qy_0.omega_-10--9_eps_1e-06.sr.cut",
                              f"fermions_torus_spec_resp_kysym_coulomb_0.0501_plus_V1_scale_0.9499_n_6_2s_{numb_qy}_ratio_1.000000_qy_0.omega_-10--9_eps_1e-06.sr.cut",
                              f"fermions_torus_spec_resp_kysym_coulomb_0.0631_plus_V1_scale_0.9369_n_6_2s_{numb_qy}_ratio_1.000000_qy_0.omega_-10--9_eps_1e-06.sr.cut",
                              f"fermions_torus_spec_resp_kysym_coulomb_0.0794_plus_V1_scale_0.9206_n_6_2s_{numb_qy}_ratio_1.000000_qy_0.omega_-10--9_eps_1e-06.sr.cut",
                              f"fermions_torus_spec_resp_kysym_coulomb_0.1_plus_V1_scale_0.9_n_6_2s_{numb_qy}_ratio_1.000000_qy_0.omega_-10-0_eps_1e-06.sr.cut",
                              f"fermions_torus_spec_resp_kysym_coulomb_0.126_plus_V1_scale_0.874_n_6_2s_{numb_qy}_ratio_1.000000_qy_0.omega_-10-0_eps_1e-06.sr.cut",
                              f"fermions_torus_spec_resp_kysym_coulomb_0.158_plus_V1_scale_0.842_n_6_2s_{numb_qy}_ratio_1.000000_qy_0.omega_-10-0_eps_1e-06.sr.cut",
                              f"fermions_torus_spec_resp_kysym_coulomb_0.2_plus_V1_scale_0.8_n_6_2s_{numb_qy}_ratio_1.000000_qy_0.omega_-10-0_eps_1e-06.sr.cut",
                              f"fermions_torus_spec_resp_kysym_coulomb_0.251_plus_V1_scale_0.749_n_6_2s_{numb_qy}_ratio_1.000000_qy_0.omega_-10-0_eps_1e-06.sr.cut",
                              f"fermions_torus_spec_resp_kysym_coulomb_0.316_plus_V1_scale_0.684_n_6_2s_{numb_qy}_ratio_1.000000_qy_0.omega_-10-0_eps_1e-06.sr.cut",
                              f"fermions_torus_spec_resp_kysym_coulomb_0.398_plus_V1_scale_0.602_n_6_2s_{numb_qy}_ratio_1.000000_qy_0.omega_-10-0_eps_1e-06.sr.cut",
                              f"fermions_torus_spec_resp_kysym_coulomb_0.501_plus_V1_scale_0.499_n_6_2s_{numb_qy}_ratio_1.000000_qy_0.omega_-10-0_eps_1e-06.sr.cut",
                              f"fermions_torus_spec_resp_kysym_coulomb_0.631_plus_V1_scale_0.369_n_6_2s_{numb_qy}_ratio_1.000000_qy_0.omega_-10-0_eps_1e-06.sr.cut",
                              f"fermions_torus_spec_resp_kysym_coulomb_0.794_plus_V1_scale_0.206_n_6_2s_{numb_qy}_ratio_1.000000_qy_0.omega_-10-0_eps_1e-06.sr.cut",
                              f"fermions_torus_spec_resp_kysym_coulomb_plus_V1_scale_0_n_6_2s_{numb_qy}_ratio_1.000000_qy_0.omega_-10-0_eps_1e-06.sr.cut"]):

        with open('stripped_files/' + file, 'r') as csvfile:
            plots = csv.reader(csvfile, delimiter=' ')
            for row in plots:
                omega.append(float(row[0])+10)
                SR.append(float(row[1]))
                lbl += [10 ** (-4 + i * 0.1)]
                # if i < 10:
                #     lbl += [0.0001*(i+1)]
                # elif 10 <= i < 19:
                #     lbl += [0.001 * (i % 10 + 2)]
                # elif 19 <= i < 28:
                #     lbl += [0.01 * (i % 19 + 2)]
                # elif 28 <= i:
                #     lbl += [0.1 * (i % 28 + 2)]

    print(np.shape(omega), np.shape(SR), np.shape(lbl))

    omega_max = []
    sr_max = []
    for i, entry in enumerate(omega):
        if SR[i] > SR[i-1] and SR[i] > SR[i+1] and omega[i] > 0:
            omega_max += [1]
            sr_max += [SR[i]]
        else:
            omega_max += [0]

    print(omega_max.count(1))

    lbl[:] = [x for i, x in enumerate(lbl) if omega_max[i] == 1]
    omega[:] = [x for i, x in enumerate(omega) if omega_max[i] == 1]

    log_omega_range = []
    lbl_values = sorted(list(set(lbl)))
    for lbl_val in lbl_values:
        omega_set = [i for i, e in enumerate(lbl) if e == lbl_val]
        max_val = max(omega[omega_set[0]:omega_set[-1]+1])
        min_val = min(omega[omega_set[0]:omega_set[-1]+1])
        range_val = max_val - min_val
        log_range_val = np.log10(range_val)
        log_omega_range += [log_range_val]

    log_lbl_values = [np.log10(i) for i in lbl_values]
    print(log_lbl_values)
    print(log_omega_range)

    im = ax.scatter(log_lbl_values, log_omega_range, s=10)

    ax.set_xlabel('$\\log_{10}(\\alpha)$')
    ax.xaxis.set_major_formatter(FormatStrFormatter('%g'))
    ax.set_ylabel('$\\log_{10}[\\mathrm{range}(\\Omega)]$')
    ax.yaxis.set_major_formatter(FormatStrFormatter('%g'))

    line_of_best_fit(ax, log_lbl_values, log_omega_range, -4, 0.5)

    # ax.set_xticks(np.arange(2, 40, 2))

    fig.subplots_adjust(top=0.95, bottom=0.1, right=0.95, left=0.11)

    plt.savefig("/home/bart/Documents/papers/SR/notes/figures/" + filename, dpi=300)
    plt.show()


def plot_2d_ltc_nbr_omega_res_max(numb_qy, filename):

    fig = plt.figure()
    ax = fig.add_subplot(111)

    omega = []
    SR = []

    name_list = []
    lbl = []

    for i, file in enumerate([f"fermions_torus_spec_resp_kysym_coulomb_0.0001_plus_V1_scale_0.9999_n_6_2s_{numb_qy}_ratio_1.000000_qy_0.omega_-10--9.992_eps_1e-06.sr.cut",
                              f"fermions_torus_spec_resp_kysym_coulomb_0.000126_plus_V1_scale_0.999874_n_6_2s_{numb_qy}_ratio_1.000000_qy_0.omega_-10--9.992_eps_1e-06.sr.cut",
                              f"fermions_torus_spec_resp_kysym_coulomb_0.000158_plus_V1_scale_0.999842_n_6_2s_{numb_qy}_ratio_1.000000_qy_0.omega_-10--9.992_eps_1e-06.sr.cut",
                              f"fermions_torus_spec_resp_kysym_coulomb_0.0002_plus_V1_scale_0.9998_n_6_2s_{numb_qy}_ratio_1.000000_qy_0.omega_-10--9.992_eps_1e-06.sr.cut",
                              f"fermions_torus_spec_resp_kysym_coulomb_0.000251_plus_V1_scale_0.999749_n_6_2s_{numb_qy}_ratio_1.000000_qy_0.omega_-10--9.992_eps_1e-06.sr.cut",
                              f"fermions_torus_spec_resp_kysym_coulomb_0.000316_plus_V1_scale_0.999684_n_6_2s_{numb_qy}_ratio_1.000000_qy_0.omega_-10--9.992_eps_1e-06.sr.cut",
                              f"fermions_torus_spec_resp_kysym_coulomb_0.000398_plus_V1_scale_0.999602_n_6_2s_{numb_qy}_ratio_1.000000_qy_0.omega_-10--9.992_eps_1e-06.sr.cut",
                              f"fermions_torus_spec_resp_kysym_coulomb_0.000501_plus_V1_scale_0.999499_n_6_2s_{numb_qy}_ratio_1.000000_qy_0.omega_-10--9.992_eps_1e-06.sr.cut",
                              f"fermions_torus_spec_resp_kysym_coulomb_0.000631_plus_V1_scale_0.999369_n_6_2s_{numb_qy}_ratio_1.000000_qy_0.omega_-10--9.992_eps_1e-06.sr.cut",
                              f"fermions_torus_spec_resp_kysym_coulomb_0.000794_plus_V1_scale_0.999206_n_6_2s_{numb_qy}_ratio_1.000000_qy_0.omega_-10--9.992_eps_1e-06.sr.cut",
                              f"fermions_torus_spec_resp_kysym_coulomb_0.001_plus_V1_scale_0.999_n_6_2s_{numb_qy}_ratio_1.000000_qy_0.omega_-10--9.9_eps_1e-06.sr.cut",
                              f"fermions_torus_spec_resp_kysym_coulomb_0.00126_plus_V1_scale_0.99874_n_6_2s_{numb_qy}_ratio_1.000000_qy_0.omega_-10--9.9_eps_1e-06.sr.cut",
                              f"fermions_torus_spec_resp_kysym_coulomb_0.00158_plus_V1_scale_0.99842_n_6_2s_{numb_qy}_ratio_1.000000_qy_0.omega_-10--9.9_eps_1e-06.sr.cut",
                              f"fermions_torus_spec_resp_kysym_coulomb_0.002_plus_V1_scale_0.998_n_6_2s_{numb_qy}_ratio_1.000000_qy_0.omega_-10--9.9_eps_1e-06.sr.cut",
                              f"fermions_torus_spec_resp_kysym_coulomb_0.00251_plus_V1_scale_0.99749_n_6_2s_{numb_qy}_ratio_1.000000_qy_0.omega_-10--9.9_eps_1e-06.sr.cut",
                              f"fermions_torus_spec_resp_kysym_coulomb_0.00316_plus_V1_scale_0.99684_n_6_2s_{numb_qy}_ratio_1.000000_qy_0.omega_-10--9.9_eps_1e-06.sr.cut",
                              f"fermions_torus_spec_resp_kysym_coulomb_0.00398_plus_V1_scale_0.99602_n_6_2s_{numb_qy}_ratio_1.000000_qy_0.omega_-10--9.9_eps_1e-06.sr.cut",
                              f"fermions_torus_spec_resp_kysym_coulomb_0.00501_plus_V1_scale_0.99499_n_6_2s_{numb_qy}_ratio_1.000000_qy_0.omega_-10--9.9_eps_1e-06.sr.cut",
                              f"fermions_torus_spec_resp_kysym_coulomb_0.00631_plus_V1_scale_0.99369_n_6_2s_{numb_qy}_ratio_1.000000_qy_0.omega_-10--9.9_eps_1e-06.sr.cut",
                              f"fermions_torus_spec_resp_kysym_coulomb_0.00794_plus_V1_scale_0.99206_n_6_2s_{numb_qy}_ratio_1.000000_qy_0.omega_-10--9.9_eps_1e-06.sr.cut",
                              f"fermions_torus_spec_resp_kysym_coulomb_0.01_plus_V1_scale_0.99_n_6_2s_{numb_qy}_ratio_1.000000_qy_0.omega_-10--9_eps_1e-06.sr.cut",
                              f"fermions_torus_spec_resp_kysym_coulomb_0.0126_plus_V1_scale_0.9874_n_6_2s_{numb_qy}_ratio_1.000000_qy_0.omega_-10--9_eps_1e-06.sr.cut",
                              f"fermions_torus_spec_resp_kysym_coulomb_0.0158_plus_V1_scale_0.9842_n_6_2s_{numb_qy}_ratio_1.000000_qy_0.omega_-10--9_eps_1e-06.sr.cut",
                              f"fermions_torus_spec_resp_kysym_coulomb_0.02_plus_V1_scale_0.98_n_6_2s_{numb_qy}_ratio_1.000000_qy_0.omega_-10--9_eps_1e-06.sr.cut",
                              f"fermions_torus_spec_resp_kysym_coulomb_0.0251_plus_V1_scale_0.9749_n_6_2s_{numb_qy}_ratio_1.000000_qy_0.omega_-10--9_eps_1e-06.sr.cut",
                              f"fermions_torus_spec_resp_kysym_coulomb_0.0316_plus_V1_scale_0.9684_n_6_2s_{numb_qy}_ratio_1.000000_qy_0.omega_-10--9_eps_1e-06.sr.cut",
                              f"fermions_torus_spec_resp_kysym_coulomb_0.0398_plus_V1_scale_0.9602_n_6_2s_{numb_qy}_ratio_1.000000_qy_0.omega_-10--9_eps_1e-06.sr.cut",
                              f"fermions_torus_spec_resp_kysym_coulomb_0.0501_plus_V1_scale_0.9499_n_6_2s_{numb_qy}_ratio_1.000000_qy_0.omega_-10--9_eps_1e-06.sr.cut",
                              f"fermions_torus_spec_resp_kysym_coulomb_0.0631_plus_V1_scale_0.9369_n_6_2s_{numb_qy}_ratio_1.000000_qy_0.omega_-10--9_eps_1e-06.sr.cut",
                              f"fermions_torus_spec_resp_kysym_coulomb_0.0794_plus_V1_scale_0.9206_n_6_2s_{numb_qy}_ratio_1.000000_qy_0.omega_-10--9_eps_1e-06.sr.cut",
                              f"fermions_torus_spec_resp_kysym_coulomb_0.1_plus_V1_scale_0.9_n_6_2s_{numb_qy}_ratio_1.000000_qy_0.omega_-10-0_eps_1e-06.sr.cut",
                              f"fermions_torus_spec_resp_kysym_coulomb_0.126_plus_V1_scale_0.874_n_6_2s_{numb_qy}_ratio_1.000000_qy_0.omega_-10-0_eps_1e-06.sr.cut",
                              f"fermions_torus_spec_resp_kysym_coulomb_0.158_plus_V1_scale_0.842_n_6_2s_{numb_qy}_ratio_1.000000_qy_0.omega_-10-0_eps_1e-06.sr.cut",
                              f"fermions_torus_spec_resp_kysym_coulomb_0.2_plus_V1_scale_0.8_n_6_2s_{numb_qy}_ratio_1.000000_qy_0.omega_-10-0_eps_1e-06.sr.cut",
                              f"fermions_torus_spec_resp_kysym_coulomb_0.251_plus_V1_scale_0.749_n_6_2s_{numb_qy}_ratio_1.000000_qy_0.omega_-10-0_eps_1e-06.sr.cut",
                              f"fermions_torus_spec_resp_kysym_coulomb_0.316_plus_V1_scale_0.684_n_6_2s_{numb_qy}_ratio_1.000000_qy_0.omega_-10-0_eps_1e-06.sr.cut",
                              f"fermions_torus_spec_resp_kysym_coulomb_0.398_plus_V1_scale_0.602_n_6_2s_{numb_qy}_ratio_1.000000_qy_0.omega_-10-0_eps_1e-06.sr.cut",
                              f"fermions_torus_spec_resp_kysym_coulomb_0.501_plus_V1_scale_0.499_n_6_2s_{numb_qy}_ratio_1.000000_qy_0.omega_-10-0_eps_1e-06.sr.cut",
                              f"fermions_torus_spec_resp_kysym_coulomb_0.631_plus_V1_scale_0.369_n_6_2s_{numb_qy}_ratio_1.000000_qy_0.omega_-10-0_eps_1e-06.sr.cut",
                              f"fermions_torus_spec_resp_kysym_coulomb_0.794_plus_V1_scale_0.206_n_6_2s_{numb_qy}_ratio_1.000000_qy_0.omega_-10-0_eps_1e-06.sr.cut",
                              f"fermions_torus_spec_resp_kysym_coulomb_plus_V1_scale_0_n_6_2s_{numb_qy}_ratio_1.000000_qy_0.omega_-10-0_eps_1e-06.sr.cut"]):

        with open('stripped_files/' + file, 'r') as csvfile:
            plots = csv.reader(csvfile, delimiter=' ')
            for row in plots:
                omega.append(float(row[0])+10)
                SR.append(float(row[1]))
                lbl += [10 ** (-4 + i * 0.1)]
                # if i < 10:
                #     lbl += [0.0001*(i+1)]
                # elif 10 <= i < 19:
                #     lbl += [0.001 * (i % 10 + 2)]
                # elif 19 <= i < 28:
                #     lbl += [0.01 * (i % 19 + 2)]
                # elif 28 <= i:
                #     lbl += [0.1 * (i % 28 + 2)]

    print(np.shape(omega), np.shape(SR), np.shape(lbl))

    omega_max = []
    sr_max = []
    for i, entry in enumerate(omega):
        if SR[i] > SR[i-1] and SR[i] > SR[i+1] and omega[i] > 0:
            omega_max += [1]
            sr_max += [SR[i]]
        else:
            omega_max += [0]

    print(omega_max.count(1))

    lbl[:] = [x for i, x in enumerate(lbl) if omega_max[i] == 1]
    omega[:] = [x for i, x in enumerate(omega) if omega_max[i] == 1]

    len_values = []
    lbl_values = sorted(list(set(lbl)))
    for lbl_val in lbl_values:
        omega_set = [i for i, e in enumerate(lbl) if e == lbl_val]
        len_val = len(omega_set)
        len_values += [len_val]

    log_lbl_values = [np.log10(i) for i in lbl_values]

    im = ax.scatter(log_lbl_values, len_values, s=10)

    ax.set_xlabel('$\\log_{10}(\\alpha)$')
    ax.xaxis.set_major_formatter(FormatStrFormatter('%g'))
    ax.set_ylabel('$n(\\Omega)$')

    ax.axhline(np.mean(len_values), c='k', zorder=-1, linewidth=0.5, linestyle='--')
    ax.axhspan(np.mean(len_values) - np.std(len_values), np.mean(len_values) + np.std(len_values), alpha=0.1, color='red')

    ax.text(-2.5, 100, "$\\langle n(\\Omega) \\rangle = {mean:.3g}\pm {sd:.3g}$".format(
        mean=np.mean(len_values), sd=np.std(len_values), fontsize=10))

    # ax.set_xticks(np.arange(2, 40, 2))

    fig.subplots_adjust(top=0.95, bottom=0.1, right=0.95, left=0.11)

    plt.savefig("/home/bart/Documents/papers/SR/notes/figures/" + filename, dpi=300)
    plt.show()


def plot_2d_ltc_mean_S_res_max(numb_qy, filename):

    fig = plt.figure()
    ax = fig.add_subplot(111)

    omega = []
    SR = []

    name_list = []
    lbl = []

    for i, file in enumerate([f"fermions_torus_spec_resp_kysym_coulomb_0.0001_plus_V1_scale_0.9999_n_6_2s_{numb_qy}_ratio_1.000000_qy_0.omega_-10--9.992_eps_1e-06.sr.cut",
                              f"fermions_torus_spec_resp_kysym_coulomb_0.000126_plus_V1_scale_0.999874_n_6_2s_{numb_qy}_ratio_1.000000_qy_0.omega_-10--9.992_eps_1e-06.sr.cut",
                              f"fermions_torus_spec_resp_kysym_coulomb_0.000158_plus_V1_scale_0.999842_n_6_2s_{numb_qy}_ratio_1.000000_qy_0.omega_-10--9.992_eps_1e-06.sr.cut",
                              f"fermions_torus_spec_resp_kysym_coulomb_0.0002_plus_V1_scale_0.9998_n_6_2s_{numb_qy}_ratio_1.000000_qy_0.omega_-10--9.992_eps_1e-06.sr.cut",
                              f"fermions_torus_spec_resp_kysym_coulomb_0.000251_plus_V1_scale_0.999749_n_6_2s_{numb_qy}_ratio_1.000000_qy_0.omega_-10--9.992_eps_1e-06.sr.cut",
                              f"fermions_torus_spec_resp_kysym_coulomb_0.000316_plus_V1_scale_0.999684_n_6_2s_{numb_qy}_ratio_1.000000_qy_0.omega_-10--9.992_eps_1e-06.sr.cut",
                              f"fermions_torus_spec_resp_kysym_coulomb_0.000398_plus_V1_scale_0.999602_n_6_2s_{numb_qy}_ratio_1.000000_qy_0.omega_-10--9.992_eps_1e-06.sr.cut",
                              f"fermions_torus_spec_resp_kysym_coulomb_0.000501_plus_V1_scale_0.999499_n_6_2s_{numb_qy}_ratio_1.000000_qy_0.omega_-10--9.992_eps_1e-06.sr.cut",
                              f"fermions_torus_spec_resp_kysym_coulomb_0.000631_plus_V1_scale_0.999369_n_6_2s_{numb_qy}_ratio_1.000000_qy_0.omega_-10--9.992_eps_1e-06.sr.cut",
                              f"fermions_torus_spec_resp_kysym_coulomb_0.000794_plus_V1_scale_0.999206_n_6_2s_{numb_qy}_ratio_1.000000_qy_0.omega_-10--9.992_eps_1e-06.sr.cut",
                              f"fermions_torus_spec_resp_kysym_coulomb_0.001_plus_V1_scale_0.999_n_6_2s_{numb_qy}_ratio_1.000000_qy_0.omega_-10--9.9_eps_1e-06.sr.cut",
                              f"fermions_torus_spec_resp_kysym_coulomb_0.00126_plus_V1_scale_0.99874_n_6_2s_{numb_qy}_ratio_1.000000_qy_0.omega_-10--9.9_eps_1e-06.sr.cut",
                              f"fermions_torus_spec_resp_kysym_coulomb_0.00158_plus_V1_scale_0.99842_n_6_2s_{numb_qy}_ratio_1.000000_qy_0.omega_-10--9.9_eps_1e-06.sr.cut",
                              f"fermions_torus_spec_resp_kysym_coulomb_0.002_plus_V1_scale_0.998_n_6_2s_{numb_qy}_ratio_1.000000_qy_0.omega_-10--9.9_eps_1e-06.sr.cut",
                              f"fermions_torus_spec_resp_kysym_coulomb_0.00251_plus_V1_scale_0.99749_n_6_2s_{numb_qy}_ratio_1.000000_qy_0.omega_-10--9.9_eps_1e-06.sr.cut",
                              f"fermions_torus_spec_resp_kysym_coulomb_0.00316_plus_V1_scale_0.99684_n_6_2s_{numb_qy}_ratio_1.000000_qy_0.omega_-10--9.9_eps_1e-06.sr.cut",
                              f"fermions_torus_spec_resp_kysym_coulomb_0.00398_plus_V1_scale_0.99602_n_6_2s_{numb_qy}_ratio_1.000000_qy_0.omega_-10--9.9_eps_1e-06.sr.cut",
                              f"fermions_torus_spec_resp_kysym_coulomb_0.00501_plus_V1_scale_0.99499_n_6_2s_{numb_qy}_ratio_1.000000_qy_0.omega_-10--9.9_eps_1e-06.sr.cut",
                              f"fermions_torus_spec_resp_kysym_coulomb_0.00631_plus_V1_scale_0.99369_n_6_2s_{numb_qy}_ratio_1.000000_qy_0.omega_-10--9.9_eps_1e-06.sr.cut",
                              f"fermions_torus_spec_resp_kysym_coulomb_0.00794_plus_V1_scale_0.99206_n_6_2s_{numb_qy}_ratio_1.000000_qy_0.omega_-10--9.9_eps_1e-06.sr.cut",
                              f"fermions_torus_spec_resp_kysym_coulomb_0.01_plus_V1_scale_0.99_n_6_2s_{numb_qy}_ratio_1.000000_qy_0.omega_-10--9_eps_1e-06.sr.cut",
                              f"fermions_torus_spec_resp_kysym_coulomb_0.0126_plus_V1_scale_0.9874_n_6_2s_{numb_qy}_ratio_1.000000_qy_0.omega_-10--9_eps_1e-06.sr.cut",
                              f"fermions_torus_spec_resp_kysym_coulomb_0.0158_plus_V1_scale_0.9842_n_6_2s_{numb_qy}_ratio_1.000000_qy_0.omega_-10--9_eps_1e-06.sr.cut",
                              f"fermions_torus_spec_resp_kysym_coulomb_0.02_plus_V1_scale_0.98_n_6_2s_{numb_qy}_ratio_1.000000_qy_0.omega_-10--9_eps_1e-06.sr.cut",
                              f"fermions_torus_spec_resp_kysym_coulomb_0.0251_plus_V1_scale_0.9749_n_6_2s_{numb_qy}_ratio_1.000000_qy_0.omega_-10--9_eps_1e-06.sr.cut",
                              f"fermions_torus_spec_resp_kysym_coulomb_0.0316_plus_V1_scale_0.9684_n_6_2s_{numb_qy}_ratio_1.000000_qy_0.omega_-10--9_eps_1e-06.sr.cut",
                              f"fermions_torus_spec_resp_kysym_coulomb_0.0398_plus_V1_scale_0.9602_n_6_2s_{numb_qy}_ratio_1.000000_qy_0.omega_-10--9_eps_1e-06.sr.cut",
                              f"fermions_torus_spec_resp_kysym_coulomb_0.0501_plus_V1_scale_0.9499_n_6_2s_{numb_qy}_ratio_1.000000_qy_0.omega_-10--9_eps_1e-06.sr.cut",
                              f"fermions_torus_spec_resp_kysym_coulomb_0.0631_plus_V1_scale_0.9369_n_6_2s_{numb_qy}_ratio_1.000000_qy_0.omega_-10--9_eps_1e-06.sr.cut",
                              f"fermions_torus_spec_resp_kysym_coulomb_0.0794_plus_V1_scale_0.9206_n_6_2s_{numb_qy}_ratio_1.000000_qy_0.omega_-10--9_eps_1e-06.sr.cut",
                              f"fermions_torus_spec_resp_kysym_coulomb_0.1_plus_V1_scale_0.9_n_6_2s_{numb_qy}_ratio_1.000000_qy_0.omega_-10-0_eps_1e-06.sr.cut",
                              f"fermions_torus_spec_resp_kysym_coulomb_0.126_plus_V1_scale_0.874_n_6_2s_{numb_qy}_ratio_1.000000_qy_0.omega_-10-0_eps_1e-06.sr.cut",
                              f"fermions_torus_spec_resp_kysym_coulomb_0.158_plus_V1_scale_0.842_n_6_2s_{numb_qy}_ratio_1.000000_qy_0.omega_-10-0_eps_1e-06.sr.cut",
                              f"fermions_torus_spec_resp_kysym_coulomb_0.2_plus_V1_scale_0.8_n_6_2s_{numb_qy}_ratio_1.000000_qy_0.omega_-10-0_eps_1e-06.sr.cut",
                              f"fermions_torus_spec_resp_kysym_coulomb_0.251_plus_V1_scale_0.749_n_6_2s_{numb_qy}_ratio_1.000000_qy_0.omega_-10-0_eps_1e-06.sr.cut",
                              f"fermions_torus_spec_resp_kysym_coulomb_0.316_plus_V1_scale_0.684_n_6_2s_{numb_qy}_ratio_1.000000_qy_0.omega_-10-0_eps_1e-06.sr.cut",
                              f"fermions_torus_spec_resp_kysym_coulomb_0.398_plus_V1_scale_0.602_n_6_2s_{numb_qy}_ratio_1.000000_qy_0.omega_-10-0_eps_1e-06.sr.cut",
                              f"fermions_torus_spec_resp_kysym_coulomb_0.501_plus_V1_scale_0.499_n_6_2s_{numb_qy}_ratio_1.000000_qy_0.omega_-10-0_eps_1e-06.sr.cut",
                              f"fermions_torus_spec_resp_kysym_coulomb_0.631_plus_V1_scale_0.369_n_6_2s_{numb_qy}_ratio_1.000000_qy_0.omega_-10-0_eps_1e-06.sr.cut",
                              f"fermions_torus_spec_resp_kysym_coulomb_0.794_plus_V1_scale_0.206_n_6_2s_{numb_qy}_ratio_1.000000_qy_0.omega_-10-0_eps_1e-06.sr.cut",
                              f"fermions_torus_spec_resp_kysym_coulomb_plus_V1_scale_0_n_6_2s_{numb_qy}_ratio_1.000000_qy_0.omega_-10-0_eps_1e-06.sr.cut"]):

        with open('stripped_files/' + file, 'r') as csvfile:
            plots = csv.reader(csvfile, delimiter=' ')
            for row in plots:
                omega.append(float(row[0])+10)
                SR.append(float(row[1]))
                lbl += [10 ** (-4 + i * 0.1)]
                # if i < 10:
                #     lbl += [0.0001*(i+1)]
                # elif 10 <= i < 19:
                #     lbl += [0.001 * (i % 10 + 2)]
                # elif 19 <= i < 28:
                #     lbl += [0.01 * (i % 19 + 2)]
                # elif 28 <= i:
                #     lbl += [0.1 * (i % 28 + 2)]

    print(np.shape(omega), np.shape(SR), np.shape(lbl))

    omega_max = []
    sr_max = []
    for i, entry in enumerate(omega):
        if SR[i] > SR[i-1] and SR[i] > SR[i+1] and omega[i] > 0:
            omega_max += [1]
            sr_max += [SR[i]]
        else:
            omega_max += [0]

    print(omega_max.count(1))

    lbl[:] = [x for i, x in enumerate(lbl) if omega_max[i] == 1]
    omega[:] = [x for i, x in enumerate(omega) if omega_max[i] == 1]

    sr_values = []
    lbl_values = sorted(list(set(lbl)))
    for lbl_val in lbl_values:
        omega_set = [i for i, e in enumerate(lbl) if e == lbl_val]
        sr_max_set = sr_max[omega_set[0]:omega_set[-1]+1]
        sr_mean = np.mean(sr_max_set)
        sr_values += [sr_mean]

    log_lbl_values = [np.log10(i) for i in lbl_values]

    im = ax.scatter(log_lbl_values, sr_values, s=10)

    ax.set_xlabel('$\\log_{10}(\\alpha)$')
    ax.xaxis.set_major_formatter(FormatStrFormatter('%g'))
    ax.set_ylabel('$\\bar{S}$')

    ax.axhline(np.mean(sr_values), c='k', zorder=-1, linewidth=0.5, linestyle='--')
    ax.axhspan(np.mean(sr_values)-np.std(sr_values), np.mean(sr_values)+np.std(sr_values), alpha=0.1, color='red')

    ax.text(-3, 18000, "$\\langle \\bar{{S}} \\rangle = ({mean:.3g})\pm ({sd:.3g})$".format(
        mean=np.mean(sr_values), sd=np.std(sr_values), fontsize=10))

    # ax.set_xticks(np.arange(2, 40, 2))

    fig.subplots_adjust(top=0.95, bottom=0.1, right=0.95, left=0.11)

    plt.savefig("/home/bart/Documents/papers/SR/notes/figures/" + filename, dpi=300)
    plt.show()


def plot_2d_ltypp_complete_res_max(numb_qy, filename):

    fig = plt.figure()
    ax = fig.add_subplot(111)

    omega = []
    SR = []

    name_list = []
    lbl = []

    for alpha_exp in np.linspace(-4, 0, 41, endpoint=True):
        name_list.append(f"fermions_torus_spec_resp_kysym_coulomb_0_plus_V1_scale_{1-10**alpha_exp:.5g}_YukawaPlaneL1_scale_{10**alpha_exp:.5g}_n_6_2s_{numb_qy}_ratio_1.000000_qy_0.omega_-10-0_eps_1e-06.sr.cut")

    for i, file in enumerate(name_list):
        with open('stripped_files/' + file, 'r') as csvfile:
            plots = csv.reader(csvfile, delimiter=' ')
            for row in plots:
                omega.append(float(row[0])+10)
                SR.append(float(row[1]))
                lbl += [10**(-4+i*0.1)]
                # if i < 10:
                #     lbl += [0.0001*(i+1)]
                # elif 10 <= i < 19:
                #     lbl += [0.001 * (i % 10 + 2)]
                # elif 19 <= i < 28:
                #     lbl += [0.01 * (i % 19 + 2)]
                # elif 28 <= i:
                #     lbl += [0.1 * (i % 28 + 2)]

    print(np.shape(omega), np.shape(SR), np.shape(lbl))

    omega_max = []
    sr_max = []
    for i, entry in enumerate(omega):
        if SR[i] > SR[i-1] and SR[i] > SR[i+1] and omega[i] > 0:
            omega_max += [1]
            sr_max += [SR[i]]
        else:
            omega_max += [0]

    print(omega_max.count(1))

    lbl[:] = [x for i, x in enumerate(lbl) if omega_max[i] == 1]
    omega[:] = [x for i, x in enumerate(omega) if omega_max[i] == 1]

    print(len(omega))

    # plot the large S points on top
    zipped = list(zip(lbl, omega, sr_max))
    zipped.sort(key=lambda pair: pair[2])
    lbl, omega, sr_max = zip(*zipped)

    im = ax.scatter(lbl, omega, c=sr_max, s=10, norm=colors.LogNorm(vmin=min(sr_max), vmax=max(sr_max)),
                    cmap=plt.cm.Reds)
    fig.colorbar(im, ax=ax, label='$S$')
    ax.set_xlim([0.00001, 10])
    ax.set_ylim([0.0001, 100])

    ax.set_xscale('log')
    ax.set_yscale('log')
    ax.set_xlabel('$\\alpha$')
    # ax.xaxis.set_major_formatter(FormatStrFormatter('%.2g'))
    ax.set_ylabel('$\\omega$')

    # ax.set_xticks(np.arange(2, 40, 2))

    fig.subplots_adjust(top=0.95, bottom=0.1, right=0.95, left=0.11)

    plt.savefig("/home/bart/Documents/papers/SR/notes/figures/" + filename, dpi=300)
    plt.show()


def plot_2d_ltypp_slope_res_max(numb_qy, filename):

    fig = plt.figure()
    ax = fig.add_subplot(111)

    omega = []
    SR = []

    name_list = []
    lbl = []

    for alpha_exp in np.linspace(-4, 0, 41, endpoint=True):
        name_list.append(f"fermions_torus_spec_resp_kysym_coulomb_0_plus_V1_scale_{1-10**alpha_exp:.5g}_YukawaPlaneL1_scale_{10**alpha_exp:.5g}_n_6_2s_{numb_qy}_ratio_1.000000_qy_0.omega_-10-0_eps_1e-06.sr.cut")

    for i, file in enumerate(name_list):
        with open('stripped_files/' + file, 'r') as csvfile:
            plots = csv.reader(csvfile, delimiter=' ')
            for row in plots:
                omega.append(float(row[0])+10)
                SR.append(float(row[1]))
                lbl += [10 ** (-4 + i * 0.1)]
                # if i < 10:
                #     lbl += [0.0001*(i+1)]
                # elif 10 <= i < 19:
                #     lbl += [0.001 * (i % 10 + 2)]
                # elif 19 <= i < 28:
                #     lbl += [0.01 * (i % 19 + 2)]
                # elif 28 <= i:
                #     lbl += [0.1 * (i % 28 + 2)]

    print(np.shape(omega), np.shape(SR), np.shape(lbl))

    omega_max = []
    sr_max = []
    for i, entry in enumerate(omega):
        if SR[i] > SR[i-1] and SR[i] > SR[i+1] and omega[i] > 0:
            omega_max += [1]
            sr_max += [SR[i]]
        else:
            omega_max += [0]

    print(omega_max.count(1))

    lbl[:] = [x for i, x in enumerate(lbl) if omega_max[i] == 1]
    omega[:] = [x for i, x in enumerate(omega) if omega_max[i] == 1]

    log_omega_range = []
    lbl_values = sorted(list(set(lbl)))
    for lbl_val in lbl_values:
        omega_set = [i for i, e in enumerate(lbl) if e == lbl_val]
        max_val = max(omega[omega_set[0]:omega_set[-1]+1])
        min_val = min(omega[omega_set[0]:omega_set[-1]+1])
        range_val = max_val - min_val
        log_range_val = np.log10(range_val)
        log_omega_range += [log_range_val]

    log_lbl_values = [np.log10(i) for i in lbl_values]
    print(log_lbl_values)
    print(log_omega_range)

    im = ax.scatter(log_lbl_values, log_omega_range, s=10)

    ax.set_xlabel('$\\log_{10}(\\alpha)$')
    ax.xaxis.set_major_formatter(FormatStrFormatter('%g'))
    ax.set_ylabel('$\\log_{10}[\\mathrm{range}(\\Omega)]$')
    ax.yaxis.set_major_formatter(FormatStrFormatter('%g'))

    line_of_best_fit(ax, log_lbl_values, log_omega_range, -4, -0.5)

    # ax.set_xticks(np.arange(2, 40, 2))

    fig.subplots_adjust(top=0.95, bottom=0.1, right=0.95, left=0.11)

    plt.savefig("/home/bart/Documents/papers/SR/notes/figures/" + filename, dpi=300)
    plt.show()


def plot_2d_ltypp_nbr_omega_res_max(numb_qy, filename):

    fig = plt.figure()
    ax = fig.add_subplot(111)

    omega = []
    SR = []

    name_list = []
    lbl = []

    for alpha_exp in np.linspace(-4, 0, 41, endpoint=True):
        name_list.append(f"fermions_torus_spec_resp_kysym_coulomb_0_plus_V1_scale_{1-10**alpha_exp:.5g}_YukawaPlaneL1_scale_{10**alpha_exp:.5g}_n_6_2s_{numb_qy}_ratio_1.000000_qy_0.omega_-10-0_eps_1e-06.sr.cut")

    for i, file in enumerate(name_list):
        with open('stripped_files/' + file, 'r') as csvfile:
            plots = csv.reader(csvfile, delimiter=' ')
            for row in plots:
                omega.append(float(row[0])+10)
                SR.append(float(row[1]))
                lbl += [10 ** (-4 + i * 0.1)]
                # if i < 10:
                #     lbl += [0.0001*(i+1)]
                # elif 10 <= i < 19:
                #     lbl += [0.001 * (i % 10 + 2)]
                # elif 19 <= i < 28:
                #     lbl += [0.01 * (i % 19 + 2)]
                # elif 28 <= i:
                #     lbl += [0.1 * (i % 28 + 2)]

    print(np.shape(omega), np.shape(SR), np.shape(lbl))

    omega_max = []
    sr_max = []
    for i, entry in enumerate(omega):
        if SR[i] > SR[i-1] and SR[i] > SR[i+1] and omega[i] > 0:
            omega_max += [1]
            sr_max += [SR[i]]
        else:
            omega_max += [0]

    print(omega_max.count(1))

    lbl[:] = [x for i, x in enumerate(lbl) if omega_max[i] == 1]
    omega[:] = [x for i, x in enumerate(omega) if omega_max[i] == 1]

    len_values = []
    lbl_values = sorted(list(set(lbl)))
    for lbl_val in lbl_values:
        omega_set = [i for i, e in enumerate(lbl) if e == lbl_val]
        len_val = len(omega_set)
        len_values += [len_val]

    log_lbl_values = [np.log10(i) for i in lbl_values]

    im = ax.scatter(log_lbl_values, len_values, s=10)

    ax.set_xlabel('$\\log_{10}(\\alpha)$')
    ax.xaxis.set_major_formatter(FormatStrFormatter('%g'))
    ax.set_ylabel('$n(\\Omega)$')

    ax.axhline(np.mean(len_values), c='k', zorder=-1, linewidth=0.5, linestyle='--')
    ax.axhspan(np.mean(len_values) - np.std(len_values), np.mean(len_values) + np.std(len_values), alpha=0.1, color='red')

    ax.text(-2.5, 60, "$\\langle n(\\Omega) \\rangle = {mean:.3g}\pm {sd:.3g}$".format(
        mean=np.mean(len_values), sd=np.std(len_values), fontsize=10))

    # ax.set_xticks(np.arange(2, 40, 2))

    fig.subplots_adjust(top=0.95, bottom=0.1, right=0.95, left=0.11)

    plt.savefig("/home/bart/Documents/papers/SR/notes/figures/" + filename, dpi=300)
    plt.show()


def plot_2d_ltypp_mean_S_res_max(numb_qy, filename):

    fig = plt.figure()
    ax = fig.add_subplot(111)

    omega = []
    SR = []

    name_list = []
    lbl = []

    for alpha_exp in np.linspace(-4, -1.2, 29, endpoint=True):
        name_list.append(f"fermions_torus_spec_resp_kysym_coulomb_0_plus_V1_scale_{1-10**alpha_exp:.5g}_YukawaPlaneL1_scale_{10**alpha_exp:.5g}_n_6_2s_{numb_qy}_ratio_1.000000_qy_0.omega_-10-0_eps_1e-06.sr.cut")

    for i, file in enumerate(name_list):
        with open('stripped_files/' + file, 'r') as csvfile:
            plots = csv.reader(csvfile, delimiter=' ')
            for row in plots:
                omega.append(float(row[0])+10)
                SR.append(float(row[1]))
                lbl += [10 ** (-4 + i * 0.1)]
                # if i < 10:
                #     lbl += [0.0001*(i+1)]
                # elif 10 <= i < 19:
                #     lbl += [0.001 * (i % 10 + 2)]
                # elif 19 <= i < 28:
                #     lbl += [0.01 * (i % 19 + 2)]
                # elif 28 <= i:
                #     lbl += [0.1 * (i % 28 + 2)]

    print(np.shape(omega), np.shape(SR), np.shape(lbl))

    omega_max = []
    sr_max = []
    for i, entry in enumerate(omega):
        if SR[i] > SR[i-1] and SR[i] > SR[i+1] and omega[i] > 0:
            omega_max += [1]
            sr_max += [SR[i]]
        else:
            omega_max += [0]

    print(omega_max.count(1))

    lbl[:] = [x for i, x in enumerate(lbl) if omega_max[i] == 1]
    omega[:] = [x for i, x in enumerate(omega) if omega_max[i] == 1]

    sr_values = []
    lbl_values = sorted(list(set(lbl)))
    for lbl_val in lbl_values:
        omega_set = [i for i, e in enumerate(lbl) if e == lbl_val]
        sr_max_set = sr_max[omega_set[0]:omega_set[-1]+1]
        sr_mean = np.mean(sr_max_set)
        sr_values += [sr_mean]

    log_lbl_values = [np.log10(i) for i in lbl_values]

    im = ax.scatter(log_lbl_values, sr_values, s=10)

    ax.set_xlabel('$\\log_{10}(\\alpha)$')
    ax.xaxis.set_major_formatter(FormatStrFormatter('%g'))
    ax.set_ylabel('$\\bar{S}$')

    ax.axhline(np.mean(sr_values), c='k', zorder=-1, linewidth=0.5, linestyle='--')
    ax.axhspan(np.mean(sr_values)-np.std(sr_values), np.mean(sr_values)+np.std(sr_values), alpha=0.1, color='red')

    ax.text(-3, 18000, "$\\langle \\bar{{S}} \\rangle = ({mean:.3g})\pm ({sd:.3g})$".format(
        mean=np.mean(sr_values), sd=np.std(sr_values), fontsize=10))

    # ax.set_xticks(np.arange(2, 40, 2))

    fig.subplots_adjust(top=0.95, bottom=0.1, right=0.95, left=0.11)

    plt.savefig("/home/bart/Documents/papers/SR/notes/figures/" + filename, dpi=300)
    plt.show()


def plot_2d_lty_complete_res_max(numb_qy, filename):

    fig = plt.figure()
    ax = fig.add_subplot(111)

    omega = []
    SR = []

    name_list = []
    lbl = []

    for alpha_exp in np.linspace(-4, 0, 41, endpoint=True):
        if "l10_" in filename and alpha_exp < -3:
            continue
        if "l100_" in filename and alpha_exp < -2:
            continue
        if alpha_exp == 0:
            name_list.append(f"fermions_torus_spec_resp_kysym_yukawa-100_plus_V1_scale_0_n_6_2s_{numb_qy}_ratio_1.000000_qy_0.omega_-10-10_eps_1e-06.sr.cut")
        else:
            name_list.append(f"fermions_torus_spec_resp_kysym_yukawa-100_{10**alpha_exp:.5g}_plus_V1_scale_{1-10**alpha_exp:.5g}_n_6_2s_{numb_qy}_ratio_1.000000_qy_0.omega_-10-10_eps_1e-06.sr.cut")

    for i, file in enumerate(name_list):
        with open('stripped_files/' + file, 'r') as csvfile:
            plots = csv.reader(csvfile, delimiter=' ')
            for row in plots:
                omega.append(float(row[0])+10)
                SR.append(float(row[1]))
                lbl += [10**(-2+i*0.1)]
                # if i < 10:
                #     lbl += [0.0001*(i+1)]
                # elif 10 <= i < 19:
                #     lbl += [0.001 * (i % 10 + 2)]
                # elif 19 <= i < 28:
                #     lbl += [0.01 * (i % 19 + 2)]
                # elif 28 <= i:
                #     lbl += [0.1 * (i % 28 + 2)]

    print(np.shape(omega), np.shape(SR), np.shape(lbl))

    omega_max = []
    sr_max = []
    for i, entry in enumerate(omega):
        if SR[i] > SR[i-1] and SR[i] > SR[i+1] and omega[i] > 0:
            omega_max += [1]
            sr_max += [SR[i]]
        else:
            omega_max += [0]

    print(omega_max.count(1))

    lbl[:] = [x for i, x in enumerate(lbl) if omega_max[i] == 1]
    omega[:] = [x for i, x in enumerate(omega) if omega_max[i] == 1]

    print(len(omega))

    # plot the large S points on top
    zipped = list(zip(lbl, omega, sr_max))
    zipped.sort(key=lambda pair: pair[2])
    lbl, omega, sr_max = zip(*zipped)

    im = ax.scatter(lbl, omega, c=sr_max, s=10, norm=colors.LogNorm(vmin=min(sr_max), vmax=max(sr_max)),
                    cmap=plt.cm.Reds)
    fig.colorbar(im, ax=ax, label='$S$')
    ax.set_xlim([0.001, 10])
    ax.set_ylim([0.0000001, 10])

    ax.set_xscale('log')
    ax.set_yscale('log')
    ax.set_xlabel('$\\alpha$')
    # ax.xaxis.set_major_formatter(FormatStrFormatter('%.2g'))
    ax.set_ylabel('$\\omega$')

    # ax.set_xticks(np.arange(2, 40, 2))

    fig.subplots_adjust(top=0.95, bottom=0.1, right=0.95, left=0.11)

    plt.savefig("/home/bart/Documents/papers/SR/notes/figures/" + filename, dpi=300)
    plt.show()


def plot_2d_lty_slope_res_max(numb_qy, filename):

    fig = plt.figure()
    ax = fig.add_subplot(111)

    omega = []
    SR = []

    name_list = []
    lbl = []

    for alpha_exp in np.linspace(-4, 0, 41, endpoint=True):
        if "l10_" in filename and alpha_exp < -3:
            continue
        if "l100_" in filename and alpha_exp < -2:
            continue
        if alpha_exp == 0:
            name_list.append(f"fermions_torus_spec_resp_kysym_yukawa-100_plus_V1_scale_0_n_6_2s_{numb_qy}_ratio_1.000000_qy_0.omega_-10-10_eps_1e-06.sr.cut")
        else:
            name_list.append(f"fermions_torus_spec_resp_kysym_yukawa-100_{10**alpha_exp:.5g}_plus_V1_scale_{1-10**alpha_exp:.5g}_n_6_2s_{numb_qy}_ratio_1.000000_qy_0.omega_-10-10_eps_1e-06.sr.cut")

    for i, file in enumerate(name_list):
        with open('stripped_files/' + file, 'r') as csvfile:
            plots = csv.reader(csvfile, delimiter=' ')
            for row in plots:
                omega.append(float(row[0])+10)
                SR.append(float(row[1]))
                lbl += [10 ** (-2 + i * 0.1)]
                # if i < 10:
                #     lbl += [0.0001*(i+1)]
                # elif 10 <= i < 19:
                #     lbl += [0.001 * (i % 10 + 2)]
                # elif 19 <= i < 28:
                #     lbl += [0.01 * (i % 19 + 2)]
                # elif 28 <= i:
                #     lbl += [0.1 * (i % 28 + 2)]

    print(np.shape(omega), np.shape(SR), np.shape(lbl))

    omega_max = []
    sr_max = []
    for i, entry in enumerate(omega):
        if SR[i] > SR[i-1] and SR[i] > SR[i+1] and omega[i] > 0:
            omega_max += [1]
            sr_max += [SR[i]]
        else:
            omega_max += [0]

    print(omega_max.count(1))

    lbl[:] = [x for i, x in enumerate(lbl) if omega_max[i] == 1]
    omega[:] = [x for i, x in enumerate(omega) if omega_max[i] == 1]

    log_omega_range = []
    lbl_values = sorted(list(set(lbl)))
    for lbl_val in lbl_values:
        omega_set = [i for i, e in enumerate(lbl) if e == lbl_val]
        max_val = max(omega[omega_set[0]:omega_set[-1]+1])
        min_val = min(omega[omega_set[0]:omega_set[-1]+1])
        range_val = max_val - min_val
        log_range_val = np.log10(range_val)
        log_omega_range += [log_range_val]

    log_lbl_values = [np.log10(i) for i in lbl_values]
    print(log_lbl_values)
    print(log_omega_range)

    im = ax.scatter(log_lbl_values, log_omega_range, s=10)

    ax.set_xlabel('$\\log_{10}(\\alpha)$')
    ax.xaxis.set_major_formatter(FormatStrFormatter('%g'))
    ax.set_ylabel('$\\log_{10}[\\mathrm{range}(\\Omega)]$')
    ax.yaxis.set_major_formatter(FormatStrFormatter('%g'))

    line_of_best_fit(ax, log_lbl_values, log_omega_range, -2, -1.5)

    # ax.set_xticks(np.arange(2, 40, 2))

    fig.subplots_adjust(top=0.95, bottom=0.1, right=0.95, left=0.11)

    plt.savefig("/home/bart/Documents/papers/SR/notes/figures/" + filename, dpi=300)
    plt.show()


def plot_2d_lty_nbr_omega_res_max(numb_qy, filename):

    fig = plt.figure()
    ax = fig.add_subplot(111)

    omega = []
    SR = []

    name_list = []
    lbl = []

    for alpha_exp in np.linspace(-4, 0, 41, endpoint=True):
        if "l10_" in filename and alpha_exp < -3:
            continue
        if "l100_" in filename and alpha_exp < -2:
            continue
        if alpha_exp == 0:
            name_list.append(f"fermions_torus_spec_resp_kysym_yukawa-100_plus_V1_scale_0_n_6_2s_{numb_qy}_ratio_1.000000_qy_0.omega_-10-10_eps_1e-06.sr.cut")
        else:
            name_list.append(f"fermions_torus_spec_resp_kysym_yukawa-100_{10**alpha_exp:.5g}_plus_V1_scale_{1-10**alpha_exp:.5g}_n_6_2s_{numb_qy}_ratio_1.000000_qy_0.omega_-10-10_eps_1e-06.sr.cut")

    for i, file in enumerate(name_list):
        with open('stripped_files/' + file, 'r') as csvfile:
            plots = csv.reader(csvfile, delimiter=' ')
            for row in plots:
                omega.append(float(row[0])+10)
                SR.append(float(row[1]))
                lbl += [10 ** (-2 + i * 0.1)]
                # if i < 10:
                #     lbl += [0.0001*(i+1)]
                # elif 10 <= i < 19:
                #     lbl += [0.001 * (i % 10 + 2)]
                # elif 19 <= i < 28:
                #     lbl += [0.01 * (i % 19 + 2)]
                # elif 28 <= i:
                #     lbl += [0.1 * (i % 28 + 2)]

    print(np.shape(omega), np.shape(SR), np.shape(lbl))

    omega_max = []
    sr_max = []
    for i, entry in enumerate(omega):
        if SR[i] > SR[i-1] and SR[i] > SR[i+1] and omega[i] > 0:
            omega_max += [1]
            sr_max += [SR[i]]
        else:
            omega_max += [0]

    print(omega_max.count(1))

    lbl[:] = [x for i, x in enumerate(lbl) if omega_max[i] == 1]
    omega[:] = [x for i, x in enumerate(omega) if omega_max[i] == 1]

    len_values = []
    lbl_values = sorted(list(set(lbl)))
    for lbl_val in lbl_values:
        omega_set = [i for i, e in enumerate(lbl) if e == lbl_val]
        len_val = len(omega_set)
        len_values += [len_val]

    log_lbl_values = [np.log10(i) for i in lbl_values]

    im = ax.scatter(log_lbl_values, len_values, s=10)

    ax.set_xlabel('$\\log_{10}(\\alpha)$')
    ax.xaxis.set_major_formatter(FormatStrFormatter('%g'))
    ax.set_ylabel('$n(\\Omega)$')

    ax.axhline(np.mean(len_values), c='k', zorder=-1, linewidth=0.5, linestyle='--')
    ax.axhspan(np.mean(len_values) - np.std(len_values), np.mean(len_values) + np.std(len_values), alpha=0.1, color='red')

    ax.text(-1.5, 38, "$\\langle n(\\Omega) \\rangle = {mean:.3g}\pm {sd:.3g}$".format(
        mean=np.mean(len_values), sd=np.std(len_values), fontsize=10))

    # ax.set_xticks(np.arange(2, 40, 2))

    fig.subplots_adjust(top=0.95, bottom=0.1, right=0.95, left=0.11)

    plt.savefig("/home/bart/Documents/papers/SR/notes/figures/" + filename, dpi=300)
    plt.show()


def plot_2d_lty_mean_S_res_max(numb_qy, filename):

    fig = plt.figure()
    ax = fig.add_subplot(111)

    omega = []
    SR = []

    name_list = []
    lbl = []

    for alpha_exp in np.linspace(-4, 0, 41, endpoint=True):
        if "l10_" in filename and alpha_exp < -3:
            continue
        if "l100_" in filename and alpha_exp < -2:
            continue
        if alpha_exp == 0:
            name_list.append(f"fermions_torus_spec_resp_kysym_yukawa-100_plus_V1_scale_0_n_6_2s_{numb_qy}_ratio_1.000000_qy_0.omega_-10-10_eps_1e-06.sr.cut")
        else:
            name_list.append(f"fermions_torus_spec_resp_kysym_yukawa-100_{10**alpha_exp:.5g}_plus_V1_scale_{1-10**alpha_exp:.5g}_n_6_2s_{numb_qy}_ratio_1.000000_qy_0.omega_-10-10_eps_1e-06.sr.cut")

    for i, file in enumerate(name_list):
        with open('stripped_files/' + file, 'r') as csvfile:
            plots = csv.reader(csvfile, delimiter=' ')
            for row in plots:
                omega.append(float(row[0])+10)
                SR.append(float(row[1]))
                lbl += [10 ** (-2 + i * 0.1)]
                # if i < 10:
                #     lbl += [0.0001*(i+1)]
                # elif 10 <= i < 19:
                #     lbl += [0.001 * (i % 10 + 2)]
                # elif 19 <= i < 28:
                #     lbl += [0.01 * (i % 19 + 2)]
                # elif 28 <= i:
                #     lbl += [0.1 * (i % 28 + 2)]

    print(np.shape(omega), np.shape(SR), np.shape(lbl))

    omega_max = []
    sr_max = []
    for i, entry in enumerate(omega):
        if SR[i] > SR[i-1] and SR[i] > SR[i+1] and omega[i] > 0:
            omega_max += [1]
            sr_max += [SR[i]]
        else:
            omega_max += [0]

    print(omega_max.count(1))

    lbl[:] = [x for i, x in enumerate(lbl) if omega_max[i] == 1]
    omega[:] = [x for i, x in enumerate(omega) if omega_max[i] == 1]

    sr_values = []
    lbl_values = sorted(list(set(lbl)))
    for lbl_val in lbl_values:
        omega_set = [i for i, e in enumerate(lbl) if e == lbl_val]
        sr_max_set = sr_max[omega_set[0]:omega_set[-1]+1]
        sr_mean = np.mean(sr_max_set)
        sr_values += [sr_mean]

    log_lbl_values = [np.log10(i) for i in lbl_values]

    im = ax.scatter(log_lbl_values, sr_values, s=10)

    ax.set_xlabel('$\\log_{10}(\\alpha)$')
    ax.xaxis.set_major_formatter(FormatStrFormatter('%g'))
    ax.set_ylabel('$\\bar{S}$')

    ax.axhline(np.mean(sr_values), c='k', zorder=-1, linewidth=0.5, linestyle='--')
    ax.axhspan(np.mean(sr_values)-np.std(sr_values), np.mean(sr_values)+np.std(sr_values), alpha=0.1, color='red')

    ax.text(-2, 36000, "$\\langle \\bar{{S}} \\rangle = ({mean:.3g})\pm ({sd:.3g})$".format(
        mean=np.mean(sr_values), sd=np.std(sr_values), fontsize=10))

    # ax.set_xticks(np.arange(2, 40, 2))

    fig.subplots_adjust(top=0.95, bottom=0.1, right=0.95, left=0.11)

    plt.savefig("/home/bart/Documents/papers/SR/notes/figures/" + filename, dpi=300)
    plt.show()


# Coulomb pseudopotentials #############################################################################################

def plot_2d_cpt_fixed(numb_qy, omega_min, omega_max, filename):

    fig = plt.figure()
    ax = fig.add_subplot(111)

    marker = itertools.cycle(('1', '2', '3', '4', ',', '+', '.', 'o', '*', '^', 'v', '>', '<', 'X', '_', 'd', '|', 'H'))

    for i, name in enumerate(["coulomb_0_plus_CoulombPlane_trunc_2", "coulomb_0_plus_CoulombPlane_trunc_4",
                              "coulomb_0_plus_CoulombPlane_trunc_6", "coulomb_0_plus_CoulombPlane_trunc_8",
                              "coulomb_0_plus_CoulombPlane_trunc_10"]):
        omega = []
        SR = []
        file = f"fermions_torus_spec_resp_kysym_{name}_n_6_2s_{numb_qy}_ratio_1.000000_qy_0" \
               f".omega_{omega_min}-{omega_max}_eps_0.0001.sr.cut"
        with open('stripped_files/' + file, 'r') as csvfile:
            plots = csv.reader(csvfile, delimiter=' ')
            for row in plots:
                omega.append(float(row[0]))
                SR.append(float(row[1]))
        lbl = [2, 4, 6, 8, 10]
        ax.scatter(omega, SR, s=2, label=f"{lbl[i]}", marker=next(marker))

    ax.set_xlabel('$\omega$')
    ax.set_ylabel('$S$')
    ax.legend(loc='upper right', handletextpad=0, borderpad=0.4, framealpha=1,
              edgecolor='k', markerscale=3,
              fontsize=10, ncol=3, labelspacing=0, columnspacing=0, title='$\\alpha$')

    fig.subplots_adjust(top=0.95, bottom=0.1, right=0.95, left=0.11)

    plt.savefig("/home/bart/Documents/papers/SR/notes/figures/" + filename, bbox_inches='tight', dpi=300)
    plt.show()


def plot_2d_cpt_fixed_full(numb_qy, omega_min, omega_max, filename):

    fig = plt.figure()
    ax = fig.add_subplot(111)

    marker = itertools.cycle(('1', '2', '3', '4', ',', '+', '.', 'o', '*', '^', 'v', '>', '<', 'X', '_', 'd', '|', 'H'))

    name_list = []
    lbl = []

    for i in range(2, 40, 2):
        name_list += [f"coulomb_0_plus_CoulombPlane_trunc_{i}"]
        lbl += [i]

    for i, name in enumerate(name_list):
        omega = []
        SR = []
        file = f"fermions_torus_spec_resp_kysym_{name}_n_6_2s_{numb_qy}_ratio_1.000000_qy_0" \
               f".omega_{omega_min}-{omega_max}_eps_0.0001.sr.cut"
        with open('stripped_files/' + file, 'r') as csvfile:
            plots = csv.reader(csvfile, delimiter=' ')
            for row in plots:
                omega.append(float(row[0]))
                SR.append(float(row[1]))
        ax.scatter(omega, SR, s=2, label=f"{lbl[i]}", marker=next(marker))

    ax.set_xlabel('$\omega$')
    ax.set_ylabel('$S$')
    ax.legend(loc='upper right', handletextpad=0, borderpad=0.4, framealpha=1,
              edgecolor='k', markerscale=3,
              fontsize=10, ncol=3, labelspacing=0, columnspacing=0, title='$\\alpha$')

    fig.subplots_adjust(top=0.95, bottom=0.1, right=0.95, left=0.11)

    plt.savefig("/home/bart/Documents/papers/SR/notes/figures/" + filename, bbox_inches='tight', dpi=300)
    plt.show()


def plot_2d_cpt_fixed_full_box(numb_qy, omega_min, omega_max, filename):

    fig = plt.figure()
    ax = fig.add_subplot(111)

    name_list = []
    lbl = []
    data_to_plot = []

    for i in range(2, 40, 2):
        name_list += [f"coulomb_0_plus_CoulombPlane_trunc_{i}"]
        lbl += [i]

    for i, name in enumerate(name_list):
        omega = []
        SR = []
        file = f"fermions_torus_spec_resp_kysym_{name}_n_6_2s_{numb_qy}_ratio_1.000000_qy_0" \
               f".omega_{omega_min}-{omega_max}_eps_0.0001.sr.cut"
        with open('stripped_files/' + file, 'r') as csvfile:
            plots = csv.reader(csvfile, delimiter=' ')
            for row in plots:
                omega.append(float(row[0]))
                SR.append(float(row[1]))
            data_to_plot += [omega]

    props = dict(markerfacecolor='b', marker='x', markersize=1)
    ax.boxplot(data_to_plot, positions=lbl, flierprops=props, widths=1)

    ax.set_xlabel('$\\alpha$')
    ax.set_ylabel('$\omega$')

    fig.subplots_adjust(top=0.95, bottom=0.1, right=0.95, left=0.11)

    plt.savefig("/home/bart/Documents/papers/SR/notes/figures/" + filename, bbox_inches='tight', dpi=300)
    plt.show()


def plot_2d_cpt_fixed_full_hist(numb_qy, omega_min, omega_max, filename):

    fig = plt.figure()
    ax = fig.add_subplot(111)

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

    counts, xedges, yedges, im = ax.hist2d(lbl, omega, bins=(19, 50), range=[[1, 39], None], cmap=plt.cm.inferno)
    fig.colorbar(im, ax=ax, label='percentage of S values',
                 format=ticker.FuncFormatter(lambda x, pos: '{0:g}'.format(x/100)))

    ax.set_xlabel('$\\alpha$')
    ax.xaxis.set_major_formatter(FormatStrFormatter('%.2g'))
    ax.set_ylabel('$\\omega$')

    ax.set_xticks(np.arange(2, 40, 2))

    fig.subplots_adjust(top=0.95, bottom=0.1, right=0.95, left=0.11)

    plt.savefig("/home/bart/Documents/papers/SR/notes/figures/" + filename, dpi=300)
    plt.show()


def plot_2d_cpt_fixed_full_max(numb_qy, omega_min, omega_max, filename):

    fig = plt.figure()
    ax = fig.add_subplot(111)

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

    omega_max = []
    for i, entry in enumerate(omega):
        if 0 < i < len(omega)-1:
            if omega[i] > omega[i-1] and omega[i] > omega[i+1]:
                omega_max += [1]
            else:
                omega_max += [0]
        else:
            omega_max += [0]

    lbl[:] = [x for i, x in enumerate(lbl) if omega_max[i] == 1]
    omega[:] = [x for i, x in enumerate(omega) if omega_max[i] == 1]

    ax.plot(lbl, omega, '.')

    ax.set_xlabel('$\\alpha$')
    ax.xaxis.set_major_formatter(FormatStrFormatter('%.2g'))
    ax.set_ylabel('$\\omega$')

    ax.set_xticks(np.arange(2, 40, 2))

    fig.subplots_adjust(top=0.95, bottom=0.1, right=0.95, left=0.11)

    plt.savefig("/home/bart/Documents/papers/SR/notes/figures/" + filename, dpi=300)
    plt.show()


def plot_2d_cpt_variable_full(numb_qy, omega_min, omega_max, filename):

    fig = plt.figure()
    ax = fig.add_subplot(111)

    marker = itertools.cycle(('1', '2', '3', '4', ',', '+', '.', 'o', '*', '^', 'v', '>', '<', 'X', '_', 'd', '|', 'H'))

    name_list = []
    lbl = []

    for i in range(2, 100, 2):
        name_list += [f"coulomb_0_plus_CoulombPlane_trunc_{i}"]
        lbl += [i]
    name_list += ["coulomb_0_plus_CoulombPlane"]
    lbl += [100]

    for i, name in enumerate(name_list):
        omega = []
        SR = []
        file = f"fermions_torus_spec_resp_kysym_{name}_n_6_2s_{numb_qy}_ratio_1.000000_qy_0" \
               f".omega_{omega_min}-{omega_max}_eps_0.0001.sr.cut"
        with open('stripped_files/' + file, 'r') as csvfile:
            plots = csv.reader(csvfile, delimiter=' ')
            for row in plots:
                omega.append(float(row[0]))
                SR.append(float(row[1]))
        ax.scatter(omega, SR, s=2, label=f"{lbl[i]}", marker=next(marker))

    ax.set_xlabel('$\omega$')
    ax.set_ylabel('$S$')
    ax.set_ylim(0)
    ax.legend(loc='upper right', handletextpad=0, borderpad=0.4, framealpha=1,
              edgecolor='k', markerscale=3,
              fontsize=10, ncol=8, labelspacing=0, columnspacing=0, title='$\\alpha$')

    fig.subplots_adjust(top=0.95, bottom=0.1, right=0.95, left=0.11)

    plt.savefig("/home/bart/Documents/papers/SR/notes/figures/" + filename, bbox_inches='tight', dpi=300)
    plt.show()


def plot_2d_cpt_variable_full_box(numb_qy, omega_min, omega_max, filename):

    fig = plt.figure()
    ax = fig.add_subplot(111)

    name_list = []
    lbl = []
    data_to_plot = []

    for i in range(2, 100, 2):  # 40
        name_list += [f"coulomb_0_plus_CoulombPlane_trunc_{i}"]
        lbl += [i]
    name_list += ["coulomb_0_plus_CoulombPlane"]
    lbl += [100]

    for i, name in enumerate(name_list):
        omega = []
        SR = []
        file = f"fermions_torus_spec_resp_kysym_{name}_n_6_2s_{numb_qy}_ratio_1.000000_qy_0" \
               f".omega_{omega_min}-{omega_max}_eps_0.0001.sr.cut"
        with open('stripped_files/' + file, 'r') as csvfile:
            plots = csv.reader(csvfile, delimiter=' ')
            for row in plots:
                omega.append(float(row[0]))
                SR.append(float(row[1]))
            data_to_plot += [omega]

    props = dict(markerfacecolor='b', marker='x', markersize=1)
    ax.boxplot(data_to_plot, positions=lbl, flierprops=props, widths=1)

    ax.set_xlabel('$\\alpha$')
    ax.set_xlim([2, 100])
    ax.set_ylabel('$\omega$')

    x = np.linspace(2, 100, 256, endpoint = True)
    # ax.plot(x, np.sqrt(np.pi*x)-10, label="$\omega=\sqrt{\pi \\alpha}-10$")
    ax.plot(x, np.sqrt(x)/(2**(-1.25 + 0.25*np.cos(2*x*np.pi))*np.pi**(0.5*np.sin(np.pi*x)**2)) - 10, label="asymptotic behaviour of $1/V_m^{(0)}$")

    pos = np.arange(2, 100, 4)
    posy = np.arange(2, 100, 4)
    ax.set(xticks=pos, xticklabels=posy)

    ax.legend(loc='upper left')

    fig.subplots_adjust(top=0.95, bottom=0.1, right=0.95, left=0.11)

    plt.savefig("/home/bart/Documents/papers/SR/notes/figures/" + filename, bbox_inches='tight', dpi=300)
    plt.show()


def plot_2d_cpt_variable_full_hist(numb_qy, omega_min, omega_max, filename):

    fig = plt.figure()
    ax = fig.add_subplot(111)

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

    counts, xedges, yedges, im = ax.hist2d(lbl, omega, bins=(19, 50), range=[[1, 101], None], cmap=plt.cm.inferno)
    fig.colorbar(im, ax=ax, label='percentage of S values',
                 format=ticker.FuncFormatter(lambda x, pos: '{0:g}'.format(x/100)))

    ax.set_xlabel('$\\alpha$')
    ax.xaxis.set_major_formatter(FormatStrFormatter('%.2g'))
    ax.set_ylabel('$\\omega$')

    ax.set_xticks(np.arange(2, 102, 6))

    fig.subplots_adjust(top=0.95, bottom=0.1, right=0.95, left=0.11)

    plt.savefig("/home/bart/Documents/papers/SR/notes/figures/" + filename, dpi=300)
    plt.show()


def plot_2d_ypt_variable_full(numb_qy, omega_min, omega_max, filename):

    fig = plt.figure()
    ax = fig.add_subplot(111)

    marker = itertools.cycle(('1', '2', '3', '4', ',', '+', '.', 'o', '*', '^', 'v', '>', '<', 'X', '_', 'd', '|', 'H'))

    name_list = []
    lbl = []

    for i in range(2, 100, 2):
        name_list += [f"coulomb_0_plus_YukawaPlaneL100_trunc_{i}"]
        lbl += [i]
    name_list += ["coulomb_0_plus_YukawaPlaneL100"]
    lbl += [100]

    for i, name in enumerate(name_list):
        omega = []
        SR = []
        file = f"fermions_torus_spec_resp_kysym_{name}_n_6_2s_{numb_qy}_ratio_1.000000_qy_0" \
               f".omega_{omega_min}-{omega_max}_eps_0.0001.sr.cut"
        with open('stripped_files/' + file, 'r') as csvfile:
            plots = csv.reader(csvfile, delimiter=' ')
            for row in plots:
                omega.append(float(row[0]))
                SR.append(float(row[1]))
        ax.scatter(omega, SR, s=2, label=f"{lbl[i]}", marker=next(marker))

    ax.set_xlabel('$\omega$')
    ax.set_ylabel('$S$')
    ax.set_ylim(0)
    ax.legend(loc='upper right', handletextpad=0, borderpad=0.4, framealpha=0.5,
              edgecolor='k', markerscale=3,
              fontsize=10, ncol=3, labelspacing=0, columnspacing=0, title='$\\alpha$')

    fig.subplots_adjust(top=0.95, bottom=0.1, right=0.95, left=0.11)

    plt.savefig("/home/bart/Documents/papers/SR/notes/figures/" + filename, bbox_inches='tight', dpi=300)
    plt.show()


def plot_2d_ypt_variable_full_box(numb_qy, omega_min, omega_max, filename):

    fig = plt.figure()
    ax = fig.add_subplot(111)

    name_list = []
    lbl = []
    data_to_plot = []

    for i in range(2, 100, 2):
        name_list += [f"coulomb_0_plus_YukawaPlaneL100_trunc_{i}"]
        lbl += [i]
    name_list += ["coulomb_0_plus_YukawaPlaneL100"]
    lbl += [100]

    for i, name in enumerate(name_list):
        omega = []
        SR = []
        file = f"fermions_torus_spec_resp_kysym_{name}_n_6_2s_{numb_qy}_ratio_1.000000_qy_0" \
               f".omega_{omega_min}-{omega_max}_eps_0.0001.sr.cut"
        with open('stripped_files/' + file, 'r') as csvfile:
            plots = csv.reader(csvfile, delimiter=' ')
            for row in plots:
                omega.append(float(row[0]))
                SR.append(float(row[1]))
            data_to_plot += [omega]

    props = dict(markerfacecolor='b', marker='x', markersize=1)
    ax.boxplot(data_to_plot, positions=lbl, flierprops=props, widths=1)

    ax.set_xlabel('$\\alpha$')
    ax.set_xlim([2, 100])
    ax.set_ylabel('$\omega$')

    # x = np.linspace(2, 100, 256, endpoint=True)
    # exp_array = np.frompyfunc(mp.exp, 1, 1)
    # pow_array = np.frompyfunc(mp.power, 2, 1)
    # hyperu_array = np.frompyfunc(mp.hyperu, 3, 1)
    # ax.plot(x, (exp_array(-x) * pow_array(x, x) * hyperu_array(x + 1, 1.5, 1)) / mp.sqrt(2) - 10, label="asymptotic behaviour of $V_{1,m}^{(0)}$")
    # ax.legend(loc='upper left')

    pos = np.arange(2, 100, 4)
    posy = np.arange(2, 100, 4)
    ax.set(xticks=pos, xticklabels=posy)

    fig.subplots_adjust(top=0.95, bottom=0.1, right=0.95, left=0.11)

    plt.savefig("/home/bart/Documents/papers/SR/notes/figures/" + filename, bbox_inches='tight', dpi=300)
    plt.show()


def plot_2d_ypt_variable_full_hist(numb_qy, omega_min, omega_max, filename):

    fig = plt.figure()
    ax = fig.add_subplot(111)

    omega = []
    SR = []

    name_list = []
    lbl = []

    for i in range(2, 100, 2):
        name_list += [f"coulomb_0_plus_YukawaPlaneL100_trunc_{i}"]

    for i, name in enumerate(name_list):
        file = f"fermions_torus_spec_resp_kysym_{name}_n_6_2s_{numb_qy}_ratio_1.000000_qy_0" \
               f".omega_{omega_min}-{omega_max}_eps_0.0001.sr.cut"
        with open('stripped_files/' + file, 'r') as csvfile:
            plots = csv.reader(csvfile, delimiter=' ')
            for row in plots:
                omega.append(float(row[0]))
                SR.append(float(row[1]))
                lbl += [2*i+2]

    counts, xedges, yedges, im = ax.hist2d(lbl, omega, bins=(19, 50), range=[[1, 101], None], cmap=plt.cm.inferno)
    fig.colorbar(im, ax=ax, label='percentage of S values',
                 format=ticker.FuncFormatter(lambda x, pos: '{0:g}'.format(x/100)))

    ax.set_xlabel('$\\alpha$')
    ax.xaxis.set_major_formatter(FormatStrFormatter('%.2g'))
    ax.set_ylabel('$\\omega$')

    ax.set_xticks(np.arange(2, 102, 4))

    fig.subplots_adjust(top=0.95, bottom=0.1, right=0.95, left=0.11)

    plt.savefig("/home/bart/Documents/papers/SR/notes/figures/" + filename, dpi=300)
    plt.show()


# Short and long range interactions ####################################################################################

def plot_2d_lpv3(numb_qy, omega_min, omega_max, filename):

    fig = plt.figure()
    ax = fig.add_subplot(111)

    marker = itertools.cycle(('1', '2', '3', '4', ',', '+', '.', 'o', '*', '^', 'v', '>', '<', 'X', '_', 'd', '|', 'H'))

    for i, name in enumerate(["V1_V3_0.0001", "V1_V3_0.001", "V1_V3_0.01", "V1_V3_0.1", "V1_V3"]):
        omega = []
        SR = []
        file = f"fermions_torus_spec_resp_kysym_{name}_n_6_2s_{numb_qy}_ratio_1.000000_qy_0" \
               f".omega_{omega_min}-{omega_max}_eps_0.0001.sr.cut"
        with open('stripped_files/' + file, 'r') as csvfile:
            plots = csv.reader(csvfile, delimiter=' ')
            for row in plots:
                omega.append(float(row[0]))
                SR.append(float(row[1]))
        ax.scatter(omega, SR, s=2, label=f"{i-4}", marker=next(marker))

    ax.set_xlabel('$\omega$')
    ax.set_ylabel('$S$')
    ax.legend(loc='upper right', handletextpad=0, borderpad=0.4, framealpha=1,
              edgecolor='k', markerscale=3,
              fontsize=10, ncol=3, labelspacing=0, columnspacing=0, title='$\log \\alpha$')

    fig.subplots_adjust(top=0.95, bottom=0.1, right=0.95, left=0.11)

    plt.savefig("/home/bart/Documents/papers/SR/notes/figures/" + filename, bbox_inches='tight', dpi=300)
    plt.show()


def plot_2d_lpv17(numb_qy, omega_min, omega_max, filename):

    fig = plt.figure()
    ax = fig.add_subplot(111)

    marker = itertools.cycle(('1', '2', '3', '4', ',', '+', '.', 'o', '*', '^', 'v', '>', '<', 'X', '_', 'd', '|', 'H'))

    for i, name in enumerate(["V1_V17_0.0001", "V1_V17_0.001", "V1_V17_0.01", "V1_V17_0.1", "V1_V17"]):
        omega = []
        SR = []
        file = f"fermions_torus_spec_resp_kysym_{name}_n_6_2s_{numb_qy}_ratio_1.000000_qy_0" \
               f".omega_{omega_min}-{omega_max}_eps_0.0001.sr.cut"
        with open('stripped_files/' + file, 'r') as csvfile:
            plots = csv.reader(csvfile, delimiter=' ')
            for row in plots:
                omega.append(float(row[0]))
                SR.append(float(row[1]))
        ax.scatter(omega, SR, s=2, label=f"{i-4}", marker=next(marker))

    ax.set_xlabel('$\omega$')
    ax.set_ylabel('$S$')
    ax.legend(loc='upper right', handletextpad=0, borderpad=0.4, framealpha=1,
              edgecolor='k', markerscale=3,
              fontsize=10, ncol=3, labelspacing=0, columnspacing=0, title='$\log \\alpha$')

    fig.subplots_adjust(top=0.95, bottom=0.1, right=0.95, left=0.11)

    plt.savefig("/home/bart/Documents/papers/SR/notes/figures/" + filename, bbox_inches='tight', dpi=300)
    plt.show()


def plot_2d_lpv17_res(numb_qy, omega_min, omega_max, filename):

    fig = plt.figure()
    ax = fig.add_subplot(111)

    marker = itertools.cycle(('1', '2', '3', '4', ',', '+', '.', 'o', '*', '^', 'v', '>', '<', 'X', '_', 'd', '|', 'H'))

    for i, name in enumerate(["V1_V17_0.0001", "V1_V17_0.001", "V1_V17_0.01", "V1_V17_0.1", "V1_V17"]):
        omega = []
        SR = []
        file = f"fermions_torus_spec_resp_kysym_{name}_n_6_2s_{numb_qy}_ratio_1.000000_qy_0" \
               f".omega_{omega_min}-{omega_max}_eps_1e-06.sr.cut"
        with open('stripped_files/' + file, 'r') as csvfile:
            plots = csv.reader(csvfile, delimiter=' ')
            for row in plots:
                omega.append(float(row[0]))
                SR.append(float(row[1]))
        ax.scatter(omega, SR, s=2, label=f"{i-4}", marker=next(marker))

    # ax.set_xlim([-10.0001, -9.9999])
    ax.set_xlabel('$\omega$')
    ax.set_ylabel('$S$')
    ax.legend(loc='upper right', handletextpad=0, borderpad=0.4, framealpha=1,
              edgecolor='k', markerscale=3,
              fontsize=10, ncol=3, labelspacing=0, columnspacing=0, title='$\log \\alpha$')

    fig.subplots_adjust(top=0.95, bottom=0.1, right=0.95, left=0.11)

    plt.savefig("/home/bart/Documents/papers/SR/notes/figures/" + filename, bbox_inches='tight', dpi=300)
    plt.show()


if __name__ == "__main__":

    # Coulomb and Laughlin tests #######################################################################################
    #
    # name = "coulomb"
    # plot_2d_q(name, 18, omega_min=-100, omega_max=100, filename=f"{name}_2d.png")
    # name = "coulomb_swap"
    # plot_2d_q(name, 18, omega_min=-100, omega_max=100, filename=f"{name}_2d.png")
    # name = "coulomb_plus_zero"
    # plot_2d_q(name, 18, omega_min=-100, omega_max=100, filename=f"{name}_2d.png")
    # name = "coulomb_plus_zero_swap"
    # plot_2d_q(name, 18, omega_min=-100, omega_max=100, filename=f"{name}_2d.png")
    # name = "coulomb_plus_V1_scale_0.0001"
    # plot_2d_q(name, 18, omega_min=-100, omega_max=100, filename=f"{name}_2d.png")
    # name = "V1"
    # plot_2d_q(name, 18, omega_min=-100, omega_max=100, filename=f"{name}_2d.png")
    # name = "coulomb_0_plus_V1"
    # plot_2d_q(name, 18, omega_min=-100, omega_max=100, filename=f"{name}_2d.png")
    # name = "coulomb_0.0001_plus_V1"
    # plot_2d_q(name, 18, omega_min=-100, omega_max=100, filename=f"{name}_2d.png")
    # plot_laughlin_res_2d(18, omega_min=-25, omega_max=5, filename="laughlin_res_2d.png")
    plot_2d_coulomb_conv_box(18, omega_min=-100, omega_max=100, filename="coulomb_conv_box_2d_offset.png")

    # Laughlin perturbed by Coulomb ####################################################################################
    #
    # plot_2d_lpc(18, omega_min=-100, omega_max=100, filename="lpc_2d.png")
    # plot_2d_lpc_early(18, omega_min=-100, omega_max=100, filename="lpc_early_2d.png")
    # plot_2d_lpc_early_max(18, omega_min=-100, omega_max=100, filename="lpc_early_max_2d.png")
    # plot_2d_lpc_linear(18, omega_min=-100, omega_max=100, filename="lpc_linear_2d.png")
    # plot_2d_lpc_linear_hist(18, omega_min=-100, omega_max=100, filename="lpc_linear_hist_2d.png")
    # plot_2d_lpc_linear_max(18, omega_min=-100, omega_max=100, filename="lpc_linear_max_2d.png")

    # Laughlin tune to Coulomb #########################################################################################
    #
    # plot_2d_ltc(18, omega_min=-100, omega_max=100, filename="ltc_2d.png")
    # plot_2d_ltc_early(18, omega_min=-100, omega_max=100, filename="ltc_early_2d.png")
    # plot_2d_ltc_early_reorth(18, omega_min=-100, omega_max=100, filename="ltc_early_reorth_2d.png")
    # plot_2d_ltc_early_max(18, omega_min=-100, omega_max=100, filename="ltc_early_max_2d.png")
    # plot_2d_ltc_early_reorth_max(18, omega_min=-100, omega_max=100, filename="ltc_early_reorth_max_2d.png")
    # plot_2d_ltc_early_res(18, omega_min=-10, omega_max=-9.992, filename="ltc_early_res_2d.png")
    # plot_2d_ltc_early_reorth_res(18, omega_min=-10, omega_max=-9.992, filename="ltc_early_reorth_res_2d.png")
    # plot_2d_ltc_early_res_max(18, omega_min=-10, omega_max=-9.992, filename="ltc_early_res_max_2d.png")
    # plot_2d_ltc_early_reorth_res_max(18, omega_min=-10, omega_max=-9.992, filename="ltc_early_reorth_res_max_2d.png")
    # plot_2d_ltc_earlyish_res(18, omega_min=-10, omega_max=-9.9, filename="ltc_earlyish_res_2d.png")
    # plot_2d_ltc_earlyish_res_max(18, omega_min=-10, omega_max=-9.9, filename="ltc_earlyish_res_max_2d.png")
    # plot_2d_ltc_latish_res(18, omega_min=-10, omega_max=-9, filename="ltc_latish_res_2d.png")
    # plot_2d_ltc_latish_res_max(18, omega_min=-10, omega_max=-9, filename="ltc_latish_res_max_2d.png")
    # plot_2d_ltc_late_res(18, omega_min=-10, omega_max=0, filename="ltc_late_res_2d.png")
    # plot_2d_ltc_late_res_max(18, omega_min=-10, omega_max=0, filename="ltc_late_res_max_2d.png")
    # plot_2d_ltc_complete_res_max(18, filename="ltc_complete_res_max_2d.png")
    # plot_2d_ltc_slope_res_max(18, filename="ltc_slope_res_max_2d.png")
    # plot_2d_ltc_nbr_omega_res_max(18, filename="ltc_nbr_omega_res_max_2d.png")
    # plot_2d_ltc_mean_S_res_max(18, filename="ltc_mean_S_res_max_2d.png")
    # plot_2d_ltypp_complete_res_max(18, filename="ltyppl1_complete_res_max_2d.png")
    # plot_2d_ltypp_slope_res_max(18, filename="ltyppl1_slope_res_max_2d.png")
    # plot_2d_ltypp_nbr_omega_res_max(18, filename="ltyppl1_nbr_omega_res_max_2d.png")
    # plot_2d_ltypp_mean_S_res_max(18, filename="ltyppl1_mean_S_res_max_2d.png")
    # plot_2d_lty_complete_res_max(18, filename="ltyl100_complete_res_max_2d.png")
    # plot_2d_lty_slope_res_max(18, filename="ltyl100_slope_res_max_2d.png")
    # plot_2d_lty_nbr_omega_res_max(18, filename="ltyl100_nbr_omega_res_max_2d.png")
    # plot_2d_lty_mean_S_res_max(18, filename="ltyl100_mean_S_res_max_2d.png")

    # Coulomb pseudopotentials #########################################################################################
    #
    # plot_2d_cpt_fixed(18, omega_min=-100, omega_max=100, filename="cpt_fixed_2d.png")
    # plot_2d_cpt_fixed_full(18, omega_min=-100, omega_max=100, filename="cpt_fixed_full_2d.png")
    # plot_2d_cpt_fixed_full_box(18, omega_min=-100, omega_max=100, filename="cpt_fixed_full_box_2d.png")
    # plot_2d_cpt_fixed_full_hist(18, omega_min=-100, omega_max=100, filename="cpt_fixed_full_hist_2d.png")
    # plot_2d_cpt_fixed_full_max(18, omega_min=-100, omega_max=100, filename="cpt_fixed_full_max_2d.png")  # old
    # plot_2d_cpt_variable_full(18, omega_min=-100, omega_max=100, filename="cpt_variable_full_2d.png")
    # plot_2d_cpt_variable_full_box(18, omega_min=-100, omega_max=100, filename="cpt_variable_full_box_2d.png")
    # plot_2d_cpt_variable_full_hist(18, omega_min=-100, omega_max=100, filename="cpt_variable_full_hist_2d.png")

    # Yukawa pseudopotentials ##########################################################################################
    #
    # plot_2d_ypt_variable_full(18, omega_min=-100, omega_max=100, filename="yptl100_variable_full_2d.png")
    # plot_2d_ypt_variable_full_box(18, omega_min=-100, omega_max=100, filename="yptl100_variable_full_box_2d.png")
    # plot_2d_ypt_variable_full_hist(18, omega_min=-100, omega_max=100, filename="yptl100_variable_full_hist_2d.png")

    # Short and long range interactions ################################################################################
    #
    # plot_2d_lpv3(18, omega_min=-100, omega_max=100, filename="lpv3_2d.png")
    # plot_2d_lpv17(18, omega_min=-100, omega_max=100, filename="lpv17_2d.png")
    # plot_2d_lpv17_res(18, omega_min=-11, omega_max=-9, filename="lpv17_res_2d.png")
