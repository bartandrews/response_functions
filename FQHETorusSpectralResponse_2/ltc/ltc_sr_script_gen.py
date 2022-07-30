import numpy as np

if __name__ == "__main__":

    SpectralResponse = "~/DiagHam_latest/build/FQHE/src/Programs/FQHEOnTorus/FQHETorusSpectralResponse"
    response_functions = "~/PycharmProjects/response_functions"
    # response_functions = "/disk/data11/tfp/BartMadhav/project3.5"

    file = open(f"ltc_sr_script.sh", "w")
    file.write("#!/bin/bash\n\n")

    # file.write("runs() {\n")
    # for alpha_exp in np.linspace(-4, 0, 11, endpoint=True):
    #     print(alpha_exp)
    #     if alpha_exp != 0:
    #         file.write(f"echo {SpectralResponse} {response_functions}/vectors_2/ltc/fermions_torus_kysym_coulomb_{10 ** alpha_exp:.5g}_plus_V1_scale_{1 - 10 ** alpha_exp:.5g}_n_6_2s_18_ratio_1.000000_ky_3.0.vec --sr-omega-min -100 --sr-omega-max 100 --sr-epsilon 1E-4 --sr-omega-interval 1E-5 --sr-spectral-resolution 1E-5 --use-coulomb --coulomb-strength {10 ** alpha_exp:.5g} --perturbation-file {response_functions}/pseudopotentials/plane/pseudopotentials_V1.dat --perturbation-strength {1 - 10 ** alpha_exp:.5g} --sr-qy-momentum 0\n")
    #     else:
    #         file.write(f"echo {SpectralResponse} {response_functions}/vectors_2/ltc/fermions_torus_kysym_coulomb_plus_V1_scale_0_n_6_2s_18_ratio_1.000000_ky_3.0.vec --sr-omega-min -100 --sr-omega-max 100 --sr-epsilon 1E-4 --sr-omega-interval 1E-5 --sr-spectral-resolution 1E-5 --use-coulomb --coulomb-strength {10 ** alpha_exp:.5g} --perturbation-file {response_functions}/pseudopotentials/plane/pseudopotentials_V1.dat --perturbation-strength {1 - 10 ** alpha_exp:.5g} --sr-qy-momentum 0\n")
    # file.write("}\n")
    # file.write("export -f runs\n")
    # file.write("runs | nohup nice parallel -j 4 &\n\n")

    file.write("runs2() {\n")
    for alpha_exp in np.linspace(-4, 0, 41, endpoint=True):
        print(alpha_exp)
        if alpha_exp != 0:
            file.write(f"echo {SpectralResponse} {response_functions}/vectors_2/ltc/fermions_torus_kysym_coulomb_{10 ** alpha_exp:.5g}_plus_V1_scale_{1 - 10 ** alpha_exp:.5g}_n_6_2s_18_ratio_1.000000_ky_3.0.vec --sr-omega-min -20 --sr-omega-max 0 --sr-epsilon 1E-6 --sr-omega-interval 1E-7 --sr-spectral-resolution 1E-4 --use-coulomb --coulomb-strength {10 ** alpha_exp:.5g} --perturbation-file {response_functions}/pseudopotentials/plane/pseudopotentials_V1.dat --perturbation-strength {1 - 10 ** alpha_exp:.5g} --sr-qy-momentum 0\n")
        else:
            file.write(f"echo {SpectralResponse} {response_functions}/vectors_2/ltc/fermions_torus_kysym_coulomb_plus_V1_scale_0_n_6_2s_18_ratio_1.000000_ky_3.0.vec --sr-omega-min -20 --sr-omega-max 0 --sr-epsilon 1E-6 --sr-omega-interval 1E-7 --sr-spectral-resolution 1E-4 --use-coulomb --coulomb-strength {10 ** alpha_exp:.5g} --perturbation-file {response_functions}/pseudopotentials/plane/pseudopotentials_V1.dat --perturbation-strength {1 - 10 ** alpha_exp:.5g} --sr-qy-momentum 0\n")
    file.write("}\n")
    file.write("export -f runs2\n")
    file.write("runs2 | nohup nice parallel -j 4 &\n\n")

    file.close()
