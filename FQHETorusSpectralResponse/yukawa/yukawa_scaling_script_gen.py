import numpy as np

if __name__ == "__main__":

    file = open(f"yukawa_scaling_script.sh", "w")
    file.write("#!/bin/bash\n\n")

    file.write("runs() {\n")
    for lambda_val in [0.0001, 0.001, 0.01, 0.1, 1, 10, 100]:
        for scaling_factor in np.linspace(1, 7, 7, endpoint=True):
            print(scaling_factor)
            if lambda_val < 10:
                center = -7.5
                interval = 5
            elif lambda_val == 10:
                center = -9.75
                interval = 0.5
            elif lambda_val == 100:
                center = -9.975
                interval = 0.05

            file.write(f"~/DiagHam_latest/build/FQHE/src/Programs/FQHEOnTorus/FQHETorusSpectralResponse /disk/data11/tfp/BartMadhav/project3/vectors/yukawa/fermions_torus_kysym_yukawa-{lambda_val}_plus_V1_scale_0_n_6_2s_18_ratio_1.000000_ky_3.0.vec --sr-omega-min {center - interval/(2**scaling_factor):.6g} --sr-omega-max {center + interval/(2**scaling_factor):.6g} --sr-epsilon {0.0001/(2**(scaling_factor-1)):.6g} --sr-omega-interval {0.00001/(2**(scaling_factor-1)):.6g} --sr-spectral-resolution 1E-5 --use-coulomb --coulomb-strength 1 --yukawa-mass {lambda_val} --perturbation-file /disk/data11/tfp/BartMadhav/project3/vectors/yukawa/pseudopotentials_V1.dat --perturbation-strength 0 --sr-qy-momentum 0\n")
    file.write("}\n")
    file.write("export -f runs\n")
    file.write("runs | nohup nice parallel -j 4 > nohup.out &\n")

    file.close()