#!/bin/bash

for i in {2..11..2}
do
nohup nice ~/DiagHam_latest/build/FQHE/src/Programs/FQHEOnTorus/FQHETorusFermionsCoulomb -p 7 -l 21 --landau-level 0 --coulomb-strength 0 --perturbation-file ~/PycharmProjects/response_functions/vectors/ypt/pseudopotentials_YukawaPlaneL1.dat --perturbation-strength 1 --nbr-perturbation $i -g --use-lapack --eigenstate -n 1 &
done
