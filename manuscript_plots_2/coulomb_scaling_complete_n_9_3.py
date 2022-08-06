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

vectors = "/home/bart/PycharmProjects/response_functions/vectors_2/"
stripped_files = "/home/bart/PycharmProjects/response_functions/FQHETorusSpectralResponse_2/stripped_files/"

# INPUT
mid = -10.6995  # midpoint (-10.6, -10.6995)
std = 0.6095  # deviation (0.5, 0.6095)


def plot_2d_q_specific(axis):

    domain = np.array([np.linspace(0, 6, 61), np.linspace(0, 6, 61), np.linspace(0, 6, 61), np.linspace(0, 6, 61),
                       np.linspace(0, 6, 61)], dtype=object)
    particles = [6, 7, 8, 8, 9]

    log_SR_max_mean = np.zeros(len(particles), dtype=object)
    log_SR_max_std = np.zeros(len(particles), dtype=object)

    for N_idx, n_val in enumerate(particles):

        print("n_val = ", n_val)

        log_SR_max_mean[N_idx] = []
        log_SR_max_std[N_idx] = []

        for j in domain[N_idx]:

            if n_val == 8 and N_idx == 2:
                file = f"fermions_torus_spec_resp_kysym_coulomb_n_{n_val:g}_2s_{3 * n_val:g}_ratio_1.000000_qx_0_qy_0" \
                       f".omega_{mid - std/(2**j):.6g}-{mid + std/(2**j):.6g}_eps_{0.0001 / (2 ** j):.6g}.sr.cut"
            else:
                file = f"fermions_torus_spec_resp_kysym_coulomb_n_{n_val:g}_2s_{3 * n_val:g}_ratio_1.000000_qy_0" \
                       f".omega_{mid - std / (2 ** j):.6g}-{mid + std / (2 ** j):.6g}_eps_{0.0001 / (2 ** j):.6g}.sr.cut"

            # get ground state energy (from dat file)
            energies = []
            dat_file = f"fermions_torus_kysym_coulomb_n_{n_val:g}_2s_{3*n_val:g}_ratio_1.000000.dat"
            with open(vectors + f'coulomb/n_{n_val:g}/' + dat_file, 'r') as csvfile:
                data = csv.reader(csvfile, delimiter=' ')
                for row in data:
                    if row[0].isnumeric():
                        energies.append(float(row[1]))
                ground = min(energies)

            omega = []
            SR = []
            with open(stripped_files + file, 'r') as csvfile:
                data = csv.reader(csvfile, delimiter=' ')
                for row in data:
                    if mid-std/(2**j) < float(row[0]) < mid+std/(2**j):
                        omega.append(float(row[0])+10-ground)
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

    axis.plot(1, 10, '.', marker='x', markersize=4, label="$\log_2(\mu_{I_{\mathrm{max}}})$", c='k')
    axis.plot(1, 10, '.', marker='^', markersize=4, label="$\log_2(\sigma_{I_{\mathrm{max}}})$", c='k')

    for N_idx, n_val in enumerate(particles):
        if N_idx == 2:
            alpha_val = 0.5
        else:
            alpha_val = 1
        axis.plot([np.log2(1 / (2 ** j)) for j in domain[N_idx]], log_SR_max_mean[N_idx], '.', marker='x',
                  markersize=4, c=f'C{n_val-particles[0]}', alpha=alpha_val)
        axis.plot([np.log2(1 / (2 ** j)) for j in domain[N_idx]], log_SR_max_std[N_idx], '.', marker='^',
                  markersize=4, c=f'C{n_val-particles[0]}', alpha=alpha_val)

    axis.set_xlim([-6, 0])
    axis.set_ylim(1)
    axis.tick_params('x', direction='in', bottom=True)
    plt.setp(axis.get_xticklabels(), visible=False)
    leg = axis.legend(loc='upper right', handletextpad=0, borderpad=0.4, framealpha=0,
                      edgecolor='w', markerscale=1.5, ncol=2, labelspacing=0, columnspacing=0)
    leg.get_frame().set_linewidth(0.5)
    axis.add_artist(leg)

    h = [plt.plot([], '.', marker="x", markersize=4, color="C2", alpha=0.5)[0]]
    plt.legend(handles=h, labels=["$\log_2(\mu_{I_{\mathrm{max}}})$, $N=8$, $q_x=0$"], loc=(0.555, 0.75), handletextpad=0,
               borderpad=0.4, framealpha=0, edgecolor='w', markerscale=1.5, ncol=2, labelspacing=0, columnspacing=0)

    xvalues = [np.log2(1/(2**j)) for j in domain[4]]
    result = stats.linregress(xvalues, log_SR_max_mean[4])
    m = result.slope
    m_err = result.stderr
    c = result.intercept
    R = result.rvalue
    axis.plot(xvalues, [m*i+c for i in xvalues], '-', c='k', zorder=-1, lw=0.5)
    axis.text(-5.3, 2.9, f"$m_\mu={m:.3g}\pm{m_err:.3g}$ ($R^2={R**2:.3g}$)")

    xvalues = [np.log2(1/(2**j)) for j in domain[4]]
    result = stats.linregress(xvalues, log_SR_max_std[4])
    m = result.slope
    m_err = result.stderr
    c = result.intercept
    R = result.rvalue
    axis.plot(xvalues, [m * i + c for i in xvalues], '-', c='k', zorder=-1, lw=0.5)
    axis.text(-5.3, 1.7, f"$m_\sigma={m:.3g}\pm{m_err:.3g}$")

    # region = Polygon(((-6, -100), (-5.5, -100), (-5.5, 100), (-6, 100)), fc=(0, 0, 0, 0.1))
    # axis.add_artist(region)


