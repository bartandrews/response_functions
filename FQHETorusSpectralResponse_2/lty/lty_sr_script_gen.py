import numpy as np

if __name__ == "__main__":

    SpectralResponse = "~/DiagHam_latest/build/FQHE/src/Programs/FQHEOnTorus/FQHETorusSpectralResponse"
    response_functions = "~/PycharmProjects/response_functions"
    # response_functions = "/disk/data11/tfp/BartMadhav/project3.5"

    file = open(f"lty_sr_script.sh", "w")
    file.write("#!/bin/bash\n\n")

    file.write("runs() {\n")
    for n_val in [6]:
        ky_val = n_val / 2 if n_val % 2 == 0 else 0  # corresponding ky value for ground state
        for lamb_exp in [-4, -3, -2, -1, 0, 1, 2]:  # -4, -3, -2, -1, 0, 1, 2
            lamb = 10 ** lamb_exp
            for alpha in np.linspace(10**-4, 1, 11):
                # alpha = 10 ** alpha_exp
                if alpha != 1:
                    file.write(f"echo {SpectralResponse} {response_functions}/vectors_2/lty/n_{n_val:g}_linear/fermions_torus_kysym_yukawa-{lamb:g}_{alpha:.5g}_plus_V1_scale_{1-alpha:.5g}_n_{n_val:g}_2s_{3*n_val:g}_ratio_1.000000_ky_{ky_val:g}.0.vec --sr-omega-min -20 --sr-omega-max 0 --sr-epsilon 1E-6 --sr-omega-interval 1E-7 --sr-spectral-resolution 1E-4 --use-coulomb --coulomb-strength {alpha:.5g} --yukawa-mass {lamb:g} --perturbation-file {response_functions}/pseudopotentials/plane/pseudopotentials_V1.dat --perturbation-strength {1-alpha:.5g} -y 0 -m 8000\n")
                else:
                    file.write(f"echo {SpectralResponse} {response_functions}/vectors_2/lty/n_{n_val:g}_linear/fermions_torus_kysym_yukawa-{lamb:g}_plus_V1_scale_0_n_{n_val:g}_2s_{3*n_val:g}_ratio_1.000000_ky_{ky_val:g}.0.vec --sr-omega-min -20 --sr-omega-max 0 --sr-epsilon 1E-6 --sr-omega-interval 1E-7 --sr-spectral-resolution 1E-4 --use-coulomb --coulomb-strength 1 --yukawa-mass {lamb:g} --perturbation-file {response_functions}/pseudopotentials/plane/pseudopotentials_V1.dat --perturbation-strength 0 -y 0 -m 8000\n")

    file.write("}\n")
    file.write("export -f runs\n")
    file.write("runs | nohup nice parallel -j 4 &\n")

    file.close()
