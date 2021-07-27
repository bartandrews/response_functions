import numpy as np

if __name__ == "__main__":

    lamb = 1

    file = open(f"lty_vec_script.sh", "w")
    file.write("#!/bin/bash\n\n")
    for Yukawa_exp in np.linspace(-4, 0, 41, endpoint=True):
        print(Yukawa_exp)
        file.write(f"~/DiagHam_latest/build/FQHE/src/Programs/FQHEOnTorus/FQHETorusFermionsCoulomb -p 6 -l 18 --landau-level 0 --coulomb-strength 0 --perturbation-file pseudopotentials_V1_scale_{1-10**Yukawa_exp:.5g}_YukawaPlaneL{lamb}_scale_{10**Yukawa_exp:.5g}.dat --perturbation-strength 1 -g --use-lapack --eigenstate -n 1;\n")
    file.write("\n")
    file.write("# delete all vec files other than ky=3\n")
    file.write("mkdir safe\n")
    file.write("mv *.dat safe\n")
    file.write("mv *ky_3* safe\n")
    file.write("rm *.vec\n")
    file.write("mv safe/* .\n")
    file.write("rm -r safe\n")

    file.close()
