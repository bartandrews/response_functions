if __name__ == "__main__":

    SpectralResponse = "~/DiagHam_latest/build/FQHE/src/Programs/FQHEOnTorus/FQHETorusSpectralResponse"
    response_functions = "~/PycharmProjects/response_functions"
    # response_functions = "/disk/data11/tfp/BartMadhav/project3.5"

    file = open(f"laughlin_sr_script.sh", "w")
    file.write("#!/bin/bash\n\n")

    file.write("runs() {\n")
    for n_val in [6]:
        ky_val = n_val / 2 if n_val % 2 == 0 else 0  # corresponding ky value for ground state
        file.write(f"echo {SpectralResponse} {response_functions}/vectors_2/laughlin/n_{n_val:g}/fermions_torus_kysym_V1_n_{n_val:g}_2s_{3*n_val:g}_ratio_1.000000_ky_{ky_val:g}.0.vec --sr-omega-min -100 --sr-omega-max 100 --sr-epsilon 1E-4 --sr-omega-interval 1E-5 --sr-spectral-resolution 1E-5 --interaction-name V1 --interaction-file {response_functions}/pseudopotentials/plane/pseudopotentials_V1.dat -m 8000\n")

    file.write("}\n")
    file.write("export -f runs\n")
    file.write("runs | nohup nice parallel -j 4 &\n")

    file.close()
