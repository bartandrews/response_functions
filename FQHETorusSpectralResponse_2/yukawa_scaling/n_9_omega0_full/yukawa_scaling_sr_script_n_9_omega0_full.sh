#!/bin/bash

runs() {
echo ~/DiagHam_latest/build/FQHE/src/Programs/FQHEOnTorus/FQHETorusSpectralResponse /disk/data11/tfp/BartMadhav/project3.5/vectors_2/yukawa/n_9/fermions_torus_kysym_yukawa-0.0001_n_9_2s_27_ratio_1.000000_ky_0.0.vec --sr-omega-min -11.309 --sr-omega-max -10.09 --sr-epsilon 0.0001 --sr-omega-interval 1e-05 --sr-spectral-resolution 1E-5 --use-coulomb --coulomb-strength 1 --yukawa-mass 0.0001 -y 0 -m 16000
echo ~/DiagHam_latest/build/FQHE/src/Programs/FQHEOnTorus/FQHETorusSpectralResponse /disk/data11/tfp/BartMadhav/project3.5/vectors_2/yukawa/n_9/fermions_torus_kysym_yukawa-0.001_n_9_2s_27_ratio_1.000000_ky_0.0.vec --sr-omega-min -11.309 --sr-omega-max -10.09 --sr-epsilon 0.0001 --sr-omega-interval 1e-05 --sr-spectral-resolution 1E-5 --use-coulomb --coulomb-strength 1 --yukawa-mass 0.001 -y 0 -m 16000
echo ~/DiagHam_latest/build/FQHE/src/Programs/FQHEOnTorus/FQHETorusSpectralResponse /disk/data11/tfp/BartMadhav/project3.5/vectors_2/yukawa/n_9/fermions_torus_kysym_yukawa-0.01_n_9_2s_27_ratio_1.000000_ky_0.0.vec --sr-omega-min -11.309 --sr-omega-max -10.09 --sr-epsilon 0.0001 --sr-omega-interval 1e-05 --sr-spectral-resolution 1E-5 --use-coulomb --coulomb-strength 1 --yukawa-mass 0.01 -y 0 -m 16000
echo ~/DiagHam_latest/build/FQHE/src/Programs/FQHEOnTorus/FQHETorusSpectralResponse /disk/data11/tfp/BartMadhav/project3.5/vectors_2/yukawa/n_9/fermions_torus_kysym_yukawa-0.1_n_9_2s_27_ratio_1.000000_ky_0.0.vec --sr-omega-min -11.309 --sr-omega-max -10.09 --sr-epsilon 0.0001 --sr-omega-interval 1e-05 --sr-spectral-resolution 1E-5 --use-coulomb --coulomb-strength 1 --yukawa-mass 0.1 -y 0 -m 16000
echo ~/DiagHam_latest/build/FQHE/src/Programs/FQHEOnTorus/FQHETorusSpectralResponse /disk/data11/tfp/BartMadhav/project3.5/vectors_2/yukawa/n_9/fermions_torus_kysym_yukawa-1_n_9_2s_27_ratio_1.000000_ky_0.0.vec --sr-omega-min -11.309 --sr-omega-max -10.09 --sr-epsilon 0.0001 --sr-omega-interval 1e-05 --sr-spectral-resolution 1E-5 --use-coulomb --coulomb-strength 1 --yukawa-mass 1 -y 0 -m 16000
echo ~/DiagHam_latest/build/FQHE/src/Programs/FQHEOnTorus/FQHETorusSpectralResponse /disk/data11/tfp/BartMadhav/project3.5/vectors_2/yukawa/n_9/fermions_torus_kysym_yukawa-10_n_9_2s_27_ratio_1.000000_ky_0.0.vec --sr-omega-min -11.309 --sr-omega-max -10.09 --sr-epsilon 0.0001 --sr-omega-interval 1e-05 --sr-spectral-resolution 1E-5 --use-coulomb --coulomb-strength 1 --yukawa-mass 10 -y 0 -m 16000
echo ~/DiagHam_latest/build/FQHE/src/Programs/FQHEOnTorus/FQHETorusSpectralResponse /disk/data11/tfp/BartMadhav/project3.5/vectors_2/yukawa/n_9/fermions_torus_kysym_yukawa-100_n_9_2s_27_ratio_1.000000_ky_0.0.vec --sr-omega-min -11.309 --sr-omega-max -10.09 --sr-epsilon 0.0001 --sr-omega-interval 1e-05 --sr-spectral-resolution 1E-5 --use-coulomb --coulomb-strength 1 --yukawa-mass 100 -y 0 -m 16000
}
export -f runs
runs | nohup nice parallel -j 10 &