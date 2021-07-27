#!/bin/bash

for i in {2..9..1}
do
~/DiagHam_latest/build/FQHE/src/Programs/FQHEOnTorus/FQHETorusFermionsCoulomb -p 6 -l 18 --landau-level 0 --coulomb-strength $(bc -l <<<"$i / 1000" | awk '{printf "%g\n", $0}') --perturbation-file pseudopotentials_V1.dat --perturbation-strength 1 -g --use-lapack --eigenstate -n 1
done
