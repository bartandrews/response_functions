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

plt.rc('text', usetex=True)
plt.rc('text.latex', preamble=r'\usepackage{amsmath}')


def line_of_best_fit(axis, x_list, y_list, xval=0.05, yval=0.70):

    parameters, cov = np.polyfit(x_list, y_list, 1, cov=True)
    _, _, r_value, _, _ = stats.linregress(x_list, y_list)
    m, m_err, c, c_err = parameters[0], np.sqrt(cov[0][0]), parameters[1], np.sqrt(cov[1][1])
    r2_value = r_value*r_value

    print("SvN = m*(Ly/lB) + c")
    print(f"(m, m_err, c, c_err) = ({m:.5f}, {m_err:.5f}, {c:.5f}, {c_err:.5f})")
    xvalues = np.linspace(min(x_list), max(x_list))
    axis.plot(xvalues, m * xvalues + c, '-', c='k', zorder=0)
    # axis.set_title("$y=({gradient:.5f}\pm{gradient_err:.5f})x+{intercept:.5f}$".format(
    #     gradient=m, gradient_err=m_err, intercept=c, rsquared=r2_value, fontsize=10))
    axis.text(-0.08, 1.1, "$y=({gradient:.5f}\pm{gradient_err:.5f})x+{intercept:.5f}$".format(
        gradient=m, gradient_err=m_err, intercept=c, rsquared=r2_value, fontsize=10), transform=axis.transAxes)
    axis.text(0.5, 0.1, "$R^2={rsquared:.5f}$".format(
        gradient=m, gradient_err=m_err, intercept=c, rsquared=r2_value, fontsize=10), transform=axis.transAxes)

    return m, m_err, c, c_err, r2_value


def plot_2d_ltc_early(axis, numb_qy, coulomb_min_val, coulomb_range_val, omega_min, omega_max):

    marker = itertools.cycle(('1', '2', '3', '4', ',', '+', '.', 'o', '*', '^', 'v', '>', '<', 'X', '_', 'd', '|', 'H'))

    for i, alpha_exp in enumerate(np.linspace(-4, 0, 11, endpoint=True)):
        alpha = 10**alpha_exp

        if alpha_exp != 0:
            name = f"coulomb_{alpha:.5g}_plus_V1_scale_{1 - alpha:.5g}"
        else:
            name = f"coulomb_plus_V1_scale_0"

        # # get range of energy spectrum (from dat file)
        # energies = []
        # dat_file = f"fermions_torus_kysym_{name}_n_6_2s_18_ratio_1.000000.dat"
        # with open('/home/bart/PycharmProjects/response_functions/vectors_2/ltc/' + dat_file, 'r') as csvfile:
        #     plots = csv.reader(csvfile, delimiter=' ')
        #     for row in plots:
        #         if row[0].isnumeric():
        #             energies.append(float(row[1]))
        #     range = max(energies) - min(energies)

        omega = []
        SR = []
        file = f"fermions_torus_spec_resp_kysym_{name}_n_6_2s_{numb_qy}_ratio_1.000000_qy_0" \
               f".omega_{omega_min}-{omega_max}_eps_0.0001.sr.cut"
        with open('/home/bart/PycharmProjects/response_functions/FQHETorusSpectralResponse_2/stripped_files/' + file, 'r') as csvfile:
            plots = csv.reader(csvfile, delimiter=' ')
            for row in plots:
                omega.append(float(row[0])+10-coulomb_min_val)
                SR.append(float(row[1])/100)
        # normalize
        # omega = np.asarray(omega)
        # min_omega, max_omega = min(omega), max(omega)
        # omega = (omega-min_omega)/(max_omega-min_omega)
        # omega = omega*coulomb_range_val + coulomb_min_val
        # omega = omega.tolist()
        axis.scatter(omega, SR, s=0.5, label=f"${alpha_exp:.2g}$", marker=next(marker))

        # print(alpha_exp, scale, range, coulomb_range_val, np.abs(max(omega)-min(omega)))

    axis.set_xlabel('$\omega$')
    axis.set_ylabel('$I/10^2$')
    axis.set_ylim(0)
    axis.legend(loc='upper center', handletextpad=0, borderpad=0.2, framealpha=1,
                edgecolor=None, markerscale=5,
                fontsize=10, ncol=4, labelspacing=0, columnspacing=0, bbox_to_anchor=(0.45, 1.54), title='$\\log\\alpha$')
    # axis.set_xlim([10-10.005, 10-9.99])

    # fig.subplots_adjust(top=0.95, bottom=0.1, right=0.95, left=0.11)


