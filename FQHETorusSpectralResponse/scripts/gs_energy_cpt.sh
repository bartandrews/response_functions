#!/bin/bash

rm -f gs_energy_cpt.dat
for m in {2..98..2}
do
	KY_CPT=$(cat ../vectors/cpt/n_6/fermions_torus_kysym_coulomb_0_plus_CoulombPlane_trunc_"$m"_n_6_2s_18_ratio_1.000000.dat | sort -k2,2g | awk 'NR == 2 { print $1 }')
	GS_CPT=$(cat ../vectors/cpt/n_6/fermions_torus_kysym_coulomb_0_plus_CoulombPlane_trunc_"$m"_n_6_2s_18_ratio_1.000000.dat | sort -k2,2g | awk 'NR == 2 { print $2 }')
	KY_YPTL0P0001=$(cat ../vectors/ypt/l0p0001/fermions_torus_kysym_coulomb_0_plus_YukawaPlaneL0.0001_trunc_"$m"_n_6_2s_18_ratio_1.000000.dat | sort -k2,2g | awk 'NR == 2 { print $1 }')
	GS_YPTL0P0001=$(cat ../vectors/ypt/l0p0001/fermions_torus_kysym_coulomb_0_plus_YukawaPlaneL0.0001_trunc_"$m"_n_6_2s_18_ratio_1.000000.dat | sort -k2,2g | awk 'NR == 2 { print $2 }')
	KY_YPTL0P001=$(cat ../vectors/ypt/l0p001/fermions_torus_kysym_coulomb_0_plus_YukawaPlaneL0.001_trunc_"$m"_n_6_2s_18_ratio_1.000000.dat | sort -k2,2g | awk 'NR == 2 { print $1 }')
	GS_YPTL0P001=$(cat ../vectors/ypt/l0p001/fermions_torus_kysym_coulomb_0_plus_YukawaPlaneL0.001_trunc_"$m"_n_6_2s_18_ratio_1.000000.dat | sort -k2,2g | awk 'NR == 2 { print $2 }')
	KY_YPTL0P01=$(cat ../vectors/ypt/l0p01/fermions_torus_kysym_coulomb_0_plus_YukawaPlaneL0.01_trunc_"$m"_n_6_2s_18_ratio_1.000000.dat | sort -k2,2g | awk 'NR == 2 { print $1 }')
	GS_YPTL0P01=$(cat ../vectors/ypt/l0p01/fermions_torus_kysym_coulomb_0_plus_YukawaPlaneL0.01_trunc_"$m"_n_6_2s_18_ratio_1.000000.dat | sort -k2,2g | awk 'NR == 2 { print $2 }')
	KY_YPTL0P1=$(cat ../vectors/ypt/l0p1/fermions_torus_kysym_coulomb_0_plus_YukawaPlaneL0.1_trunc_"$m"_n_6_2s_18_ratio_1.000000.dat | sort -k2,2g | awk 'NR == 2 { print $1 }')
	GS_YPTL0P1=$(cat ../vectors/ypt/l0p1/fermions_torus_kysym_coulomb_0_plus_YukawaPlaneL0.1_trunc_"$m"_n_6_2s_18_ratio_1.000000.dat | sort -k2,2g | awk 'NR == 2 { print $2 }')
	KY_YPTL1=$(cat ../vectors/ypt/l1/fermions_torus_kysym_coulomb_0_plus_YukawaPlaneL1_trunc_"$m"_n_6_2s_18_ratio_1.000000.dat | sort -k2,2g | awk 'NR == 2 { print $1 }')
	GS_YPTL1=$(cat ../vectors/ypt/l1/fermions_torus_kysym_coulomb_0_plus_YukawaPlaneL1_trunc_"$m"_n_6_2s_18_ratio_1.000000.dat | sort -k2,2g | awk 'NR == 2 { print $2 }')
	KY_YPTL10=$(cat ../vectors/ypt/l10/fermions_torus_kysym_coulomb_0_plus_YukawaPlaneL10_trunc_"$m"_n_6_2s_18_ratio_1.000000.dat | sort -k2,2g | awk 'NR == 2 { print $1 }')
	GS_YPTL10=$(cat ../vectors/ypt/l10/fermions_torus_kysym_coulomb_0_plus_YukawaPlaneL10_trunc_"$m"_n_6_2s_18_ratio_1.000000.dat | sort -k2,2g | awk 'NR == 2 { print $2 }')
	printf "%i \t %.15f \t %.15f \t %.15f \t %.15f \t %.15f \t %.15f \t %.15f \n" $m $GS_CPT $GS_YPTL0P0001 $GS_YPTL0P001 $GS_YPTL0P01 $GS_YPTL0P1 $GS_YPTL1 $GS_YPTL10 >> gs_energy_cpt.dat
