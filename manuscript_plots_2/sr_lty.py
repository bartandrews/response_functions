import csv
import itertools
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
from matplotlib.ticker import FormatStrFormatter
from scipy import stats

plt.rc('text', usetex=True)
plt.rc('text.latex', preamble=r'\usepackage{amsmath}')

vectors = "/home/bart/PycharmProjects/response_functions/vectors_2/"
stripped_files = "/home/bart/PycharmProjects/response_functions/FQHETorusSpectralResponse_2/stripped_files/"


def plot_2d_q(axis, name, numb_qy, omega_min, omega_max):

    marker = itertools.cycle(('1', '2', '3', '4', ',', '+', '.', 'o', '*', '^', 'v', '>', '<', 'X', '_', 'd', '|', 'H'))

    # get laughlin gap and ground state energy (from dat file)
    energies = []
    dat_file = f"fermions_torus_kysym_V1_n_{numb_qy/3:g}_2s_{numb_qy:g}_ratio_1.000000.dat"
    with open(vectors + f'laughlin/n_{numb_qy/3:g}/' + dat_file, 'r') as csvfile:
        data = csv.reader(csvfile, delimiter=' ')
        for row in data:
            if row[0].isnumeric():
                energies.append(float(row[1]))
        laughlin_gap = sorted(energies)[3] - sorted(energies)[0]
        laughlin_ground = min(energies)

    # get coulomb gap and ground state energy (from dat file)
    energies = []
    dat_file = f"fermions_torus_kysym_coulomb_n_{numb_qy / 3:g}_2s_{numb_qy:g}_ratio_1.000000.dat"
    with open(vectors + f'coulomb/n_{numb_qy / 3:g}/' + dat_file, 'r') as csvfile:
        data = csv.reader(csvfile, delimiter=' ')
        for row in data:
            if row[0].isnumeric():
                energies.append(float(row[1]))
        coulomb_gap = sorted(energies)[3] - sorted(energies)[0]
        coulomb_ground = min(energies)

    if name == "V1":
        scale = laughlin_gap / coulomb_gap
        offset = laughlin_ground
    elif name == "coulomb":
        scale = 1
        offset = coulomb_ground
    else:
        scale = 1
        offset = 0

    print(scale, offset)

    for qy_value in range(numb_qy):
        omega = []
        SR = []
        file = f"fermions_torus_spec_resp_kysym_{name}_n_{numb_qy/3:g}_2s_{numb_qy:g}_ratio_1.000000_qy_{qy_value:g}" \
               f".omega_{omega_min:g}-{omega_max:g}_eps_0.0001.sr.cut"
        with open(stripped_files + file, 'r') as csvfile:
            plots = csv.reader(csvfile, delimiter=' ')
            for row in plots:
                omega.append((float(row[0])+10)/scale - offset)
                SR.append(float(row[1])/100)
        axis.scatter(omega, SR, s=1, label=qy_value, marker=next(marker))

        if name == 'coulomb' and qy_value == 0:

            orig_min = min(omega)
            orig_max = max(omega)
            # original_min = min(omega)-10-1.3711444004959
            # original_max = max(omega)-10-1.3711444004959
            # print("original min = ", original_min)
            print("lower quartile = ", np.percentile(omega, 25))
            print("median = ", np.median(omega))
            print("upper quartile = ", np.percentile(omega, 75))
            # print("original max = ", original_max)
            # print(f"mean = {(original_max+original_min)/2:.6g}+-{(original_max-original_min)/2:.6g}")
            print(f"mean = {(orig_max + orig_min) / 2:.6g}+-{(orig_max - orig_min) / 2:.6g}")

    axis.set_xlabel('$\omega-\omega_0$')
    axis.xaxis.set_major_formatter(FormatStrFormatter('$%g$'))
    axis.yaxis.set_major_formatter(FormatStrFormatter('$%g$'))
    axis.set_ylabel('$I/10^2$')
    axis.set_ylim(bottom=0)

    if name == "V1":
        leg = axis.legend(loc='upper right', handletextpad=0, borderpad=0.2, framealpha=1,
                          edgecolor=None, markerscale=5, ncol=10, labelspacing=0, columnspacing=0,
                          bbox_to_anchor=(2.2, 1.6), title='$q_y$')
        leg.get_frame().set_linewidth(0.5)


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
                      bbox_to_anchor=(0.5, 1.4), title='$\log\lambda$')
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
                      bbox_to_anchor=(0.5, 1.47), title='$\\alpha$')
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

    fig = plt.figure(figsize=(6, 7.5))
    super_grid = gridspec.GridSpec(2, 1, height_ratios=[1, 3], hspace=0.55)  # 0.5
    top_super_grid = gridspec.GridSpecFromSubplotSpec(1, 2, super_grid[0, 0], wspace=0.4)
    left_cell = top_super_grid[0, 0]
    right_cell = top_super_grid[0, 1]
    bottom_super_grid = gridspec.GridSpecFromSubplotSpec(2, 1, super_grid[1, 0], height_ratios=[2, 1], hspace=0.4)
    top_grid = bottom_super_grid[0, 0]
    bottom_grid = bottom_super_grid[1, 0]
    middle_inner_grid = gridspec.GridSpecFromSubplotSpec(2, 2, top_grid, wspace=0, hspace=0)
    upper_left_cell = middle_inner_grid[0, 0]
    upper_right_cell = middle_inner_grid[0, 1]
    lower_left_cell = middle_inner_grid[1, 0]
    lower_right_cell = middle_inner_grid[1, 1]

    ax0 = plt.subplot(left_cell)
    plot_2d_q(ax0, "V1", 18, omega_min=-100, omega_max=100)
    ax1 = plt.subplot(right_cell)
    plot_2d_q(ax1, "coulomb", 18, omega_min=-100, omega_max=100)

    ax2 = plt.subplot(upper_left_cell)
    plot_2d_lty_omega_mean_alpha(ax2, 18, omega_min_val=-20, omega_max_val=0)
    ax3 = plt.subplot(lower_left_cell, sharex=ax2)
    plot_2d_lty_omega_range_alpha(ax3, 18, omega_min_val=-20, omega_max_val=0)
    ax4 = plt.subplot(upper_right_cell, sharey=ax2)
    plot_2d_lty_omega_mean_lambda(ax4, 18, omega_min_val=-20, omega_max_val=0)
    ax5 = plt.subplot(lower_right_cell, sharex=ax4, sharey=ax3)
    plot_2d_lty_omega_range_lambda(ax5, 18, omega_min_val=-20, omega_max_val=0)
    ax6 = plt.subplot(bottom_grid)
    plot_2d_lty_omega_mean_lambda_finite(ax6, omega_min_val=-20, omega_max_val=0)

    fig.text(0.05, 0.87, "(a)", fontsize=12)
    fig.text(0.495, 0.87, "(b)", fontsize=12)
    fig.text(0.11, 0.605, "(c)", fontsize=12)
    fig.text(0.495, 0.605, "(d)", fontsize=12)
    fig.text(0.05, 0.23, "(e)", fontsize=12)

    ax0.text(0.05, 0.8, "$V_1$", fontsize=11, transform=ax0.transAxes)
    ax1.text(0.05, 0.8, "Coulomb", fontsize=11, transform=ax1.transAxes)
    ax2.text(0.1, 0.2, "center", fontsize=11, transform=ax2.transAxes)
    ax3.text(0.1, 0.2, "spread", fontsize=11, transform=ax3.transAxes)
    ax6.text(0.875, 0.73, "$\\alpha=1$", fontsize=11, transform=ax6.transAxes)

    plt.savefig("sr_lty.png", bbox_inches='tight', dpi=300)
    plt.show()
