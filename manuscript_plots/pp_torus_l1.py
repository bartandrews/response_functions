import numpy as np
import csv
import os
from heapq import nsmallest
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import matplotlib.gridspec as gridspec

plt.rc('text', usetex=True)
plt.rc('text.latex', preamble=r'\usepackage{amsmath}')

if __name__ == "__main__":

    directory = '/home/bart/KDevProjects/response_functions/vectors/pp_torus_l1'
    pp_file = 'pseudopotentials_YukawaPlaneL1.dat'

    idx_list = [i for i in range(9)]  # number of plots
    flux_limit = 60  # largest flux considered

    # construct pp_list
    with open(os.path.join(directory, pp_file), 'r') as csvfile:
        pp = csv.reader(csvfile, delimiter=' ')
        pp_list = []
        for i, row in enumerate(pp):
            if i > 0:
                for idx in idx_list:
                    pp_list.append(float(row[(2 * idx + 1) + 2]))

    # construct data
    data = []
    for idx in idx_list:
        for flux in range(6, flux_limit+1, 2):

            spec_file = f'fermions_torus_YukawaPlaneL1_V{2*idx+1}_only_n_2_2s_{flux}_ratio_1.000000.dat'

            with open(os.path.join(directory, spec_file), 'r') as csvfile:
                spec = csv.reader(csvfile, delimiter=' ')
                E_list = []
                for i, row in enumerate(spec):
                    if i > 0:
                        E_list.append(float(row[2]))

            absolute_difference_function = lambda list_value: abs(list_value - pp_list[idx])
            clos_vals = nsmallest(3, E_list, key=absolute_difference_function)
            data_line = [flux, pp_list[idx], clos_vals[0], clos_vals[1], clos_vals[2],
                         np.mean(clos_vals), np.std(clos_vals)]
            data.append(data_line)

    # construct plot_data
    plot_data = []
    for i in pp_list:
        for j in range(len(data)):
            if data[j][1] == i:
                plot_data.append([data[j][0], data[j][1], data[j][5], data[j][6]])

    print(plot_data)

    ####################################################################################################################

    fig = plt.figure(figsize=(6, 8))
    gs = gridspec.GridSpec(5, 2, hspace=1, wspace=0.5)

    red_points = []

    for idx in idx_list:

        ax = plt.subplot(gs[idx])

        l_values = [row[0] for row in plot_data if row[1] == pp_list[idx]]
        E_diff_values = [row[2]-row[1] for row in plot_data if row[1] == pp_list[idx]]
        E_std_values = [row[3] for row in plot_data if row[1] == pp_list[idx]]
        ax.errorbar(l_values, E_diff_values, E_std_values, label=f'$V_{{{2*idx+1}}}$', marker='x', markersize=5, capsize=3)
        ax.axhspan(-0.01*pp_list[idx], 0.01*pp_list[idx], alpha=0.5, color='slateblue')
        for i in range(len(l_values)):
            if E_diff_values[i]+E_std_values[i] < 0.01*pp_list[idx] and E_diff_values[i]-E_std_values[i] > -0.01*pp_list[idx]:
                ax.axvline(l_values[i], linestyle='--', c='r')
                red_points.append((2*idx+1, l_values[i]))
                break

        # leg = ax.legend(loc='upper center', handletextpad=0.5, handlelength=0, labelspacing=0.2, borderpad=0.35,
        #                  framealpha=1, edgecolor='k', markerscale=0.8, fontsize=10, ncol=8, columnspacing=1)
        # leg.get_frame().set_linewidth(0.5)

        ax.xaxis.set_major_formatter(ticker.FormatStrFormatter('$%g$'))
        ax.yaxis.set_major_formatter(ticker.FormatStrFormatter('$%g$'))
        ax.set_xlabel("$l$")
        ax.set_ylabel(f"$\\bar{{E}}_{{{2*idx+1}}}-V_{{{2*idx+1}}}$")
        ax.set_xticks(np.arange(6, flux_limit+1, 6))
        # ax.text(0.85, 0.62, f'$V_{{{2*idx+1}}}$', fontsize=11, transform=ax.transAxes)
        # ax.set_title(f'$V_{{{2*idx+1}}}$')

    ax = plt.subplot(gs[len(idx_list)])
    x_val = [x[0] for x in red_points]
    y_val = [x[1] for x in red_points]
    ax.plot(x_val, y_val, '.', c='r')
    ax.set_xlabel("$\\alpha$")
    ax.set_ylabel("$l_\\text{crit}$")

    print(red_points)
    plt.savefig("/home/bart/Documents/papers/SR/pp_torus_l1.png", bbox_inches='tight', dpi=300)
    plt.show()
