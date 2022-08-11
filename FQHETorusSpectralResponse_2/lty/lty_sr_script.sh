#!/bin/bash

runs() {
echo ~/DiagHam_latest/build/FQHE/src/Programs/FQHEOnTorus/FQHETorusSpectralResponse ~/PycharmProjects/response_functions/vectors_2/lty/n_9_alpha_1/fermions_torus_kysym_yukawa-0.0001_plus_V1_scale_0_n_9_2s_27_ratio_1.000000_ky_0.0.vec --sr-omega-min -20 --sr-omega-max 0 --sr-epsilon 1E-6 --sr-omega-interval 1E-7 --sr-spectral-resolution 1E-4 --use-coulomb --coulomb-strength 1 --yukawa-mass 0.0001 --perturbation-file ~/PycharmProjects/response_functions/pseudopotentials/plane/pseudopotentials_V1.dat --perturbation-strength 0 -y 0 -m 8000
echo ~/DiagHam_latest/build/FQHE/src/Programs/FQHEOnTorus/FQHETorusSpectralResponse ~/PycharmProjects/response_functions/vectors_2/lty/n_9_alpha_1/fermions_torus_kysym_yukawa-0.001_plus_V1_scale_0_n_9_2s_27_ratio_1.000000_ky_0.0.vec --sr-omega-min -20 --sr-omega-max 0 --sr-epsilon 1E-6 --sr-omega-interval 1E-7 --sr-spectral-resolution 1E-4 --use-coulomb --coulomb-strength 1 --yukawa-mass 0.001 --perturbation-file ~/PycharmProjects/response_functions/pseudopotentials/plane/pseudopotentials_V1.dat --perturbation-strength 0 -y 0 -m 8000
echo ~/DiagHam_latest/build/FQHE/src/Programs/FQHEOnTorus/FQHETorusSpectralResponse ~/PycharmProjects/response_functions/vectors_2/lty/n_9_alpha_1/fermions_torus_kysym_yukawa-0.01_plus_V1_scale_0_n_9_2s_27_ratio_1.000000_ky_0.0.vec --sr-omega-min -20 --sr-omega-max 0 --sr-epsilon 1E-6 --sr-omega-interval 1E-7 --sr-spectral-resolution 1E-4 --use-coulomb --coulomb-strength 1 --yukawa-mass 0.01 --perturbation-file ~/PycharmProjects/response_functions/pseudopotentials/plane/pseudopotentials_V1.dat --perturbation-strength 0 -y 0 -m 8000
echo ~/DiagHam_latest/build/FQHE/src/Programs/FQHEOnTorus/FQHETorusSpectralResponse ~/PycharmProjects/response_functions/vectors_2/lty/n_9_alpha_1/fermions_torus_kysym_yukawa-0.1_plus_V1_scale_0_n_9_2s_27_ratio_1.000000_ky_0.0.vec --sr-omega-min -20 --sr-omega-max 0 --sr-epsilon 1E-6 --sr-omega-interval 1E-7 --sr-spectral-resolution 1E-4 --use-coulomb --coulomb-strength 1 --yukawa-mass 0.1 --perturbation-file ~/PycharmProjects/response_functions/pseudopotentials/plane/pseudopotentials_V1.dat --perturbation-strength 0 -y 0 -m 8000
echo ~/DiagHam_latest/build/FQHE/src/Programs/FQHEOnTorus/FQHETorusSpectralResponse ~/PycharmProjects/response_functions/vectors_2/lty/n_9_alpha_1/fermions_torus_kysym_yukawa-1_plus_V1_scale_0_n_9_2s_27_ratio_1.000000_ky_0.0.vec --sr-omega-min -20 --sr-omega-max 0 --sr-epsilon 1E-6 --sr-omega-interval 1E-7 --sr-spectral-resolution 1E-4 --use-coulomb --coulomb-strength 1 --yukawa-mass 1 --perturbation-file ~/PycharmProjects/response_functions/pseudopotentials/plane/pseudopotentials_V1.dat --perturbation-strength 0 -y 0 -m 8000
echo ~/DiagHam_latest/build/FQHE/src/Programs/FQHEOnTorus/FQHETorusSpectralResponse ~/PycharmProjects/response_functions/vectors_2/lty/n_9_alpha_1/fermions_torus_kysym_yukawa-10_plus_V1_scale_0_n_9_2s_27_ratio_1.000000_ky_0.0.vec --sr-omega-min -20 --sr-omega-max 0 --sr-epsilon 1E-6 --sr-omega-interval 1E-7 --sr-spectral-resolution 1E-4 --use-coulomb --coulomb-strength 1 --yukawa-mass 10 --perturbation-file ~/PycharmProjects/response_functions/pseudopotentials/plane/pseudopotentials_V1.dat --perturbation-strength 0 -y 0 -m 8000
echo ~/DiagHam_latest/build/FQHE/src/Programs/FQHEOnTorus/FQHETorusSpectralResponse ~/PycharmProjects/response_functions/vectors_2/lty/n_9_alpha_1/fermions_torus_kysym_yukawa-100_plus_V1_scale_0_n_9_2s_27_ratio_1.000000_ky_0.0.vec --sr-omega-min -20 --sr-omega-max 0 --sr-epsilon 1E-6 --sr-omega-interval 1E-7 --sr-spectral-resolution 1E-4 --use-coulomb --coulomb-strength 1 --yukawa-mass 100 --perturbation-file ~/PycharmProjects/response_functions/pseudopotentials/plane/pseudopotentials_V1.dat --perturbation-strength 0 -y 0 -m 8000
}
export -f runs
runs | nohup nice parallel -j 4 &
