import csv
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
from matplotlib.ticker import FormatStrFormatter

plt.rc('text', usetex=True)
plt.rc('text.latex', preamble=r'\usepackage{amsmath}')

vectors = "/home/bart/PycharmProjects/response_functions/vectors_2/"
stripped_files = "/home/bart/PycharmProjects/response_functions/FQHETorusSpectralResponse_2/stripped_files/"

# INPUT
mid = -10.6995  # midpoint (-10.6, -10.6995)
std = 0.6095  # deviation (0.5, 0.6095)


def plot_2d_Smax_mean_omega(axis, numb_qy):

    for lamb_idx, lamb_exp in enumerate([-4, -3, -2, -1, 0, 1, 2]):
        lamb = 10 ** lamb_exp

        domain = [0, 1, 2, 3, 4, 5, 6]

        SR_max_mean = []
        SR_max_std = []

        for j in domain:

            omega = []
            SR = []
            file = f"fermions_torus_spec_resp_kysym_yukawa-{lamb:g}_n_{numb_qy/3:g}_2s_{numb_qy:g}_ratio_1.000000_qy_0" \
                   f".omega_{mid - std/(2**j):.6g}-{mid + std/(2**j):.6g}_eps_{0.0001/(2**j):.6g}.sr.cut"

            with open(stripped_files + file, 'r') as csvfile:
                data = csv.reader(csvfile, delimiter=' ')
                for row in data:
                    omega.append(float(row[0]))
                    SR.append(float(row[1]))

            omega_max = []
            sr_max = []
            for i, entry in enumerate(omega):
                if i == 0:  # first point
                    if SR[i] > SR[i+1]:
                        omega_max += [1]
                        sr_max += [SR[i]]
                    else:
                        omega_max += [0]
                elif i == len(omega) - 1:  # last point
                    if SR[i] > SR[i-1]:
                        omega_max += [1]
                        sr_max += [SR[i]]
                    else:
                        omega_max += [0]
                else:  # other points
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
            log_scale_factors += [np.log2(1 / (2**j))]
            log_SR_max_mean += [np.log2(SR_max_mean[i])]
            log_SR_max_std += [np.log2(SR_max_std[i])]

        axis.set_ylabel('$\log_2(\mu_{I_{\mathrm{max}}})$')

        axis.scatter(log_scale_factors, log_SR_max_mean, s=10, c=f"C{lamb_idx:g}", label=f"${np.log10(lamb):g}$")
        # axis.plot(log_scale_factors[-3:], log_SR_max_mean[-3:], c=f"C{lamb_idx:g}", ls="--")
        # axis.plot(log_scale_factors[:5], log_SR_max_mean[:5], c=f"C{lamb_idx:g}")
        axis.plot(log_scale_factors, log_SR_max_mean, c=f"C{lamb_idx:g}")

    leg = axis.legend(loc='center', handletextpad=0, borderpad=0.2, framealpha=1,
                      edgecolor=None, markerscale=1, ncol=4, labelspacing=0, columnspacing=0,
                      bbox_to_anchor=(0.5, 1.35), title='$\log\lambda$')
    leg.get_frame().set_linewidth(0.5)


