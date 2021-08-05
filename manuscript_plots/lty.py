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

plt.rc('text', usetex=True)
plt.rc('text.latex', preamble=r'\usepackage{amsmath}')


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


def plot_2d_lty_omega_mean(axis, numb_qy):

    for lamb_val in [0.0001, 0.001, 0.01, 0.1, 1, 10, 100]:

        print("lambda = ", lamb_val)

        omega = []
        SR = []

        name_list = []
        lbl = []

        for alpha_exp in np.linspace(-4, 0, 41, endpoint=True):
            if lamb_val == 10 and alpha_exp < -3:
                lower_lim = -3
                continue
            if lamb_val == 100 and alpha_exp < -2:
                lower_lim = -2
                continue
            if lamb_val < 10:
                lower_lim = -4
            if alpha_exp == 0:
                name_list.append(f"fermions_torus_spec_resp_kysym_yukawa-{lamb_val}_plus_V1_scale_0_n_6_2s_{numb_qy}_ratio_1.000000_qy_0.omega_-10-10_eps_1e-06.sr.cut")
            else:
                name_list.append(f"fermions_torus_spec_resp_kysym_yukawa-{lamb_val}_{10**alpha_exp:.5g}_plus_V1_scale_{1-10**alpha_exp:.5g}_n_6_2s_{numb_qy}_ratio_1.000000_qy_0.omega_-10-10_eps_1e-06.sr.cut")

        print("lower_lim = ", lower_lim)

        for i, file in enumerate(name_list):
            with open('/home/bart/PycharmProjects/response_functions/FQHETorusSpectralResponse/stripped_files/' + file, 'r') as csvfile:
                plots = csv.reader(csvfile, delimiter=' ')
                for row in plots:
                    omega.append(float(row[0])+10)
                    SR.append(float(row[1]))
                    lbl += [10 ** (lower_lim + i * 0.1)]
                    # if i < 10:
                    #     lbl += [0.0001*(i+1)]
                    # elif 10 <= i < 19:
                    #     lbl += [0.001 * (i % 10 + 2)]
                    # elif 19 <= i < 28:
                    #     lbl += [0.01 * (i % 19 + 2)]
                    # elif 28 <= i:
                    #     lbl += [0.1 * (i % 28 + 2)]

        # print(np.shape(omega), np.shape(SR), np.shape(lbl))

        omega_max = []
        sr_max = []
        for i, entry in enumerate(omega):
            if SR[i] > SR[i-1] and SR[i] > SR[i+1] and omega[i] > 0:
                omega_max += [1]
                sr_max += [SR[i]]
            else:
                omega_max += [0]

        # print(omega_max.count(1))

        lbl[:] = [x for i, x in enumerate(lbl) if omega_max[i] == 1]
        omega[:] = [x for i, x in enumerate(omega) if omega_max[i] == 1]

        log_mean_vals = []
        lbl_values = sorted(list(set(lbl)))
        for lbl_val in lbl_values:
            omega_set = [i for i, e in enumerate(lbl) if e == lbl_val]
            mean_val = np.average(omega[omega_set[0]:omega_set[-1]+1])
            log_mean_val = np.log10(mean_val)
            log_mean_vals += [log_mean_val]

        log_lbl_values = [np.log10(i) for i in lbl_values]
        # print(log_lbl_values)
        # print(log_omega_range)

        im = axis.scatter(log_lbl_values, log_mean_vals, s=10, label=f"${np.log10(lamb_val):g}$")

    axis.set_xlabel('$\\log \\alpha$')
    axis.xaxis.set_major_formatter(FormatStrFormatter('$%g$'))
    axis.set_ylabel('$\\log\\bar{\\Omega}$')
    axis.yaxis.set_major_formatter(FormatStrFormatter('$%g$'))

    # leg = axis.legend(loc='upper left', handletextpad=0, borderpad=0.2, framealpha=0,
    #                   edgecolor='w', markerscale=1, ncol=1, labelspacing=0, columnspacing=0, bbox_to_anchor=(-0.05, 1.01), title='$\log\lambda$')
    # leg.get_frame().set_linewidth(0.5)


