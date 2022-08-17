import csv
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
from matplotlib.ticker import FormatStrFormatter
from scipy import stats

plt.rc('text', usetex=True)
plt.rc('text.latex', preamble=r'\usepackage{amsmath}')

vectors = "/home/bart/PycharmProjects/response_functions/vectors_2/"
stripped_files = "/home/bart/PycharmProjects/response_functions/FQHETorusSpectralResponse_2/stripped_files/"


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


def plot_2d_lty_omega_mean_alpha(axis, numb_qy, omega_min_val, omega_max_val):

    for lamb_exp in [-4, -3, -2, -1, 0, 1, 2]:
        lamb = 10 ** lamb_exp

        omega = []
        SR = []
        name_list = []
        lbl = []
        ground_states = []

        for alpha in np.linspace(10**-4, 1, 41):
            # alpha = 10 ** alpha_exp
            if alpha != 1:
                name = f"yukawa-{lamb:g}_{alpha:.5g}_plus_V1_scale_{1-alpha:.5g}"
            else:
                name = f"yukawa-{lamb:g}_plus_V1_scale_0"
            name_list.append(f"fermions_torus_spec_resp_kysym_{name}_n_{numb_qy/3:g}_2s_{numb_qy:g}_ratio_1.000000_qy_0.omega_{omega_min_val:g}-{omega_max_val:g}_eps_1e-06.sr.cut")

            # get ground state energy (from dat file)
            energies = []
            dir_name = f"n_{numb_qy / 3:g}_linear" if numb_qy == 18 else f"n_{numb_qy / 3:g}_alpha_1"
            dat_file = f"fermions_torus_kysym_{name}_n_{numb_qy / 3:g}_2s_{numb_qy:g}_ratio_1.000000.dat"
            with open(vectors + f'lty/{dir_name}/' + dat_file, 'r') as csvfile:
                data = csv.reader(csvfile, delimiter=' ')
                for row in data:
                    if row[0].isnumeric():
                        energies.append(float(row[1]))
                ground = min(energies)
            ground_states.append(ground)

        for i, file in enumerate(name_list):
            with open(stripped_files + file, 'r') as csvfile:
                data = csv.reader(csvfile, delimiter=' ')
                for row in data:
                    omega.append(float(row[0])+10 - ground_states[i])
                    SR.append(float(row[1]))
                    # lbl += [10 ** (-4 + i * 0.1)]
                    lbl += [10**-4 + i*(1-10**-4)/41]

        omega_max = []
        sr_max = []
        for i, entry in enumerate(omega):
            if SR[i] > SR[i-1] and SR[i] > SR[i+1]:
                omega_max += [1]
                sr_max += [SR[i]]
            else:
                omega_max += [0]

        lbl[:] = [x for i, x in enumerate(lbl) if omega_max[i] == 1]
        omega[:] = [x for i, x in enumerate(omega) if omega_max[i] == 1]

        mean_vals, log_mean_vals = [], []
        lbl_values = sorted(list(set(lbl)))
        for lbl_val in lbl_values:
            omega_set = [i for i, e in enumerate(lbl) if e == lbl_val]
            mean_val = np.average(omega[omega_set[0]:omega_set[-1]+1])
            mean_vals += [mean_val]
            # log_mean_val = np.log10(mean_val)
            # log_mean_vals += [log_mean_val]

        # log_lbl_values = [np.log10(i) for i in lbl_values]

        axis.scatter(lbl_values, mean_vals, s=10, label=f"${np.log10(lamb):g}$")

    axis.set_xlabel('$\\alpha$')
    axis.xaxis.set_major_formatter(FormatStrFormatter('$%g$'))
    axis.set_ylabel('$\\bar{\\Omega}$')
    axis.yaxis.set_major_formatter(FormatStrFormatter('$%g$'))

    leg = axis.legend(loc='center', handletextpad=0, borderpad=0.2, framealpha=1,
                      edgecolor=None, markerscale=1, ncol=4, labelspacing=0, columnspacing=0,
                      bbox_to_anchor=(0.5, 1.35), title='$\log\lambda$')
    leg.get_frame().set_linewidth(0.5)


