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


def plot_2d_ltc_complete_res_max(axis, numb_qy):

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

        with open('/home/bart/KDevProjects/response_functions/FQHETorusSpectralResponse/stripped_files/' + file, 'r') as csvfile:
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

    im = axis.scatter(lbl, omega, c=sr_max, s=1, norm=colors.LogNorm(vmin=min(sr_max), vmax=max(sr_max)),
                    cmap=plt.cm.Reds)
    cb = fig.colorbar(im, ax=axis, pad=0.02)
    cb.set_label("$S$", labelpad=-1)
    axis.set_xlim([0.00001, 10])
    axis.set_ylim([0.00001, 10])

    axis.set_xscale('log')
    axis.set_yscale('log')
    axis.set_xlabel('$\\alpha$')
    # ax.xaxis.set_major_formatter(FormatStrFormatter('%.2g'))
    axis.set_ylabel('$\\omega$')
    # axis.cbaxis.labelpad = 0

    # ax.set_xticks(np.arange(2, 40, 2))

    # fig.subplots_adjust(top=0.95, bottom=0.1, right=0.95, left=0.11)


def plot_2d_ltc_slope_res_max(axis, numb_qy):

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

        with open('/home/bart/KDevProjects/response_functions/FQHETorusSpectralResponse/stripped_files/' + file, 'r') as csvfile:
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

    im = axis.scatter(log_lbl_values, log_omega_range, s=5)

    axis.set_xlabel('$\\log_{10}(\\alpha)$')
    axis.xaxis.set_major_formatter(FormatStrFormatter('$%g$'))
    axis.set_ylabel('$\\log_{10}[\\mathrm{range}(\\Omega)]$')
    axis.yaxis.set_major_formatter(FormatStrFormatter('$%g$'))

    line_of_best_fit(axis, log_lbl_values, log_omega_range)

    # ax.set_xticks(np.arange(2, 40, 2))

    # fig.subplots_adjust(top=0.95, bottom=0.1, right=0.95, left=0.11)


def plot_2d_ltc_nbr_omega_res_max(axis, numb_qy):

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

        with open('/home/bart/KDevProjects/response_functions/FQHETorusSpectralResponse/stripped_files/' + file, 'r') as csvfile:
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

    im = axis.scatter(log_lbl_values, len_values, s=5)

    axis.set_xlabel('$\\log_{10}(\\alpha)$')
    axis.xaxis.set_major_formatter(FormatStrFormatter('$%g$'))
    axis.set_ylabel('$n(\\Omega)$')

    axis.axhline(np.mean(len_values), c='k', zorder=-1, linewidth=0.5, linestyle='--')
    axis.axhspan(np.mean(len_values) - np.std(len_values), np.mean(len_values) + np.std(len_values), alpha=0.1, color='red')

    axis.text(0.3, 0.85, "$\\langle n(\\Omega) \\rangle = {mean:.3g}\pm {sd:.3g}$".format(
        mean=np.mean(len_values), sd=np.std(len_values), fontsize=10), transform=axis.transAxes)

    # ax.set_xticks(np.arange(2, 40, 2))

    # fig.subplots_adjust(top=0.95, bottom=0.1, right=0.95, left=0.11)


def plot_2d_ltc_mean_S_res_max(axis, numb_qy):

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

        with open('/home/bart/KDevProjects/response_functions/FQHETorusSpectralResponse/stripped_files/' + file, 'r') as csvfile:
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
        sr_values += [sr_mean/10000]

    log_lbl_values = [np.log10(i) for i in lbl_values]

    im = axis.scatter(log_lbl_values, sr_values, s=5)

    axis.set_xlabel('$\\log_{10}(\\alpha)$')
    axis.xaxis.set_major_formatter(FormatStrFormatter('$%g$'))
    axis.set_ylabel('$\\bar{S}/10^{4}$')

    axis.axhline(np.mean(sr_values), c='k', zorder=-1, linewidth=0.5, linestyle='--')
    axis.axhspan(np.mean(sr_values)-np.std(sr_values), np.mean(sr_values)+np.std(sr_values), alpha=0.1, color='red')

    axis.text(0.27, 0.85, "$\\langle \\bar{{S}} \\rangle / 10^4 = {mean:.3g}\pm {sd:.3g}$".format(
        mean=np.mean(sr_values), sd=np.std(sr_values), fontsize=10), transform=axis.transAxes)

    # ax.set_xticks(np.arange(2, 40, 2))

    # fig.subplots_adjust(top=0.95, bottom=0.1, right=0.95, left=0.11)


if __name__ == "__main__":

    fig = plt.figure(figsize=(6, 5))
    gs = gridspec.GridSpec(2, 2, hspace=0.4, wspace=0.4)

    ax0 = plt.subplot(gs[0])
    plot_2d_ltc_complete_res_max(ax0, 18)
    ax1 = plt.subplot(gs[1])
    plot_2d_ltc_slope_res_max(ax1, 18)
    ax2 = plt.subplot(gs[2])
    plot_2d_ltc_nbr_omega_res_max(ax2, 18)
    ax3 = plt.subplot(gs[3])
    plot_2d_ltc_mean_S_res_max(ax3, 18)

    fig.text(0.02, 0.9, "(a)", fontsize=12)
    fig.text(0.49, 0.9, "(b)", fontsize=12)
    fig.text(0.02, 0.4, "(c)", fontsize=12)
    fig.text(0.49, 0.4, "(d)", fontsize=12)

    plt.savefig("/home/bart/Documents/papers/SR/ltc.png", bbox_inches='tight', dpi=300)
    plt.show()
