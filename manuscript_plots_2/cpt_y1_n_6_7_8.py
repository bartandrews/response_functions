import csv
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
import matplotlib.ticker as ticker
from matplotlib.transforms import Bbox
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.ticker import FormatStrFormatter

plt.rc('text', usetex=True)
plt.rc('text.latex', preamble=r'\usepackage{amsmath}')

vectors = "/home/bart/PycharmProjects/response_functions/vectors_2/"
stripped_files = "/home/bart/PycharmProjects/response_functions/FQHETorusSpectralResponse_2/stripped_files/"


def plot_3d_cpt_variable_full(axis, numb_qy, omega_min, omega_max):

    omega = []
    SR = []
    name_list = []
    lbl = []

    if axis == ax0:
        for i in range(2, 8+6, 2):
            name_list += [f"coulomb_0_plus_YukawaPlaneL0.1_trunc_{i}"]
    elif axis == ax2:
        for i in range(2, 10+6, 2):
            name_list += [f"coulomb_0_plus_YukawaPlaneL0.1_trunc_{i}"]
    elif axis == ax4:
        for i in range(2, 12+6, 2):
            name_list += [f"coulomb_0_plus_YukawaPlaneL0.1_trunc_{i}"]

    for i, name in enumerate(name_list):
        file = f"fermions_torus_spec_resp_kysym_{name}_n_{numb_qy/3:g}_2s_{numb_qy:g}_ratio_1.000000_qy_0" \
               f".omega_{omega_min:g}-{omega_max:g}_eps_0.0001.sr.cut"

        # get ground state energy (from dat file)
        energies = []
        dir_name = f"n_{numb_qy/3:g}/l0.1" if numb_qy == 18 else f"n_{numb_qy/3:g}_lambda_0.1"
        dat_file = f"fermions_torus_kysym_{name}_n_{numb_qy/3:g}_2s_{numb_qy:g}_ratio_1.000000.dat"
        with open(vectors + f'ypt/{dir_name}/' + dat_file, 'r') as csvfile:
            data = csv.reader(csvfile, delimiter=' ')
            for row in data:
                if row[0].isnumeric():
                    energies.append(float(row[1]))
            ground = min(energies)

        with open(stripped_files + file, 'r') as csvfile:
            data = csv.reader(csvfile, delimiter=' ')
            for row in data:
                omega.append(float(row[0])+10-ground)
                SR.append(float(row[1])/1000)
                lbl += [2*i+1]

    axis.scatter(lbl, omega, SR, s=0.1, c=lbl, cmap='brg')

    axis.set_xlabel('$\\beta$')
    axis.xaxis.set_major_formatter(FormatStrFormatter('$%g$'))
    if axis == ax0:
        axis.set_xticks(np.arange(1, 8+4, 2))
    elif axis == ax2:
        axis.set_xticks(np.arange(1, 10+4, 2))
    elif axis == ax4:
        axis.set_xticks(np.arange(1, 12+4, 2))
    axis.yaxis.set_major_formatter(FormatStrFormatter('$%g$'))
    axis.set_ylabel('$\\omega-\omega_0$')
    axis.zaxis.set_major_formatter(FormatStrFormatter('$%g$'))
    axis.set_zlabel('$I/10^3$')
    axis.set_facecolor((0, 0, 0, 0))
    if axis == ax0:  # N=6
        axis.set_position(Bbox.from_bounds(0, 0.64, 0.44, 0.28))
    elif axis == ax2:  # N=7
        axis.set_position(Bbox.from_bounds(0, 0.35, 0.44, 0.28))
    elif axis == ax4:  # N=8
        axis.set_position(Bbox.from_bounds(0, 0.07, 0.44, 0.28))
    axis.tick_params(axis='both', which='major', pad=0)
    axis.xaxis.labelpad = 0
    axis.yaxis.labelpad = 0
    axis.zaxis.labelpad = 0

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


