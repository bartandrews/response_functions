#!/bin/bash

for i in {2..100..2}
do
~/DiagHam_latest/build/FQHE/src/Programs/FQHEOnTorus/FQHETorusFermionsCoulomb -p 6 -l 18 --landau-level 0 --coulomb-strength 0 --perturbation-file pseudopotentials_CoulombPlane.dat --perturbation-strength 1 --nbr-perturbation $i -g --use-lapack --eigenstate -n 1
done
