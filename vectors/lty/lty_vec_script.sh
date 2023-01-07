#!/bin/bash

runs() {
echo ~/DiagHam_latest/build/FQHE/src/Programs/FQHEOnTorus/FQHETorusFermionsCoulomb -p 6 -l 18 --landau-level 0 --coulomb-strength 1 --yukawa-mass 1000 --perturbation-file pseudopotentials_V1.dat --perturbation-strength 0 -g --use-lapack --eigenstate -n 1
echo ~/DiagHam_latest/build/FQHE/src/Programs/FQHEOnTorus/FQHETorusFermionsCoulomb -p 6 -l 18 --landau-level 0 --coulomb-strength 1 --yukawa-mass 10000 --perturbation-file pseudopotentials_V1.dat --perturbation-strength 0 -g --use-lapack --eigenstate -n 1
echo ~/DiagHam_latest/build/FQHE/src/Programs/FQHEOnTorus/FQHETorusFermionsCoulomb -p 7 -l 21 --landau-level 0 --coulomb-strength 1 --yukawa-mass 1000 --perturbation-file pseudopotentials_V1.dat --perturbation-strength 0 -g --use-lapack --eigenstate -n 1
echo ~/DiagHam_latest/build/FQHE/src/Programs/FQHEOnTorus/FQHETorusFermionsCoulomb -p 7 -l 21 --landau-level 0 --coulomb-strength 1 --yukawa-mass 10000 --perturbation-file pseudopotentials_V1.dat --perturbation-strength 0 -g --use-lapack --eigenstate -n 1
echo ~/DiagHam_latest/build/FQHE/src/Programs/FQHEOnTorus/FQHETorusFermionsCoulomb -p 8 -l 24 --landau-level 0 --coulomb-strength 1 --yukawa-mass 1000 --perturbation-file pseudopotentials_V1.dat --perturbation-strength 0 -g --use-lapack --eigenstate -n 1
echo ~/DiagHam_latest/build/FQHE/src/Programs/FQHEOnTorus/FQHETorusFermionsCoulomb -p 8 -l 24 --landau-level 0 --coulomb-strength 1 --yukawa-mass 10000 --perturbation-file pseudopotentials_V1.dat --perturbation-strength 0 -g --use-lapack --eigenstate -n 1
echo ~/DiagHam_latest/build/FQHE/src/Programs/FQHEOnTorus/FQHETorusFermionsCoulomb -p 9 -l 27 --landau-level 0 --coulomb-strength 1 --yukawa-mass 1000 --perturbation-file pseudopotentials_V1.dat --perturbation-strength 0 -g --use-lapack --eigenstate -n 1
echo ~/DiagHam_latest/build/FQHE/src/Programs/FQHEOnTorus/FQHETorusFermionsCoulomb -p 9 -l 27 --landau-level 0 --coulomb-strength 1 --yukawa-mass 10000 --perturbation-file pseudopotentials_V1.dat --perturbation-strength 0 -g --use-lapack --eigenstate -n 1
}
export -f runs
runs | nohup nice parallel -j 6 &