def plot_3d_ltc(axis, numb_qy, coulomb_min_val, coulomb_range_val, omega_min, omega_max):

    omega = []
    SR = []

    for i, alpha_exp in enumerate(np.linspace(-4, 0, 11, endpoint=True)):
        alpha = 10 ** alpha_exp

        if alpha_exp != 0:
            name = f"coulomb_{alpha:.5g}_plus_V1_scale_{1 - alpha:.5g}"
        else:
            name = f"coulomb_plus_V1_scale_0"

        # # get range of energy spectrum (from dat file)
        # energies = []
        # dat_file = f"fermions_torus_kysym_{name}_n_6_2s_18_ratio_1.000000.dat"
        # with open('/home/bart/PycharmProjects/response_functions/vectors_2/ltc/' + dat_file, 'r') as csvfile:
        #     plots = csv.reader(csvfile, delimiter=' ')
        #     for row in plots:
        #         if row[0].isnumeric():
        #             energies.append(float(row[1]))
        #     range = max(energies) - min(energies)

        file = f"fermions_torus_spec_resp_kysym_{name}_n_6_2s_{numb_qy}_ratio_1.000000_qy_0" \
               f".omega_{omega_min}-{omega_max}_eps_0.0001.sr.cut"
        with open('/home/bart/PycharmProjects/response_functions/FQHETorusSpectralResponse_2/stripped_files/' + file, 'r') as csvfile:
            plots = csv.reader(csvfile, delimiter=' ')
            for row in plots:
                omega.append(float(row[0])+10-coulomb_min_val)
                SR.append(float(row[1])/100)
        # normalize
        # omega_tmp = np.asarray(omega[-10000:])
        # min_omega_tmp, max_omega_tmp = min(omega_tmp), max(omega_tmp)
        # omega_tmp = (omega_tmp - min_omega_tmp) / (max_omega_tmp - min_omega_tmp)
        # omega_tmp = omega_tmp * coulomb_range_val + coulomb_min_val
        # omega[-10000:] = omega_tmp.tolist()

    log_alpha = []
    for alpha_exp in np.linspace(-4, 0, 11, endpoint=True):
        log_alpha += [alpha_exp]*10000

    axis.scatter(log_alpha, omega, SR, s=0.5, c=log_alpha, cmap='brg')

    axis.set_xlabel('$\log \\alpha$')
    axis.xaxis.set_major_formatter(FormatStrFormatter('$%.2g$'))
    axis.set_ylabel('$\\omega$')
    axis.set_zlabel('$I/10^2$')
    axis.set_zlim(0)
    axis.set_position(Bbox.from_bounds(0.48, 0.67, 0.415, 0.31))
    axis.tick_params(axis='both', which='major', pad=0)
    axis.xaxis.labelpad = 0
    axis.yaxis.labelpad = 0
    axis.zaxis.labelpad = -2

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

    # fig.subplots_adjust(top=1.2, bottom=0, right=1, left=-0.1, hspace=0, wspace=0)


