#!/bin/bash

# generate the vec files
for i in {1..10..1}
do
~/DiagHam_latest/build/FQHE/src/Programs/FQHEOnTorus/FQHETorusFermionsCoulomb -p 6 -l 18 --landau-level 0 --coulomb-strength $(bc -l <<<"$i / 10000" | awk '{printf "%g\n", $0}') --perturbation-file pseudopotentials_V1_reorth.dat --perturbation-strength $(bc -l <<<"1 - $i / 10000" | awk '{printf "%g\n", $0}') --force-reorthogonalize -g --use-lapack --eigenstate -n 1
done

# delete all vec files other than ky=3
mkdir safe
mv *.dat safe
mv *ky_3* safe
rm *.vec
mv safe/* .
rm -r safe
