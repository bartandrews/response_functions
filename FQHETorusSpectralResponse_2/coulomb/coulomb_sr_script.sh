#!/bin/bash

runs() {
echo ~/DiagHam_latest/build/FQHE/src/Programs/FQHEOnTorus/FQHETorusSpectralResponse ~/PycharmProjects/response_functions/vectors/coulomb/fermions_torus_kysym_coulomb_n_6_2s_18_ratio_1.000000_ky_3.0.vec --sr-omega-min -100 --sr-omega-max 100 --sr-epsilon 1E-4 --sr-omega-interval 1E-5 --sr-spectral-resolution 1E-5 --use-coulomb --coulomb-strength 1
}
export -f runs
runs | nohup nice parallel -j 1 &
