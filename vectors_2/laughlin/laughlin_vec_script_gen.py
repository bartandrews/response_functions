if __name__ == "__main__":

    TwoBodyGeneric = "~/DiagHam_latest/build/FQHE/src/Programs/FQHEOnTorus/FQHETorusFermionsTwoBodyGeneric"
    response_functions = "~/PycharmProjects/response_functions"
    # response_functions = "/disk/data11/tfp/BartMadhav/project3.5"

    file = open(f"laughlin_vec_script.sh", "w")
    file.write("#!/bin/bash\n\n")
    file.write("runs() {\n")

    for n_val in [8]:
        file.write(f"echo {TwoBodyGeneric} -p {n_val:g} -l {3*n_val:g} --interaction-name V1 --interaction-file {response_functions}/pseudopotentials/plane/pseudopotentials_V1.dat -g --use-lapack --eigenstate -n 1 -m 8000\n")

    file.write("}\n")
    file.write("export -f runs\n")
    file.write("runs | nohup nice parallel -j 4 &\n")

    file.close()
