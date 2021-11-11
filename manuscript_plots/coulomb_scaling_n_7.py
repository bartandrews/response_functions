import numpy as np
import matplotlib.pyplot as plt
from matplotlib.transforms import Bbox
from mpl_toolkits.mplot3d import Axes3D
import random
import csv
import heapq
import glob
import itertools
import matplotlib.gridspec as gridspec
from matplotlib.ticker import FormatStrFormatter, LogLocator
import matplotlib.ticker as ticker
import matplotlib.colors as colors
from scipy import stats
from scipy.special import hyperu
# from mpmath import sqrt, pi, gamma, hyperu, fac, fac2, exp
import mpmath as mp
from matplotlib.patches import ConnectionPatch, Polygon


plt.rc('text', usetex=True)
plt.rc('text.latex', preamble=r'\usepackage{amsmath}')


def line_of_best_fit(axis, x_list, y_list, xval=0.05, yval=0.70, name="m"):

    parameters, cov = np.polyfit(x_list, y_list, 1, cov=True)
    _, _, r_value, _, _ = stats.linregress(x_list, y_list)
    m, m_err, c, c_err = parameters[0], np.sqrt(cov[0][0]), parameters[1], np.sqrt(cov[1][1])
    r2_value = r_value*r_value

    # print("SvN = m*(Ly/lB) + c")
    # print(f"(m, m_err, c, c_err) = ({m:.5f}, {m_err:.5f}, {c:.5f}, {c_err:.5f})")
    xvalues = np.linspace(min(x_list)-2, max(x_list))
    axis.plot(xvalues, m * xvalues + c, '-', c='k', zorder=-1, lw=0.5)
    axis.text(xval, yval, "${name}={gradient:.3g}\pm{gradient_err:.3g}$".format(name=name,
        gradient=m, gradient_err=m_err, intercept=c, rsquared=r2_value, fontsize=10), transform=axis.transAxes)

    return m, m_err, c, c_err, r2_value


def plot_coulomb(axis, omega_min, omega_max, epsilon):

    marker = itertools.cycle(('1', '2', '3', '4', ',', '+', '.', 'o', '*', '^', 'v', '>', '<', 'X', '_', 'd', '|', 'H'))

    omega = []
    SR = []
    file = f"fermions_torus_spec_resp_kysym_coulomb_n_7_2s_21_ratio_1.000000_qy_0" \
           f".omega_{omega_min}-{omega_max}_eps_{epsilon}.sr.cut"
    with open('/home/bart/PycharmProjects/response_functions/FQHETorusSpectralResponse/stripped_files/' + file, 'r') as csvfile:
        plots = csv.reader(csvfile, delimiter=' ')
        for row in plots:
            omega.append(float(row[0])+10)
            SR.append(float(row[1]))
    axis.scatter(omega, SR, s=1, marker=next(marker))

    axis.set_xlabel('$\omega$')
    axis.set_xticks(np.arange(0, 6, 1))
    axis.set_ylabel('$S\epsilon / 10^{-4}$')
    axis.set_xlim([omega_min+10, omega_max+10])
    axis.set_ylim(bottom=0)
    #axis.axvline(1.25, color='k', linewidth=1, ls='--')
    #axis.axvline(3.75, color='k', linewidth=1, ls='--')
    region = Polygon(((1.25, 0), (3.75, 0), (3.75, 1200), (1.25, 1200)), fc=(1, 0, 0, 0.2))
    axis.add_artist(region)


def plot_coulomb_zoomed(axis, omega_min, omega_max, epsilon):

    marker = itertools.cycle(('1', '2', '3', '4', ',', '+', '.', 'o', '*', '^', 'v', '>', '<', 'X', '_', 'd', '|', 'H'))

    omega = []
    SR = []
    file = f"fermions_torus_spec_resp_kysym_coulomb_n_7_2s_21_ratio_1.000000_qy_0" \
           f".omega_{omega_min}-{omega_max}_eps_{epsilon}.sr.cut"
    with open('/home/bart/PycharmProjects/response_functions/FQHETorusSpectralResponse/stripped_files/' + file, 'r') as csvfile:
        plots = csv.reader(csvfile, delimiter=' ')
        for row in plots:
            omega.append(float(row[0])+10)
            SR.append(float(row[1])/2)
    axis.scatter(omega, SR, s=1, marker=next(marker))

    axis.set_xlabel('$\omega$')
    axis.set_xticks(np.arange(0, 6, 1))
    axis.set_ylabel('$S\epsilon / 10^{-4}$')
    axis.set_xlim([omega_min+10, omega_max+10])
    axis.set_ylim(bottom=0)
    region = Polygon(((1.25, 0), (3.75, 0), (3.75, 1200), (1.25, 1200)), fc=(1, 0, 0, 0.2))
    axis.add_artist(region)