def plot_2d_Smax_std_omega(axis, numb_qy):

    for lamb_idx, lamb_exp in enumerate([-4, -3, -2, -1, 0, 1, 2]):
        lamb = 10 ** lamb_exp

        domain = [0, 1, 2, 3, 4, 5, 6]

        SR_max_mean = []
        SR_max_std = []

        for j in domain:

            omega = []
            SR = []
            file = f"fermions_torus_spec_resp_kysym_yukawa-{lamb:g}_n_{numb_qy/3:g}_2s_{numb_qy:g}_ratio_1.000000_qy_0" \
                   f".omega_{mid - std / (2 ** j):.6g}-{mid + std / (2 ** j):.6g}_eps_{0.0001 / (2 ** j):.6g}.sr.cut"

            with open(stripped_files + file, 'r') as csvfile:
                plots = csv.reader(csvfile, delimiter=' ')
                for row in plots:
                    omega.append(float(row[0]))
                    SR.append(float(row[1]))

            omega_max = []
            sr_max = []
            for i, entry in enumerate(omega):
                if i == 0:  # first point
                    if SR[i] > SR[i + 1]:
                        omega_max += [1]
                        sr_max += [SR[i]]
                    else:
                        omega_max += [0]
                elif i == len(omega) - 1:  # last point
                    if SR[i] > SR[i - 1]:
                        omega_max += [1]
                        sr_max += [SR[i]]
                    else:
                        omega_max += [0]
                else:  # other points
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
            log_scale_factors += [np.log2(1 / (2 ** j))]
            log_SR_max_mean += [np.log2(SR_max_mean[i])]
            log_SR_max_std += [np.log2(SR_max_std[i])]

        axis.set_xlabel('$\log_2(\mathrm{range}(\omega)/\mathrm{range}(\omega_\mathrm{init}))$')
        axis.set_ylabel('$\log_2(\sigma_{I_{\mathrm{max}}})$')

        axis.scatter(log_scale_factors, log_SR_max_std, s=10, c=f"C{lamb_idx:g}", label=f"${np.log10(lamb):g}$")
        # axis.plot(log_scale_factors[-3:], log_SR_max_std[-3:], c=f"C{lamb_idx:g}", ls="--")
        # axis.plot(log_scale_factors[:5], log_SR_max_std[:5], c=f"C{lamb_idx:g}")
        axis.plot(log_scale_factors, log_SR_max_std, c=f"C{lamb_idx:g}")


def plot_2d_Smax_mean_lambda(axis, numb_qy):
    
    domain = [0, 1, 2, 3, 4, 5, 6]
    lamb_list = [0.0001, 0.001, 0.01, 0.1, 1, 10, 100]

    for j in domain:

        SR_max_mean = []
        SR_max_std = []

        for lamb_idx, lamb in enumerate(lamb_list):

            omega = []
            SR = []
            file = f"fermions_torus_spec_resp_kysym_yukawa-{lamb:g}_n_{numb_qy/3:g}_2s_{numb_qy:g}_ratio_1.000000_qy_0" \
                   f".omega_{mid - std / (2**j):.6g}-{mid + std / (2**j):.6g}_eps_{0.0001 / (2**j):.6g}.sr.cut"
            with open(stripped_files + file, 'r') as csvfile:
                data = csv.reader(csvfile, delimiter=' ')
                for row in data:
                    omega.append(float(row[0]))
                    SR.append(float(row[1]))

            omega_max = []
            sr_max = []
            for i, entry in enumerate(omega):
                if i == 0:  # first point
                    if SR[i] > SR[i + 1]:
                        omega_max += [1]
                        sr_max += [SR[i]]
                    else:
                        omega_max += [0]
                elif i == len(omega) - 1:  # last point
                    if SR[i] > SR[i - 1]:
                        omega_max += [1]
                        sr_max += [SR[i]]
                    else:
                        omega_max += [0]
                else:  # other points
                    if SR[i] > SR[i - 1] and SR[i] > SR[i + 1]:
                        omega_max += [1]
                        sr_max += [SR[i]]
                    else:
                        omega_max += [0]

            SR_max_mean += [np.mean(sr_max)]
            SR_max_std += [np.std(sr_max)]

        log_lambda = [np.log10(i) for i in lamb_list]
        log_SR_max_mean = []
        log_SR_max_std = []

        for i in range(len(SR_max_mean)):
            log_SR_max_mean += [np.log2(SR_max_mean[i])]
            log_SR_max_std += [np.log2(SR_max_std[i])]

        axis.scatter(log_lambda, log_SR_max_mean, s=10, c=f"C{j:g}", label=f"${np.log2(1/2**j):g}$")
        axis.plot(log_lambda, log_SR_max_mean, c=f"C{j:g}")

    leg = axis.legend(loc='center', handletextpad=0, borderpad=0.2, framealpha=1,
                      edgecolor=None, markerscale=1, ncol=4, labelspacing=0, columnspacing=0,
                      bbox_to_anchor=(0.5, 1.35), title='$\log_2(\mathrm{range}(\omega)/\mathrm{range}(\omega_\mathrm{init}))$')
    leg.get_frame().set_linewidth(0.5)

    plt.setp(axis.get_yticklabels(), visible=False)
    plt.tick_params(
        axis='y',  # changes apply to the x-axis
        which='both',  # both major and minor ticks are affected
        left=False,  # ticks along the bottom edge are off
        right=False,  # ticks along the top edge are off
        labelbottom=False)