def plot_2d_ltc_complete_res_max(axis, numb_qy, coulomb_min_val, coulomb_range_val):

    omega = []
    SR = []
    lbl = []

    for i, alpha_exp in enumerate(np.linspace(-4, 0, 41, endpoint=True)):
        alpha = 10 ** alpha_exp

        if alpha_exp != 0:
            name = f"coulomb_{alpha:.5g}_plus_V1_scale_{1 - alpha:.5g}"
        else:
            name = f"coulomb_plus_V1_scale_0"

        # # get range of energy spectrum (from dat file)
        # energies = []
        # dat_file = f"fermions_torus_kysym_{name}_n_6_2s_18_ratio_1.000000.dat"
        # with open('/home/bart/PycharmProjects/response_functions/vectors_2/ltc/' + dat_file, 'r') as csvfile:
        #     plots = csv.reader(csvfile, delimiter=' ')
        #     for row in plots:
        #         if row[0].isnumeric():
        #             energies.append(float(row[1]))
        #     range = max(energies) - min(energies)

        file = f"fermions_torus_spec_resp_kysym_{name}_n_6_2s_{numb_qy}_ratio_1.000000_qy_0" \
               f".omega_-20-0_eps_1e-06.sr.cut"
        with open('/home/bart/PycharmProjects/response_functions/FQHETorusSpectralResponse_2/stripped_files/' + file, 'r') as csvfile:
            plots = csv.reader(csvfile, delimiter=' ')
            for row in plots:
                omega.append(float(row[0])+10-coulomb_min_val)
                SR.append(float(row[1]))
                lbl += [alpha]
        # normalize
        # omega_tmp = np.asarray(omega[-10000:])
        # min_omega_tmp, max_omega_tmp = min(omega_tmp), max(omega_tmp)
        # omega_tmp = (omega_tmp - min_omega_tmp) / (max_omega_tmp - min_omega_tmp)
        # omega_tmp = omega_tmp * coulomb_range_val + coulomb_min_val
        # omega[-10000:] = omega_tmp.tolist()
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

    # print(len(omega))

    # plot the large S points on top
    zipped = list(zip(lbl, omega, sr_max))
    zipped.sort(key=lambda pair: pair[2])
    lbl, omega, sr_max = zip(*zipped)

    im = axis.scatter(lbl, omega, c=sr_max, s=1, norm=colors.LogNorm(vmin=min(sr_max), vmax=max(sr_max)),
                    cmap=plt.cm.Reds)
    cb = fig.colorbar(im, ax=axis, pad=0.02)
    cb.set_label("$I_\mathrm{max}$", labelpad=-1, y=0.55)
    #axis.set_xlim([0.00001, 10])
    #axis.set_ylim([0.00001, 10])

    # axis.set_xscale('log')
    # x_major = LogLocator(base=10.0, numticks=4)
    # axis.xaxis.set_major_locator(x_major)
    # x_minor = LogLocator(base=10.0, subs=np.arange(1.0, 10.0) * 0.1, numticks=10)
    # axis.xaxis.set_minor_locator(x_minor)
    # axis.xaxis.set_minor_formatter(ticker.NullFormatter())
    # axis.set_yscale('log')
    # y_major = LogLocator(base=10.0, numticks=4)
    # axis.yaxis.set_major_locator(y_major)
    # y_minor = LogLocator(base=10.0, subs=np.arange(1.0, 10.0) * 0.1, numticks=10)
    # axis.yaxis.set_minor_locator(y_minor)
    # axis.yaxis.set_minor_formatter(ticker.NullFormatter())
    axis.set_xlabel('$\\alpha$')
    ##  ax.xaxis.set_major_formatter(FormatStrFormatter('%.2g'))
    axis.set_ylabel('$\\omega$')
    ## axis.cbaxis.labelpad = 0

    # ax.set_xticks(np.arange(2, 40, 2))

    # fig.subplots_adjust(top=0.95, bottom=0.1, right=0.95, left=0.11)