def plot_2d_q_specific(axis):

    domain = np.linspace(1, 7, 7, endpoint=True)

    SR_max_mean = []
    SR_max_std = []

    for j in domain:

        print(j)

        omega = []
        SR = []
        file = f"fermions_torus_spec_resp_kysym_coulomb_n_7_2s_21_ratio_1.000000_qy_0" \
               f".omega_{-7.5-5/(2**j):.6g}-{-7.5+5/(2**j):.6g}_eps_{0.0001/(2**(j-1)):.6g}.sr.cut"
        with open('/home/bart/PycharmProjects/response_functions/FQHETorusSpectralResponse/stripped_files/' + file, 'r') as csvfile:
            plots = csv.reader(csvfile, delimiter=' ')
            for row in plots:
                omega.append(float(row[0]))
                SR.append(float(row[1]))

        # print("mean(SR) = ", np.mean(SR))
        # print("std(SR) = ", np.std(SR))

        omega_max = []
        sr_max = []
        for i, entry in enumerate(omega):
            if SR[i] > SR[i - 1] and SR[i] > SR[i + 1]:
                omega_max += [1]
                sr_max += [SR[i]]
            else:
                omega_max += [0]

        SR_max_mean += [np.mean(sr_max)]
        # print("mean(SR_max) = ", np.mean(sr_max))
        SR_max_std += [np.std(sr_max)]
        # print("std(SR_max) = ", np.std(sr_max))

    log_scale_factors = []
    log_SR_max_mean = []
    log_SR_max_std = []

    for i, j in enumerate(domain):
        log_scale_factors += [np.log2(1/(2**(j-1)))]
        log_SR_max_mean += [np.log2(SR_max_mean[i])]
        log_SR_max_std += [np.log2(SR_max_std[i])]

    # marker = itertools.cycle(('1', '2', '3', '4', ',', '+', '.', 'o', '*', '^', 'v', '>', '<', 'X', '_', 'd', '|', 'H'))
    #
    axis.set_xlabel('$\log_2(\mathrm{range}(\omega)/\mathrm{range}(\omega_0))$')
    # ax.set_ylabel('$\log_2(\sigma_{S_{\mathrm{max}}})$')
    # ax.set_ylim(bottom=0)

    axis.scatter(log_scale_factors, log_SR_max_mean, marker='x', s=10, label="$\log_2(\mu_{S_{\mathrm{max}}})$")
    axis.scatter(log_scale_factors, log_SR_max_std, marker='^', s=10, label="$\log_2(\sigma_{S_{\mathrm{max}}})$")

    leg = axis.legend(loc='upper center', bbox_to_anchor=(0.5, 1.2), handletextpad=0, borderpad=0.4, framealpha=0,
                      edgecolor='w', markerscale=1.5, ncol=2, labelspacing=0, columnspacing=0)
    leg.get_frame().set_linewidth(0.5)

    line_of_best_fit(axis, log_scale_factors[:-2], log_SR_max_mean[:-2], xval=0.05, yval=0.05, name="m_\mu")
    line_of_best_fit(axis, log_scale_factors[:-2], log_SR_max_std[:-2], xval=0.29, yval=0.855, name="m_\sigma")


