#!/bin/bash

runs() {
for i in {2..98..2}
do
	KY=$(cat ../vectors/cpt/n_6/fermions_torus_kysym_coulomb_0_plus_CoulombPlane_trunc_"$i"_n_6_2s_18_ratio_1.000000.dat | sort -k2,2g | awk 'NR == 2 { print $1 }')
	# echo $KY
	echo ~/DiagHam_latest/build/FQHE/src/Programs/FQHEOnTorus/FQHETorusSpectralResponse ../vectors/cpt/n_6/fermions_torus_kysym_coulomb_0_plus_CoulombPlane_trunc_"$i"_n_6_2s_18_ratio_1.000000_ky_"$KY".0.vec --sr-omega-min -100 --sr-omega-max 100 --sr-epsilon 1E-4 --sr-omega-interval 1E-5 --sr-spectral-resolution 1E-5 --use-coulomb --coulomb-strength 0 --perturbation-file ../vectors/cpt/pseudopotentials_CoulombPlane.dat --perturbation-strength 1 --nbr-perturbation $i --sr-qy-momentum 0
done

KY=$(cat ../vectors/cpt/n_6/fermions_torus_kysym_coulomb_0_plus_CoulombPlane_n_6_2s_18_ratio_1.000000.dat | sort -k2,2g | awk 'NR == 2 { print $1 }')
# echo $KY
echo ~/DiagHam_latest/build/FQHE/src/Programs/FQHEOnTorus/FQHETorusSpectralResponse ../vectors/cpt/n_6/fermions_torus_kysym_coulomb_0_plus_CoulombPlane_n_6_2s_18_ratio_1.000000_ky_"$KY".0.vec --sr-omega-min -100 --sr-omega-max 100 --sr-epsilon 1E-4 --sr-omega-interval 1E-5 --sr-spectral-resolution 1E-5 --use-coulomb --coulomb-strength 0 --perturbation-file ../vectors/cpt/pseudopotentials_CoulombPlane.dat --perturbation-strength 1 --nbr-perturbation 100 --sr-qy-momentum 0
}
export -f runs
runs | nohup parallel -j 4 > nohup.out &
