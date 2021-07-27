from mpmath import sqrt, pi, gamma, hyperu, fac, fac2
import matplotlib.pyplot as plt
import numpy as np
import csv

plt.rc('text', usetex=True)
plt.rc('text.latex', preamble=r'\usepackage{amsmath}')


def coulomb(m_val):

    V = (sqrt(pi)/2) * fac2(2*m_val-1)/(2**m_val * fac(m_val))

    return V


def yukawa(m_val, lamb_val):

    V = (lamb_val/(2*sqrt(pi))) * gamma(m_val + 1/2) * hyperu(m_val+1, 3/2, lamb_val*lamb_val)

    return V


# define a list of easily-visible markers
markers = [(3, 0, 0), (4, 0, 0), (5, 0, 0), (6, 0, 0), (4, 1, 0), (5, 1, 0), (6, 1, 0),
           (3, 2, 0), (4, 2, 0), (5, 2, 0), (6, 2, 0), 'X', 'x', 'd', 'D', 'P',
           '$a$', '$b$', '$c$', '$d$', '$e$', '$f$', '$g$', '$h$', '$i$', '$j$', '$k$', '$l$', '$m$', '$n$', '$o$',
           '$p$', '$q$', '$r$', '$s$', '$t$', '$u$', '$v$', '$w$', '$x$', '$y$', '$z$']


if __name__ == "__main__":

    fig = plt.figure(figsize=(6, 2.5))
    ax = plt.subplot(111)

    pp = np.zeros((100, 8))

    for m in range(100):
        pp[m, 0] = coulomb(m)
        pp[m, 1] = yukawa(m, 0.0001)
        pp[m, 2] = yukawa(m, 0.001)
        pp[m, 3] = yukawa(m, 0.01)
        pp[m, 4] = yukawa(m, 0.1)
        pp[m, 5] = yukawa(m, 1)
        pp[m, 6] = yukawa(m, 10)
        pp[m, 7] = yukawa(m, 100)

    reduced_marker_size = 3

    mvals = range(100)
    ax.plot(mvals, pp[:, 0], 'o-', label='Coulomb', zorder=8, fillstyle='none')
    ax.plot(mvals, pp[:, 1], marker=markers[1], label='Yukawa ($\lambda=10^{-4}$)', zorder=7, markersize=reduced_marker_size)
    ax.plot(mvals, pp[:, 2], marker=markers[2], label='Yukawa ($\lambda=10^{-3}$)', zorder=6, markersize=reduced_marker_size)
    ax.plot(mvals, pp[:, 3], marker=markers[3], label='Yukawa ($\lambda=10^{-2}$)', zorder=5, markersize=reduced_marker_size)
    ax.plot(mvals, pp[:, 4], marker=markers[4], label='Yukawa ($\lambda=10^{-1}$)', zorder=4, markersize=reduced_marker_size)
    ax.plot(mvals, pp[:, 5], marker=markers[5], label='Yukawa ($\lambda=1$)', zorder=3, markersize=reduced_marker_size)
    ax.plot(mvals, pp[:, 6], marker=markers[6], label='Yukawa ($\lambda=10$)', zorder=2, markersize=reduced_marker_size)
    ax.plot(mvals, pp[:, 7], marker=markers[7], label='Yukawa ($\lambda=10^2$)', zorder=1, markersize=reduced_marker_size)
    ax.set_xlabel('$\\alpha$', fontsize=11)
    ax.set_ylabel('$V^{(0)}_{\\alpha}$', fontsize=11)

    ax.legend(loc='upper right', handletextpad=0, borderpad=0.4, framealpha=1,
              edgecolor='w', markerscale=1,
              fontsize=10, ncol=1, labelspacing=0, columnspacing=0)

    plt.savefig("/home/bart/Documents/papers/SR/pp.png", bbox_inches='tight', dpi=300)
    plt.show()
