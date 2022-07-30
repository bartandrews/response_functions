import numpy as np

if __name__ == "__main__":

    SpectralResponse = "~/DiagHam_latest/build/FQHE/src/Programs/FQHEOnTorus/FQHETorusSpectralResponse"
    response_functions = "~/PycharmProjects/response_functions"
    # response_functions = "/disk/data11/tfp/BartMadhav/project3.5"

    file = open(f"lty_sr_script.sh", "w")
    file.write("#!/bin/bash\n\n")

    file.write("runs() {\n")
    for numb_part in [6]:

        if numb_part % 2 == 0:
            ky_sec = numb_part/2
        else:
            ky_sec = 0

        for lamb in [0.0001, 0.001, 0.01, 0.1]:
            for alpha_exp in np.linspace(-4, 0, 41, endpoint=True):
                alpha = 10 ** alpha_exp
                if alpha_exp != 0:
                    file.write(f"echo {SpectralResponse} {response_functions}/vectors_2/lty/n_{numb_part}/fermions_torus_kysym_yukawa-{lamb:.5g}_{alpha:.5g}_plus_V1_scale_{1-alpha:.5g}_n_{numb_part}_2s_{numb_part*3}_ratio_1.000000_ky_{int(ky_sec)}.0.vec --sr-omega-min -20 --sr-omega-max 0 --sr-epsilon 1E-6 --sr-omega-interval 1E-7 --sr-spectral-resolution 1E-4 --use-coulomb --coulomb-strength {alpha:.5g} --yukawa-mass {lamb:.5g} --perturbation-file ../pseudopotentials_V1.dat --perturbation-strength {1-alpha:.5g} --sr-qy-momentum 0\n")
                else:
                    file.write(f"echo {SpectralResponse} {response_functions}/vectors_2/lty/n_{numb_part}/fermions_torus_kysym_yukawa-{lamb:.5g}_plus_V1_scale_0_n_{numb_part}_2s_{numb_part * 3}_ratio_1.000000_ky_{int(ky_sec)}.0.vec --sr-omega-min -20 --sr-omega-max 0 --sr-epsilon 1E-6 --sr-omega-interval 1E-7 --sr-spectral-resolution 1E-4 --use-coulomb --coulomb-strength 1 --yukawa-mass {lamb:.5g} --perturbation-file ../pseudopotentials_V1.dat --perturbation-strength 0 --sr-qy-momentum 0\n")

    file.write("}\n")
    file.write("export -f runs\n")
    file.write("runs | nohup nice parallel -j 4 &\n\n")

    # file.write("runs2() {\n")
    # for Yukawa_exp in np.linspace(-4, 0, 41, endpoint=True):
    #     print(Yukawa_exp)
    #     file.write(f"echo ~/DiagHam_latest/build/FQHE/src/Programs/FQHEOnTorus/FQHETorusSpectralResponse ~/PycharmProjects/response_functions/vectors/lty/l1/fermions_torus_kysym_yukawa-1_{10 ** Yukawa_exp:.5g}_plus_V1_scale_{1 - 10 ** Yukawa_exp:.5g}_n_6_2s_18_ratio_1.000000_ky_3.0.vec --sr-omega-min -10 --sr-omega-max 10 --sr-epsilon 1E-6 --sr-omega-interval 1E-7 --sr-spectral-resolution 1E-4 --use-coulomb --coulomb-strength {10 ** Yukawa_exp:.5g} --yukawa-mass 1 --perturbation-file ~/PycharmProjects/response_functions/vectors/lty/pseudopotentials_V1.dat --perturbation-strength {1 - 10 ** Yukawa_exp:.5g} --sr-qy-momentum 0\n")
    # file.write("}\n")
    # file.write("export -f runs2\n")
    # file.write("runs2 | nohup parallel -j 3 > nohup.out &\n")

    file.close()
