#!/bin/bash

# generate the vec files
#for i in {2..10..1}
#do
#~/DiagHam_latest/build/FQHE/src/Programs/FQHEOnTorus/FQHETorusFermionsCoulomb -p 6 -l 18 --landau-level 0 --coulomb-strength $(bc -l <<<"$i / 10" | awk '{printf "%g\n", $0}') --perturbation-file pseudopotentials_V1.dat --perturbation-strength $(bc -l <<<"1 - $i / 10" | awk '{printf "%g\n", $0}') -g --use-lapack --eigenstate -n 1
#done
~/DiagHam_latest/build/FQHE/src/Programs/FQHEOnTorus/FQHETorusFermionsCoulomb -p 6 -l 18 --landau-level 0 --coulomb-strength 0.000126 --perturbation-file pseudopotentials_V1.dat --perturbation-strength 0.999874 -g --use-lapack --eigenstate -n 1
~/DiagHam_latest/build/FQHE/src/Programs/FQHEOnTorus/FQHETorusFermionsCoulomb -p 6 -l 18 --landau-level 0 --coulomb-strength 0.000158 --perturbation-file pseudopotentials_V1.dat --perturbation-strength 0.999842 -g --use-lapack --eigenstate -n 1
~/DiagHam_latest/build/FQHE/src/Programs/FQHEOnTorus/FQHETorusFermionsCoulomb -p 6 -l 18 --landau-level 0 --coulomb-strength 0.000200 --perturbation-file pseudopotentials_V1.dat --perturbation-strength 0.999800 -g --use-lapack --eigenstate -n 1
~/DiagHam_latest/build/FQHE/src/Programs/FQHEOnTorus/FQHETorusFermionsCoulomb -p 6 -l 18 --landau-level 0 --coulomb-strength 0.000251 --perturbation-file pseudopotentials_V1.dat --perturbation-strength 0.999749 -g --use-lapack --eigenstate -n 1
#~/DiagHam_latest/build/FQHE/src/Programs/FQHEOnTorus/FQHETorusFermionsCoulomb -p 6 -l 18 --landau-level 0 --coulomb-strength 0.000316 --perturbation-file pseudopotentials_V1.dat --perturbation-strength 0.999684 -g --use-lapack --eigenstate -n 1
~/DiagHam_latest/build/FQHE/src/Programs/FQHEOnTorus/FQHETorusFermionsCoulomb -p 6 -l 18 --landau-level 0 --coulomb-strength 0.000398 --perturbation-file pseudopotentials_V1.dat --perturbation-strength 0.999602 -g --use-lapack --eigenstate -n 1
~/DiagHam_latest/build/FQHE/src/Programs/FQHEOnTorus/FQHETorusFermionsCoulomb -p 6 -l 18 --landau-level 0 --coulomb-strength 0.000501 --perturbation-file pseudopotentials_V1.dat --perturbation-strength 0.999499 -g --use-lapack --eigenstate -n 1
~/DiagHam_latest/build/FQHE/src/Programs/FQHEOnTorus/FQHETorusFermionsCoulomb -p 6 -l 18 --landau-level 0 --coulomb-strength 0.000631 --perturbation-file pseudopotentials_V1.dat --perturbation-strength 0.999369 -g --use-lapack --eigenstate -n 1
~/DiagHam_latest/build/FQHE/src/Programs/FQHEOnTorus/FQHETorusFermionsCoulomb -p 6 -l 18 --landau-level 0 --coulomb-strength 0.000794 --perturbation-file pseudopotentials_V1.dat --perturbation-strength 0.999206 -g --use-lapack --eigenstate -n 1

