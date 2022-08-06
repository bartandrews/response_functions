import csv
import numpy as np


def gs_ky_val(file_name):
    ky, energy = [], []
    with open(file_name, 'r') as csvfile:
        data = csv.reader(csvfile, delimiter=' ')
        for row in data:
            if row[0].isnumeric():
                ky.append(float(row[0]))
                energy.append(float(row[1]))

    return int(ky[np.argmin(energy)])


if __name__ == "__main__":

    SpectralResponse = "~/DiagHam_latest/build/FQHE/src/Programs/FQHEOnTorus/FQHETorusSpectralResponse"
    response_functions = "/home/bart/PycharmProjects/response_functions"
    # response_functions = "/disk/data11/tfp/BartMadhav/project3.5"

    file = open(f"ypt_sr_script.sh", "w")
    file.write("#!/bin/bash\n\n")

    file.write("runs() {\n")
    for n_val in [7]:
        for lamb_exp in [-1]:  # -3, -2, -1, 0, 1, 2
            lamb = 10 ** lamb_exp
            for trunc in range(2, 16, 2):  # 102
                if trunc != 100:
                    dat_file = f"{response_functions}/vectors_2/ypt/n_{n_val:g}_lambda_{lamb:g}/fermions_torus_kysym_coulomb_0_plus_YukawaPlaneL{lamb:g}_trunc_{trunc:g}_n_{n_val:g}_2s_{3*n_val:g}_ratio_1.000000.dat"
                    ky_val = gs_ky_val(dat_file)

                    file.write(f"echo {SpectralResponse} {response_functions}/vectors_2/ypt/n_{n_val:g}_lambda_{lamb:g}/fermions_torus_kysym_coulomb_0_plus_YukawaPlaneL{lamb:g}_trunc_{trunc:g}_n_{n_val:g}_2s_{3*n_val:g}_ratio_1.000000_ky_{ky_val:g}.0.vec --sr-omega-min -20 --sr-omega-max 0 --sr-epsilon 1E-4 --sr-omega-interval 1E-5 --sr-spectral-resolution 1E-5 --use-coulomb --coulomb-strength 0 --perturbation-file {response_functions}/pseudopotentials/plane/pseudopotentials_YukawaPlaneL{lamb:g}.dat --perturbation-strength 1 --nbr-perturbation {trunc:g} -y 0 -m 8000\n")
                else:
                    dat_file = f"{response_functions}/vectors_2/ypt/n_{n_val:g}_lambda_{lamb:g}/fermions_torus_kysym_coulomb_0_plus_YukawaPlaneL{lamb:g}_n_{n_val:g}_2s_{3 * n_val:g}_ratio_1.000000.dat"
                    ky_val = gs_ky_val(dat_file)

                    file.write(f"echo {SpectralResponse} {response_functions}/vectors_2/ypt/n_{n_val:g}_lambda_{lamb:g}/fermions_torus_kysym_coulomb_0_plus_YukawaPlaneL{lamb:g}_n_{n_val:g}_2s_{3*n_val:g}_ratio_1.000000_ky_{ky_val:g}.0.vec --sr-omega-min -20 --sr-omega-max 0 --sr-epsilon 1E-4 --sr-omega-interval 1E-5 --sr-spectral-resolution 1E-5 --use-coulomb --coulomb-strength 0 --perturbation-file {response_functions}/pseudopotentials/plane/pseudopotentials_YukawaPlaneL{lamb:g}.dat --perturbation-strength 1 --nbr-perturbation {trunc:g} -y 0 -m 8000\n")

    file.write("}\n")
    file.write("export -f runs\n")
    file.write("runs | nohup nice parallel -j 4 &\n")

    file.close()
