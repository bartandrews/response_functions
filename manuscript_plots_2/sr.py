import csv
import itertools
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
from matplotlib.ticker import FormatStrFormatter


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
                          edgecolor=None, markerscale=5, ncol=10, labelspacing=0, columnspacing=0, bbox_to_anchor=(2.2, 1.4), title='$q_y$')
        leg.get_frame().set_linewidth(0.5)


if __name__ == "__main__":

    fig = plt.figure(figsize=(6, 2.5))
    gs = gridspec.GridSpec(1, 2, hspace=0.4, wspace=0.4)

    ax0 = plt.subplot(gs[0])
    plot_2d_q(ax0, "V1", 18, omega_min=-100, omega_max=100)
    # ax1 = plt.subplot(gs[1])
    # plot_2d_q(ax1, "coulomb", 24, omega_min=-100, omega_max=100)

    fig.text(0.04, 0.85, "(a)", fontsize=12)
    fig.text(0.49, 0.85, "(b)", fontsize=12)

    fig.text(0.405, 0.8, "$V_1$", fontsize=11)
    fig.text(0.79, 0.8, "Coulomb", fontsize=11)

    # plt.savefig("sr.png", bbox_inches='tight', dpi=300)
    plt.show()
