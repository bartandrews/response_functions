from mpmath import sqrt, pi, gamma, hyperu, fac, fac2
import matplotlib.pyplot as plt
import numpy as np
import csv


def coulomb(m_val):

    V = (sqrt(pi)/2) * fac2(2*m_val-1)/(2**m_val * fac(m_val))

    return V


def yukawa(m_val, lamb_val):

    V = (lamb_val/(2*sqrt(pi))) * gamma(m_val + 1/2) * hyperu(m_val+1, 3/2, lamb_val*lamb_val)

    return V


if __name__ == "__main__":

    for i in range(18):
        print(i, coulomb(i))

    # file = open(f"pseudopotentials_Plane.dat", "w")
    #
    # for m in range(100):
    #     print(m, coulomb(m), yukawa(m, 0.0001), yukawa(m, 0.001), yukawa(m, 0.01), yukawa(m, 0.1), yukawa(m, 1), yukawa(m, 10))
    #     file.write(f"{m}\t{coulomb(m)}\t{yukawa(m, 0.0001)}\t{yukawa(m, 0.001)}\t{yukawa(m, 0.01)}\t{yukawa(m, 0.1)}\t{yukawa(m, 1)}\t{yukawa(m, 10)}\n")
    #
    # file.close()

    ####################################################################################################################

    # fig = plt.figure()
    # ax = plt.subplot(111)
    #
    # pp = np.zeros((100, 7))
    #
    # for m in range(100):
    #     pp[m, 0] = coulomb(m)
    #     pp[m, 1] = yukawa(m, 0.0001)
    #     pp[m, 2] = yukawa(m, 0.001)
    #     pp[m, 3] = yukawa(m, 0.01)
    #     pp[m, 4] = yukawa(m, 0.1)
    #     pp[m, 5] = yukawa(m, 1)
    #     pp[m, 6] = yukawa(m, 10)
    #
    # mvals = range(100)
    # ax.plot(mvals, pp[:, 0], '.', label='coulomb')
    # ax.plot(mvals, pp[:, 1], label='yukawa($10^{-4}$)')
    # ax.plot(mvals, pp[:, 2], label='yukawa($10^{-3}$)')
    # ax.plot(mvals, pp[:, 3], label='yukawa($10^{-2}$)')
    # ax.plot(mvals, pp[:, 4], label='yukawa($10^{-1}$)')
    # ax.plot(mvals, pp[:, 5], label='yukawa($1$)')
    # ax.plot(mvals, pp[:, 6], label='yukawa($10$)')
    # ax.set_xlabel('$\\alpha$')
    # ax.set_ylabel('$V_{\\alpha}$')
    #
    # ax.legend(loc='upper right', handletextpad=0, borderpad=0.4, framealpha=1,
    #           edgecolor='k', markerscale=3,
    #           fontsize=10, ncol=1, labelspacing=0, columnspacing=0)
    #
    # plt.savefig("/home/bart/Documents/papers/SR/figures/pseudopotentials.png", bbox_inches='tight', dpi=300)
    # plt.show()

    ####################################################################################################################

    # fig = plt.figure()
    # ax = plt.subplot(111)
    #
    # gs = np.zeros((50, 8))
    #
    # filepath = '/home/bart/KDevProjects/response_functions/FQHETorusSpectralResponse/gs_energy_cpt.dat'
    #
    # with open(filepath, 'r') as csvfile:
    #     plots = csv.reader(csvfile, delimiter='\t')
    #     for i, row in enumerate(plots):
    #         for j in range(8):
    #             gs[i, j] = float(row[j])
    #
    # ax.plot(gs[:, 0], gs[:, 1], '.', label='coulomb')
    # ax.plot(gs[:, 0], gs[:, 2], label='yukawa($10^{-4}$)')
    # ax.plot(gs[:, 0], gs[:, 3], label='yukawa($10^{-3}$)')
    # ax.plot(gs[:, 0], gs[:, 4], label='yukawa($10^{-2}$)')
    # ax.plot(gs[:, 0], gs[:, 5], label='yukawa($10^{-1}$)')
    # ax.plot(gs[:, 0], gs[:, 6], label='yukawa($1$)')
    # ax.plot(gs[:, 0], gs[:, 7], label='yukawa($10$)')
    # ax.set_xlabel('$\\alpha$')
    # ax.set_ylabel('$E_0$')
    #
    # ax.legend(loc='upper left', handletextpad=0, borderpad=0.4, framealpha=1,
    #           edgecolor='k', markerscale=3,
    #           fontsize=10, ncol=1, labelspacing=0, columnspacing=0)
    #
    # plt.savefig("/home/bart/Documents/papers/SR/figures/pseudopotentials_gs_cpt.png", bbox_inches='tight', dpi=300)
    # plt.show()

    ####################################################################################################################

    # fig = plt.figure()
    # ax = plt.subplot(111)
    #
    # filepath = '/home/bart/KDevProjects/response_functions/FQHETorusSpectralResponse/gs_energy_ltc.dat'
    #
    # alpha = []
    # gs = []
    #
    # with open(filepath, 'r') as csvfile:
    #     plots = csv.reader(csvfile, delimiter='\t')
    #     for i, row in enumerate(plots):
    #         alpha.append(float(row[0]))
    #         gs.append(float(row[1]))
    #
    # ax.plot(alpha, gs, '.')
    # ax.set_xlabel('$\\alpha$')
    # ax.set_xscale('log')
    # ax.set_ylabel('$E_0$')
    #
    # plt.savefig("/home/bart/Documents/papers/SR/figures/pseudopotentials_gs_ltc.png", bbox_inches='tight', dpi=300)
    # plt.show()
