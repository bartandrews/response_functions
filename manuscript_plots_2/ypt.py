import csv
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
import matplotlib.ticker as ticker

plt.rc('text', usetex=True)
plt.rc('text.latex', preamble=r'\usepackage{amsmath}')

vectors = "/home/bart/PycharmProjects/response_functions/vectors_2/"
stripped_files = "/home/bart/PycharmProjects/response_functions/FQHETorusSpectralResponse_2/stripped_files/"


def plot_2d_cpt_variable_full_box(axis, lamb, numb_qy, omega_min, omega_max):

    name_list = []
    lbl = []
    data_to_plot = []

    for i in range(2, 50, 2):  # 2, 100, 2
        name_list += [f"coulomb_0_plus_YukawaPlaneL{lamb:g}_trunc_{i}"]
        lbl += [i]
    # name_list += [f"coulomb_0_plus_YukawaPlaneL{lamb:g}"]
    # lbl += [100]

    lbl = [i-1 for i in lbl]

    for i, name in enumerate(name_list):
        omega = []
        SR = []
        file = f"fermions_torus_spec_resp_kysym_{name}_n_{numb_qy/3:g}_2s_{numb_qy:g}_ratio_1.000000_qy_0" \
               f".omega_{omega_min:g}-{omega_max:g}_eps_0.0001.sr.cut"

        # get ground state energy (from dat file)
        energies = []
        dat_file = f"fermions_torus_kysym_{name}_n_{numb_qy/3:g}_2s_{numb_qy:g}_ratio_1.000000.dat"
        with open(vectors + f'ypt/n_{numb_qy/3:g}/l{lamb:g}/' + dat_file, 'r') as csvfile:
            data = csv.reader(csvfile, delimiter=' ')
            for row in data:
                if row[0].isnumeric():
                    energies.append(float(row[1]))
            ground = min(energies)

        with open(stripped_files + file, 'r') as csvfile:
            plots = csv.reader(csvfile, delimiter=' ')
            for row in plots:
                omega.append(float(row[0])+10-ground)
                SR.append(float(row[1]))
            data_to_plot += [omega]

    props_intern = dict(markerfacecolor='b', marker='x', markersize=0.1)
    bp_dict = axis.boxplot(data_to_plot, positions=lbl, flierprops=props_intern, whiskerprops={"linewidth": 0.5}, boxprops={"linewidth": 0.5}, capprops={"linewidth": 0.5}, medianprops={"linewidth": 0.5}, widths=1)

    print(bp_dict['medians'][0].get_ydata()[0])
    print([item.get_ydata() for item in bp_dict['medians']])

    axis.set_xlabel('$\\beta$')
    axis.set_xlim([2, 40])  # 100
    axis.set_ylabel('$\omega-\omega_0$')

    # if lamb == 0.001:
    #     x = np.linspace(2, 100, 256)
    #     axis.plot(x, np.sqrt(x)/(2**(-1.25 + 0.25*np.cos(2*x*np.pi))*np.pi**(0.5*np.sin(np.pi*x)**2)), label="asymptotic behaviour of $1/V_m^{(0)}$", lw=0.5, zorder=5, c='g')
    #
    if lamb in [0.001, 0.01, 0.1]:
        axis.axhline(0.6871294212729, c='r', ls='--', zorder=-10, lw=1)
        axis.axhspan(0.5519419212778998, 0.8634669212659001, alpha=0.1, color='r')
    #
    # if lamb == 100:
    #     axis.axhline(0.00002, c='b', ls='--', zorder=-10, lw=1)
    #     axis.axhspan(-0.0075, 0.0075, alpha=0.1, color='b')

    pos = np.arange(0, 40.1, 10)  # 100.1, 20
    posy = np.arange(0, 40.1, 10)  # 100.1, 20
    axis.set(xticks=pos, xticklabels=posy)
    axis.xaxis.set_major_formatter(ticker.FormatStrFormatter('$%g$'))
    axis.yaxis.set_major_formatter(ticker.FormatStrFormatter('$%g$'))


if __name__ == "__main__":

    fig = plt.figure(figsize=(6, 7))
    gs = gridspec.GridSpec(3, 2, hspace=0.4, wspace=0.4)

    ax0 = plt.subplot(gs[0])
    plot_2d_cpt_variable_full_box(ax0, 0.001, 18, omega_min=-20, omega_max=0)
    ax1 = plt.subplot(gs[1])
    plot_2d_cpt_variable_full_box(ax1, 0.01, 18, omega_min=-20, omega_max=0)
    ax2 = plt.subplot(gs[2])
    plot_2d_cpt_variable_full_box(ax2, 0.1, 18, omega_min=-20, omega_max=0)
    ax3 = plt.subplot(gs[3])
    plot_2d_cpt_variable_full_box(ax3, 1, 18, omega_min=-20, omega_max=0)
    ax4 = plt.subplot(gs[4])
    plot_2d_cpt_variable_full_box(ax4, 10, 18, omega_min=-20, omega_max=0)
    ax5 = plt.subplot(gs[5])
    plot_2d_cpt_variable_full_box(ax5, 100, 18, omega_min=-20, omega_max=0)

    fig.text(0.04, 0.88, "(a)", fontsize=12)
    fig.text(0.5, 0.88, "(b)", fontsize=12)
    fig.text(0.04, 0.595, "(c)", fontsize=12)
    fig.text(0.5, 0.595, "(d)", fontsize=12)
    fig.text(0.04, 0.31, "(e)", fontsize=12)
    fig.text(0.5, 0.31, "(f)", fontsize=12)

    props = dict(boxstyle='round', facecolor='white', alpha=1)
    ax0.text(0.65, 0.85, "$\lambda=10^{-3}$", fontsize=11, transform=ax0.transAxes, bbox=props)
    ax1.text(0.65, 0.85, "$\lambda=10^{-2}$", fontsize=11, transform=ax1.transAxes, bbox=props)
    ax2.text(0.65, 0.85, "$\lambda=10^{-1}$", fontsize=11, transform=ax2.transAxes, bbox=props)
    ax3.text(0.77, 0.85, "$\lambda=1$", fontsize=11, transform=ax3.transAxes, bbox=props)
    ax4.text(0.73, 0.85, "$\lambda=10$", fontsize=11, transform=ax4.transAxes, bbox=props)
    ax5.text(0.69, 0.85, "$\lambda=100$", fontsize=11, transform=ax5.transAxes, bbox=props)

    plt.savefig("ypt.png", bbox_inches='tight', dpi=300)
    plt.show()