~/DiagHam_latest/build/FQHE/src/Programs/FQHEOnTorus/FQHETorusFermionsCoulomb -p 6 -l 18 --landau-level 0 --coulomb-strength 0.00126 --perturbation-file pseudopotentials_V1.dat --perturbation-strength 0.99874 -g --use-lapack --eigenstate -n 1
~/DiagHam_latest/build/FQHE/src/Programs/FQHEOnTorus/FQHETorusFermionsCoulomb -p 6 -l 18 --landau-level 0 --coulomb-strength 0.00158 --perturbation-file pseudopotentials_V1.dat --perturbation-strength 0.99842 -g --use-lapack --eigenstate -n 1
~/DiagHam_latest/build/FQHE/src/Programs/FQHEOnTorus/FQHETorusFermionsCoulomb -p 6 -l 18 --landau-level 0 --coulomb-strength 0.00200 --perturbation-file pseudopotentials_V1.dat --perturbation-strength 0.99800 -g --use-lapack --eigenstate -n 1
~/DiagHam_latest/build/FQHE/src/Programs/FQHEOnTorus/FQHETorusFermionsCoulomb -p 6 -l 18 --landau-level 0 --coulomb-strength 0.00251 --perturbation-file pseudopotentials_V1.dat --perturbation-strength 0.99749 -g --use-lapack --eigenstate -n 1
#~/DiagHam_latest/build/FQHE/src/Programs/FQHEOnTorus/FQHETorusFermionsCoulomb -p 6 -l 18 --landau-level 0 --coulomb-strength 0.00316 --perturbation-file pseudopotentials_V1.dat --perturbation-strength 0.99684 -g --use-lapack --eigenstate -n 1
~/DiagHam_latest/build/FQHE/src/Programs/FQHEOnTorus/FQHETorusFermionsCoulomb -p 6 -l 18 --landau-level 0 --coulomb-strength 0.00398 --perturbation-file pseudopotentials_V1.dat --perturbation-strength 0.99602 -g --use-lapack --eigenstate -n 1
~/DiagHam_latest/build/FQHE/src/Programs/FQHEOnTorus/FQHETorusFermionsCoulomb -p 6 -l 18 --landau-level 0 --coulomb-strength 0.00501 --perturbation-file pseudopotentials_V1.dat --perturbation-strength 0.99499 -g --use-lapack --eigenstate -n 1
~/DiagHam_latest/build/FQHE/src/Programs/FQHEOnTorus/FQHETorusFermionsCoulomb -p 6 -l 18 --landau-level 0 --coulomb-strength 0.00631 --perturbation-file pseudopotentials_V1.dat --perturbation-strength 0.99369 -g --use-lapack --eigenstate -n 1
~/DiagHam_latest/build/FQHE/src/Programs/FQHEOnTorus/FQHETorusFermionsCoulomb -p 6 -l 18 --landau-level 0 --coulomb-strength 0.00794 --perturbation-file pseudopotentials_V1.dat --perturbation-strength 0.99206 -g --use-lapack --eigenstate -n 1

~/DiagHam_latest/build/FQHE/src/Programs/FQHEOnTorus/FQHETorusFermionsCoulomb -p 6 -l 18 --landau-level 0 --coulomb-strength 0.0126 --perturbation-file pseudopotentials_V1.dat --perturbation-strength 0.9874 -g --use-lapack --eigenstate -n 1
~/DiagHam_latest/build/FQHE/src/Programs/FQHEOnTorus/FQHETorusFermionsCoulomb -p 6 -l 18 --landau-level 0 --coulomb-strength 0.0158 --perturbation-file pseudopotentials_V1.dat --perturbation-strength 0.9842 -g --use-lapack --eigenstate -n 1
~/DiagHam_latest/build/FQHE/src/Programs/FQHEOnTorus/FQHETorusFermionsCoulomb -p 6 -l 18 --landau-level 0 --coulomb-strength 0.0200 --perturbation-file pseudopotentials_V1.dat --perturbation-strength 0.9800 -g --use-lapack --eigenstate -n 1
~/DiagHam_latest/build/FQHE/src/Programs/FQHEOnTorus/FQHETorusFermionsCoulomb -p 6 -l 18 --landau-level 0 --coulomb-strength 0.0251 --perturbation-file pseudopotentials_V1.dat --perturbation-strength 0.9749 -g --use-lapack --eigenstate -n 1
#~/DiagHam_latest/build/FQHE/src/Programs/FQHEOnTorus/FQHETorusFermionsCoulomb -p 6 -l 18 --landau-level 0 --coulomb-strength 0.0316 --perturbation-file pseudopotentials_V1.dat --perturbation-strength 0.9684 -g --use-lapack --eigenstate -n 1
~/DiagHam_latest/build/FQHE/src/Programs/FQHEOnTorus/FQHETorusFermionsCoulomb -p 6 -l 18 --landau-level 0 --coulomb-strength 0.0398 --perturbation-file pseudopotentials_V1.dat --perturbation-strength 0.9602 -g --use-lapack --eigenstate -n 1
~/DiagHam_latest/build/FQHE/src/Programs/FQHEOnTorus/FQHETorusFermionsCoulomb -p 6 -l 18 --landau-level 0 --coulomb-strength 0.0501 --perturbation-file pseudopotentials_V1.dat --perturbation-strength 0.9499 -g --use-lapack --eigenstate -n 1
~/DiagHam_latest/build/FQHE/src/Programs/FQHEOnTorus/FQHETorusFermionsCoulomb -p 6 -l 18 --landau-level 0 --coulomb-strength 0.0631 --perturbation-file pseudopotentials_V1.dat --perturbation-strength 0.9369 -g --use-lapack --eigenstate -n 1
~/DiagHam_latest/build/FQHE/src/Programs/FQHEOnTorus/FQHETorusFermionsCoulomb -p 6 -l 18 --landau-level 0 --coulomb-strength 0.0794 --perturbation-file pseudopotentials_V1.dat --perturbation-strength 0.9206 -g --use-lapack --eigenstate -n 1

