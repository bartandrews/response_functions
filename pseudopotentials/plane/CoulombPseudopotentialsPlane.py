import numpy as np
from scipy.special import factorial, factorial2


def pseudopotential(m_val):

    V = (np.sqrt(np.pi)/2) * factorial2(2*m_val-1)/(2**m_val * factorial(m_val))

    return V


if __name__ == "__main__":

    file = open("pseudopotentials_CoulombPlane.dat", "w")

    file.write("Name = CoulombPlane\n")
    file.write("Pseudopotentials = ")

    for m in range(100):
        print(m, pseudopotential(m))
        file.write(f"{pseudopotential(m)} ")

    file.close()