def plot_2d_lty_omega_range_alpha(axis, numb_qy, omega_min_val, omega_max_val):

    for lamb_exp in [-4, -3, -2, -1, 0, 1, 2]:
        lamb = 10 ** lamb_exp

        omega = []
        SR = []
        name_list = []
        lbl = []
        ground_states = []

        for alpha in np.linspace(10**-4, 1, 41):
            # alpha = 10 ** alpha_exp
            if alpha != 1:
                name = f"yukawa-{lamb:g}_{alpha:.5g}_plus_V1_scale_{1-alpha:.5g}"
            else:
                name = f"yukawa-{lamb}_plus_V1_scale_0"
            name_list.append(f"fermions_torus_spec_resp_kysym_{name}_n_{numb_qy / 3:g}_2s_{numb_qy:g}_ratio_1.000000_qy_0.omega_{omega_min_val:g}-{omega_max_val:g}_eps_1e-06.sr.cut")

            # get ground state energy (from dat file)
            energies = []
            dir_name = f"n_{numb_qy / 3:g}_linear" if numb_qy == 18 else f"n_{numb_qy / 3:g}_alpha_1"
            dat_file = f"fermions_torus_kysym_{name}_n_{numb_qy / 3:g}_2s_{numb_qy:g}_ratio_1.000000.dat"
            with open(vectors + f'lty/{dir_name}/' + dat_file, 'r') as csvfile:
                data = csv.reader(csvfile, delimiter=' ')
                for row in data:
                    if row[0].isnumeric():
                        energies.append(float(row[1]))
                ground = min(energies)
            ground_states.append(ground)

        for i, file in enumerate(name_list):
            with open(stripped_files + file, 'r') as csvfile:
                plots = csv.reader(csvfile, delimiter=' ')
                for row in plots:
                    omega.append(float(row[0])+10 - ground_states[i])
                    SR.append(float(row[1]))
                    # lbl += [10 ** (-4 + i * 0.1)]
                    lbl += [10**-4 + i*(1-10**-4)/41]

        omega_max = []
        sr_max = []
        for i, entry in enumerate(omega):
            if SR[i] > SR[i-1] and SR[i] > SR[i+1]:
                omega_max += [1]
                sr_max += [SR[i]]
            else:
                omega_max += [0]

        lbl[:] = [x for i, x in enumerate(lbl) if omega_max[i] == 1]
        omega[:] = [x for i, x in enumerate(omega) if omega_max[i] == 1]

        omega_range, log_omega_range = [], []
        lbl_values = sorted(list(set(lbl)))
        for lbl_val in lbl_values:
            omega_set = [i for i, e in enumerate(lbl) if e == lbl_val]
            max_val = max(omega[omega_set[0]:omega_set[-1]+1])
            min_val = min(omega[omega_set[0]:omega_set[-1]+1])
            range_val = max_val - min_val
            omega_range += [range_val]
            # log_range_val = np.log10(range_val)
            # log_omega_range += [log_range_val]

        # log_lbl_values = [np.log10(i) for i in lbl_values]

        axis.scatter(lbl_values, omega_range, s=10, label=f"${np.log10(lamb):g}$")

    axis.set_xlabel('$\\alpha$')
    axis.xaxis.set_major_formatter(FormatStrFormatter('$%g$'))
    axis.set_ylabel('$\\mathrm{range}(\\Omega)$')
    axis.yaxis.set_major_formatter(FormatStrFormatter('$%g$'))


