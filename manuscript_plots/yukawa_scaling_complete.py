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


def plot_2d_Smax_mean_omega(axis):

    for lambda_idx, lambda_val in enumerate([0.0001, 0.001, 0.01, 0.1, 1, 10, 100]):

        if lambda_val < 10:
            center = -7.5
            interval = 5
        elif lambda_val == 10:
            center = -9.75
            interval = 0.5
        elif lambda_val == 100:
            center = -9.975
            interval = 0.05

        if lambda_val == 100:
            max_val = 3
        else:
            max_val = 7

        domain = np.linspace(1, max_val, max_val, endpoint=True)

        SR_max_mean = []
        SR_max_std = []

        for j in domain:

            omega = []
            SR = []
            file = f"fermions_torus_spec_resp_kysym_yukawa-{lambda_val}_plus_V1_scale_0_n_6_2s_18_ratio_1.000000_qy_0" \
                   f".omega_{center - interval/(2**j):.6g}-{center + interval/(2**j):.6g}_eps_{0.0001/(2**(j-1)):.6g}.sr.cut"
            with open('/home/bart/PycharmProjects/response_functions/FQHETorusSpectralResponse/stripped_files/' + file, 'r') as csvfile:
                plots = csv.reader(csvfile, delimiter=' ')
                for row in plots:
                    omega.append(float(row[0]))
                    SR.append(float(row[1]))

            omega_max = []
            sr_max = []
            for i, entry in enumerate(omega):
                if SR[i] > SR[i-1] and SR[i] > SR[i+1]:
                    omega_max += [1]
                    sr_max += [SR[i]]
                else:
                    omega_max += [0]

            SR_max_mean += [np.mean(sr_max)]
            SR_max_std += [np.std(sr_max)]

        log_scale_factors = []
        log_SR_max_mean = []
        log_SR_max_std = []

        for i, j in enumerate(domain):
            log_scale_factors += [np.log2(1 / (2**(j-1)))]
            log_SR_max_mean += [np.log2(SR_max_mean[i])]
            log_SR_max_std += [np.log2(SR_max_std[i])]

        axis.set_ylabel('$\log_2(\mu_{S_{\mathrm{max}}})$')


        if lambda_val < 0.1:
            axis.scatter(log_scale_factors, log_SR_max_mean, s=10, c=f"C{lambda_idx}",
                         label=f"${np.log10(lambda_val):g}$")
            axis.plot(log_scale_factors[-3:], log_SR_max_mean[-3:], c=f"C{lambda_idx}", ls="--")
            axis.plot(log_scale_factors[:5], log_SR_max_mean[:5], c=f"C{lambda_idx}")
        elif lambda_val == 0.1:
            axis.scatter(log_scale_factors[:5], log_SR_max_mean[:5], s=10, c=f"C{lambda_idx}",
                         label=f"${np.log10(lambda_val):g}$")
            axis.plot(log_scale_factors[:5], log_SR_max_mean[:5], c=f"C{lambda_idx}")
        elif lambda_val == 1:
            axis.scatter(log_scale_factors[:5], log_SR_max_mean[:5], s=10, c=f"C{lambda_idx}",
                         label=f"${np.log10(lambda_val):g}$")
            axis.plot(log_scale_factors[:5], log_SR_max_mean[:5], c=f"C{lambda_idx}")
        elif lambda_val == 10:
            axis.scatter(log_scale_factors[:3], log_SR_max_mean[:3], s=10, c=f"C{lambda_idx}",
                         label=f"${np.log10(lambda_val):g}$")
            axis.plot(log_scale_factors[:3], log_SR_max_mean[:3], c=f"C{lambda_idx}")
        elif lambda_val == 100:
            axis.scatter(log_scale_factors[:3], log_SR_max_mean[:3], s=10, c=f"C{lambda_idx}",
                         label=f"${np.log10(lambda_val):g}$")
            axis.plot(log_scale_factors[:3], log_SR_max_mean[:3], c=f"C{lambda_idx}")

    # axis.set_ylim(bottom=5)

    leg = axis.legend(loc='center', handletextpad=0, borderpad=0.2, framealpha=1,
                      edgecolor=None, markerscale=1, ncol=4, labelspacing=0, columnspacing=0,
                      bbox_to_anchor=(0.5, 1.35), title='$\log\lambda$')
    leg.get_frame().set_linewidth(0.5)


