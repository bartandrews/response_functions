import numpy as np

if __name__ == "__main__":

    Coulomb = "~/DiagHam_latest/build/FQHE/src/Programs/FQHEOnTorus/FQHETorusFermionsCoulomb"
    response_functions = "~/PycharmProjects/response_functions"
    # response_functions = "/disk/data11/tfp/BartMadhav/project3"

    file = open(f"ltc_vec_script.sh", "w")
    file.write("#!/bin/bash\n\n")
    file.write("runs() {\n")
    for alpha_exp in np.linspace(-4, 0, 41, endpoint=True):
        print(alpha_exp)
        file.write(f"echo {Coulomb} -p 6 -l 18 --landau-level 0 --coulomb-strength {10 ** alpha_exp:.5g} --perturbation-file {response_functions}/pseudopotentials/plane/pseudopotentials_V1.dat --perturbation-strength {1 - 10 ** alpha_exp:.5g} -g --use-lapack --eigenstate -n 1 -m 160000\n")
    file.write("}\n")
    file.write("export -f runs\n")
    file.write("runs | nohup nice parallel -j 4;\n")
    file.write("\n")
    file.write("# delete all vec files other than ky=3\n")
    file.write("mkdir safe\n")
    file.write("mv *.dat safe\n")
    file.write("mv *ky_3* safe\n")
    file.write("rm *.vec\n")
    file.write("mv safe/* .\n")
    file.write("rm -r safe\n")

    file.close()
