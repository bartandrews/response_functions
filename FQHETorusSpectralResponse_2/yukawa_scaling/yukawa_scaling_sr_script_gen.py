if __name__ == "__main__":

    SpectralResponse = "~/DiagHam_latest/build/FQHE/src/Programs/FQHEOnTorus/FQHETorusSpectralResponse"
    # response_functions = "~/PycharmProjects/response_functions"
    response_functions = "/disk/data11/tfp/BartMadhav/project3.5"

    # INPUT
    n_val = 9  # number of particles
    mid = -10.6995  # midpoint
    std = 0.6095  # deviation

    ky_val = n_val / 2 if n_val % 2 == 0 else 0  # corresponding ky value for ground state

    file = open(f"yukawa_scaling_sr_script.sh", "w")
    file.write("#!/bin/bash\n\n")

    file.write("runs() {\n")
    for lamb_exp in [-4, -3, -2, -1, 0, 1, 2]:
        lamb = 10 ** lamb_exp
        for i in [0]:  # 0, 1, 2, 3, 4, 5, 6
            file.write(f"echo {SpectralResponse} {response_functions}/vectors_2/yukawa/n_{n_val:g}/fermions_torus_kysym_yukawa-{lamb:g}_n_{n_val:g}_2s_{3*n_val:g}_ratio_1.000000_ky_{ky_val:g}.0.vec --sr-omega-min {mid-std/(2**i):.6g} --sr-omega-max {mid+std/(2**i):.6g} --sr-epsilon {0.0001/(2**i):.6g} --sr-omega-interval {0.00001/(2**i):.6g} --sr-spectral-resolution 1E-5 --use-coulomb --coulomb-strength 1 --yukawa-mass {lamb:g} -y 0 -m 16000\n")

    file.write("}\n")
    file.write("export -f runs\n")
    file.write("runs | nohup nice parallel -j 10 &\n")

    file.close()