def plot_2d_Smax_std_omega(axis):

    for lambda_idx, lambda_val in enumerate([0.0001, 0.001, 0.01, 0.1, 1, 10, 100]):

        if lambda_val < 10:
            center = -7.5
            interval = 5
        elif lambda_val == 10:
            center = -9.75
            interval = 0.5
        elif lambda_val == 100:
            center = -9.975
            interval = 0.05

        if lambda_val == 100:
            max_val = 3
        else:
            max_val = 7

        domain = np.linspace(1, max_val, max_val, endpoint=True)

        SR_max_mean = []
        SR_max_std = []

        for j in domain:

            omega = []
            SR = []
            file = f"fermions_torus_spec_resp_kysym_yukawa-{lambda_val}_plus_V1_scale_0_n_6_2s_18_ratio_1.000000_qy_0" \
                   f".omega_{center - interval / (2 ** j):.6g}-{center + interval / (2 ** j):.6g}_eps_{0.0001 / (2 ** (j - 1)):.6g}.sr.cut"
            with open('/home/bart/PycharmProjects/response_functions/FQHETorusSpectralResponse/stripped_files/' + file,
                      'r') as csvfile:
                plots = csv.reader(csvfile, delimiter=' ')
                for row in plots:
                    omega.append(float(row[0]))
                    SR.append(float(row[1]))

            omega_max = []
            sr_max = []
            for i, entry in enumerate(omega):
                if SR[i] > SR[i - 1] and SR[i] > SR[i + 1]:
                    omega_max += [1]
                    sr_max += [SR[i]]
                else:
                    omega_max += [0]

            SR_max_mean += [np.mean(sr_max)]
            SR_max_std += [np.std(sr_max)]

        log_scale_factors = []
        log_SR_max_mean = []
        log_SR_max_std = []

        for i, j in enumerate(domain):
            log_scale_factors += [np.log2(1 / (2 ** (j - 1)))]
            log_SR_max_mean += [np.log2(SR_max_mean[i])]
            log_SR_max_std += [np.log2(SR_max_std[i])]

        axis.set_xlabel('$\log_2(\mathrm{range}(\omega)/\mathrm{range}(\omega_0))$')
        axis.set_ylabel('$\log_2(\sigma_{S_{\mathrm{max}}})$')

        if lambda_val < 0.1:
            axis.scatter(log_scale_factors, log_SR_max_std, s=10, c=f"C{lambda_idx}",
                         label=f"${np.log10(lambda_val):g}$")
            axis.plot(log_scale_factors[-3:], log_SR_max_std[-3:], c=f"C{lambda_idx}", ls="--")
            axis.plot(log_scale_factors[:5], log_SR_max_std[:5], c=f"C{lambda_idx}")
        elif lambda_val == 0.1:
            axis.scatter(log_scale_factors[:5], log_SR_max_std[:5], s=10, c=f"C{lambda_idx}",
                         label=f"${np.log10(lambda_val):g}$")
            axis.plot(log_scale_factors[:5], log_SR_max_std[:5], c=f"C{lambda_idx}")
        elif lambda_val == 1:
            axis.scatter(log_scale_factors[:5], log_SR_max_std[:5], s=10, c=f"C{lambda_idx}",
                         label=f"${np.log10(lambda_val):g}$")
            axis.plot(log_scale_factors[:5], log_SR_max_std[:5], c=f"C{lambda_idx}")
        elif lambda_val == 10:
            axis.scatter(log_scale_factors[:3], log_SR_max_std[:3], s=10, c=f"C{lambda_idx}",
                         label=f"${np.log10(lambda_val):g}$")
            axis.plot(log_scale_factors[:3], log_SR_max_std[:3], c=f"C{lambda_idx}")
        elif lambda_val == 100:
            axis.scatter(log_scale_factors[:3], log_SR_max_std[:3], s=10, c=f"C{lambda_idx}",
                         label=f"${np.log10(lambda_val):g}$")
            axis.plot(log_scale_factors[:3], log_SR_max_std[:3], c=f"C{lambda_idx}")


