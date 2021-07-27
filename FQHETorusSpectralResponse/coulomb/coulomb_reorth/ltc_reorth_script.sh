#!/bin/bash

runs() {
for i in {1..10..1}
do
	echo ~/DiagHam_latest/build/FQHE/src/Programs/FQHEOnTorus/FQHETorusSpectralResponse ../vectors/ltc/reorth/fermions_torus_kysym_coulomb_$(bc -l <<<"$i / 10000" | awk '{printf "%g\n", $0}')_plus_V1_reorth_scale_$(bc -l <<<"1 - $i / 10000" | awk '{printf "%g\n", $0}')_n_6_2s_18_ratio_1.000000_ky_3.0.vec --sr-omega-min -10 --sr-omega-max -9.992 --sr-epsilon 1E-6 --sr-omega-interval 1E-7 --sr-spectral-resolution 1E-4 --use-coulomb --coulomb-strength $(bc -l <<<"$i / 10000" | awk '{printf "%g\n", $0}') --perturbation-file ../vectors/ltc/reorth/pseudopotentials_V1_reorth.dat --perturbation-strength $(bc -l <<<"1 - $i / 10000" | awk '{printf "%g\n", $0}') --sr-qy-momentum 0
done
#echo ~/DiagHam_latest/build/FQHE/src/Programs/FQHEOnTorus/FQHETorusSpectralResponse ../vectors/ltc/reorth/fermions_torus_kysym_coulomb_plus_V1_scale_0_n_6_2s_18_ratio_1.000000_ky_3.0.vec --sr-omega-min -100 --sr-omega-max 100 --sr-epsilon 1E-4 --sr-omega-interval 1E-5 --sr-spectral-resolution 1E-5 --use-coulomb --coulomb-strength 1 --perturbation-file ../vectors/ltc/reorth/pseudopotentials_V1_reorth.dat --perturbation-strength 0 --sr-qy-momentum 0
}
export -f runs
runs | nohup parallel -j 4 > nohup.out &