def plot_2d_lty_omega_range(axis, numb_qy):

    for lamb_val in [0.0001, 0.001, 0.01, 0.1, 1, 10, 100]:

        print("lambda = ", lamb_val)

        omega = []
        SR = []

        name_list = []
        lbl = []

        for alpha_exp in np.linspace(-4, 0, 41, endpoint=True):
            if lamb_val == 10 and alpha_exp < -3:
                lower_lim = -3
                continue
            if lamb_val == 100 and alpha_exp < -2:
                lower_lim = -2
                continue
            if lamb_val < 10:
                lower_lim = -4
            if alpha_exp == 0:
                name_list.append(f"fermions_torus_spec_resp_kysym_yukawa-{lamb_val}_plus_V1_scale_0_n_6_2s_{numb_qy}_ratio_1.000000_qy_0.omega_-10-10_eps_1e-06.sr.cut")
            else:
                name_list.append(f"fermions_torus_spec_resp_kysym_yukawa-{lamb_val}_{10**alpha_exp:.5g}_plus_V1_scale_{1-10**alpha_exp:.5g}_n_6_2s_{numb_qy}_ratio_1.000000_qy_0.omega_-10-10_eps_1e-06.sr.cut")

        print("lower_lim = ", lower_lim)

        for i, file in enumerate(name_list):
            with open('/home/bart/PycharmProjects/response_functions/FQHETorusSpectralResponse/stripped_files/' + file, 'r') as csvfile:
                plots = csv.reader(csvfile, delimiter=' ')
                for row in plots:
                    omega.append(float(row[0])+10)
                    SR.append(float(row[1]))
                    lbl += [10 ** (lower_lim + i * 0.1)]
                    # if i < 10:
                    #     lbl += [0.0001*(i+1)]
                    # elif 10 <= i < 19:
                    #     lbl += [0.001 * (i % 10 + 2)]
                    # elif 19 <= i < 28:
                    #     lbl += [0.01 * (i % 19 + 2)]
                    # elif 28 <= i:
                    #     lbl += [0.1 * (i % 28 + 2)]

        # print(np.shape(omega), np.shape(SR), np.shape(lbl))

        omega_max = []
        sr_max = []
        for i, entry in enumerate(omega):
            if SR[i] > SR[i-1] and SR[i] > SR[i+1] and omega[i] > 0:
                omega_max += [1]
                sr_max += [SR[i]]
            else:
                omega_max += [0]

        # print(omega_max.count(1))

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
        # print(log_lbl_values)
        # print(log_omega_range)

        im = axis.scatter(log_lbl_values, log_omega_range, s=10, label=f"${np.log10(lamb_val):g}$")

    axis.set_xlabel('$\\log \\alpha$')
    axis.xaxis.set_major_formatter(FormatStrFormatter('$%g$'))
    axis.set_ylabel('$\\log[\\mathrm{range}(\\Omega)]$')
    axis.yaxis.set_major_formatter(FormatStrFormatter('$%g$'))

    leg = axis.legend(loc='center', handletextpad=0, borderpad=0.2, framealpha=1,
                      edgecolor=None, markerscale=1, ncol=7, labelspacing=0, columnspacing=0, bbox_to_anchor=(-0.2, 1.2), title='$\log\lambda$')
    leg.get_frame().set_linewidth(0.5)


if __name__ == "__main__":

    fig = plt.figure(figsize=(6, 2.5))
    gs = gridspec.GridSpec(1, 2, hspace=0.4, wspace=0.4)

    ax0 = plt.subplot(gs[0])
    plot_2d_lty_omega_mean(ax0, 18)
    ax1 = plt.subplot(gs[1])
    plot_2d_lty_omega_range(ax1, 18)

    fig.text(0.04, 0.85, "(a)", fontsize=12)
    fig.text(0.49, 0.85, "(b)", fontsize=12)

    fig.text(0.15, 0.79, "average", fontsize=11)
    fig.text(0.6, 0.79, "spread", fontsize=11)

    plt.savefig("/home/bart/Documents/papers/SR/lty.png", bbox_inches='tight', dpi=300)
    plt.show()