def plot_2d_Smax_mean_lambda(axis):
    
    domain = np.linspace(1, 7, 7, endpoint=True, dtype=int)
    lambda_list = [0.0001, 0.001, 0.01, 0.1, 1, 10, 100]

    for j in domain:

        SR_max_mean = []
        SR_max_std = []

        for lambda_idx, lambda_val in enumerate(lambda_list):

            if j > 3 and lambda_val == 100:
                continue

            if lambda_val < 10:
                center = -7.5
                interval = 5
            elif lambda_val == 10:
                center = -9.75
                interval = 0.5
            elif lambda_val == 100:
                center = -9.975
                interval = 0.05

            omega = []
            SR = []
            file = f"fermions_torus_spec_resp_kysym_yukawa-{lambda_val}_plus_V1_scale_0_n_6_2s_18_ratio_1.000000_qy_0" \
                   f".omega_{center - interval / (2**j):.6g}-{center + interval / (2**j):.6g}_eps_{0.0001 / (2**(j-1)):.6g}.sr.cut"
            with open('/home/bart/PycharmProjects/response_functions/FQHETorusSpectralResponse/stripped_files/' + file, 'r') as csvfile:
                plots = csv.reader(csvfile, delimiter=' ')
                for row in plots:
                    omega.append(float(row[0]))
                    SR.append(float(row[1]))

            omega_max = []
            sr_max = []
            for i, entry in enumerate(omega):
                if SR[i] > SR[i-1] and SR[i] > SR[i + 1]:
                    omega_max += [1]
                    sr_max += [SR[i]]
                else:
                    omega_max += [0]

            SR_max_mean += [np.mean(sr_max)]
            SR_max_std += [np.std(sr_max)]

        log_lambda = [np.log10(i) for i in lambda_list]
        log_SR_max_mean = []
        log_SR_max_std = []

        for i in range(len(SR_max_mean)):
            log_SR_max_mean += [np.log2(SR_max_mean[i])]
            log_SR_max_std += [np.log2(SR_max_std[i])]

        # axis.set_ylabel('$\log_2(\mu_{S_{\mathrm{max}}})$')

        if j >= 6:
            axis.scatter(log_lambda[:3], log_SR_max_mean[:3], s=10, c=f"C{j-1}", label=f"${np.log2(1/2**(j-1)):g}$")
            axis.plot(log_lambda[:3], log_SR_max_mean[:3], c=f"C{j-1}", ls="--")
        elif j >= 4:
            axis.scatter(log_lambda[:5], log_SR_max_mean[:5], s=10, c=f"C{j-1}", label=f"${np.log2(1/2**(j-1)):g}$")
            axis.plot(log_lambda[:5], log_SR_max_mean[:5], c=f"C{j-1}")
        else:
            axis.scatter(log_lambda, log_SR_max_mean, s=10, c=f"C{j-1}", label=f"${np.log2(1/2**(j-1)):g}$")
            axis.plot(log_lambda, log_SR_max_mean, c=f"C{j-1}")

    # axis.set_ylim(bottom=5)

    leg = axis.legend(loc='center', handletextpad=0, borderpad=0.2, framealpha=1,
                      edgecolor=None, markerscale=1, ncol=4, labelspacing=0, columnspacing=0,
                      bbox_to_anchor=(0.5, 1.35), title='$\log_2(\mathrm{range}(\omega)/\mathrm{range}(\omega_0))$')
    leg.get_frame().set_linewidth(0.5)

    plt.setp(axis.get_yticklabels(), visible=False)
    plt.tick_params(
        axis='y',  # changes apply to the x-axis
        which='both',  # both major and minor ticks are affected
        left=False,  # ticks along the bottom edge are off
        right=False,  # ticks along the top edge are off
        labelbottom=False)


