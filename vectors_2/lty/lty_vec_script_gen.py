import numpy as np

if __name__ == "__main__":

    Coulomb = "~/DiagHam_latest/build/FQHE/src/Programs/FQHEOnTorus/FQHETorusFermionsCoulomb"
    response_functions = "~/PycharmProjects/response_functions"
    # response_functions = "/disk/data11/tfp/BartMadhav/project3.5"

    file = open(f"lty_vec_script.sh", "w")
    file.write("#!/bin/bash\n\n")
    file.write("runs() {\n")

    for numb_part in [7]:
        for lamb_exp in [-4, -3, -2, -1, 0, 1, 2]:
            for alpha_exp in [0]:
                lamb = 10 ** lamb_exp
                alpha = 10 ** alpha_exp
                file.write(f"echo {Coulomb} -p {numb_part:g} -l {3*numb_part:g} "
                           f"--landau-level 0 --coulomb-strength {alpha:.5g} --yukawa-mass {lamb:.5g} "
                           f"--perturbation-file {response_functions}/pseudopotentials/plane/pseudopotentials_V1.dat --perturbation-strength {1-alpha:.5g} "
                           f"-g --use-lapack --eigenstate -n 1\n")
    file.write("}\n")
    file.write("export -f runs\n")
    file.write("runs | nohup nice parallel -j 4 &\n")
    # file.write("\n")
    # file.write("# delete all vec files other than ky=3\n")
    # file.write("mkdir safe\n")
    # file.write("mv *.dat safe\n")
    # file.write("mv *ky_3* safe\n")
    # file.write("rm *.vec\n")
    # file.write("mv safe/* .\n")
    # file.write("rm -r safe\n")

    file.close()
