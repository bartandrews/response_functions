#!/bin/bash

runs() {
echo ~/DiagHam_latest/build/FQHE/src/Programs/FQHEOnTorus/FQHETorusFermionsCoulomb -p 6 -l 18 --landau-level 0 --coulomb-strength 1 -g --use-lapack --eigenstate -n 1 -m 8000
}
export -f runs
runs | nohup nice parallel -j 4;