def plot_2d_lty_omega_mean_lambda(axis, numb_qy, omega_min_val, omega_max_val):

    for alpha in np.linspace(10**-4, 1, 11):  # [-4, -3, -2, -1, 0]
        # alpha = 10 ** alpha_exp

        omega = []
        SR = []
        name_list = []
        lbl = []
        ground_states = []

        for lamb_exp in np.linspace(-4, 2, 7):
            lamb = 10 ** lamb_exp
            if alpha != 1:
                name = f"yukawa-{lamb:g}_{alpha:.5g}_plus_V1_scale_{1-alpha:.5g}"
            else:
                name = f"yukawa-{lamb:g}_plus_V1_scale_0"
            name_list.append(f"fermions_torus_spec_resp_kysym_{name}_n_{numb_qy / 3:g}_2s_{numb_qy:g}_ratio_1.000000_qy_0.omega_{omega_min_val:g}-{omega_max_val:g}_eps_1e-06.sr.cut")

            # get ground state energy (from dat file)
            energies = []
            dir_name = f"n_{numb_qy / 3:g}_linear" if numb_qy == 18 else f"n_{numb_qy / 3:g}_alpha_1"
            dat_file = f"fermions_torus_kysym_{name}_n_{numb_qy / 3:g}_2s_{numb_qy:g}_ratio_1.000000.dat"
            with open(vectors + f'lty/{dir_name}/' + dat_file, 'r') as csvfile:
                data = csv.reader(csvfile, delimiter=' ')
                for row in data:
                    if row[0].isnumeric():
                        energies.append(float(row[1]))
                ground = min(energies)
            ground_states.append(ground)

        for i, file in enumerate(name_list):
            with open(stripped_files + file, 'r') as csvfile:
                data = csv.reader(csvfile, delimiter=' ')
                for row in data:
                    omega.append(float(row[0])+10-ground_states[i])
                    SR.append(float(row[1]))
                    lbl += [10 ** (-4 + i)]

        omega_max = []
        sr_max = []
        for i, entry in enumerate(omega):
            if SR[i] > SR[i-1] and SR[i] > SR[i+1]:
                omega_max += [1]
                sr_max += [SR[i]]
            else:
                omega_max += [0]

        lbl[:] = [x for i, x in enumerate(lbl) if omega_max[i] == 1]
        omega[:] = [x for i, x in enumerate(omega) if omega_max[i] == 1]

        log_mean_vals = []
        lbl_values = sorted(list(set(lbl)))
        for lbl_val in lbl_values:
            omega_set = [i for i, e in enumerate(lbl) if e == lbl_val]
            mean_val = np.average(omega[omega_set[0]:omega_set[-1]+1])
            # log_mean_val = np.log10(mean_val)
            log_mean_val = mean_val
            log_mean_vals += [log_mean_val]

        log_lbl_values = [np.log10(i) for i in lbl_values]
        # log_lbl_values = lbl_values

        axis.scatter(log_lbl_values, log_mean_vals, s=10, label=f"${alpha:.1g}$")
        axis.plot(log_lbl_values, log_mean_vals)

    # axis.set_xlabel('$\\log \\lambda$')
    axis.xaxis.set_major_formatter(FormatStrFormatter('$%g$'))
    # axis.set_ylabel('$\\log\\bar{\\Omega}$')
    axis.yaxis.set_major_formatter(FormatStrFormatter('$%g$'))

    leg = axis.legend(loc='center', handletextpad=0, borderpad=0.2, framealpha=1,
                      edgecolor=None, markerscale=1, ncol=4, labelspacing=0, columnspacing=0,
                      bbox_to_anchor=(0.5, 1.42), title='$\\alpha$')
    leg.get_frame().set_linewidth(0.5)

    plt.setp(axis.get_yticklabels(), visible=False)
    plt.tick_params(
        axis='y',  # changes apply to the x-axis
        which='both',  # both major and minor ticks are affected
        left=False,  # ticks along the bottom edge are off
        right=False,  # ticks along the top edge are off
        labelbottom=False)


