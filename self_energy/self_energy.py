import numpy as np
from scipy.integrate import quad


def integrand(t, n, z):
    return np.exp(-z*t) * t**n


def expint(n, z):
    return quad(integrand, 1, np.inf, args=(n, z))[0]


def self_energy_const(m_val):

    w = -4 * np.sqrt(2*np.pi / m_val)

    for l_max in range(100):
        for l1 in range(-l_max, l_max+1):
            for l2 in range(-l_max, l_max+1):
                l_mag = np.sqrt(l1**2 + l2**2)
                if l_max-1 < l_mag <= l_max:
                    if not l1 == l2 == 0:
                        w_new = w + 2 * np.sqrt(2*np.pi / m_val) * expint(-0.5, np.pi*(l1**2 + l2**2))
                        # print(l1, l2, abs(w - w_new))
                        if abs(w - w_new) < 1e-15:
                            return w_new
                        else:
                            w = w_new


if __name__ == "__main__":

    Ns = 36  # 2*np.pi to benchmark against Eq.2.17 of Bonsall & Maradudin
    print(f"W({Ns}) = {self_energy_const(Ns)}")
