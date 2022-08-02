#!/bin/bash

runs() {
echo ~/DiagHam_latest/build/FQHE/src/Programs/FQHEOnTorus/FQHETorusSpectralResponse ~/PycharmProjects/response_functions/vectors_2/laughlin/n_6/fermions_torus_kysym_V1_n_6_2s_18_ratio_1.000000_ky_3.0.vec --sr-omega-min -100 --sr-omega-max 100 --sr-epsilon 1E-4 --sr-omega-interval 1E-5 --sr-spectral-resolution 1E-5 --interaction-name V1 --interaction-file ~/PycharmProjects/response_functions/pseudopotentials/plane/pseudopotentials_V1.dat -m 8000
}
export -f runs
runs | nohup nice parallel -j 4 &
