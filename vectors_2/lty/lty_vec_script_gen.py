if __name__ == "__main__":

    Coulomb = "~/DiagHam_latest/build/FQHE/src/Programs/FQHEOnTorus/FQHETorusFermionsCoulomb"
    response_functions = "~/PycharmProjects/response_functions"
    # response_functions = "/disk/data11/tfp/BartMadhav/project3.5"

    file = open(f"lty_vec_script.sh", "w")
    file.write("#!/bin/bash\n\n")
    file.write("runs() {\n")

    for n_val in [6]:
        for lamb_exp in [-4, -3, -2, -1, 0, 1, 2]:
            lamb = 10 ** lamb_exp
            for alpha_exp in [-4, -3, -2, -1, 0]:
                alpha = 10 ** alpha_exp
                file.write(f"echo {Coulomb} -p {n_val:g} -l {3*n_val:g} --landau-level 0 --coulomb-strength {alpha:.5g} --yukawa-mass {lamb:.5g} --perturbation-file {response_functions}/pseudopotentials/plane/pseudopotentials_V1.dat --perturbation-strength {1-alpha:.5g} -g --use-lapack --eigenstate -n 1 -m 8000\n")

    file.write("}\n")
    file.write("export -f runs\n")
    file.write("runs | nohup nice parallel -j 4 &\n")

    file.close()
