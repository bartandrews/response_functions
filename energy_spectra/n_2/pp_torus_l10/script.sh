#!/bin/bash

for L in {6..62..2}
do
  echo $L
  ~/DiagHam_latest/build/FQHE/src/Programs/FQHEOnTorus/FQHETorusFermionsWithTranslations -p 2 -l $L --landau-level 0 --use-lapack --interaction-file pseudopotentials_YukawaPlaneL10_V1_only.dat -n 1000 --ratio 1;
  ~/DiagHam_latest/build/FQHE/src/Programs/FQHEOnTorus/FQHETorusFermionsWithTranslations -p 2 -l $L --landau-level 0 --use-lapack --interaction-file pseudopotentials_YukawaPlaneL10_V3_only.dat -n 1000 --ratio 1;
  ~/DiagHam_latest/build/FQHE/src/Programs/FQHEOnTorus/FQHETorusFermionsWithTranslations -p 2 -l $L --landau-level 0 --use-lapack --interaction-file pseudopotentials_YukawaPlaneL10_V5_only.dat -n 1000 --ratio 1;
  ~/DiagHam_latest/build/FQHE/src/Programs/FQHEOnTorus/FQHETorusFermionsWithTranslations -p 2 -l $L --landau-level 0 --use-lapack --interaction-file pseudopotentials_YukawaPlaneL10_V7_only.dat -n 1000 --ratio 1;
  ~/DiagHam_latest/build/FQHE/src/Programs/FQHEOnTorus/FQHETorusFermionsWithTranslations -p 2 -l $L --landau-level 0 --use-lapack --interaction-file pseudopotentials_YukawaPlaneL10_V9_only.dat -n 1000 --ratio 1;
  ~/DiagHam_latest/build/FQHE/src/Programs/FQHEOnTorus/FQHETorusFermionsWithTranslations -p 2 -l $L --landau-level 0 --use-lapack --interaction-file pseudopotentials_YukawaPlaneL10_V11_only.dat -n 1000 --ratio 1;
  ~/DiagHam_latest/build/FQHE/src/Programs/FQHEOnTorus/FQHETorusFermionsWithTranslations -p 2 -l $L --landau-level 0 --use-lapack --interaction-file pseudopotentials_YukawaPlaneL10_V13_only.dat -n 1000 --ratio 1;
  ~/DiagHam_latest/build/FQHE/src/Programs/FQHEOnTorus/FQHETorusFermionsWithTranslations -p 2 -l $L --landau-level 0 --use-lapack --interaction-file pseudopotentials_YukawaPlaneL10_V15_only.dat -n 1000 --ratio 1;
  ~/DiagHam_latest/build/FQHE/src/Programs/FQHEOnTorus/FQHETorusFermionsWithTranslations -p 2 -l $L --landau-level 0 --use-lapack --interaction-file pseudopotentials_YukawaPlaneL10_V17_only.dat -n 1000 --ratio 1
done
