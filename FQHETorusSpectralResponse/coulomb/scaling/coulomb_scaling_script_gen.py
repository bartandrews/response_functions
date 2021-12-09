import numpy as np

if __name__ == "__main__":

    n_val = 10  # number of particles (INPUT)
    ky_val = n_val/2 if n_val % 2 == 0 else 0  # corresponding ky value for ground state

    file = open(f"coulomb_scaling_script.sh", "w")
    file.write("#!/bin/bash\n\n")

    file.write("runs() {\n")
    for i in np.linspace(0, 6, 61, endpoint=True):
        print("scaling_factor = ", i)
        # file.write(f"echo ~/DiagHam_latest/build/FQHE/src/Programs/FQHEOnTorus/FQHETorusSpectralResponse /disk/data11/tfp/BartMadhav/project3/vectors/coulomb/n_{n_val:g}/fermions_torus_kysym_coulomb_n_{n_val:g}_2s_{3*n_val:g}_ratio_1.000000_ky_{ky_val:g}.0.vec --sr-omega-min {-7.5-2.5/(2**i):.6g} --sr-omega-max {-7.5+2.5/(2**i):.6g} --sr-epsilon {0.0001/(2**i):.6g} --sr-omega-interval {0.00001/(2**i):.6g} --sr-spectral-resolution 1E-5 --use-coulomb --coulomb-strength 1 -y 0 -S --processors 8 -m 100000\n")
        file.write(f"echo ~/DiagHam_latest/build/FQHE/src/Programs/FQHEOnTorus/FQHETorusSpectralResponse /disk/data11/tfp/BartMadhav/project3/vectors/coulomb/n_{n_val:g}/fermions_torus_kysym_coulomb_n_{n_val:g}_2s_{3*n_val:g}_ratio_1.000000_ky_{ky_val:g}.0.vec --sr-omega-min -100 --sr-omega-max 100 --sr-epsilon {0.0001/(2**i):.6g} --sr-omega-interval {0.00001/(2**i):.6g} --sr-spectral-resolution 1E-5 --use-coulomb --coulomb-strength 1 -y 0 -S --processors 8 -m 100000\n")
    file.write("}\n")
    file.write("export -f runs\n")
    file.write("runs | nohup nice parallel -j 4 > nohup.out &\n")

    file.close()
