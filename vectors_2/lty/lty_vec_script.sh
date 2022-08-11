#!/bin/bash

runs() {
echo ~/DiagHam_latest/build/FQHE/src/Programs/FQHEOnTorus/FQHETorusFermionsCoulomb -p 9 -l 27 --landau-level 0 --coulomb-strength 1 --yukawa-mass 0.0001 --perturbation-file ~/PycharmProjects/response_functions/pseudopotentials/plane/pseudopotentials_V1.dat --perturbation-strength 0 -g --use-lapack --eigenstate -n 1 -m 8000
echo ~/DiagHam_latest/build/FQHE/src/Programs/FQHEOnTorus/FQHETorusFermionsCoulomb -p 9 -l 27 --landau-level 0 --coulomb-strength 1 --yukawa-mass 0.001 --perturbation-file ~/PycharmProjects/response_functions/pseudopotentials/plane/pseudopotentials_V1.dat --perturbation-strength 0 -g --use-lapack --eigenstate -n 1 -m 8000
echo ~/DiagHam_latest/build/FQHE/src/Programs/FQHEOnTorus/FQHETorusFermionsCoulomb -p 9 -l 27 --landau-level 0 --coulomb-strength 1 --yukawa-mass 0.01 --perturbation-file ~/PycharmProjects/response_functions/pseudopotentials/plane/pseudopotentials_V1.dat --perturbation-strength 0 -g --use-lapack --eigenstate -n 1 -m 8000
echo ~/DiagHam_latest/build/FQHE/src/Programs/FQHEOnTorus/FQHETorusFermionsCoulomb -p 9 -l 27 --landau-level 0 --coulomb-strength 1 --yukawa-mass 0.1 --perturbation-file ~/PycharmProjects/response_functions/pseudopotentials/plane/pseudopotentials_V1.dat --perturbation-strength 0 -g --use-lapack --eigenstate -n 1 -m 8000
echo ~/DiagHam_latest/build/FQHE/src/Programs/FQHEOnTorus/FQHETorusFermionsCoulomb -p 9 -l 27 --landau-level 0 --coulomb-strength 1 --yukawa-mass 1 --perturbation-file ~/PycharmProjects/response_functions/pseudopotentials/plane/pseudopotentials_V1.dat --perturbation-strength 0 -g --use-lapack --eigenstate -n 1 -m 8000
echo ~/DiagHam_latest/build/FQHE/src/Programs/FQHEOnTorus/FQHETorusFermionsCoulomb -p 9 -l 27 --landau-level 0 --coulomb-strength 1 --yukawa-mass 10 --perturbation-file ~/PycharmProjects/response_functions/pseudopotentials/plane/pseudopotentials_V1.dat --perturbation-strength 0 -g --use-lapack --eigenstate -n 1 -m 8000
echo ~/DiagHam_latest/build/FQHE/src/Programs/FQHEOnTorus/FQHETorusFermionsCoulomb -p 9 -l 27 --landau-level 0 --coulomb-strength 1 --yukawa-mass 100 --perturbation-file ~/PycharmProjects/response_functions/pseudopotentials/plane/pseudopotentials_V1.dat --perturbation-strength 0 -g --use-lapack --eigenstate -n 1 -m 8000
}
export -f runs
runs | nohup nice parallel -j 4 &
