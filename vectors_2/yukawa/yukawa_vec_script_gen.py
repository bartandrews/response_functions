if __name__ == "__main__":

    Coulomb = "~/DiagHam_latest/build/FQHE/src/Programs/FQHEOnTorus/FQHETorusFermionsCoulomb"
    response_functions = "~/PycharmProjects/response_functions"
    # response_functions = "/disk/data11/tfp/BartMadhav/project3.5"

    file = open(f"yukawa_vec_script.sh", "w")
    file.write("#!/bin/bash\n\n")
    file.write("runs() {\n")

    for n_val in [6]:
        for lamb_exp in [-4, -3, -2, -1, 1, 2, 3]:
            lamb = 10 ** lamb_exp
            file.write(f"echo {Coulomb} -p {n_val:g} -l {3*n_val:g} --landau-level 0 --coulomb-strength 1 --yukawa-mass {lamb:g} -g --use-lapack --eigenstate -n 1 -m 8000\n")

    file.write("}\n")
    file.write("export -f runs\n")
    file.write("runs | nohup nice parallel -j 4 &\n")

    file.close()