~/DiagHam_latest/build/FQHE/src/Programs/FQHEOnTorus/FQHETorusFermionsCoulomb -p 6 -l 18 --landau-level 0 --coulomb-strength 0.126 --perturbation-file pseudopotentials_V1.dat --perturbation-strength 0.874 -g --use-lapack --eigenstate -n 1
~/DiagHam_latest/build/FQHE/src/Programs/FQHEOnTorus/FQHETorusFermionsCoulomb -p 6 -l 18 --landau-level 0 --coulomb-strength 0.158 --perturbation-file pseudopotentials_V1.dat --perturbation-strength 0.842 -g --use-lapack --eigenstate -n 1
~/DiagHam_latest/build/FQHE/src/Programs/FQHEOnTorus/FQHETorusFermionsCoulomb -p 6 -l 18 --landau-level 0 --coulomb-strength 0.200 --perturbation-file pseudopotentials_V1.dat --perturbation-strength 0.800 -g --use-lapack --eigenstate -n 1
~/DiagHam_latest/build/FQHE/src/Programs/FQHEOnTorus/FQHETorusFermionsCoulomb -p 6 -l 18 --landau-level 0 --coulomb-strength 0.251 --perturbation-file pseudopotentials_V1.dat --perturbation-strength 0.749 -g --use-lapack --eigenstate -n 1
#~/DiagHam_latest/build/FQHE/src/Programs/FQHEOnTorus/FQHETorusFermionsCoulomb -p 6 -l 18 --landau-level 0 --coulomb-strength 0.316 --perturbation-file pseudopotentials_V1.dat --perturbation-strength 0.684 -g --use-lapack --eigenstate -n 1
~/DiagHam_latest/build/FQHE/src/Programs/FQHEOnTorus/FQHETorusFermionsCoulomb -p 6 -l 18 --landau-level 0 --coulomb-strength 0.398 --perturbation-file pseudopotentials_V1.dat --perturbation-strength 0.602 -g --use-lapack --eigenstate -n 1
~/DiagHam_latest/build/FQHE/src/Programs/FQHEOnTorus/FQHETorusFermionsCoulomb -p 6 -l 18 --landau-level 0 --coulomb-strength 0.501 --perturbation-file pseudopotentials_V1.dat --perturbation-strength 0.499 -g --use-lapack --eigenstate -n 1
~/DiagHam_latest/build/FQHE/src/Programs/FQHEOnTorus/FQHETorusFermionsCoulomb -p 6 -l 18 --landau-level 0 --coulomb-strength 0.631 --perturbation-file pseudopotentials_V1.dat --perturbation-strength 0.369 -g --use-lapack --eigenstate -n 1
~/DiagHam_latest/build/FQHE/src/Programs/FQHEOnTorus/FQHETorusFermionsCoulomb -p 6 -l 18 --landau-level 0 --coulomb-strength 0.794 --perturbation-file pseudopotentials_V1.dat --perturbation-strength 0.206 -g --use-lapack --eigenstate -n 1



# delete all vec files other than ky=3
mkdir safe
mv *.dat safe
mv *ky_3* safe
rm *.vec
mv safe/* .
rm -r safe
