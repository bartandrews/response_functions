#!/bin/bash

runs() {
echo ~/DiagHam_latest/build/FQHE/src/Programs/FQHEOnTorus/FQHETorusFermionsCoulomb -p 8 -l 24 --landau-level 0 --coulomb-strength 0 --perturbation-file ~/PycharmProjects/response_functions/pseudopotentials/plane/pseudopotentials_YukawaPlaneL0.1.dat --perturbation-strength 1 --nbr-perturbation 2 -g --use-lapack --eigenstate -n 1 -m 8000
echo ~/DiagHam_latest/build/FQHE/src/Programs/FQHEOnTorus/FQHETorusFermionsCoulomb -p 8 -l 24 --landau-level 0 --coulomb-strength 0 --perturbation-file ~/PycharmProjects/response_functions/pseudopotentials/plane/pseudopotentials_YukawaPlaneL0.1.dat --perturbation-strength 1 --nbr-perturbation 4 -g --use-lapack --eigenstate -n 1 -m 8000
echo ~/DiagHam_latest/build/FQHE/src/Programs/FQHEOnTorus/FQHETorusFermionsCoulomb -p 8 -l 24 --landau-level 0 --coulomb-strength 0 --perturbation-file ~/PycharmProjects/response_functions/pseudopotentials/plane/pseudopotentials_YukawaPlaneL0.1.dat --perturbation-strength 1 --nbr-perturbation 6 -g --use-lapack --eigenstate -n 1 -m 8000
echo ~/DiagHam_latest/build/FQHE/src/Programs/FQHEOnTorus/FQHETorusFermionsCoulomb -p 8 -l 24 --landau-level 0 --coulomb-strength 0 --perturbation-file ~/PycharmProjects/response_functions/pseudopotentials/plane/pseudopotentials_YukawaPlaneL0.1.dat --perturbation-strength 1 --nbr-perturbation 8 -g --use-lapack --eigenstate -n 1 -m 8000
echo ~/DiagHam_latest/build/FQHE/src/Programs/FQHEOnTorus/FQHETorusFermionsCoulomb -p 8 -l 24 --landau-level 0 --coulomb-strength 0 --perturbation-file ~/PycharmProjects/response_functions/pseudopotentials/plane/pseudopotentials_YukawaPlaneL0.1.dat --perturbation-strength 1 --nbr-perturbation 10 -g --use-lapack --eigenstate -n 1 -m 8000
echo ~/DiagHam_latest/build/FQHE/src/Programs/FQHEOnTorus/FQHETorusFermionsCoulomb -p 8 -l 24 --landau-level 0 --coulomb-strength 0 --perturbation-file ~/PycharmProjects/response_functions/pseudopotentials/plane/pseudopotentials_YukawaPlaneL0.1.dat --perturbation-strength 1 --nbr-perturbation 12 -g --use-lapack --eigenstate -n 1 -m 8000
echo ~/DiagHam_latest/build/FQHE/src/Programs/FQHEOnTorus/FQHETorusFermionsCoulomb -p 8 -l 24 --landau-level 0 --coulomb-strength 0 --perturbation-file ~/PycharmProjects/response_functions/pseudopotentials/plane/pseudopotentials_YukawaPlaneL0.1.dat --perturbation-strength 1 --nbr-perturbation 14 -g --use-lapack --eigenstate -n 1 -m 8000
echo ~/DiagHam_latest/build/FQHE/src/Programs/FQHEOnTorus/FQHETorusFermionsCoulomb -p 8 -l 24 --landau-level 0 --coulomb-strength 0 --perturbation-file ~/PycharmProjects/response_functions/pseudopotentials/plane/pseudopotentials_YukawaPlaneL0.1.dat --perturbation-strength 1 --nbr-perturbation 16 -g --use-lapack --eigenstate -n 1 -m 8000
}
export -f runs
runs | nohup nice parallel -j 4 &