def plot_2d_gap_omega_res_max(axis):

    omega = []
    SR = []

    omega_max_gap_mean = []
    # omega_max_gap_std = []

    for i, file in enumerate([f"fermions_torus_spec_resp_kysym_coulomb_n_7_2s_21_ratio_1.000000_qy_0.omega_-10--5_eps_0.0001.sr.cut",
                              f"fermions_torus_spec_resp_kysym_coulomb_n_7_2s_21_ratio_1.000000_qy_0.omega_-8.75--6.25_eps_5e-05.sr.cut",
                              f"fermions_torus_spec_resp_kysym_coulomb_n_7_2s_21_ratio_1.000000_qy_0.omega_-8.125--6.875_eps_2.5e-05.sr.cut",
                              f"fermions_torus_spec_resp_kysym_coulomb_n_7_2s_21_ratio_1.000000_qy_0.omega_-7.8125--7.1875_eps_1.25e-05.sr.cut",
                              f"fermions_torus_spec_resp_kysym_coulomb_n_7_2s_21_ratio_1.000000_qy_0.omega_-7.65625--7.34375_eps_6.25e-06.sr.cut",
                              f"fermions_torus_spec_resp_kysym_coulomb_n_7_2s_21_ratio_1.000000_qy_0.omega_-7.57812--7.42188_eps_3.125e-06.sr.cut",
                              f"fermions_torus_spec_resp_kysym_coulomb_n_7_2s_21_ratio_1.000000_qy_0.omega_-7.53906--7.46094_eps_1.5625e-06.sr.cut"]):

        with open('/home/bart/PycharmProjects/response_functions/FQHETorusSpectralResponse/stripped_files/' + file, 'r') as csvfile:
            plots = csv.reader(csvfile, delimiter=' ')
            for row in plots:
                omega.append(float(row[0])+10)
                SR.append(float(row[1]))

        omega_max = []
        for i, entry in enumerate(omega):
            if SR[i] > SR[i-1] and SR[i] > SR[i+1] and omega[i] > 0:
                omega_max += [omega[i]]

        omega_gaps = [omega_max[i]-omega_max[i-1] for i in range(1, len(omega_max))]
        omega_max_gap_mean += [np.log2(np.mean(omega_gaps))]
        # omega_max_gap_std += [np.log2(np.std(omega_gaps))]

    # print(omega_max_gap_std)

    axis.plot([0, -1, -2, -3, -4, -5, -6], omega_max_gap_mean, 'x', markersize=4, label="$\log_2\langle \Delta\Omega \\rangle$", c="C2")
    # axis.errorbar([0, -1, -2, -3, -4, -5, -6], omega_max_gap_mean, yerr=omega_max_gap_std, markersize=3, label="$\log_2\langle \Delta\Omega \\rangle$", c="C2")
    axis.plot([0, -1, -2, -3, -4, -5, -6], [np.log2((np.abs(5/(2**i) - 5/(2**(i-1))))) for i in range(0, 7)], 'x', markersize=4, label="$\log_2|\Delta\\bar{\omega}_i - \Delta\\bar{\omega}_{i-1}|$", c="C3")


    axis.set_xlabel('$\log_2 (\mathrm{range}(\omega) / \mathrm{range}(\omega_0))$')
    axis.xaxis.set_major_formatter(FormatStrFormatter('$%g$'))
    axis.set_ylim(top=7)
    # axis.set_ylabel('$\langle \Delta\Omega \\rangle$')

    region = Polygon(((-7, -100), (-4, -100), (-4, 100), (-7, 100)), fc=(0, 0, 0, 0.2))
    axis.add_artist(region)

    leg = axis.legend(loc='upper left', handletextpad=0, borderpad=0.4, framealpha=1,
                      edgecolor='k', markerscale=1, ncol=1, labelspacing=0, columnspacing=0)
    leg.get_frame().set_linewidth(0.5)


