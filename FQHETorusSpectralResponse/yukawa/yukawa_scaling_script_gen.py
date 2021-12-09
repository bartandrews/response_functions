import numpy as np

if __name__ == "__main__":

    file = open(f"yukawa_scaling_script.sh", "w")
    file.write("#!/bin/bash\n\n")

    file.write("runs() {\n")
    for n_val in [8]:
        ky_val = n_val / 2 if n_val % 2 == 0 else 0  # corresponding ky value for ground state
        for lambda_val in [0.0001, 0.001, 0.01, 0.1, 1, 10, 100]:
            if lambda_val < 10:
                center = -7.5
                interval = 5
            elif lambda_val == 10:
                center = -9.75
                interval = 0.5
            elif lambda_val == 100:
                center = -9.975
                interval = 0.05

            file.write(f"echo ~/DiagHam_latest/build/FQHE/src/Programs/FQHEOnTorus/FQHETorusSpectralResponse /disk/data11/tfp/BartMadhav/project3/vectors/yukawa/n_{n_val:g}/fermions_torus_kysym_yukawa-{lambda_val}_plus_V1_scale_0_n_{n_val:g}_2s_{3*n_val:g}_ratio_1.000000_ky_{ky_val:g}.0.vec --sr-omega-min {center-interval/2:.6g} --sr-omega-max {center+interval/2:.6g} --sr-epsilon 0.0001 --sr-omega-interval 0.00001 --sr-spectral-resolution 1E-5 --use-coulomb --coulomb-strength 1 --yukawa-mass {lambda_val} --perturbation-file /disk/data11/tfp/BartMadhav/project3/vectors/yukawa/pseudopotentials_V1.dat --perturbation-strength 0 --sr-qy-momentum 0 -S --processors 8 -m 100000\n")
    file.write("}\n")
    file.write("export -f runs\n")
    file.write("runs | nohup nice parallel -j 4 > nohup.out &\n")

    file.close()