def plot_2d_Smax_std_lambda(axis, numb_qy):

    domain = [0, 1, 2, 3, 4, 5, 6]
    lamb_list = [0.0001, 0.001, 0.01, 0.1, 1, 10, 100]

    for j in domain:

        SR_max_mean = []
        SR_max_std = []

        for lamb_idx, lamb in enumerate(lamb_list):

            omega = []
            SR = []
            file = f"fermions_torus_spec_resp_kysym_yukawa-{lamb}_n_{numb_qy/3:g}_2s_{numb_qy:g}_ratio_1.000000_qy_0" \
                   f".omega_{mid - std / (2 ** j):.6g}-{mid + std / (2 ** j):.6g}_eps_{0.0001 / (2 ** j):.6g}.sr.cut"
            with open(stripped_files + file, 'r') as csvfile:
                data = csv.reader(csvfile, delimiter=' ')
                for row in data:
                    omega.append(float(row[0]))
                    SR.append(float(row[1]))

            omega_max = []
            sr_max = []
            for i, entry in enumerate(omega):
                if i == 0:  # first point
                    if SR[i] > SR[i + 1]:
                        omega_max += [1]
                        sr_max += [SR[i]]
                    else:
                        omega_max += [0]
                elif i == len(omega) - 1:  # last point
                    if SR[i] > SR[i - 1]:
                        omega_max += [1]
                        sr_max += [SR[i]]
                    else:
                        omega_max += [0]
                else:  # other points
                    if SR[i] > SR[i - 1] and SR[i] > SR[i + 1]:
                        omega_max += [1]
                        sr_max += [SR[i]]
                    else:
                        omega_max += [0]

            SR_max_mean += [np.mean(sr_max)]
            SR_max_std += [np.std(sr_max)]

        log_lambda = [np.log10(i) for i in lamb_list]
        log_SR_max_mean = []
        log_SR_max_std = []

        for i in range(len(SR_max_mean)):
            log_SR_max_mean += [np.log2(SR_max_mean[i])]
            log_SR_max_std += [np.log2(SR_max_std[i])]

        axis.scatter(log_lambda, log_SR_max_std, s=10, c=f"C{j:g}", label=f"${np.log2(1 / 2 ** j):g}$")
        axis.plot(log_lambda, log_SR_max_std, c=f"C{j:g}")

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

    particles = [6, 7, 8, 9]
    lamb_list = [0.0001, 0.001, 0.01, 0.1, 1, 10, 100]
    log_SR_max_mean = np.zeros(len(particles), dtype=object)
    log_SR_max_std = np.zeros(len(particles), dtype=object)

    for n_idx, n_val in enumerate(particles):

        log_SR_max_mean[n_idx] = []
        log_SR_max_std[n_idx] = []

        for lamb_idx, lamb in enumerate(lamb_list):

            omega = []
            SR = []
            file = f"fermions_torus_spec_resp_kysym_yukawa-{lamb:g}_n_{n_val:g}_2s_{3*n_val:g}_" \
                   f"ratio_1.000000_qy_0.omega_{mid - std:.6g}-{mid + std:.6g}_eps_0.0001.sr.cut"
            with open(stripped_files + file, 'r') as csvfile:
                data = csv.reader(csvfile, delimiter=' ')
                for row in data:
                    omega.append(float(row[0]))
                    SR.append(float(row[1]))

            omega_max = []
            sr_max = []
            for i, entry in enumerate(omega[1:-1]):
                if i == 0:  # first point
                    if SR[i] > SR[i + 1]:
                        omega_max += [1]
                        sr_max += [SR[i]]
                    else:
                        omega_max += [0]
                elif i == len(omega) - 1:  # last point
                    if SR[i] > SR[i - 1]:
                        omega_max += [1]
                        sr_max += [SR[i]]
                    else:
                        omega_max += [0]
                else:  # other points
                    if SR[i] > SR[i - 1] and SR[i] > SR[i + 1]:
                        omega_max += [1]
                        sr_max += [SR[i]]
                    else:
                        omega_max += [0]

            log_SR_max_mean[n_idx] += [np.log2(np.mean(sr_max))]
            log_SR_max_std[n_idx] += [np.log2(np.std(sr_max))]

        axis.scatter([np.log10(i) for i in lamb_list], log_SR_max_mean[n_idx], s=10, c=f"C{n_idx}", label=f"${n_val}$")
        axis.plot([np.log10(i) for i in lamb_list], log_SR_max_mean[n_idx], c=f"C{n_idx}")

    axis.set_ylabel('$\log_2(\mu_{I_\mathrm{max}})$')
    axis.set_xlabel('$\log \lambda$')

    leg = axis.legend(loc='center left', handletextpad=0, borderpad=0.2, framealpha=1,
                      edgecolor=None, markerscale=1, ncol=8, labelspacing=0, columnspacing=0, title='$N$',
                      bbox_to_anchor=(0, 0.36))
    leg.get_frame().set_linewidth(0.5)