def plot_2d_Smax_std_lambda(axis):

    domain = np.linspace(1, 7, 7, endpoint=True, dtype=int)
    lambda_list = [0.0001, 0.001, 0.01, 0.1, 1, 10, 100]

    for j in domain:

        SR_max_mean = []
        SR_max_std = []

        for lambda_idx, lambda_val in enumerate(lambda_list):

            if j > 3 and lambda_val == 100:
                continue

            if lambda_val < 10:
                center = -7.5
                interval = 5
            elif lambda_val == 10:
                center = -9.75
                interval = 0.5
            elif lambda_val == 100:
                center = -9.975
                interval = 0.05

            omega = []
            SR = []
            file = f"fermions_torus_spec_resp_kysym_yukawa-{lambda_val}_plus_V1_scale_0_n_6_2s_18_ratio_1.000000_qy_0" \
                   f".omega_{center - interval / (2 ** j):.6g}-{center + interval / (2 ** j):.6g}_eps_{0.0001 / (2 ** (j - 1)):.6g}.sr.cut"
            with open('/home/bart/PycharmProjects/response_functions/FQHETorusSpectralResponse/stripped_files/' + file,
                      'r') as csvfile:
                plots = csv.reader(csvfile, delimiter=' ')
                for row in plots:
                    omega.append(float(row[0]))
                    SR.append(float(row[1]))

            omega_max = []
            sr_max = []
            for i, entry in enumerate(omega):
                if SR[i] > SR[i - 1] and SR[i] > SR[i + 1]:
                    omega_max += [1]
                    sr_max += [SR[i]]
                else:
                    omega_max += [0]

            SR_max_mean += [np.mean(sr_max)]
            SR_max_std += [np.std(sr_max)]

        log_lambda = [np.log10(i) for i in lambda_list]
        log_SR_max_mean = []
        log_SR_max_std = []

        for i in range(len(SR_max_mean)):
            log_SR_max_mean += [np.log2(SR_max_mean[i])]
            log_SR_max_std += [np.log2(SR_max_std[i])]

        # axis.set_ylabel('$\log_2(\mu_{S_{\mathrm{max}}})$')

        if j >= 6:
            axis.scatter(log_lambda[:3], log_SR_max_std[:3], s=10, c=f"C{j-1}", label=f"${np.log2(1 / 2 ** (j - 1)):g}$")
            axis.plot(log_lambda[:3], log_SR_max_std[:3], c=f"C{j-1}", ls="--")
        elif j >= 4:
            axis.scatter(log_lambda[:5], log_SR_max_std[:5], s=10, c=f"C{j-1}", label=f"${np.log2(1 / 2 ** (j - 1)):g}$")
            axis.plot(log_lambda[:5], log_SR_max_std[:5], c=f"C{j-1}")
        else:
            axis.scatter(log_lambda, log_SR_max_std, s=10, c=f"C{j-1}", label=f"${np.log2(1 / 2 ** (j - 1)):g}$")
            axis.plot(log_lambda, log_SR_max_std, c=f"C{j-1}")

    axis.set_xlabel('$\\log \\lambda$')
    axis.xaxis.set_major_formatter(FormatStrFormatter('$%g$'))
    # axis.set_ylabel('$\\log[\\mathrm{range}(\\Omega)]$')
    axis.yaxis.set_major_formatter(FormatStrFormatter('$%g$'))

    plt.setp(axis.get_yticklabels(), visible=False)
    plt.tick_params(
        axis='y',  # changes apply to the x-axis
        which='both',  # both major and minor ticks are affected
        left=False,  # ticks along the bottom edge are off
        right=False,  # ticks along the top edge are off
        labelbottom=False)


