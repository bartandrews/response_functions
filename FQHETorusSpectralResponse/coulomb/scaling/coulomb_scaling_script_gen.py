import numpy as np

if __name__ == "__main__":

    file = open(f"coulomb_scaling_script.sh", "w")
    file.write("#!/bin/bash\n\n")

    file.write("runs() {\n")
    for scaling_factor in np.linspace(1, 7, 7, endpoint=True):
        print(scaling_factor)
        # file.write(f"echo ~/DiagHam_latest/build/FQHE/src/Programs/FQHEOnTorus/FQHETorusSpectralResponse /disk/data11/tfp/BartMadhav/project3/vectors/coulomb/n_7/fermions_torus_kysym_coulomb_n_7_2s_21_ratio_1.000000_ky_0.0.vec --sr-omega-min {-7.5-5/(2**scaling_factor):.6g} --sr-omega-max {-7.5+5/(2**scaling_factor):.6g} --sr-epsilon {0.0001/(2**(scaling_factor-1)):.6g} --sr-omega-interval {0.00001/(2**(scaling_factor-1)):.6g} --sr-spectral-resolution 1E-5 --use-coulomb --coulomb-strength 1 -y 0 -S --processors 8 -m 100000\n")
        file.write(f"echo ~/DiagHam_latest/build/FQHE/src/Programs/FQHEOnTorus/FQHETorusSpectralResponse /disk/data11/tfp/BartMadhav/project3/vectors/coulomb/n_8/fermions_torus_kysym_coulomb_n_8_2s_24_ratio_1.000000_ky_4.0.vec --sr-omega-min -100 --sr-omega-max 100 --sr-epsilon {0.0001/(2**(scaling_factor-1)):.6g} --sr-omega-interval {0.00001/(2**(scaling_factor-1)):.6g} --sr-spectral-resolution 1E-5 --use-coulomb --coulomb-strength 1 -y 0 -S --processors 8 -m 100000\n")
    file.write("}\n")
    file.write("export -f runs\n")
    file.write("runs | nohup nice parallel -j 4 > nohup.out &\n")

    file.close()
