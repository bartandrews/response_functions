#!/bin/bash

for L in {6..62..2}
do
  echo $L
  ~/DiagHam_latest/build/FQHE/src/Programs/FQHEOnTorus/FQHETorusFermionsWithTranslations -p 2 -l $L --landau-level 0 --use-lapack --interaction-file pseudopotentials_CoulombPlane_V19_only.dat -n 1000 --ratio 1
done
