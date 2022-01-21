import numpy as np
import matplotlib.pyplot as plt
import csv
import matplotlib.gridspec as gridspec
from matplotlib.ticker import FormatStrFormatter
from matplotlib.lines import Line2D
from matplotlib.patches import Polygon
from scipy import stats


plt.rc('text', usetex=True)
plt.rc('text.latex', preamble=r'\usepackage{amsmath}')


def plot_2d_q_specific(axis):

    domain = np.array([np.linspace(0, 4.7, 48, endpoint=True)], dtype=object)

    particles = [8]

    log_SR_max_mean = np.zeros(len(particles), dtype=object)
    log_SR_max_std = np.zeros(len(particles), dtype=object)

    for N_idx, N in enumerate(particles):

        print("N = ", N)

        log_SR_max_mean[N_idx] = []
        log_SR_max_std[N_idx] = []

        for j in domain[N_idx]:

            file = f"fermions_torus_spec_resp_kysym_coulomb_n_{N:g}_2s_{3*N:g}_ratio_1.000000_qx_0_qy_0" \
                   f".omega_-100-100_eps_{0.0001/(2**j):.6g}.sr.cut"

            omega = []
            SR = []
            with open('/home/bart/PycharmProjects/response_functions/FQHETorusSpectralResponse/stripped_files/' + file, 'r') as csvfile:
                plots = csv.reader(csvfile, delimiter=' ')
                for row in plots:
                    if -7.5-2.5/(2**j) < float(row[0]) < -7.5+2.5/(2**j):
                        omega.append(float(row[0])+10)
                        SR.append(float(row[1]))

            omega_max = []
            sr_max = []
            for i, entry in enumerate(omega[1:-1]):
                if SR[i] > SR[i-1] and SR[i] > SR[i+1] and omega[i] > 0:
                    omega_max += [1]
                    sr_max += [SR[i]]
                else:
                    omega_max += [0]

            log_SR_max_mean[N_idx] += [np.log2(np.mean(sr_max))]
            log_SR_max_std[N_idx] += [np.log2(np.std(sr_max))]

    axis.plot(1, 10, '.', marker='x', markersize=4, label="$\log_2(\mu_{S_{\mathrm{max}}})$", c='k')
    axis.plot(1, 10, '.', marker='^', markersize=4, label="$\log_2(\sigma_{S_{\mathrm{max}}})$", c='k')

    for N_idx, N in enumerate(particles):
        axis.plot([np.log2(1 / (2 ** j)) for j in domain[N_idx]], log_SR_max_mean[N_idx], '.', marker='x',
                  markersize=4, c=f'C2')
        axis.plot([np.log2(1 / (2 ** j)) for j in domain[N_idx]], log_SR_max_std[N_idx], '.', marker='^',
                  markersize=4, c=f'C2')

    axis.set_xlim([-6, 0])
    axis.tick_params('x', direction='in', bottom=True)
    plt.setp(axis.get_xticklabels(), visible=False)
    leg = axis.legend(loc='upper right', handletextpad=0, borderpad=0.4, framealpha=0,
                      edgecolor='w', markerscale=1.5, ncol=2, labelspacing=0, columnspacing=0)
    leg.get_frame().set_linewidth(0.5)

    region = Polygon(((-6, -100), (-4.1, -100), (-4.1, 100), (-6, 100)), fc=(0, 0, 0, 0.1))
    axis.add_artist(region)

    xvalues = [np.log2(1/(2**j)) for j in domain[0]][:-6]
    result = stats.linregress(xvalues, log_SR_max_mean[0][:-6])
    m = result.slope
    m_err = result.stderr
    c = result.intercept
    R = result.rvalue
    axis.plot(xvalues, [m*i+c for i in xvalues], '-', c='k', zorder=-1, lw=0.5)
    axis.text(-5, 9, f"$m_\mu={m:.3g}\pm{m_err:.3g}$ ($R^2={R**2:.3g}$)")

    xvalues = [np.log2(1/(2**j)) for j in domain[0]][:-6]
    result = stats.linregress(xvalues, log_SR_max_std[0][:-6])
    m = result.slope
    m_err = result.stderr
    c = result.intercept
    R = result.rvalue
    axis.plot(xvalues, [m * i + c for i in xvalues], '-', c='k', zorder=-1, lw=0.5)
    axis.text(-5, 8.4, f"$m_\sigma={m:.3g}\pm{m_err:.3g}$ ($R^2={R**2:.3g}$)")