def plot_2d_ltc_slope_res_max(axis, numb_qy, coulomb_min_val, coulomb_range_val):

    omega = []
    SR = []
    lbl = []

    for i, alpha_exp in enumerate(np.linspace(-4, 0, 41, endpoint=True)):
        alpha = 10 ** alpha_exp

        if alpha_exp != 0:
            name = f"coulomb_{alpha:.5g}_plus_V1_scale_{1 - alpha:.5g}"
        else:
            name = f"coulomb_plus_V1_scale_0"

        # get specific range
        energies = []
        dat_file = f"fermions_torus_kysym_{name}_n_6_2s_{numb_qy}_ratio_1.000000.dat"
        with open('/home/bart/PycharmProjects/response_functions/vectors_2/ltc/' + dat_file,
                  'r') as csvfile:
            plots = csv.reader(csvfile, delimiter=' ')
            for row in plots:
                if row[0].isnumeric():
                    energies.append(float(row[1]))
            range = np.abs(max(energies) - min(energies))

        scale = range / coulomb_range_val

        file = f"fermions_torus_spec_resp_kysym_{name}_n_6_2s_{numb_qy}_ratio_1.000000_qy_0" \
               f".omega_-20-0_eps_1e-06.sr.cut"
        with open('/home/bart/PycharmProjects/response_functions/FQHETorusSpectralResponse_2/stripped_files/' + file, 'r') as csvfile:
            plots = csv.reader(csvfile, delimiter=' ')
            for row in plots:
                omega.append(float(row[0])+10-coulomb_min_val)
                SR.append(float(row[1]))
                lbl += [10 ** (-4 + i * 0.1)]
        # normalize
        # omega_tmp = np.asarray(omega[-10000:])
        # min_omega_tmp, max_omega_tmp = min(omega_tmp), max(omega_tmp)
        # omega_tmp = (omega_tmp - min_omega_tmp) / (max_omega_tmp - min_omega_tmp)
        # omega_tmp = omega_tmp * coulomb_range_val + coulomb_min_val
        # omega[-10000:] = omega_tmp.tolist()

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
        #log_range_val = np.log10(range_val)
        log_range_val = range_val
        log_omega_range += [log_range_val]

    #log_lbl_values = [np.log10(i) for i in lbl_values]
    log_lbl_values = lbl_values
    print(log_lbl_values)
    print(log_omega_range)

    im = axis.scatter(log_lbl_values, log_omega_range, s=5)

    # axis.set_xlabel('$\log \\alpha$')
    axis.set_xlabel('$\\alpha$')
    axis.xaxis.set_major_formatter(FormatStrFormatter('$%g$'))
    # axis.set_ylabel('$\log [\\mathrm{range}(\\Omega)]$')
    axis.set_ylabel('$\\mathrm{range}(\\Omega)$')
    axis.yaxis.set_major_formatter(FormatStrFormatter('$%g$'))

    line_of_best_fit(axis, log_lbl_values, log_omega_range)

    # ax.set_xticks(np.arange(2, 40, 2))

    # fig.subplots_adjust(top=0.95, bottom=0.1, right=0.95, left=0.11)


def plot_2d_ltc_nbr_omega_res_max(axis, numb_qy, coulomb_min_val, coulomb_range_val):

    omega = []
    SR = []
    lbl = []

    for i, alpha_exp in enumerate(np.linspace(-4, 0, 41, endpoint=True)):
        alpha = 10 ** alpha_exp

        if alpha_exp != 0:
            name = f"coulomb_{alpha:.5g}_plus_V1_scale_{1 - alpha:.5g}"
        else:
            name = f"coulomb_plus_V1_scale_0"

        # get specific range
        energies = []
        dat_file = f"fermions_torus_kysym_{name}_n_6_2s_{numb_qy}_ratio_1.000000.dat"
        with open('/home/bart/PycharmProjects/response_functions/vectors_2/ltc/' + dat_file,
                  'r') as csvfile:
            plots = csv.reader(csvfile, delimiter=' ')
            for row in plots:
                if row[0].isnumeric():
                    energies.append(float(row[1]))
            range = np.abs(max(energies) - min(energies))

        scale = range / coulomb_range_val

        file = f"fermions_torus_spec_resp_kysym_{name}_n_6_2s_{numb_qy}_ratio_1.000000_qy_0" \
               f".omega_-20-0_eps_1e-06.sr.cut"
        with open('/home/bart/PycharmProjects/response_functions/FQHETorusSpectralResponse_2/stripped_files/' + file, 'r') as csvfile:
            plots = csv.reader(csvfile, delimiter=' ')
            for row in plots:
                omega.append(float(row[0])+10-coulomb_min_val)
                SR.append(float(row[1]))
                lbl += [10 ** (-4 + i * 0.1)]
        # normalize
        # omega_tmp = np.asarray(omega[-10000:])
        # min_omega_tmp, max_omega_tmp = min(omega_tmp), max(omega_tmp)
        # omega_tmp = (omega_tmp - min_omega_tmp) / (max_omega_tmp - min_omega_tmp)
        # omega_tmp = omega_tmp * coulomb_range_val + coulomb_min_val
        # omega[-10000:] = omega_tmp.tolist()

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

    im = axis.scatter(log_lbl_values, len_values, s=5)

    axis.set_xlabel('$\log \\alpha$')
    axis.xaxis.set_major_formatter(FormatStrFormatter('$%g$'))
    axis.set_ylabel('$n(I_\mathrm{max})$')

    axis.axhline(np.mean(len_values), c='k', zorder=-1, linewidth=0.5, linestyle='--')
    axis.axhspan(np.mean(len_values) - np.std(len_values), np.mean(len_values) + np.std(len_values), alpha=0.1, color='red')

    axis.text(0.23, 0.835, "$\\langle n(I_\mathrm{{max}}) \\rangle = {mean:.3g}\pm {sd:.3g}$".format(
        mean=np.mean(len_values), sd=np.std(len_values), fontsize=10), transform=axis.transAxes)

    # ax.set_xticks(np.arange(2, 40, 2))

    # fig.subplots_adjust(top=0.95, bottom=0.1, right=0.95, left=0.11)


