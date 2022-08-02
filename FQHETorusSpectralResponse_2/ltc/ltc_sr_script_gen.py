import numpy as np

if __name__ == "__main__":

    SpectralResponse = "~/DiagHam_latest/build/FQHE/src/Programs/FQHEOnTorus/FQHETorusSpectralResponse"
    response_functions = "~/PycharmProjects/response_functions"
    # response_functions = "/disk/data11/tfp/BartMadhav/project3.5"

    file = open(f"ltc_sr_script.sh", "w")
    file.write("#!/bin/bash\n\n")

    # subfigures (a,b)
    # file.write("runs2() {\n")
    # for n_val in [6]:
    #     ky_val = n_val / 2 if n_val % 2 == 0 else 0  # corresponding ky value for ground state
    #     for alpha_exp in np.linspace(-4, 0, 11):
    #         alpha = 10 ** alpha_exp
    #         if alpha_exp != 0:
    #             file.write(
    #                 f"echo {SpectralResponse} {response_functions}/vectors_2/ltc/n_{n_val:g}/fermions_torus_kysym_coulomb_{alpha:.5g}_plus_V1_scale_{1 - alpha:.5g}_n_{n_val:g}_2s_{3 * n_val:g}_ratio_1.000000_ky_{ky_val:g}.0.vec --sr-omega-min -20 --sr-omega-max 0 --sr-epsilon 1E-4 --sr-omega-interval 1E-5 --sr-spectral-resolution 1E-5 --use-coulomb --coulomb-strength {alpha:.5g} --perturbation-file {response_functions}/pseudopotentials/plane/pseudopotentials_V1.dat --perturbation-strength {1 - alpha:.5g} -y 0 -m 8000\n")
    #         else:
    #             file.write(
    #                 f"echo {SpectralResponse} {response_functions}/vectors_2/ltc/n_{n_val:g}/fermions_torus_kysym_coulomb_plus_V1_scale_0_n_{n_val:g}_2s_{3 * n_val:g}_ratio_1.000000_ky_{ky_val:g}.0.vec --sr-omega-min -20 --sr-omega-max 0 --sr-epsilon 1E-4 --sr-omega-interval 1E-5 --sr-spectral-resolution 1E-5 --use-coulomb --coulomb-strength {alpha:.5g} --perturbation-file {response_functions}/pseudopotentials/plane/pseudopotentials_V1.dat --perturbation-strength {1 - alpha:.5g} -y 0 -m 8000\n")

    # subfigures (c-f)
    file.write("runs2() {\n")
    for n_val in [6]:
        ky_val = n_val / 2 if n_val % 2 == 0 else 0  # corresponding ky value for ground state
        for alpha_exp in np.linspace(-4, 0, 41):
            alpha = 10 ** alpha_exp
            if alpha_exp != 0:
                file.write(f"echo {SpectralResponse} {response_functions}/vectors_2/ltc/n_{n_val:g}/fermions_torus_kysym_coulomb_{alpha:.5g}_plus_V1_scale_{1 - alpha:.5g}_n_{n_val:g}_2s_{3 * n_val:g}_ratio_1.000000_ky_{ky_val:g}.0.vec --sr-omega-min -20 --sr-omega-max 0 --sr-epsilon 1E-6 --sr-omega-interval 1E-7 --sr-spectral-resolution 1E-4 --use-coulomb --coulomb-strength {alpha:.5g} --perturbation-file {response_functions}/pseudopotentials/plane/pseudopotentials_V1.dat --perturbation-strength {1 - alpha:.5g} -y 0 -m 8000\n")
            else:
                file.write(f"echo {SpectralResponse} {response_functions}/vectors_2/ltc/n_{n_val:g}/fermions_torus_kysym_coulomb_plus_V1_scale_0_n_{n_val:g}_2s_{3 * n_val:g}_ratio_1.000000_ky_{ky_val:g}.0.vec --sr-omega-min -20 --sr-omega-max 0 --sr-epsilon 1E-6 --sr-omega-interval 1E-7 --sr-spectral-resolution 1E-4 --use-coulomb --coulomb-strength {alpha:.5g} --perturbation-file {response_functions}/pseudopotentials/plane/pseudopotentials_V1.dat --perturbation-strength {1 - alpha:.5g} -y 0 -m 8000\n")

    file.write("}\n")
    file.write("export -f runs2\n")
    file.write("runs2 | nohup nice parallel -j 4 &\n")

    file.close()
