import numpy as np
from scipy.special import factorial, factorial2
import operator as op
from functools import reduce


def ncr(n, r):
    r = min(r, n-r)
    numer = reduce(op.mul, range(n, n-r, -1), 1)
    denom = reduce(op.mul, range(1, r+1), 1)
    return numer // denom


def pseudopotential(R_val, Q_val, L_val):

    V = (2/R_val) * (ncr(4*Q_val-2*L_val, 2*Q_val-L_val)
                     * ncr(4*Q_val+2*L_val+2, 2*Q_val+L_val+1)) / (ncr(4*Q_val+2, 2*Q_val+1)**2)

    return V


if __name__ == "__main__":

    # LLL on a sphere, Jain book Eq. 3.224

    R = 1  # np.sqrt(2 / (2/3))
    Q = 9

    file = open("pseudopotentials_CoulombSphere.dat", "w")

    file.write("Name = CoulombSphere\n")
    file.write("Pseudopotentials = ")

    for m in range(20):
        print(m, pseudopotential(R, Q, m))
        file.write(f"{pseudopotential(R, Q, m)} ")

    file.close()