def plot_2d_nbr_omega_res_max(axis):

    omega = []
    SR = []

    name_list = []
    lbl = []

    for i, file in enumerate([f"fermions_torus_spec_resp_kysym_coulomb_n_7_2s_21_ratio_1.000000_qy_0.omega_-10--5_eps_0.0001.sr.cut",
                              f"fermions_torus_spec_resp_kysym_coulomb_n_7_2s_21_ratio_1.000000_qy_0.omega_-8.75--6.25_eps_5e-05.sr.cut",
                              f"fermions_torus_spec_resp_kysym_coulomb_n_7_2s_21_ratio_1.000000_qy_0.omega_-8.125--6.875_eps_2.5e-05.sr.cut",
                              f"fermions_torus_spec_resp_kysym_coulomb_n_7_2s_21_ratio_1.000000_qy_0.omega_-7.8125--7.1875_eps_1.25e-05.sr.cut",
                              f"fermions_torus_spec_resp_kysym_coulomb_n_7_2s_21_ratio_1.000000_qy_0.omega_-7.65625--7.34375_eps_6.25e-06.sr.cut",
                              f"fermions_torus_spec_resp_kysym_coulomb_n_7_2s_21_ratio_1.000000_qy_0.omega_-7.57812--7.42188_eps_3.125e-06.sr.cut",
                              f"fermions_torus_spec_resp_kysym_coulomb_n_7_2s_21_ratio_1.000000_qy_0.omega_-7.53906--7.46094_eps_1.5625e-06.sr.cut"]):

        with open('/home/bart/PycharmProjects/response_functions/FQHETorusSpectralResponse/stripped_files/' + file, 'r') as csvfile:
            plots = csv.reader(csvfile, delimiter=' ')
            for row in plots:
                omega.append(float(row[0])+10)
                SR.append(float(row[1]))
                lbl += [0 - i]

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

    im = axis.scatter(lbl_values, len_values, s=10)

    axis.set_xlabel('$\log_2 (\mathrm{range}(\omega) / \mathrm{range}(\omega_0))$')
    axis.xaxis.set_major_formatter(FormatStrFormatter('$%g$'))
    axis.set_ylabel('$n(S_\mathrm{max})$')

    #axis.axhline(np.mean(len_values), c='k', zorder=-1, linewidth=0.5, linestyle='--')
    #axis.axhspan(np.mean(len_values) - np.std(len_values), np.mean(len_values) + np.std(len_values), alpha=0.1, color='red')

    # axis.text(0.3, 0.85, "$\\langle n(\\Omega) \\rangle = {mean:.3g}\pm {sd:.3g}$".format(
    #     mean=np.mean(len_values), sd=np.std(len_values), fontsize=10), transform=axis.transAxes)

    region = Polygon(((-7, -100), (-4, -100), (-4, 100), (-7, 100)), fc=(0, 0, 0, 0.2))
    axis.add_artist(region)

    x_list = lbl_values[2:]
    y_list = len_values[2:]

    parameters, cov = np.polyfit(x_list, y_list, 1, cov=True)
    _, _, r_value, _, _ = stats.linregress(x_list, y_list)
    m, m_err, c, c_err = parameters[0], np.sqrt(cov[0][0]), parameters[1], np.sqrt(cov[1][1])
    r2_value = r_value * r_value

    # print("SvN = m*(Ly/lB) + c")
    # print(f"(m, m_err, c, c_err) = ({m:.5f}, {m_err:.5f}, {c:.5f}, {c_err:.5f})")
    xvalues = np.linspace(min(x_list) - 2, max(x_list))
    axis.plot(xvalues, m * xvalues + c, '--', c='k', zorder=-1, lw=0.5)
    axis.text(0.4, 0.2, "$m={gradient:.3g}\pm{gradient_err:.3g}$".format(gradient=m, gradient_err=m_err,
                                                                     intercept=c, rsquared=r2_value,
                                                                     fontsize=10), transform=axis.transAxes)


