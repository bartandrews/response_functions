# import numpy as np
# from scipy.special import gamma, hyperu
from mpmath import sqrt, pi, gamma, hyperu


def pseudopotential(m_val, lamb_val):

    V = (lamb_val/(2*sqrt(pi))) * gamma(m_val + 1/2) * hyperu(m_val+1, 3/2, lamb_val*lamb_val)

    return V


if __name__ == "__main__":

    lamb = 10

    for val in [1, 3, 5, 7, 9, 11, 13, 15, 17]:
        file = open(f"pseudopotentials_YukawaPlaneL{lamb}_V{val}_only.dat", "w")

        file.write(f"Name = YukawaPlaneL{lamb}_V{val}_only\n")
        file.write("Pseudopotentials = ")

        for m in range(100):
            if m == val:
                print(m, pseudopotential(m, lamb))
                file.write(f"{pseudopotential(m, lamb)} ")
                break
            else:
                print(m, 0)
                file.write("0 ")

        file.close()