def plot_2d_gap_omega_res_max(axis):

    domain = np.array([np.linspace(0, 4.7, 48, endpoint=True)], dtype=object)
    particles = [8]
    omega_max_gap_mean = np.zeros(len(particles), dtype=object)

    for N_idx, N in enumerate(particles):

        omega_max_gap_mean[N_idx] = []

        for j in domain[N_idx]:

            file = f"fermions_torus_spec_resp_kysym_coulomb_n_{N:g}_2s_{3*N:g}_ratio_1.000000_qx_0_qy_0" \
                   f".omega_-100-100_eps_{0.0001/(2**j):.6g}.sr.cut"

            omega = []
            SR = []
            with open('/home/bart/PycharmProjects/response_functions/FQHETorusSpectralResponse/stripped_files/' + file, 'r') as csvfile:
                plots = csv.reader(csvfile, delimiter=' ')
                for row in plots:
                    if -7.5 - 2.5 / (2 ** j) < float(row[0]) < -7.5 + 2.5 / (2 ** j):
                        omega.append(float(row[0])+10)
                        SR.append(float(row[1]))

            omega_max = []
            for i, entry in enumerate(omega[1:-1]):
                if SR[i] > SR[i-1] and SR[i] > SR[i+1] and omega[i] > 0:
                    omega_max += [omega[i]]

            omega_gaps = [omega_max[i]-omega_max[i-1] for i in range(1, len(omega_max))]
            omega_max_gap_mean[N_idx] += [np.log2(np.mean(omega_gaps))]

    axis.plot(1, 0, '.', marker='+', markersize=4, label="$\log_2|\Delta\\bar{\omega}_i - \Delta\\bar{\omega}_{i-1}|$", c='k')
    axis.plot(1, 0, '.', marker='v', markersize=4, label="$\log_2\langle \Delta\Omega \\rangle$", c='k')

    axis.plot([-i for i in domain[0]],
              [np.log2((np.abs(5 / (2 ** i) - 5 / (2 ** (i - 1))))) for i in domain[0]], '+',
              markersize=4, c="k")

    for N_idx, N in enumerate(particles):
        axis.plot([-i for i in domain[N_idx]], omega_max_gap_mean[N_idx], 'v', markersize=4, c=f"C2")

    axis.tick_params('x', direction='in', bottom=True)
    plt.setp(axis.get_xticklabels(), visible=False)
    axis.set_ylim(top=7)

    leg = axis.legend(loc='upper right', handletextpad=0, borderpad=0.4, framealpha=0,
                      edgecolor='w', markerscale=1.5, ncol=2, labelspacing=0, columnspacing=0)
    leg.get_frame().set_linewidth(0.5)

    region = Polygon(((-6, -100), (-4.1, -100), (-4.1, 100), (-6, 100)), fc=(0, 0, 0, 0.1))
    axis.add_artist(region)


def plot_2d_nbr_omega_res_max(axis):
    domain = np.array([np.linspace(0, 4.7, 48, endpoint=True)], dtype=object)
    particles = [8]
    lbl_values = np.zeros(len(particles), dtype=object)
    number_of_peaks = np.zeros(len(particles), dtype=object)

    for N_idx, N in enumerate(particles):

        lbl = []
        number_of_peaks[N_idx] = []

        for j in domain[N_idx]:

            file = f"fermions_torus_spec_resp_kysym_coulomb_n_{N:g}_2s_{3*N:g}_ratio_1.000000_qx_0_qy_0" \
                   f".omega_-100-100_eps_{0.0001/(2**j):.6g}.sr.cut"

            omega = []
            SR = []
            with open('/home/bart/PycharmProjects/response_functions/FQHETorusSpectralResponse/stripped_files/' + file, 'r') as csvfile:
                plots = csv.reader(csvfile, delimiter=' ')
                for row in plots:
                    if -7.5 - 2.5 / (2 ** j) < float(row[0]) < -7.5 + 2.5 / (2 ** j):
                        omega.append(float(row[0])+10)
                        SR.append(float(row[1]))
                        lbl += [0-j]

            omega_max = []
            sr_max = []
            for i, entry in enumerate(omega[1:-1]):
                if SR[i] > SR[i-1] and SR[i] > SR[i+1] and omega[i] > 0:
                    omega_max += [1]
                    sr_max += [SR[i]]
                else:
                    omega_max += [0]

            number_of_peaks[N_idx] += [np.sum(omega_max)]

        lbl_values[N_idx] = sorted(list(set(lbl)), reverse=True)

    for N_idx, N in enumerate(particles):
        axis.plot(lbl_values[N_idx], number_of_peaks[N_idx], '.', markersize=4, c=f'C2')

    axis.tick_params('x', direction='in', bottom=True)
    plt.setp(axis.get_xticklabels(), visible=False)
    axis.set_ylabel('$n(S_\mathrm{max})$')

    region = Polygon(((-6, -100), (-4.1, -100), (-4.1, 100), (-6, 100)), fc=(0, 0, 0, 0.1))
    axis.add_artist(region)