def plot_2d_mean_S_res_max(axis):

    omega = []
    SR = []

    name_list = []
    lbl = []

    for i, file in enumerate([f"fermions_torus_spec_resp_kysym_coulomb_n_7_2s_21_ratio_1.000000_qy_0.omega_-10--5_eps_0.0001.sr.cut",
                              f"fermions_torus_spec_resp_kysym_coulomb_n_7_2s_21_ratio_1.000000_qy_0.omega_-8.75--6.25_eps_5e-05.sr.cut",
                              f"fermions_torus_spec_resp_kysym_coulomb_n_7_2s_21_ratio_1.000000_qy_0.omega_-8.125--6.875_eps_2.5e-05.sr.cut",
                              f"fermions_torus_spec_resp_kysym_coulomb_n_7_2s_21_ratio_1.000000_qy_0.omega_-7.8125--7.1875_eps_1.25e-05.sr.cut",
                              f"fermions_torus_spec_resp_kysym_coulomb_n_7_2s_21_ratio_1.000000_qy_0.omega_-7.65625--7.34375_eps_6.25e-06.sr.cut",
                              f"fermions_torus_spec_resp_kysym_coulomb_n_7_2s_21_ratio_1.000000_qy_0.omega_-7.57812--7.42188_eps_3.125e-06.sr.cut",
                              f"fermions_torus_spec_resp_kysym_coulomb_n_7_2s_21_ratio_1.000000_qy_0.omega_-7.53906--7.46094_eps_1.5625e-06.sr.cut"]):

        with open('/home/bart/PycharmProjects/response_functions/FQHETorusSpectralResponse/stripped_files/' + file, 'r') as csvfile:
            plots = csv.reader(csvfile, delimiter=' ')
            for row in plots:
                omega.append(float(row[0])+10)
                SR.append(float(row[1]))
                lbl += [0-i]

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
        sr_values += [(sr_mean/10000)*2**lbl_val]

    im = axis.scatter(lbl_values, sr_values, s=10)

    axis.set_xlabel('$\log_2(\mathrm{range}(\omega)/\mathrm{range}(\omega_0))$')
    axis.xaxis.set_major_formatter(FormatStrFormatter('$%g$'))
    axis.set_ylabel('$\\bar{S}_\mathrm{max}\epsilon$')

    axis.axhline(np.mean(sr_values[2:]), c='k', zorder=-1, linewidth=0.5, linestyle='--')
    # axis.axhspan(np.mean(sr_values[2:])-np.std(sr_values[2:]), np.mean(sr_values[2:])+np.std(sr_values[2:]), alpha=0.1, color='red')

    axis.text(0.375, 0.3, "$\\langle \\bar{{S}}_\mathrm{{max}}\epsilon \\rangle = {mean:.3g}$".format(
        mean=np.mean(sr_values), sd=np.std(sr_values), fontsize=10), transform=axis.transAxes)
    axis.text(0.645, 0.2, "$\pm{sd:.3g}$".format(
        mean=np.mean(sr_values), sd=np.std(sr_values), fontsize=10), transform=axis.transAxes)

    region = Polygon(((-7, -0.03), (-4, -0.03), (-4, 0.03), (-7, 0.03)), fc=(0, 0, 0, 0.2))
    axis.add_artist(region)

    # ax.set_xticks(np.arange(2, 40, 2))

    # fig.subplots_adjust(top=0.95, bottom=0.1, right=0.95, left=0.11)


if __name__ == "__main__":

    fig = plt.figure(figsize=(6, 7.5))
    gs = gridspec.GridSpec(3, 2, hspace=0.4, wspace=0.4)

    ax0 = plt.subplot(gs[0])
    plot_coulomb(ax0, omega_min=-10, omega_max=-5, epsilon=0.0001)
    #ax1 = plt.subplot(gs[1])
    #plot_2d_q_specific(ax1)
    ax2 = plt.subplot(gs[2])
    plot_coulomb_zoomed(ax2, omega_min=-8.75, omega_max=-6.25, epsilon=5e-05)
    # ax3 = plt.subplot(gs[3])
    # plot_2d_gap_omega_res_max(ax3)
    # ax4 = plt.subplot(gs[4])
    # plot_2d_nbr_omega_res_max(ax4)
    # ax5 = plt.subplot(gs[5])
    # plot_2d_mean_S_res_max(ax5)

    left_connector = ConnectionPatch(xyA=(1.25, 0), xyB=(1.25, 1200), coordsA="data", coordsB="data",
                                     axesA=ax0, axesB=ax2, arrowstyle='-',
                                     facecolor='k', edgecolor='k')
    right_connector = ConnectionPatch(xyA=(3.75, 0), xyB=(3.75, 1200), coordsA="data", coordsB="data",
                                     axesA=ax0, axesB=ax2, arrowstyle='-',
                                     facecolor='k', edgecolor='k')
    ax2.add_artist(left_connector)
    ax2.add_artist(right_connector)

    fig.text(0.02, 0.9, "(a)", fontsize=12)
    fig.text(0.49, 0.9, "(b)", fontsize=12)
    # fig.text(0.02, 0.62, "(c)", fontsize=12)
    fig.text(0.49, 0.62, "(c)", fontsize=12)
    fig.text(0.02, 0.33, "(d)", fontsize=12)
    fig.text(0.49, 0.33, "(e)", fontsize=12)

    plt.savefig("/home/bart/Documents/papers/SR/coulomb_scaling_n_7.png", bbox_inches='tight', dpi=300)
    plt.show()
