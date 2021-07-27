# import numpy as np
# from scipy.special import gamma, hyperu
from mpmath import sqrt, pi, gamma, hyperu


def pseudopotential(m_val, lamb_val):

    V = (lamb_val/(2*sqrt(pi))) * gamma(m_val + 1/2) * hyperu(m_val+1, 3/2, lamb_val*lamb_val)

    return V


if __name__ == "__main__":

    lamb = 100

    file = open(f"pseudopotentials_YukawaPlaneL{lamb}.dat", "w")

    file.write(f"Name = YukawaPlaneL{lamb}\n")
    file.write("Pseudopotentials = ")

    for m in range(100):
        print(m, pseudopotential(m, lamb))
        file.write(f"{pseudopotential(m, lamb)} ")

    file.close()