def plot_2d_cpt_variable_full_box(axis, numb_qy, omega_min, omega_max):

    name_list = []
    lbl = []
    data_to_plot = []

    for i in range(2, int(numb_qy/2)+6, 2):  # 40
        name_list += [f"coulomb_0_plus_YukawaPlaneL0.1_trunc_{i}"]
        lbl += [i-1]

    for i, name in enumerate(name_list):
        omega = []
        SR = []
        file = f"fermions_torus_spec_resp_kysym_{name}_n_{numb_qy/3:g}_2s_{numb_qy:g}_ratio_1.000000_qy_0" \
               f".omega_{omega_min:g}-{omega_max:g}_eps_0.0001.sr.cut"

        # get ground state energy (from dat file)
        energies = []
        dir_name = f"n_{numb_qy / 3:g}/l0.1" if numb_qy == 18 else f"n_{numb_qy / 3:g}_lambda_0.1"
        dat_file = f"fermions_torus_kysym_{name}_n_{numb_qy / 3:g}_2s_{numb_qy:g}_ratio_1.000000.dat"
        with open(vectors + f'ypt/{dir_name}/' + dat_file, 'r') as csvfile:
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

    props = dict(markerfacecolor='b', marker='x', markersize=5, markeredgewidth=0.01)
    bp_dict = axis.boxplot(data_to_plot, positions=lbl, flierprops=props, whiskerprops={"linewidth": 0.5}, boxprops={"linewidth": 0.5}, capprops={"linewidth": 0.5}, medianprops={"linewidth": 0.5}, widths=1)

    print(bp_dict['medians'][0].get_ydata()[0])
    print([item.get_ydata() for item in bp_dict['medians']])

    axis.set_xlabel('$\\beta$')
    if axis == ax1:
        axis.set_xlim([0, 8+4])
    elif axis == ax3:
        axis.set_xlim([0, 10+4])
    elif axis == ax5:
        axis.set_xlim([0, 12+4])
    axis.set_ylabel('$\omega-\omega_0$')

    if axis == ax1:  # N=6
        axis.axhline(0.6871294212729, c='r', ls='--', zorder=-10, lw=1)
        axis.axhspan(0.5519419212778998, 0.8634669212659001, alpha=0.1, color='red')
    elif axis == ax3:  # N=7
        axis.axhline(0.8657296828534005, c='r', ls='--', zorder=-10, lw=1)
        axis.axhspan(0.7107321828593998, 1.0466871828474007, alpha=0.1, color='red')
    elif axis == ax5:  # N=8
        axis.axhline(1.0395240344364, c='r', ls='--', zorder=-10, lw=1)
        axis.axhspan(0.8753165344434004, 1.2261315344294004, alpha=0.1, color='red')

    axis.xaxis.set_major_formatter(ticker.FormatStrFormatter('$%g$'))
    axis.yaxis.set_major_formatter(ticker.FormatStrFormatter('$%g$'))


if __name__ == "__main__":

    fig = plt.figure(figsize=(6, 7.5))
    gs = gridspec.GridSpec(3, 2, hspace=0.4, wspace=0.4)

    ax0 = plt.subplot(gs[0], projection='3d')
    plot_3d_cpt_variable_full(ax0, 18, omega_min=-20, omega_max=0)
    ax1 = plt.subplot(gs[1])
    plot_2d_cpt_variable_full_box(ax1, 18, omega_min=-20, omega_max=0)
    ax2 = plt.subplot(gs[2], projection='3d')
    plot_3d_cpt_variable_full(ax2, 21, omega_min=-20, omega_max=0)
    ax3 = plt.subplot(gs[3])
    plot_2d_cpt_variable_full_box(ax3, 21, omega_min=-20, omega_max=0)
    ax4 = plt.subplot(gs[4], projection='3d')
    plot_3d_cpt_variable_full(ax4, 24, omega_min=-20, omega_max=0)
    ax5 = plt.subplot(gs[5])
    plot_2d_cpt_variable_full_box(ax5, 24, omega_min=-20, omega_max=0)

    fig.text(0.02, 0.875, "(a)", fontsize=12)
    fig.text(0.2, 0.845, "$N=6$", fontsize=12)
    fig.text(0.49, 0.875, "(b)", fontsize=12)

    fig.text(0.02, 0.59, "(c)", fontsize=12)
    fig.text(0.2, 0.556, "$N=7$", fontsize=12)
    fig.text(0.49, 0.59, "(d)", fontsize=12)

    fig.text(0.02, 0.31, "(e)", fontsize=12)
    fig.text(0.2, 0.275, "$N=8$", fontsize=12)
    fig.text(0.49, 0.31, "(f)", fontsize=12)

    plt.savefig("cpt_y1_n_6_7_8.png", bbox_inches='tight', dpi=300)
    plt.show()
