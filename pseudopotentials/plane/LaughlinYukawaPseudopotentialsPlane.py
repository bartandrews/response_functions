import numpy as np
# from scipy.special import gamma, hyperu
from mpmath import sqrt, pi, gamma, hyperu


def pseudopotential(m_val, lamb_val):

    V = (lamb_val/(2*sqrt(pi))) * gamma(m_val + 1/2) * hyperu(m_val+1, 3/2, lamb_val*lamb_val)

    return V


if __name__ == "__main__":

    lamb = 0.0001

    for Yukawa_exp in np.linspace(-4, 0, 41, endpoint=True):
        print(Yukawa_exp)
        file = open(f"pseudopotentials_V1_scale_{1-10**Yukawa_exp:.5g}_YukawaPlaneL{lamb}_scale_{10**Yukawa_exp:.5g}.dat", "w")

        file.write(f"Name = V1_scale_{1-10**Yukawa_exp:.5g}_YukawaPlaneL{lamb}_scale_{10**Yukawa_exp:.5g}\n")
        file.write("Pseudopotentials = ")

        for m in range(100):
            # print(m, pseudopotential(m, lamb))
            if m == 1:
                file.write(f"{1*(1-10**Yukawa_exp)+pseudopotential(m, lamb)*(10**Yukawa_exp)} ")
            else:
                file.write(f"{pseudopotential(m, lamb)*(10**Yukawa_exp)} ")

        file.close()