def plot_2d_ltc_mean_S_res_max(axis, numb_qy, coulomb_min_val, coulomb_range_val):

    omega = []
    SR = []
    lbl = []

    for i, alpha_exp in enumerate(np.linspace(-4, 0, 41, endpoint=True)):
        alpha = 10 ** alpha_exp

        if alpha_exp != 0:
            name = f"coulomb_{alpha:.5g}_plus_V1_scale_{1 - alpha:.5g}"
        else:
            name = f"coulomb_plus_V1_scale_0"

        # get specific range
        energies = []
        dat_file = f"fermions_torus_kysym_{name}_n_6_2s_{numb_qy}_ratio_1.000000.dat"
        with open('/home/bart/PycharmProjects/response_functions/vectors_2/ltc/' + dat_file,
                  'r') as csvfile:
            plots = csv.reader(csvfile, delimiter=' ')
            for row in plots:
                if row[0].isnumeric():
                    energies.append(float(row[1]))
            range = np.abs(max(energies) - min(energies))

        scale = range / coulomb_range_val

        file = f"fermions_torus_spec_resp_kysym_{name}_n_6_2s_{numb_qy}_ratio_1.000000_qy_0" \
               f".omega_-20-0_eps_1e-06.sr.cut"
        with open('/home/bart/PycharmProjects/response_functions/FQHETorusSpectralResponse_2/stripped_files/' + file, 'r') as csvfile:
            plots = csv.reader(csvfile, delimiter=' ')
            for row in plots:
                omega.append(float(row[0])+10-coulomb_min_val)
                SR.append(float(row[1]))
                lbl += [10 ** (-4 + i * 0.1)]
        # normalize
        # omega_tmp = np.asarray(omega[-10000:])
        # min_omega_tmp, max_omega_tmp = min(omega_tmp), max(omega_tmp)
        # omega_tmp = (omega_tmp - min_omega_tmp) / (max_omega_tmp - min_omega_tmp)
        # omega_tmp = omega_tmp * coulomb_range_val + coulomb_min_val
        # omega[-10000:] = omega_tmp.tolist()

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
        sr_values += [sr_mean/1000]

    log_lbl_values = [np.log10(i) for i in lbl_values]

    im = axis.scatter(log_lbl_values, sr_values, s=5)

    axis.set_xlabel('$\log \\alpha$')
    axis.xaxis.set_major_formatter(FormatStrFormatter('$%g$'))
    axis.set_ylabel('$\mu_{I_\mathrm{max}}/10^{3}$')

    axis.axhline(np.mean(sr_values), c='k', zorder=-1, linewidth=0.5, linestyle='--')
    axis.axhspan(np.mean(sr_values)-np.std(sr_values), np.mean(sr_values)+np.std(sr_values), alpha=0.1, color='red')

    axis.text(0.17, 0.825, "$\\langle \mu_{{I_\mathrm{{max}}}} \\rangle / 10^3 = {mean:.3g}\pm {sd:.3g}$".format(
        mean=np.mean(sr_values), sd=np.std(sr_values), fontsize=10), transform=axis.transAxes)

    # ax.set_xticks(np.arange(2, 40, 2))

    # fig.subplots_adjust(top=0.95, bottom=0.1, right=0.95, left=0.11)