def plot_2d_lty_omega_range_lambda(axis, numb_qy, omega_min_val, omega_max_val):

    for alpha in np.linspace(10**-4, 1, 11):  # [-4, -3, -2, -1, 0]
        # alpha = 10 ** alpha_exp

        omega = []
        SR = []
        name_list = []
        lbl = []
        ground_states = []

        for lamb_exp in np.linspace(-4, 2, 7):
            lamb = 10 ** lamb_exp
            if alpha != 1:
                name = f"yukawa-{lamb:g}_{alpha:g}_plus_V1_scale_{1-alpha:g}"
            else:
                name = f"yukawa-{lamb:g}_plus_V1_scale_0"
            name_list.append(f"fermions_torus_spec_resp_kysym_{name}_n_{numb_qy/3:g}_2s_{numb_qy:g}_ratio_1.000000_qy_0.omega_{omega_min_val:g}-{omega_max_val:g}_eps_1e-06.sr.cut")

            # get ground state energy (from dat file)
            energies = []
            dir_name = f"n_{numb_qy/3:g}_linear" if numb_qy == 18 else f"n_{numb_qy/3:g}_alpha_1"
            dat_file = f"fermions_torus_kysym_{name}_n_{numb_qy/3:g}_2s_{numb_qy:g}_ratio_1.000000.dat"
            with open(vectors + f'lty/{dir_name}/' + dat_file, 'r') as csvfile:
                data = csv.reader(csvfile, delimiter=' ')
                for row in data:
                    if row[0].isnumeric():
                        energies.append(float(row[1]))
                ground = min(energies)
            ground_states.append(ground)

        for i, file in enumerate(name_list):
            with open(stripped_files + file, 'r') as csvfile:
                plots = csv.reader(csvfile, delimiter=' ')
                for row in plots:
                    omega.append(float(row[0])+10-ground_states[i])
                    SR.append(float(row[1]))
                    lbl += [10 ** (-4 + i)]

        omega_max = []
        sr_max = []
        for i, entry in enumerate(omega):
            if SR[i] > SR[i-1] and SR[i] > SR[i+1]:
                omega_max += [1]
                sr_max += [SR[i]]
            else:
                omega_max += [0]

        lbl[:] = [x for i, x in enumerate(lbl) if omega_max[i] == 1]
        omega[:] = [x for i, x in enumerate(omega) if omega_max[i] == 1]

        log_omega_range = []
        lbl_values = sorted(list(set(lbl)))
        for lbl_val in lbl_values:
            omega_set = [i for i, e in enumerate(lbl) if e == lbl_val]
            max_val = max(omega[omega_set[0]:omega_set[-1]+1])
            min_val = min(omega[omega_set[0]:omega_set[-1]+1])
            range_val = max_val - min_val
            # log_range_val = np.log10(range_val)
            log_range_val = range_val
            log_omega_range += [log_range_val]

        log_lbl_values = [np.log10(i) for i in lbl_values]
        # log_lbl_values = lbl_values

        axis.scatter(log_lbl_values, log_omega_range, s=10, label=f"${alpha:.1g}$")
        axis.plot(log_lbl_values, log_omega_range)

    axis.set_xlabel('$\\log\\lambda$')
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


