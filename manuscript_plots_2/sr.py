import csv
import itertools
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
from matplotlib.ticker import FormatStrFormatter


plt.rc('text', usetex=True)
plt.rc('text.latex', preamble=r'\usepackage{amsmath}')


def plot_2d_q(axis, name, numb_qy, omega_min, omega_max):

    marker = itertools.cycle(('1', '2', '3', '4', ',', '+', '.', 'o', '*', '^', 'v', '>', '<', 'X', '_', 'd', '|', 'H'))

    for qy_value in range(numb_qy):
        omega = []
        SR = []
        file = f"fermions_torus_spec_resp_kysym_{name}_n_6_2s_{numb_qy}_ratio_1.000000_qy_{qy_value}" \
               f".omega_{omega_min}-{omega_max}_eps_0.0001.sr.cut"
        with open('/home/bart/PycharmProjects/response_functions/FQHETorusSpectralResponse_2/stripped_files/' + file, 'r') as csvfile:
            plots = csv.reader(csvfile, delimiter=' ')
            for row in plots:
                # if float(row[0])+10 > -0.015:
                #     if name == "V1" and float(row[0])+10 > 0.015:
                #         continue
                #     omega.append(float(row[0])+10)
                if name == "V1":
                    omega.append((float(row[0])+10) + 1.371144)
                elif name == "coulomb":
                    omega.append((float(row[0])+10) + 1.371144)
                SR.append(float(row[1])/100)
        axis.scatter(omega, SR, s=1, label=qy_value, marker=next(marker))

        # if name == 'coulomb' and qy_value == 0:
        #     print("lower quartile = ", np.percentile(omega, 25))
        #     print("median = ", np.median(omega))
        #     print("upper quartile = ", np.percentile(omega, 75))

    axis.set_xlabel('$\omega$')
    axis.xaxis.set_major_formatter(FormatStrFormatter('$%g$'))
    axis.yaxis.set_major_formatter(FormatStrFormatter('$%g$'))
    axis.set_ylabel('$I/10^2$')
    axis.set_ylim(bottom=0)
    # if name == "V1":
    #     axis.set_xlim([-0.015, 0.015])

    if name == "V1":
        leg = axis.legend(loc='upper right', handletextpad=0, borderpad=0.2, framealpha=1,
                          edgecolor=None, markerscale=5, ncol=10, labelspacing=0, columnspacing=0, bbox_to_anchor=(2.2, 1.4), title='$q_y$')
        leg.get_frame().set_linewidth(0.5)


if __name__ == "__main__":

    fig = plt.figure(figsize=(6, 2.5))
    gs = gridspec.GridSpec(1, 2, hspace=0.4, wspace=0.4)

    ax0 = plt.subplot(gs[0])
    plot_2d_q(ax0, "V1", 18, omega_min=-100, omega_max=100)
    ax1 = plt.subplot(gs[1])
    plot_2d_q(ax1, "coulomb", 18, omega_min=-100, omega_max=100)

    fig.text(0.02, 0.85, "(a)", fontsize=12)
    fig.text(0.47, 0.85, "(b)", fontsize=12)

    fig.text(0.405, 0.8, "$V_1$", fontsize=11)
    fig.text(0.79, 0.8, "Coulomb", fontsize=11)

    plt.savefig("sr.png", bbox_inches='tight', dpi=300)
    plt.show()