if __name__ == "__main__":

    # get coulomb ground state energy and range (from dat file)
    energies = []
    dat_file = f"fermions_torus_kysym_coulomb_n_6_2s_18_ratio_1.000000.dat"
    with open('/home/bart/PycharmProjects/response_functions/vectors_2/sr/' + dat_file,
              'r') as csvfile:
        plots = csv.reader(csvfile, delimiter=' ')
        for row in plots:
            if row[0].isnumeric():
                energies.append(float(row[1]))
        coulomb_gs = min(energies)
        coulomb_range = max(energies) - min(energies)

    # # get coulomb range and min (from low res sr file)
    # omegas = []
    # sr_file = f"fermions_torus_spec_resp_kysym_coulomb_plus_V1_scale_0_n_6_2s_18_ratio_1.000000_qy_0.omega_-100-100_eps_0.0001.sr.cut"
    # with open('/home/bart/PycharmProjects/response_functions/FQHETorusSpectralResponse_2/stripped_files/' + sr_file,
    #           'r') as csvfile:
    #     plots = csv.reader(csvfile, delimiter=' ')
    #     for row in plots:
    #         omegas.append(float(row[0]))
    #     coulomb_range_low = np.abs(max(omegas) - min(omegas))
    #     coulomb_min_low = min(omegas)+10-coulomb_gs
    #
    # # get coulomb range and min (from high res sr file)
    # omegas = []
    # sr_file = f"fermions_torus_spec_resp_kysym_coulomb_plus_V1_scale_0_n_6_2s_18_ratio_1.000000_qy_0.omega_-20-0_eps_1e-06.sr.cut"
    # with open('/home/bart/PycharmProjects/response_functions/FQHETorusSpectralResponse_2/stripped_files/' + sr_file,
    #           'r') as csvfile:
    #     plots = csv.reader(csvfile, delimiter=' ')
    #     for row in plots:
    #         omegas.append(float(row[0]))
    #     coulomb_range_high = np.abs(max(omegas) - min(omegas))
    #     coulomb_min_high = min(omegas) + 10 - coulomb_gs

    fig = plt.figure(figsize=(6, 7.5))
    gs = gridspec.GridSpec(3, 2, hspace=0.4, wspace=0.4)

    ax0 = plt.subplot(gs[0])
    plot_2d_ltc_early(ax0, 18, coulomb_gs, coulomb_range, omega_min=-100, omega_max=100)
    ax1 = plt.subplot(gs[1], projection='3d')
    plot_3d_ltc(ax1, 18, coulomb_gs, coulomb_range, omega_min=-100, omega_max=100)
    ax2 = plt.subplot(gs[2])
    plot_2d_ltc_complete_res_max(ax2, 18, coulomb_gs, coulomb_range)
    ax3 = plt.subplot(gs[3])
    plot_2d_ltc_slope_res_max(ax3, 18, coulomb_gs, coulomb_range)
    ax4 = plt.subplot(gs[4])
    plot_2d_ltc_nbr_omega_res_max(ax4, 18, coulomb_gs, coulomb_range)
    ax5 = plt.subplot(gs[5])
    plot_2d_ltc_mean_S_res_max(ax5, 18, coulomb_gs, coulomb_range)

    fig.text(0.02, 0.9, "(a)", fontsize=12)
    fig.text(0.49, 0.9, "(b)", fontsize=12)
    fig.text(0.02, 0.62, "(c)", fontsize=12)
    fig.text(0.49, 0.62, "(d)", fontsize=12)
    fig.text(0.02, 0.33, "(e)", fontsize=12)
    fig.text(0.49, 0.33, "(f)", fontsize=12)

    plt.savefig("ltc.png", bbox_inches='tight', dpi=300)
    plt.show()