def plot_2d_gap_omega_res_max(axis):

    domain = np.array([np.linspace(0, 6, 61), np.linspace(0, 6, 61), np.linspace(0, 6, 61), np.linspace(0, 6, 61),
                       np.linspace(0, 6, 61)], dtype=object)
    particles = [6, 7, 8, 8, 9]

    omega_max_gap_mean = np.zeros(len(particles), dtype=object)

    for N_idx, n_val in enumerate(particles):

        omega_max_gap_mean[N_idx] = []

        for j in domain[N_idx]:

            if n_val == 8 and N_idx == 2:
                file = f"fermions_torus_spec_resp_kysym_coulomb_n_{n_val:g}_2s_{3 * n_val:g}_ratio_1.000000_qx_0_qy_0" \
                       f".omega_{mid - std / (2 ** j):.6g}-{mid + std / (2 ** j):.6g}_eps_{0.0001 / (2 ** j):.6g}.sr.cut"
            else:
                file = f"fermions_torus_spec_resp_kysym_coulomb_n_{n_val:g}_2s_{3 * n_val:g}_ratio_1.000000_qy_0" \
                       f".omega_{mid - std / (2 ** j):.6g}-{mid + std / (2 ** j):.6g}_eps_{0.0001 / (2 ** j):.6g}.sr.cut"

            # get ground state energy (from dat file)
            energies = []
            dat_file = f"fermions_torus_kysym_coulomb_n_{n_val:g}_2s_{3 * n_val:g}_ratio_1.000000.dat"
            with open(vectors + f'coulomb/n_{n_val:g}/' + dat_file, 'r') as csvfile:
                data = csv.reader(csvfile, delimiter=' ')
                for row in data:
                    if row[0].isnumeric():
                        energies.append(float(row[1]))
                ground = min(energies)

            omega = []
            SR = []
            with open(stripped_files + file, 'r') as csvfile:
                data = csv.reader(csvfile, delimiter=' ')
                for row in data:
                    if mid - std / (2 ** j) < float(row[0]) < mid + std / (2 ** j):
                        omega.append(float(row[0])+10-ground)
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

    for N_idx, n_val in enumerate(particles):
        if N_idx == 2:
            alpha_val = 0.5
        else:
            alpha_val = 1
        axis.plot([-i for i in domain[N_idx]], omega_max_gap_mean[N_idx], 'v', markersize=4, c=f"C{n_val-particles[0]}",
                  alpha=alpha_val)

    axis.tick_params('x', direction='in', bottom=True)
    plt.setp(axis.get_xticklabels(), visible=False)
    axis.set_ylim(top=7)

    leg = axis.legend(loc='upper right', handletextpad=0, borderpad=0.4, framealpha=0,
                      edgecolor='w', markerscale=1.5, ncol=2, labelspacing=0, columnspacing=0)
    leg.get_frame().set_linewidth(0.5)

    # region = Polygon(((-6, -100), (-4.1, -100), (-4.1, 100), (-6, 100)), fc=(0, 0, 0, 0.1))
    # axis.add_artist(region)


