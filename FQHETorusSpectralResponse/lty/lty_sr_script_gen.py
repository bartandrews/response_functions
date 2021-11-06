import numpy as np

if __name__ == "__main__":

    file = open(f"lty_sr_script.sh", "w")
    file.write("#!/bin/bash\n\n")

    file.write("runs() {\n")
    for numb_part in [9, 10]:

        if numb_part == 7:
            ky_sec = 7
        elif numb_part == 8:
            ky_sec = 4
        elif numb_part == 9:
            ky_sec = 9
        elif numb_part == 10:
            ky_sec = 5

        file.write(f"echo ~/DiagHam_latest/build/FQHE/src/Programs/FQHEOnTorus/FQHETorusSpectralResponse /disk/data11/tfp/BartMadhav/project3/vectors/lty/fermions_torus_kysym_yukawa-0.0001_plus_V1_scale_0_n_{numb_part}_2s_{numb_part*3}_ratio_1.000000_ky_{ky_sec}.0.vec --sr-omega-min -10 --sr-omega-max 10 --sr-epsilon 1E-6 --sr-omega-interval 1E-7 --sr-spectral-resolution 1E-4 --use-coulomb --coulomb-strength 1 --yukawa-mass 0.0001 --perturbation-file /disk/data11/tfp/BartMadhav/project3/vectors/lty/pseudopotentials_V1.dat --perturbation-strength 0 --sr-qy-momentum 0\n")
        file.write(f"echo ~/DiagHam_latest/build/FQHE/src/Programs/FQHEOnTorus/FQHETorusSpectralResponse /disk/data11/tfp/BartMadhav/project3/vectors/lty/fermions_torus_kysym_yukawa-0.001_plus_V1_scale_0_n_{numb_part}_2s_{numb_part*3}_ratio_1.000000_ky_{ky_sec}.0.vec --sr-omega-min -10 --sr-omega-max 10 --sr-epsilon 1E-6 --sr-omega-interval 1E-7 --sr-spectral-resolution 1E-4 --use-coulomb --coulomb-strength 1 --yukawa-mass 0.001 --perturbation-file /disk/data11/tfp/BartMadhav/project3/vectors/lty/pseudopotentials_V1.dat --perturbation-strength 0 --sr-qy-momentum 0\n")
        file.write(f"echo ~/DiagHam_latest/build/FQHE/src/Programs/FQHEOnTorus/FQHETorusSpectralResponse /disk/data11/tfp/BartMadhav/project3/vectors/lty/fermions_torus_kysym_yukawa-0.01_plus_V1_scale_0_n_{numb_part}_2s_{numb_part*3}_ratio_1.000000_ky_{ky_sec}.0.vec --sr-omega-min -10 --sr-omega-max 10 --sr-epsilon 1E-6 --sr-omega-interval 1E-7 --sr-spectral-resolution 1E-4 --use-coulomb --coulomb-strength 1 --yukawa-mass 0.01 --perturbation-file /disk/data11/tfp/BartMadhav/project3/vectors/lty/pseudopotentials_V1.dat --perturbation-strength 0 --sr-qy-momentum 0\n")
        file.write(f"echo ~/DiagHam_latest/build/FQHE/src/Programs/FQHEOnTorus/FQHETorusSpectralResponse /disk/data11/tfp/BartMadhav/project3/vectors/lty/fermions_torus_kysym_yukawa-0.1_plus_V1_scale_0_n_{numb_part}_2s_{numb_part*3}_ratio_1.000000_ky_{ky_sec}.0.vec --sr-omega-min -10 --sr-omega-max 10 --sr-epsilon 1E-6 --sr-omega-interval 1E-7 --sr-spectral-resolution 1E-4 --use-coulomb --coulomb-strength 1 --yukawa-mass 0.1 --perturbation-file /disk/data11/tfp/BartMadhav/project3/vectors/lty/pseudopotentials_V1.dat --perturbation-strength 0 --sr-qy-momentum 0\n")
        file.write(f"echo ~/DiagHam_latest/build/FQHE/src/Programs/FQHEOnTorus/FQHETorusSpectralResponse /disk/data11/tfp/BartMadhav/project3/vectors/lty/fermions_torus_kysym_yukawa-1_plus_V1_scale_0_n_{numb_part}_2s_{numb_part*3}_ratio_1.000000_ky_{ky_sec}.0.vec --sr-omega-min -10 --sr-omega-max 10 --sr-epsilon 1E-6 --sr-omega-interval 1E-7 --sr-spectral-resolution 1E-4 --use-coulomb --coulomb-strength 1 --yukawa-mass 1 --perturbation-file /disk/data11/tfp/BartMadhav/project3/vectors/lty/pseudopotentials_V1.dat --perturbation-strength 0 --sr-qy-momentum 0\n")
        file.write(f"echo ~/DiagHam_latest/build/FQHE/src/Programs/FQHEOnTorus/FQHETorusSpectralResponse /disk/data11/tfp/BartMadhav/project3/vectors/lty/fermions_torus_kysym_yukawa-10_plus_V1_scale_0_n_{numb_part}_2s_{numb_part*3}_ratio_1.000000_ky_{ky_sec}.0.vec --sr-omega-min -10 --sr-omega-max 10 --sr-epsilon 1E-6 --sr-omega-interval 1E-7 --sr-spectral-resolution 1E-4 --use-coulomb --coulomb-strength 1 --yukawa-mass 10 --perturbation-file /disk/data11/tfp/BartMadhav/project3/vectors/lty/pseudopotentials_V1.dat --perturbation-strength 0 --sr-qy-momentum 0\n")
        file.write(f"echo ~/DiagHam_latest/build/FQHE/src/Programs/FQHEOnTorus/FQHETorusSpectralResponse /disk/data11/tfp/BartMadhav/project3/vectors/lty/fermions_torus_kysym_yukawa-100_plus_V1_scale_0_n_{numb_part}_2s_{numb_part*3}_ratio_1.000000_ky_{ky_sec}.0.vec --sr-omega-min -10 --sr-omega-max 10 --sr-epsilon 1E-6 --sr-omega-interval 1E-7 --sr-spectral-resolution 1E-4 --use-coulomb --coulomb-strength 1 --yukawa-mass 100 --perturbation-file /disk/data11/tfp/BartMadhav/project3/vectors/lty/pseudopotentials_V1.dat --perturbation-strength 0 --sr-qy-momentum 0\n")
    file.write("}\n")
    file.write("export -f runs\n")
    file.write("runs | nohup nice parallel -j 7 &\n\n")

    # file.write("runs2() {\n")
    # for Yukawa_exp in np.linspace(-4, 0, 41, endpoint=True):
    #     print(Yukawa_exp)
    #     file.write(f"echo ~/DiagHam_latest/build/FQHE/src/Programs/FQHEOnTorus/FQHETorusSpectralResponse ~/PycharmProjects/response_functions/vectors/lty/l1/fermions_torus_kysym_yukawa-1_{10 ** Yukawa_exp:.5g}_plus_V1_scale_{1 - 10 ** Yukawa_exp:.5g}_n_6_2s_18_ratio_1.000000_ky_3.0.vec --sr-omega-min -10 --sr-omega-max 10 --sr-epsilon 1E-6 --sr-omega-interval 1E-7 --sr-spectral-resolution 1E-4 --use-coulomb --coulomb-strength {10 ** Yukawa_exp:.5g} --yukawa-mass 1 --perturbation-file ~/PycharmProjects/response_functions/vectors/lty/pseudopotentials_V1.dat --perturbation-strength {1 - 10 ** Yukawa_exp:.5g} --sr-qy-momentum 0\n")
    # file.write("}\n")
    # file.write("export -f runs2\n")
    # file.write("runs2 | nohup parallel -j 3 > nohup.out &\n")

    file.close()