def plot_2d_mean_S_res_max(axis):
    domain = np.array([np.linspace(0, 4.7, 48, endpoint=True)], dtype=object)
    particles = [8]
    lbl_values = np.zeros(len(particles), dtype=object)
    S_max_bar = np.zeros(len(particles), dtype=object)

    for N_idx, N in enumerate(particles):

        lbl = []
        S_max_bar[N_idx] = []

        for j in domain[N_idx]:

            file = f"fermions_torus_spec_resp_kysym_coulomb_n_{N:g}_2s_{3*N:g}_ratio_1.000000_qx_0_qy_0" \
                   f".omega_-100-100_eps_{0.0001/(2**j):.6g}.sr.cut"

            omega = []
            SR = []
            with open('/home/bart/PycharmProjects/response_functions/FQHETorusSpectralResponse/stripped_files/' + file, 'r') as csvfile:
                plots = csv.reader(csvfile, delimiter=' ')
                for row in plots:
                    if -7.5 - 2.5 / (2 ** j) < float(row[0]) < -7.5 + 2.5 / (2 ** j):
                        omega.append(float(row[0])+10)
                        SR.append(float(row[1]))
                        lbl += [0-j]

            omega_max = []
            sr_max = []
            for i, entry in enumerate(omega[1:-1]):
                if SR[i] > SR[i-1] and SR[i] > SR[i+1] and omega[i] > 0:
                    omega_max += [1]
                    sr_max += [SR[i]]
                else:
                    omega_max += [0]

            S_max_bar[N_idx] += [np.mean(sr_max)*0.0001/(2**j)]

        lbl_values[N_idx] = sorted(list(set(lbl)), reverse=True)

    for N_idx, N in enumerate(particles):
        axis.plot(lbl_values[N_idx], S_max_bar[N_idx], '.', markersize=4, c=f'C2')

    axis.set_xlabel('$\log_2(\mathrm{range}(\omega)/\mathrm{range}(\omega_0))$', labelpad=10)
    axis.xaxis.set_major_formatter(FormatStrFormatter('$%g$'))
    axis.set_ylabel('$\mu_{S_\mathrm{max}}\epsilon$')

    region = Polygon(((-6, -100), (-4.1, -100), (-4.1, 100), (-6, 100)), fc=(0, 0, 0, 0.1))
    axis.add_artist(region)

    custom_lines = [Line2D([0], [0], color='C2', lw=4)]
    axis.legend(custom_lines, ['$N=8$, $q_x=0$'], bbox_to_anchor=(0.65, 5.6), ncol=3)


if __name__ == "__main__":

    fig = plt.figure(figsize=(6, 7.5))
    gs = gridspec.GridSpec(4, 1, hspace=0, height_ratios=[2, 1, 1, 1])

    ax0 = plt.subplot(gs[0])
    plot_2d_q_specific(ax0)
    ax1 = plt.subplot(gs[1], sharex=ax0)
    plot_2d_gap_omega_res_max(ax1)
    ax2 = plt.subplot(gs[2], sharex=ax1)
    plot_2d_nbr_omega_res_max(ax2)
    ax3 = plt.subplot(gs[3], sharex=ax2)
    plot_2d_mean_S_res_max(ax3)

    fig.text(0.02, 0.87, "(a)", fontsize=12)
    fig.text(0.02, 0.56, "(b)", fontsize=12)
    fig.text(0.02, 0.405, "(c)", fontsize=12)
    fig.text(0.02, 0.25, "(d)", fontsize=12)

    plt.savefig("/home/bart/Documents/papers/SR/coulomb_scaling_n_8_qx_0.png", bbox_inches='tight', dpi=300)
    plt.show()
