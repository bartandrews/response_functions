import numpy as np

if __name__ == "__main__":

    file = open(f"lty_vec_script.sh", "w")
    file.write("#!/bin/bash\n\n")
    file.write("runs() {\n")

    for numb_part in [8, 9, 10]:
        for lamb in [0.0001, 0.001, 0.01, 0.1, 1, 10, 100]:
            file.write(f"echo ~/DiagHam_latest/build/FQHE/src/Programs/FQHEOnTorus/FQHETorusFermionsCoulomb -p {numb_part} -l {3*numb_part} "
                       f"--landau-level 0 --coulomb-strength 1 --yukawa-mass {lamb} "
                       f"--perturbation-file pseudopotentials_V1.dat --perturbation-strength 0 "
                       f"-g --use-lapack --eigenstate -n 1\n")
    file.write("}\n")
    file.write("export -f runs\n")
    file.write("runs | nohup nice parallel -j 6 &\n")
    file.write("\n")
    # file.write("# delete all vec files other than ky=3\n")
    # file.write("mkdir safe\n")
    # file.write("mv *.dat safe\n")
    # file.write("mv *ky_3* safe\n")
    # file.write("rm *.vec\n")
    # file.write("mv safe/* .\n")
    # file.write("rm -r safe\n")

    file.close()