def plot_2d_nbr_omega_res_max(axis):

    domain = np.array([np.linspace(0, 6, 61), np.linspace(0, 6, 61), np.linspace(0, 6, 61), np.linspace(0, 6, 61),
                       np.linspace(0, 6, 61)], dtype=object)
    particles = [6, 7, 8, 8, 9]

    lbl_values = np.zeros(len(particles), dtype=object)
    number_of_peaks = np.zeros(len(particles), dtype=object)

    for N_idx, n_val in enumerate(particles):

        lbl = []
        number_of_peaks[N_idx] = []

        for j in domain[N_idx]:

            if n_val == 8 and N_idx == 2:
                file = f"fermions_torus_spec_resp_kysym_coulomb_n_{n_val:g}_2s_{3 * n_val:g}_ratio_1.000000_qx_0_qy_0" \
                       f".omega_{mid - std / (2 ** j):.6g}-{mid + std / (2 ** j):.6g}_eps_{0.0001 / (2 ** j):.6g}.sr.cut"
            else:
                file = f"fermions_torus_spec_resp_kysym_coulomb_n_{n_val:g}_2s_{3 * n_val:g}_ratio_1.000000_qy_0" \
                       f".omega_{mid - std / (2 ** j):.6g}-{mid + std / (2 ** j):.6g}_eps_{0.0001 / (2 ** j):.6g}.sr.cut"

            # get ground state energy (from dat file)
            energies = []
            dat_file = f"fermions_torus_kysym_coulomb_n_{n_val:g}_2s_{3 * n_val:g}_ratio_1.000000.dat"
            with open(vectors + f'coulomb/n_{n_val:g}/' + dat_file, 'r') as csvfile:
                data = csv.reader(csvfile, delimiter=' ')
                for row in data:
                    if row[0].isnumeric():
                        energies.append(float(row[1]))
                ground = min(energies)

            omega = []
            SR = []
            with open(stripped_files + file, 'r') as csvfile:
                plots = csv.reader(csvfile, delimiter=' ')
                for row in plots:
                    if mid - std / (2 ** j) < float(row[0]) < mid + std / (2 ** j):
                        omega.append(float(row[0])+10-ground)
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

    for N_idx, n_val in enumerate(particles):
        if N_idx == 2:
            alpha_val = 0.5
        else:
            alpha_val = 1
        axis.plot(lbl_values[N_idx], number_of_peaks[N_idx], '.', markersize=4, c=f'C{n_val-particles[0]}', alpha=alpha_val)

    axis.tick_params('x', direction='in', bottom=True)
    plt.setp(axis.get_xticklabels(), visible=False)
    axis.set_ylabel('$n(I_\mathrm{max})$')

    # region = Polygon(((-6, -100), (-4.1, -100), (-4.1, 100), (-6, 100)), fc=(0, 0, 0, 0.1))
    # axis.add_artist(region)


def plot_2d_mean_S_res_max(axis):

    domain = np.array([np.linspace(0, 6, 61), np.linspace(0, 6, 61), np.linspace(0, 6, 61), np.linspace(0, 6, 61),
                       np.linspace(0, 6, 61)], dtype=object)
    particles = [6, 7, 8, 8, 9]

    lbl_values = np.zeros(len(particles), dtype=object)
    S_max_bar = np.zeros(len(particles), dtype=object)

    for N_idx, n_val in enumerate(particles):

        lbl = []
        S_max_bar[N_idx] = []

        for j in domain[N_idx]:

            if n_val == 8 and N_idx == 2:
                file = f"fermions_torus_spec_resp_kysym_coulomb_n_{n_val:g}_2s_{3 * n_val:g}_ratio_1.000000_qx_0_qy_0" \
                       f".omega_{mid - std / (2 ** j):.6g}-{mid + std / (2 ** j):.6g}_eps_{0.0001 / (2 ** j):.6g}.sr.cut"
            else:
                file = f"fermions_torus_spec_resp_kysym_coulomb_n_{n_val:g}_2s_{3 * n_val:g}_ratio_1.000000_qy_0" \
                       f".omega_{mid - std / (2 ** j):.6g}-{mid + std / (2 ** j):.6g}_eps_{0.0001 / (2 ** j):.6g}.sr.cut"

            # get ground state energy (from dat file)
            energies = []
            dat_file = f"fermions_torus_kysym_coulomb_n_{n_val:g}_2s_{3 * n_val:g}_ratio_1.000000.dat"
            with open(vectors + f'coulomb/n_{n_val:g}/' + dat_file, 'r') as csvfile:
                data = csv.reader(csvfile, delimiter=' ')
                for row in data:
                    if row[0].isnumeric():
                        energies.append(float(row[1]))
                ground = min(energies)

            omega = []
            SR = []
            with open(stripped_files + file, 'r') as csvfile:
                plots = csv.reader(csvfile, delimiter=' ')
                for row in plots:
                    if mid - std / (2 ** j) < float(row[0]) < mid + std / (2 ** j):
                        omega.append(float(row[0])+10-ground)
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

    for N_idx, n_val in enumerate(particles):
        if N_idx == 2:
            alpha_val = 0.5
        else:
            alpha_val = 1
        axis.plot(lbl_values[N_idx], S_max_bar[N_idx], '.', markersize=4, c=f'C{n_val-particles[0]}', alpha=alpha_val)

    axis.set_xlabel('$\log_2(\mathrm{range}(\omega)/\mathrm{range}(\omega_\mathrm{init}))$', labelpad=10)
    axis.xaxis.set_major_formatter(FormatStrFormatter('$%g$'))
    axis.set_ylabel('$\mu_{I_\mathrm{max}}\epsilon$')

    custom_lines = [Line2D([0], [0], color='C0', lw=4),
                    Line2D([0], [0], color='C1', lw=4),
                    Line2D([0], [0], color='C2', lw=4),
                    Line2D([0], [0], color='C3', lw=4)]
    axis.legend(custom_lines, ['$6$', '$7$', '$8$', '$9$'], bbox_to_anchor=(0.815, 5.6), ncol=4, title="$N$")

    # region = Polygon(((-6, -100), (-4.1, -100), (-4.1, 100), (-6, 100)), fc=(0, 0, 0, 0.1))
    # axis.add_artist(region)


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

    plt.savefig("coulomb_scaling_complete_n_9_3.png", bbox_inches='tight', dpi=300)
    plt.show()
