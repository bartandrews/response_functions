#!/bin/bash

runs() {
echo ~/DiagHam_latest/build/FQHE/src/Programs/FQHEOnTorus/FQHETorusFermionsTwoBodyGeneric -p 6 -l 18 --interaction-name V1 --interaction-file ~/PycharmProjects/response_functions/pseudopotentials/plane/pseudopotentials_V1.dat -g --use-lapack --eigenstate -n 1 -m 8000
}
export -f runs
runs | nohup nice parallel -j 4;