def plot_2d_lty_omega_mean_lambda_finite(axis, omega_min_val, omega_max_val):

    for numb_idx, n_val in enumerate([6, 7, 8, 9]):

        omega = []
        SR = []
        name_list = []
        lbl = []
        ground_states = []

        for lamb_exp in np.linspace(-4, 2, 7):
            lamb = 10 ** lamb_exp
            name_list.append(f"fermions_torus_spec_resp_kysym_yukawa-{lamb:.5g}_plus_V1_scale_0_n_{n_val:g}_2s_{n_val*3:g}_ratio_1.000000_qy_0.omega_{omega_min_val:g}-{omega_max_val:g}_eps_1e-06.sr.cut")

            # get ground state energy (from dat file)
            energies = []
            dir_name = f"n_{n_val:g}" if n_val == 6 else f"n_{n_val:g}_alpha_1"
            dat_file = f"fermions_torus_kysym_yukawa-{lamb:.5g}_plus_V1_scale_0_n_{n_val:g}_2s_{3*n_val:g}_ratio_1.000000.dat"
            with open(vectors + f'lty/{dir_name}/' + dat_file, 'r') as csvfile:
                data = csv.reader(csvfile, delimiter=' ')
                for row in data:
                    if row[0].isnumeric():
                        energies.append(float(row[1]))
                ground = min(energies)
            ground_states.append(ground)

        for i, file in enumerate(name_list):
            with open(stripped_files + file, 'r') as csvfile:
                plots = csv.reader(csvfile, delimiter=' ')
                for row in plots:
                    omega.append(float(row[0])+10-ground_states[i])
                    SR.append(float(row[1]))
                    lbl += [10 ** (-4+i)]

        omega_max = []
        sr_max = []
        for i, entry in enumerate(omega):
            if SR[i] > SR[i-1] and SR[i] > SR[i+1]:
                omega_max += [1]
                sr_max += [SR[i]]
            else:
                omega_max += [0]

        lbl[:] = [x for i, x in enumerate(lbl) if omega_max[i] == 1]
        omega[:] = [x for i, x in enumerate(omega) if omega_max[i] == 1]

        log_mean_vals = []
        lbl_values = sorted(list(set(lbl)))
        for lbl_val in lbl_values:
            omega_set = [i for i, e in enumerate(lbl) if e == lbl_val]
            mean_val = np.average(omega[omega_set[0]:omega_set[-1]+1])
            log_mean_val = np.log10(mean_val)
            # log_mean_val = mean_val
            log_mean_vals += [log_mean_val]

        log_lbl_values = [np.log10(i) for i in lbl_values]
        # log_lbl_values = lbl_values

        axis.scatter(log_lbl_values, log_mean_vals, s=10, label=f"${n_val:g}$", c=f"C{numb_idx}")
        axis.plot(log_lbl_values, log_mean_vals, c=f"C{numb_idx}")

        # plot the transition point
        x1 = log_lbl_values[0]
        y1 = log_mean_vals[0]
        x2 = log_lbl_values[1]
        y2 = log_mean_vals[1]
        m = (y2-y1)/(x2-x1)
        c = y1-m*x1
        v1 = log_lbl_values[-2]
        w1 = log_mean_vals[-2]
        v2 = log_lbl_values[-1]
        w2 = log_mean_vals[-1]
        alpha = (w2-w1)/(v2-v1)
        beta = w1-alpha*v1
        xint = (beta-c)/(m-alpha)
        yint = m*xint + c
        axis.scatter(xint, yint, marker='x', s=10, c=f"C{numb_idx}")
        if n_val == 9:
            xvalues1 = np.linspace(-4, xint)
            xvalues2 = np.linspace(xint, 2)
            axis.plot(xvalues1, m * xvalues1 + c, '--', c='k', zorder=0, lw=0.5)
            print(m)
            axis.plot(xvalues2, alpha * xvalues2 + beta, '--', c='k', zorder=0, lw=0.5)
            print(alpha)

    axis.set_xlabel('$\\log\\lambda$')
    axis.xaxis.set_major_formatter(FormatStrFormatter('$%g$'))
    axis.set_ylabel('$\\log\\bar{\\Omega}$')
    axis.yaxis.set_major_formatter(FormatStrFormatter('$%g$'))

    leg = axis.legend(loc='lower left', handletextpad=0, borderpad=0.2, framealpha=1,
                      edgecolor=None, markerscale=1, ncol=8, labelspacing=0, columnspacing=0, title='$N$')
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
    plot_2d_lty_omega_mean_alpha(ax0, 18, omega_min_val=-20, omega_max_val=0)
    ax1 = plt.subplot(lower_left_cell, sharex=ax0)
    plot_2d_lty_omega_range_alpha(ax1, 18, omega_min_val=-20, omega_max_val=0)
    ax2 = plt.subplot(upper_right_cell, sharey=ax0)
    plot_2d_lty_omega_mean_lambda(ax2, 18, omega_min_val=-20, omega_max_val=0)
    ax3 = plt.subplot(lower_right_cell, sharex=ax2, sharey=ax1)
    plot_2d_lty_omega_range_lambda(ax3, 18, omega_min_val=-20, omega_max_val=0)
    ax4 = plt.subplot(bottom_grid)
    plot_2d_lty_omega_mean_lambda_finite(ax4, omega_min_val=-20, omega_max_val=0)

    fig.text(0.11, 0.95, "(a)", fontsize=12)
    fig.text(0.495, 0.95, "(b)", fontsize=12)
    fig.text(0.05, 0.35, "(c)", fontsize=12)

    fig.text(0.15, 0.7, "center", fontsize=11)
    fig.text(0.15, 0.48, "spread", fontsize=11)
    fig.text(0.81, 0.27, "$\\alpha=1$", fontsize=11)

    plt.savefig("lty_newer.png", bbox_inches='tight', dpi=300)
    plt.show()