def plot_2d_Smax_mean_lambda_finite_size(axis):

    particles = [6, 7, 8]
    lambda_list = [0.0001, 0.001, 0.01, 0.1, 1, 10, 100]
    log_SR_max_mean = np.zeros(len(particles), dtype=object)
    log_SR_max_std = np.zeros(len(particles), dtype=object)

    for N_val, N in enumerate(particles):

        log_SR_max_mean[N_val] = []
        log_SR_max_std[N_val] = []

        for lambda_idx, lambda_val in enumerate(lambda_list):

            if lambda_val < 10:
                omax = -5
            elif lambda_val == 10:
                omax = -9.5
            elif lambda_val == 100:
                omax = -9.95

            omega = []
            SR = []
            file = f"fermions_torus_spec_resp_kysym_yukawa-{lambda_val}_plus_V1_scale_0_n_{N:g}_2s_{3*N:g}_" \
                   f"ratio_1.000000_qy_0.omega_-10-{omax}_eps_0.0001.sr.cut"
            with open('/home/bart/PycharmProjects/response_functions/FQHETorusSpectralResponse/stripped_files/' + file,
                      'r') as csvfile:
                plots = csv.reader(csvfile, delimiter=' ')
                for row in plots:
                    omega.append(float(row[0]))
                    SR.append(float(row[1]))

            omega_max = []
            sr_max = []
            for i, entry in enumerate(omega[1:-1]):
                if SR[i] > SR[i-1] and SR[i] > SR[i+1]:
                    omega_max += [1]
                    sr_max += [SR[i]]
                else:
                    omega_max += [0]

            log_SR_max_mean[N_val] += [np.log2(np.mean(sr_max))]
            log_SR_max_std[N_val] += [np.log2(np.std(sr_max))]

        axis.scatter([np.log10(i) for i in lambda_list], log_SR_max_mean[N_val], s=10, c=f"C{N_val}", label=f"${N}$")
        axis.plot([np.log10(i) for i in lambda_list], log_SR_max_mean[N_val], c=f"C{N_val}")

    axis.set_ylabel('$\log_2(\mu_{S_\mathrm{max}})$')
    axis.set_xlabel('$\log \lambda$')

    leg = axis.legend(loc='upper left', handletextpad=0, borderpad=0.2, framealpha=1,
                      edgecolor=None, markerscale=1, ncol=8, labelspacing=0, columnspacing=0, title='$N$')
    leg.get_frame().set_linewidth(0.5)


if __name__ == "__main__":

    fig = plt.figure(figsize=(6, 4.5))
    #gs = gridspec.GridSpec(1, 2, hspace=0.4, wspace=0.4)
    outer_grid = gridspec.GridSpec(2, 1, height_ratios=[1, 0.5], hspace=0.4)  # 0.5
    top_grid = outer_grid[0, 0]
    bottom_grid = outer_grid[1, 0]
    top_inner_grid = gridspec.GridSpecFromSubplotSpec(2, 2, top_grid, wspace=0, hspace=0)
    upper_left_cell = top_inner_grid[0, 0]
    upper_right_cell = top_inner_grid[0, 1]
    lower_left_cell = top_inner_grid[1, 0]
    lower_right_cell = top_inner_grid[1, 1]

    ax0 = plt.subplot(upper_left_cell)
    plot_2d_Smax_mean_omega(ax0)
    ax1 = plt.subplot(lower_left_cell, sharex=ax0)
    plot_2d_Smax_std_omega(ax1)
    ax2 = plt.subplot(upper_right_cell, sharey=ax0)
    plot_2d_Smax_mean_lambda(ax2)
    ax3 = plt.subplot(lower_right_cell, sharex=ax2, sharey=ax1)
    plot_2d_Smax_std_lambda(ax3)
    ax4 = plt.subplot(bottom_grid)
    plot_2d_Smax_mean_lambda_finite_size(ax4)

    fig.text(0.11, 0.95, "(a)", fontsize=12)
    fig.text(0.495, 0.95, "(b)", fontsize=12)
    fig.text(0.05, 0.35, "(c)", fontsize=12)

    fig.text(0.15, 0.7, "center", fontsize=11)
    fig.text(0.15, 0.485, "spread", fontsize=11)
    fig.text(0.37, 0.27, "$\\mathrm{range}(\omega)=\\mathrm{range}(\omega_0)$", fontsize=11)

    plt.savefig("/home/bart/Documents/papers/SR/yukawa_scaling_complete.png", bbox_inches='tight', dpi=300)
    plt.show()
