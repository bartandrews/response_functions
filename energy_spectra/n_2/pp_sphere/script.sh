#!/bin/bash

for L in {18..36..2}
do
  echo $L
  ~/DiagHam_latest/build/FQHE/src/Programs/FQHEOnSphere/FQHESphereFermionsTwoBodyGeneric -p 2 -l $L --use-lapack --interaction-file pseudopotential_coulomb_l_0_2s_18.dat -n 1000
done