done
KY_CPT=$(cat ../vectors/cpt/n_6/fermions_torus_kysym_coulomb_0_plus_CoulombPlane_n_6_2s_18_ratio_1.000000.dat | sort -k2,2g | awk 'NR == 2 { print $1 }')
GS_CPT=$(cat ../vectors/cpt/n_6/fermions_torus_kysym_coulomb_0_plus_CoulombPlane_n_6_2s_18_ratio_1.000000.dat | sort -k2,2g | awk 'NR == 2 { print $2 }')
KY_YPTL0P0001=$(cat ../vectors/ypt/l0p0001/fermions_torus_kysym_coulomb_0_plus_YukawaPlaneL0.0001_n_6_2s_18_ratio_1.000000.dat | sort -k2,2g | awk 'NR == 2 { print $1 }')
GS_YPTL0P0001=$(cat ../vectors/ypt/l0p0001/fermions_torus_kysym_coulomb_0_plus_YukawaPlaneL0.0001_n_6_2s_18_ratio_1.000000.dat | sort -k2,2g | awk 'NR == 2 { print $2 }')
KY_YPTL0P001=$(cat ../vectors/ypt/l0p001/fermions_torus_kysym_coulomb_0_plus_YukawaPlaneL0.001_n_6_2s_18_ratio_1.000000.dat | sort -k2,2g | awk 'NR == 2 { print $1 }')
GS_YPTL0P001=$(cat ../vectors/ypt/l0p001/fermions_torus_kysym_coulomb_0_plus_YukawaPlaneL0.001_n_6_2s_18_ratio_1.000000.dat | sort -k2,2g | awk 'NR == 2 { print $2 }')
KY_YPTL0P01=$(cat ../vectors/ypt/l0p01/fermions_torus_kysym_coulomb_0_plus_YukawaPlaneL0.01_n_6_2s_18_ratio_1.000000.dat | sort -k2,2g | awk 'NR == 2 { print $1 }')
GS_YPTL0P01=$(cat ../vectors/ypt/l0p01/fermions_torus_kysym_coulomb_0_plus_YukawaPlaneL0.01_n_6_2s_18_ratio_1.000000.dat | sort -k2,2g | awk 'NR == 2 { print $2 }')
KY_YPTL0P1=$(cat ../vectors/ypt/l0p1/fermions_torus_kysym_coulomb_0_plus_YukawaPlaneL0.1_n_6_2s_18_ratio_1.000000.dat | sort -k2,2g | awk 'NR == 2 { print $1 }')
GS_YPTL0P1=$(cat ../vectors/ypt/l0p1/fermions_torus_kysym_coulomb_0_plus_YukawaPlaneL0.1_n_6_2s_18_ratio_1.000000.dat | sort -k2,2g | awk 'NR == 2 { print $2 }')
KY_YPTL1=$(cat ../vectors/ypt/l1/fermions_torus_kysym_coulomb_0_plus_YukawaPlaneL1_n_6_2s_18_ratio_1.000000.dat | sort -k2,2g | awk 'NR == 2 { print $1 }')
GS_YPTL1=$(cat ../vectors/ypt/l1/fermions_torus_kysym_coulomb_0_plus_YukawaPlaneL1_n_6_2s_18_ratio_1.000000.dat | sort -k2,2g | awk 'NR == 2 { print $2 }')
KY_YPTL10=$(cat ../vectors/ypt/l10/fermions_torus_kysym_coulomb_0_plus_YukawaPlaneL10_n_6_2s_18_ratio_1.000000.dat | sort -k2,2g | awk 'NR == 2 { print $1 }')
GS_YPTL10=$(cat ../vectors/ypt/l10/fermions_torus_kysym_coulomb_0_plus_YukawaPlaneL10_n_6_2s_18_ratio_1.000000.dat | sort -k2,2g | awk 'NR == 2 { print $2 }')
printf "%i \t %.15f \t %.15f \t %.15f \t %.15f \t %.15f \t %.15f \t %.15f \n" $m $GS_CPT $GS_YPTL0P0001 $GS_YPTL0P001 $GS_YPTL0P01 $GS_YPTL0P1 $GS_YPTL1 $GS_YPTL10 >> gs_energy_cpt.dat