if __name__ == "__main__":

    fig = plt.figure(figsize=(6, 4.5))
    outer_grid = gridspec.GridSpec(2, 1, height_ratios=[1, 0.5], hspace=0.4)  # 0.5
    top_grid = outer_grid[0, 0]
    bottom_grid = outer_grid[1, 0]
    top_inner_grid = gridspec.GridSpecFromSubplotSpec(2, 2, top_grid, wspace=0, hspace=0)
    upper_left_cell = top_inner_grid[0, 0]
    upper_right_cell = top_inner_grid[0, 1]
    lower_left_cell = top_inner_grid[1, 0]
    lower_right_cell = top_inner_grid[1, 1]

    ax0 = plt.subplot(upper_left_cell)
    plot_2d_Smax_mean_omega(ax0, 18)
    ax1 = plt.subplot(lower_left_cell, sharex=ax0)
    plot_2d_Smax_std_omega(ax1, 18)
    ax2 = plt.subplot(upper_right_cell, sharey=ax0)
    plot_2d_Smax_mean_lambda(ax2, 18)
    ax3 = plt.subplot(lower_right_cell, sharex=ax2, sharey=ax1)
    plot_2d_Smax_std_lambda(ax3, 18)
    ax4 = plt.subplot(bottom_grid)
    plot_2d_Smax_mean_lambda_finite_size(ax4)

    fig.text(0.11, 0.95, "(a)", fontsize=12)
    fig.text(0.495, 0.95, "(b)", fontsize=12)
    fig.text(0.05, 0.35, "(c)", fontsize=12)

    fig.text(0.15, 0.7, "center", fontsize=11)
    fig.text(0.15, 0.485, "spread", fontsize=11)
    fig.text(0.515, 0.17, "$\\mathrm{range}(\omega)=\\mathrm{range}(\omega_\mathrm{init})$", fontsize=11)

    plt.savefig("yukawa_scaling_complete.png", bbox_inches='tight', dpi=300)
    plt.show()
