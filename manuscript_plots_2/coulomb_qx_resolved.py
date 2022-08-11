import csv
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
import matplotlib.ticker as ticker

plt.rc('text', usetex=True)
plt.rc('text.latex', preamble=r'\usepackage{amsmath}')

vectors = "/home/bart/PycharmProjects/response_functions/vectors_2/"
stripped_files = "/home/bart/PycharmProjects/response_functions/FQHETorusSpectralResponse_2/stripped_files/"


def plot_2d_qx_resolved_full_box(axis, numb_qy, omega_min, omega_max):

    data_to_plot = []
    qx_list = []

    for qx in range(numb_qy):
        qx_list += [qx]
        omega = []
        SR = []
        file = f"fermions_torus_spec_resp_kysym_coulomb_n_{numb_qy/3:g}_2s_{numb_qy:g}_ratio_1.000000_qy_{qx}" \
               f".omega_{omega_min:g}-{omega_max:g}_eps_0.0001.sr.cut"

        # # get ground state energy (from dat file)
        # energies = []
        # dat_file = f"fermions_torus_kysym_coulomb_n_{numb_qy/3:g}_2s_{numb_qy:g}_ratio_1.000000.dat"
        # with open(vectors + f'coulomb/n_{numb_qy/3:g}/' + dat_file, 'r') as csvfile:
        #     data = csv.reader(csvfile, delimiter=' ')
        #     for row in data:
        #         if row[0].isnumeric():
        #             energies.append(float(row[1]))
        #     ground = min(energies)

        with open(stripped_files + file, 'r') as csvfile:
            plots = csv.reader(csvfile, delimiter=' ')
            for row in plots:
                omega.append(float(row[0])+10)
                SR.append(float(row[1]))
            data_to_plot += [omega]

    print(np.shape(qx_list), np.shape(data_to_plot))

    props_intern = dict(markerfacecolor='b', marker='x', markersize=0.1)
    bp_dict = axis.boxplot(data_to_plot, positions=qx_list, flierprops=props_intern, whiskerprops={"linewidth": 0.5}, boxprops={"linewidth": 0.5}, capprops={"linewidth": 0.5}, medianprops={"linewidth": 0.5}, widths=1)

    # print(bp_dict['medians'][0].get_ydata()[0])
    # print([item.get_ydata() for item in bp_dict['medians']])
    #
    axis.set_xlabel('$q_x$')
    # axis.set_xlim([2, 40])  # 100
    axis.set_ylabel('$\omega$')
    #
    pos = np.arange(0, 24, 4)  # 100.1, 20
    posy = np.arange(0, 24, 4)  # 100.1, 20
    axis.set(xticks=pos, xticklabels=posy)
    axis.xaxis.set_major_formatter(ticker.FormatStrFormatter('$%g$'))
    axis.yaxis.set_major_formatter(ticker.FormatStrFormatter('$%g$'))


if __name__ == "__main__":

    fig = plt.figure(figsize=(6, 2))
    gs = gridspec.GridSpec(1, 2, hspace=0.4, wspace=0.4)

    ax0 = plt.subplot(gs[0])
    plot_2d_qx_resolved_full_box(ax0, 18, omega_min=-100, omega_max=100)
    # ax1 = plt.subplot(gs[1])
    # plot_2d_cpt_variable_full_box(ax1, 0.01, 18, omega_min=-20, omega_max=0)

    # fig.text(0.04, 0.88, "(a)", fontsize=12)
    # fig.text(0.5, 0.88, "(b)", fontsize=12)

    # props = dict(boxstyle='round', facecolor='white', alpha=1)
    # ax0.text(0.65, 0.85, "$\lambda=10^{-3}$", fontsize=11, transform=ax0.transAxes, bbox=props)
    # ax1.text(0.65, 0.85, "$\lambda=10^{-2}$", fontsize=11, transform=ax1.transAxes, bbox=props)

    plt.savefig("coulomb_qx_resolved.png", bbox_inches='tight', dpi=300)
    plt.show()
