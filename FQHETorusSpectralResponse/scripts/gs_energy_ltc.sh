#!/bin/bash

rm -f gs_energy_ltc.dat

ALPHA=$(bc ~/.bcrc -l <<<"pow(10,-4)" | awk '{printf "%.15f\n", $0}')
echo $ALPHA
KY_LTC=$(cat ~/PycharmProjects/response_functions/vectors/ltc/fermions_torus_kysym_coulomb_0.0001_plus_V1_scale_0.9999_n_6_2s_18_ratio_1.000000.dat | sort -k2,2g | awk 'NR == 2 { print $1 }')
GS_LTC=$(cat ~/PycharmProjects/response_functions/vectors/ltc/fermions_torus_kysym_coulomb_0.0001_plus_V1_scale_0.9999_n_6_2s_18_ratio_1.000000.dat | sort -k2,2g | awk 'NR == 2 { print $2 }')
printf "%.15f \t %.15f \t %.15f \n" $ALPHA $GS_LTC $KY_LTC >> gs_energy_ltc.dat
ALPHA=$(bc ~/.bcrc -l <<<"pow(10,-3.9)" | awk '{printf "%.15f\n", $0}')
echo $ALPHA
KY_LTC=$(cat ~/PycharmProjects/response_functions/vectors/ltc/fermions_torus_kysym_coulomb_0.000126_plus_V1_scale_0.999874_n_6_2s_18_ratio_1.000000.dat | sort -k2,2g | awk 'NR == 2 { print $1 }')
GS_LTC=$(cat ~/PycharmProjects/response_functions/vectors/ltc/fermions_torus_kysym_coulomb_0.000126_plus_V1_scale_0.999874_n_6_2s_18_ratio_1.000000.dat | sort -k2,2g | awk 'NR == 2 { print $2 }')
printf "%.15f \t %.15f \t %.15f \n" $ALPHA $GS_LTC $KY_LTC >> gs_energy_ltc.dat
ALPHA=$(bc ~/.bcrc -l <<<"pow(10,-3.8)" | awk '{printf "%.15f\n", $0}')
echo $ALPHA
KY_LTC=$(cat ~/PycharmProjects/response_functions/vectors/ltc/fermions_torus_kysym_coulomb_0.000158_plus_V1_scale_0.999842_n_6_2s_18_ratio_1.000000.dat | sort -k2,2g | awk 'NR == 2 { print $1 }')
GS_LTC=$(cat ~/PycharmProjects/response_functions/vectors/ltc/fermions_torus_kysym_coulomb_0.000158_plus_V1_scale_0.999842_n_6_2s_18_ratio_1.000000.dat | sort -k2,2g | awk 'NR == 2 { print $2 }')
printf "%.15f \t %.15f \t %.15f \n" $ALPHA $GS_LTC $KY_LTC >> gs_energy_ltc.dat
ALPHA=$(bc ~/.bcrc -l <<<"pow(10,-3.7)" | awk '{printf "%.15f\n", $0}')
echo $ALPHA
KY_LTC=$(cat ~/PycharmProjects/response_functions/vectors/ltc/fermions_torus_kysym_coulomb_0.0002_plus_V1_scale_0.9998_n_6_2s_18_ratio_1.000000.dat | sort -k2,2g | awk 'NR == 2 { print $1 }')
GS_LTC=$(cat ~/PycharmProjects/response_functions/vectors/ltc/fermions_torus_kysym_coulomb_0.0002_plus_V1_scale_0.9998_n_6_2s_18_ratio_1.000000.dat | sort -k2,2g | awk 'NR == 2 { print $2 }')
printf "%.15f \t %.15f \t %.15f \n" $ALPHA $GS_LTC $KY_LTC >> gs_energy_ltc.dat
ALPHA=$(bc ~/.bcrc -l <<<"pow(10,-3.6)" | awk '{printf "%.15f\n", $0}')
echo $ALPHA
KY_LTC=$(cat ~/PycharmProjects/response_functions/vectors/ltc/fermions_torus_kysym_coulomb_0.000251_plus_V1_scale_0.999749_n_6_2s_18_ratio_1.000000.dat | sort -k2,2g | awk 'NR == 2 { print $1 }')
GS_LTC=$(cat ~/PycharmProjects/response_functions/vectors/ltc/fermions_torus_kysym_coulomb_0.000251_plus_V1_scale_0.999749_n_6_2s_18_ratio_1.000000.dat | sort -k2,2g | awk 'NR == 2 { print $2 }')
printf "%.15f \t %.15f \t %.15f \n" $ALPHA $GS_LTC $KY_LTC >> gs_energy_ltc.dat
ALPHA=$(bc ~/.bcrc -l <<<"pow(10,-3.5)" | awk '{printf "%.15f\n", $0}')
echo $ALPHA
KY_LTC=$(cat ~/PycharmProjects/response_functions/vectors/ltc/fermions_torus_kysym_coulomb_0.000316_plus_V1_scale_0.999684_n_6_2s_18_ratio_1.000000.dat | sort -k2,2g | awk 'NR == 2 { print $1 }')
GS_LTC=$(cat ~/PycharmProjects/response_functions/vectors/ltc/fermions_torus_kysym_coulomb_0.000316_plus_V1_scale_0.999684_n_6_2s_18_ratio_1.000000.dat | sort -k2,2g | awk 'NR == 2 { print $2 }')
printf "%.15f \t %.15f \t %.15f \n" $ALPHA $GS_LTC $KY_LTC >> gs_energy_ltc.dat
ALPHA=$(bc ~/.bcrc -l <<<"pow(10,-3.4)" | awk '{printf "%.15f\n", $0}')
echo $ALPHA
KY_LTC=$(cat ~/PycharmProjects/response_functions/vectors/ltc/fermions_torus_kysym_coulomb_0.000398_plus_V1_scale_0.999602_n_6_2s_18_ratio_1.000000.dat | sort -k2,2g | awk 'NR == 2 { print $1 }')
GS_LTC=$(cat ~/PycharmProjects/response_functions/vectors/ltc/fermions_torus_kysym_coulomb_0.000398_plus_V1_scale_0.999602_n_6_2s_18_ratio_1.000000.dat | sort -k2,2g | awk 'NR == 2 { print $2 }')
printf "%.15f \t %.15f \t %.15f \n" $ALPHA $GS_LTC $KY_LTC >> gs_energy_ltc.dat
ALPHA=$(bc ~/.bcrc -l <<<"pow(10,-3.3)" | awk '{printf "%.15f\n", $0}')
echo $ALPHA
KY_LTC=$(cat ~/PycharmProjects/response_functions/vectors/ltc/fermions_torus_kysym_coulomb_0.000501_plus_V1_scale_0.999499_n_6_2s_18_ratio_1.000000.dat | sort -k2,2g | awk 'NR == 2 { print $1 }')
GS_LTC=$(cat ~/PycharmProjects/response_functions/vectors/ltc/fermions_torus_kysym_coulomb_0.000501_plus_V1_scale_0.999499_n_6_2s_18_ratio_1.000000.dat | sort -k2,2g | awk 'NR == 2 { print $2 }')
printf "%.15f \t %.15f \t %.15f \n" $ALPHA $GS_LTC $KY_LTC >> gs_energy_ltc.dat
ALPHA=$(bc ~/.bcrc -l <<<"pow(10,-3.2)" | awk '{printf "%.15f\n", $0}')
echo $ALPHA
KY_LTC=$(cat ~/PycharmProjects/response_functions/vectors/ltc/fermions_torus_kysym_coulomb_0.000631_plus_V1_scale_0.999369_n_6_2s_18_ratio_1.000000.dat | sort -k2,2g | awk 'NR == 2 { print $1 }')
GS_LTC=$(cat ~/PycharmProjects/response_functions/vectors/ltc/fermions_torus_kysym_coulomb_0.000631_plus_V1_scale_0.999369_n_6_2s_18_ratio_1.000000.dat | sort -k2,2g | awk 'NR == 2 { print $2 }')
printf "%.15f \t %.15f \t %.15f \n" $ALPHA $GS_LTC $KY_LTC >> gs_energy_ltc.dat
ALPHA=$(bc ~/.bcrc -l <<<"pow(10,-3.1)" | awk '{printf "%.15f\n", $0}')
echo $ALPHA
KY_LTC=$(cat ~/PycharmProjects/response_functions/vectors/ltc/fermions_torus_kysym_coulomb_0.000794_plus_V1_scale_0.999206_n_6_2s_18_ratio_1.000000.dat | sort -k2,2g | awk 'NR == 2 { print $1 }')
GS_LTC=$(cat ~/PycharmProjects/response_functions/vectors/ltc/fermions_torus_kysym_coulomb_0.000794_plus_V1_scale_0.999206_n_6_2s_18_ratio_1.000000.dat | sort -k2,2g | awk 'NR == 2 { print $2 }')
printf "%.15f \t %.15f \t %.15f \n" $ALPHA $GS_LTC $KY_LTC >> gs_energy_ltc.dat
########################################################################################################################
ALPHA=$(bc ~/.bcrc -l <<<"pow(10,-3)" | awk '{printf "%.15f\n", $0}')
echo $ALPHA
KY_LTC=$(cat ~/PycharmProjects/response_functions/vectors/ltc/fermions_torus_kysym_coulomb_0.001_plus_V1_scale_0.999_n_6_2s_18_ratio_1.000000.dat | sort -k2,2g | awk 'NR == 2 { print $1 }')
GS_LTC=$(cat ~/PycharmProjects/response_functions/vectors/ltc/fermions_torus_kysym_coulomb_0.001_plus_V1_scale_0.999_n_6_2s_18_ratio_1.000000.dat | sort -k2,2g | awk 'NR == 2 { print $2 }')
printf "%.15f \t %.15f \t %.15f \n" $ALPHA $GS_LTC $KY_LTC >> gs_energy_ltc.dat
ALPHA=$(bc ~/.bcrc -l <<<"pow(10,-2.9)" | awk '{printf "%.15f\n", $0}')
echo $ALPHA
KY_LTC=$(cat ~/PycharmProjects/response_functions/vectors/ltc/fermions_torus_kysym_coulomb_0.00126_plus_V1_scale_0.99874_n_6_2s_18_ratio_1.000000.dat | sort -k2,2g | awk 'NR == 2 { print $1 }')
GS_LTC=$(cat ~/PycharmProjects/response_functions/vectors/ltc/fermions_torus_kysym_coulomb_0.00126_plus_V1_scale_0.99874_n_6_2s_18_ratio_1.000000.dat | sort -k2,2g | awk 'NR == 2 { print $2 }')
printf "%.15f \t %.15f \t %.15f \n" $ALPHA $GS_LTC $KY_LTC >> gs_energy_ltc.dat
ALPHA=$(bc ~/.bcrc -l <<<"pow(10,-2.8)" | awk '{printf "%.15f\n", $0}')
echo $ALPHA
KY_LTC=$(cat ~/PycharmProjects/response_functions/vectors/ltc/fermions_torus_kysym_coulomb_0.00158_plus_V1_scale_0.99842_n_6_2s_18_ratio_1.000000.dat | sort -k2,2g | awk 'NR == 2 { print $1 }')
GS_LTC=$(cat ~/PycharmProjects/response_functions/vectors/ltc/fermions_torus_kysym_coulomb_0.00158_plus_V1_scale_0.99842_n_6_2s_18_ratio_1.000000.dat | sort -k2,2g | awk 'NR == 2 { print $2 }')
printf "%.15f \t %.15f \t %.15f \n" $ALPHA $GS_LTC $KY_LTC >> gs_energy_ltc.dat
ALPHA=$(bc ~/.bcrc -l <<<"pow(10,-2.7)" | awk '{printf "%.15f\n", $0}')
echo $ALPHA
KY_LTC=$(cat ~/PycharmProjects/response_functions/vectors/ltc/fermions_torus_kysym_coulomb_0.002_plus_V1_scale_0.998_n_6_2s_18_ratio_1.000000.dat | sort -k2,2g | awk 'NR == 2 { print $1 }')
GS_LTC=$(cat ~/PycharmProjects/response_functions/vectors/ltc/fermions_torus_kysym_coulomb_0.002_plus_V1_scale_0.998_n_6_2s_18_ratio_1.000000.dat | sort -k2,2g | awk 'NR == 2 { print $2 }')
printf "%.15f \t %.15f \t %.15f \n" $ALPHA $GS_LTC $KY_LTC >> gs_energy_ltc.dat
ALPHA=$(bc ~/.bcrc -l <<<"pow(10,-2.6)" | awk '{printf "%.15f\n", $0}')
echo $ALPHA
KY_LTC=$(cat ~/PycharmProjects/response_functions/vectors/ltc/fermions_torus_kysym_coulomb_0.00251_plus_V1_scale_0.99749_n_6_2s_18_ratio_1.000000.dat | sort -k2,2g | awk 'NR == 2 { print $1 }')
GS_LTC=$(cat ~/PycharmProjects/response_functions/vectors/ltc/fermions_torus_kysym_coulomb_0.00251_plus_V1_scale_0.99749_n_6_2s_18_ratio_1.000000.dat | sort -k2,2g | awk 'NR == 2 { print $2 }')
printf "%.15f \t %.15f \t %.15f \n" $ALPHA $GS_LTC $KY_LTC >> gs_energy_ltc.dat
ALPHA=$(bc ~/.bcrc -l <<<"pow(10,-2.5)" | awk '{printf "%.15f\n", $0}')
echo $ALPHA
KY_LTC=$(cat ~/PycharmProjects/response_functions/vectors/ltc/fermions_torus_kysym_coulomb_0.00316_plus_V1_scale_0.99684_n_6_2s_18_ratio_1.000000.dat | sort -k2,2g | awk 'NR == 2 { print $1 }')
GS_LTC=$(cat ~/PycharmProjects/response_functions/vectors/ltc/fermions_torus_kysym_coulomb_0.00316_plus_V1_scale_0.99684_n_6_2s_18_ratio_1.000000.dat | sort -k2,2g | awk 'NR == 2 { print $2 }')
printf "%.15f \t %.15f \t %.15f \n" $ALPHA $GS_LTC $KY_LTC >> gs_energy_ltc.dat
ALPHA=$(bc ~/.bcrc -l <<<"pow(10,-2.4)" | awk '{printf "%.15f\n", $0}')
echo $ALPHA
KY_LTC=$(cat ~/PycharmProjects/response_functions/vectors/ltc/fermions_torus_kysym_coulomb_0.00398_plus_V1_scale_0.99602_n_6_2s_18_ratio_1.000000.dat | sort -k2,2g | awk 'NR == 2 { print $1 }')
GS_LTC=$(cat ~/PycharmProjects/response_functions/vectors/ltc/fermions_torus_kysym_coulomb_0.00398_plus_V1_scale_0.99602_n_6_2s_18_ratio_1.000000.dat | sort -k2,2g | awk 'NR == 2 { print $2 }')
printf "%.15f \t %.15f \t %.15f \n" $ALPHA $GS_LTC $KY_LTC >> gs_energy_ltc.dat
ALPHA=$(bc ~/.bcrc -l <<<"pow(10,-2.3)" | awk '{printf "%.15f\n", $0}')
echo $ALPHA
KY_LTC=$(cat ~/PycharmProjects/response_functions/vectors/ltc/fermions_torus_kysym_coulomb_0.00501_plus_V1_scale_0.99499_n_6_2s_18_ratio_1.000000.dat | sort -k2,2g | awk 'NR == 2 { print $1 }')
GS_LTC=$(cat ~/PycharmProjects/response_functions/vectors/ltc/fermions_torus_kysym_coulomb_0.00501_plus_V1_scale_0.99499_n_6_2s_18_ratio_1.000000.dat | sort -k2,2g | awk 'NR == 2 { print $2 }')
printf "%.15f \t %.15f \t %.15f \n" $ALPHA $GS_LTC $KY_LTC >> gs_energy_ltc.dat
ALPHA=$(bc ~/.bcrc -l <<<"pow(10,-2.2)" | awk '{printf "%.15f\n", $0}')
echo $ALPHA
KY_LTC=$(cat ~/PycharmProjects/response_functions/vectors/ltc/fermions_torus_kysym_coulomb_0.00631_plus_V1_scale_0.99369_n_6_2s_18_ratio_1.000000.dat | sort -k2,2g | awk 'NR == 2 { print $1 }')
GS_LTC=$(cat ~/PycharmProjects/response_functions/vectors/ltc/fermions_torus_kysym_coulomb_0.00631_plus_V1_scale_0.99369_n_6_2s_18_ratio_1.000000.dat | sort -k2,2g | awk 'NR == 2 { print $2 }')
printf "%.15f \t %.15f \t %.15f \n" $ALPHA $GS_LTC $KY_LTC >> gs_energy_ltc.dat
ALPHA=$(bc ~/.bcrc -l <<<"pow(10,-2.1)" | awk '{printf "%.15f\n", $0}')
echo $ALPHA
KY_LTC=$(cat ~/PycharmProjects/response_functions/vectors/ltc/fermions_torus_kysym_coulomb_0.00794_plus_V1_scale_0.99206_n_6_2s_18_ratio_1.000000.dat | sort -k2,2g | awk 'NR == 2 { print $1 }')
GS_LTC=$(cat ~/PycharmProjects/response_functions/vectors/ltc/fermions_torus_kysym_coulomb_0.00794_plus_V1_scale_0.99206_n_6_2s_18_ratio_1.000000.dat | sort -k2,2g | awk 'NR == 2 { print $2 }')
printf "%.15f \t %.15f \t %.15f \n" $ALPHA $GS_LTC $KY_LTC >> gs_energy_ltc.dat
########################################################################################################################
ALPHA=$(bc ~/.bcrc -l <<<"pow(10,-2)" | awk '{printf "%.15f\n", $0}')
echo $ALPHA
KY_LTC=$(cat ~/PycharmProjects/response_functions/vectors/ltc/fermions_torus_kysym_coulomb_0.01_plus_V1_scale_0.99_n_6_2s_18_ratio_1.000000.dat | sort -k2,2g | awk 'NR == 2 { print $1 }')
GS_LTC=$(cat ~/PycharmProjects/response_functions/vectors/ltc/fermions_torus_kysym_coulomb_0.01_plus_V1_scale_0.99_n_6_2s_18_ratio_1.000000.dat | sort -k2,2g | awk 'NR == 2 { print $2 }')
printf "%.15f \t %.15f \t %.15f \n" $ALPHA $GS_LTC $KY_LTC >> gs_energy_ltc.dat
ALPHA=$(bc ~/.bcrc -l <<<"pow(10,-1.9)" | awk '{printf "%.15f\n", $0}')
echo $ALPHA
KY_LTC=$(cat ~/PycharmProjects/response_functions/vectors/ltc/fermions_torus_kysym_coulomb_0.0126_plus_V1_scale_0.9874_n_6_2s_18_ratio_1.000000.dat | sort -k2,2g | awk 'NR == 2 { print $1 }')
GS_LTC=$(cat ~/PycharmProjects/response_functions/vectors/ltc/fermions_torus_kysym_coulomb_0.0126_plus_V1_scale_0.9874_n_6_2s_18_ratio_1.000000.dat | sort -k2,2g | awk 'NR == 2 { print $2 }')
printf "%.15f \t %.15f \t %.15f \n" $ALPHA $GS_LTC $KY_LTC >> gs_energy_ltc.dat
ALPHA=$(bc ~/.bcrc -l <<<"pow(10,-1.8)" | awk '{printf "%.15f\n", $0}')
echo $ALPHA
KY_LTC=$(cat ~/PycharmProjects/response_functions/vectors/ltc/fermions_torus_kysym_coulomb_0.0158_plus_V1_scale_0.9842_n_6_2s_18_ratio_1.000000.dat | sort -k2,2g | awk 'NR == 2 { print $1 }')
GS_LTC=$(cat ~/PycharmProjects/response_functions/vectors/ltc/fermions_torus_kysym_coulomb_0.0158_plus_V1_scale_0.9842_n_6_2s_18_ratio_1.000000.dat | sort -k2,2g | awk 'NR == 2 { print $2 }')
printf "%.15f \t %.15f \t %.15f \n" $ALPHA $GS_LTC $KY_LTC >> gs_energy_ltc.dat
ALPHA=$(bc ~/.bcrc -l <<<"pow(10,-1.7)" | awk '{printf "%.15f\n", $0}')
echo $ALPHA
KY_LTC=$(cat ~/PycharmProjects/response_functions/vectors/ltc/fermions_torus_kysym_coulomb_0.02_plus_V1_scale_0.98_n_6_2s_18_ratio_1.000000.dat | sort -k2,2g | awk 'NR == 2 { print $1 }')
GS_LTC=$(cat ~/PycharmProjects/response_functions/vectors/ltc/fermions_torus_kysym_coulomb_0.02_plus_V1_scale_0.98_n_6_2s_18_ratio_1.000000.dat | sort -k2,2g | awk 'NR == 2 { print $2 }')
printf "%.15f \t %.15f \t %.15f \n" $ALPHA $GS_LTC $KY_LTC >> gs_energy_ltc.dat
ALPHA=$(bc ~/.bcrc -l <<<"pow(10,-1.6)" | awk '{printf "%.15f\n", $0}')
echo $ALPHA
KY_LTC=$(cat ~/PycharmProjects/response_functions/vectors/ltc/fermions_torus_kysym_coulomb_0.0251_plus_V1_scale_0.9749_n_6_2s_18_ratio_1.000000.dat | sort -k2,2g | awk 'NR == 2 { print $1 }')
GS_LTC=$(cat ~/PycharmProjects/response_functions/vectors/ltc/fermions_torus_kysym_coulomb_0.0251_plus_V1_scale_0.9749_n_6_2s_18_ratio_1.000000.dat | sort -k2,2g | awk 'NR == 2 { print $2 }')
printf "%.15f \t %.15f \t %.15f \n" $ALPHA $GS_LTC $KY_LTC >> gs_energy_ltc.dat
ALPHA=$(bc ~/.bcrc -l <<<"pow(10,-1.5)" | awk '{printf "%.15f\n", $0}')
echo $ALPHA
KY_LTC=$(cat ~/PycharmProjects/response_functions/vectors/ltc/fermions_torus_kysym_coulomb_0.0316_plus_V1_scale_0.9684_n_6_2s_18_ratio_1.000000.dat | sort -k2,2g | awk 'NR == 2 { print $1 }')
GS_LTC=$(cat ~/PycharmProjects/response_functions/vectors/ltc/fermions_torus_kysym_coulomb_0.0316_plus_V1_scale_0.9684_n_6_2s_18_ratio_1.000000.dat | sort -k2,2g | awk 'NR == 2 { print $2 }')
printf "%.15f \t %.15f \t %.15f \n" $ALPHA $GS_LTC $KY_LTC >> gs_energy_ltc.dat
ALPHA=$(bc ~/.bcrc -l <<<"pow(10,-1.4)" | awk '{printf "%.15f\n", $0}')
echo $ALPHA
KY_LTC=$(cat ~/PycharmProjects/response_functions/vectors/ltc/fermions_torus_kysym_coulomb_0.0398_plus_V1_scale_0.9602_n_6_2s_18_ratio_1.000000.dat | sort -k2,2g | awk 'NR == 2 { print $1 }')
GS_LTC=$(cat ~/PycharmProjects/response_functions/vectors/ltc/fermions_torus_kysym_coulomb_0.0398_plus_V1_scale_0.9602_n_6_2s_18_ratio_1.000000.dat | sort -k2,2g | awk 'NR == 2 { print $2 }')
printf "%.15f \t %.15f \t %.15f \n" $ALPHA $GS_LTC $KY_LTC >> gs_energy_ltc.dat
ALPHA=$(bc ~/.bcrc -l <<<"pow(10,-1.3)" | awk '{printf "%.15f\n", $0}')
echo $ALPHA
KY_LTC=$(cat ~/PycharmProjects/response_functions/vectors/ltc/fermions_torus_kysym_coulomb_0.0501_plus_V1_scale_0.9499_n_6_2s_18_ratio_1.000000.dat | sort -k2,2g | awk 'NR == 2 { print $1 }')
GS_LTC=$(cat ~/PycharmProjects/response_functions/vectors/ltc/fermions_torus_kysym_coulomb_0.0501_plus_V1_scale_0.9499_n_6_2s_18_ratio_1.000000.dat | sort -k2,2g | awk 'NR == 2 { print $2 }')
printf "%.15f \t %.15f \t %.15f \n" $ALPHA $GS_LTC $KY_LTC >> gs_energy_ltc.dat
ALPHA=$(bc ~/.bcrc -l <<<"pow(10,-1.2)" | awk '{printf "%.15f\n", $0}')
echo $ALPHA
KY_LTC=$(cat ~/PycharmProjects/response_functions/vectors/ltc/fermions_torus_kysym_coulomb_0.0631_plus_V1_scale_0.9369_n_6_2s_18_ratio_1.000000.dat | sort -k2,2g | awk 'NR == 2 { print $1 }')
GS_LTC=$(cat ~/PycharmProjects/response_functions/vectors/ltc/fermions_torus_kysym_coulomb_0.0631_plus_V1_scale_0.9369_n_6_2s_18_ratio_1.000000.dat | sort -k2,2g | awk 'NR == 2 { print $2 }')
printf "%.15f \t %.15f \t %.15f \n" $ALPHA $GS_LTC $KY_LTC >> gs_energy_ltc.dat
ALPHA=$(bc ~/.bcrc -l <<<"pow(10,-1.1)" | awk '{printf "%.15f\n", $0}')
echo $ALPHA
KY_LTC=$(cat ~/PycharmProjects/response_functions/vectors/ltc/fermions_torus_kysym_coulomb_0.0794_plus_V1_scale_0.9206_n_6_2s_18_ratio_1.000000.dat | sort -k2,2g | awk 'NR == 2 { print $1 }')
GS_LTC=$(cat ~/PycharmProjects/response_functions/vectors/ltc/fermions_torus_kysym_coulomb_0.0794_plus_V1_scale_0.9206_n_6_2s_18_ratio_1.000000.dat | sort -k2,2g | awk 'NR == 2 { print $2 }')
printf "%.15f \t %.15f \t %.15f \n" $ALPHA $GS_LTC $KY_LTC >> gs_energy_ltc.dat
########################################################################################################################
ALPHA=$(bc ~/.bcrc -l <<<"pow(10,-1)" | awk '{printf "%.15f\n", $0}')
echo $ALPHA
KY_LTC=$(cat ~/PycharmProjects/response_functions/vectors/ltc/fermions_torus_kysym_coulomb_0.1_plus_V1_scale_0.9_n_6_2s_18_ratio_1.000000.dat | sort -k2,2g | awk 'NR == 2 { print $1 }')
GS_LTC=$(cat ~/PycharmProjects/response_functions/vectors/ltc/fermions_torus_kysym_coulomb_0.1_plus_V1_scale_0.9_n_6_2s_18_ratio_1.000000.dat | sort -k2,2g | awk 'NR == 2 { print $2 }')
printf "%.15f \t %.15f \t %.15f \n" $ALPHA $GS_LTC $KY_LTC >> gs_energy_ltc.dat
ALPHA=$(bc ~/.bcrc -l <<<"pow(10,-0.9)" | awk '{printf "%.15f\n", $0}')
echo $ALPHA
KY_LTC=$(cat ~/PycharmProjects/response_functions/vectors/ltc/fermions_torus_kysym_coulomb_0.126_plus_V1_scale_0.874_n_6_2s_18_ratio_1.000000.dat | sort -k2,2g | awk 'NR == 2 { print $1 }')
GS_LTC=$(cat ~/PycharmProjects/response_functions/vectors/ltc/fermions_torus_kysym_coulomb_0.126_plus_V1_scale_0.874_n_6_2s_18_ratio_1.000000.dat | sort -k2,2g | awk 'NR == 2 { print $2 }')
printf "%.15f \t %.15f \t %.15f \n" $ALPHA $GS_LTC $KY_LTC >> gs_energy_ltc.dat
ALPHA=$(bc ~/.bcrc -l <<<"pow(10,-0.8)" | awk '{printf "%.15f\n", $0}')
echo $ALPHA
KY_LTC=$(cat ~/PycharmProjects/response_functions/vectors/ltc/fermions_torus_kysym_coulomb_0.158_plus_V1_scale_0.842_n_6_2s_18_ratio_1.000000.dat | sort -k2,2g | awk 'NR == 2 { print $1 }')
GS_LTC=$(cat ~/PycharmProjects/response_functions/vectors/ltc/fermions_torus_kysym_coulomb_0.158_plus_V1_scale_0.842_n_6_2s_18_ratio_1.000000.dat | sort -k2,2g | awk 'NR == 2 { print $2 }')
printf "%.15f \t %.15f \t %.15f \n" $ALPHA $GS_LTC $KY_LTC >> gs_energy_ltc.dat
ALPHA=$(bc ~/.bcrc -l <<<"pow(10,-0.7)" | awk '{printf "%.15f\n", $0}')
echo $ALPHA
KY_LTC=$(cat ~/PycharmProjects/response_functions/vectors/ltc/fermions_torus_kysym_coulomb_0.2_plus_V1_scale_0.8_n_6_2s_18_ratio_1.000000.dat | sort -k2,2g | awk 'NR == 2 { print $1 }')
GS_LTC=$(cat ~/PycharmProjects/response_functions/vectors/ltc/fermions_torus_kysym_coulomb_0.2_plus_V1_scale_0.8_n_6_2s_18_ratio_1.000000.dat | sort -k2,2g | awk 'NR == 2 { print $2 }')
printf "%.15f \t %.15f \t %.15f \n" $ALPHA $GS_LTC $KY_LTC >> gs_energy_ltc.dat
ALPHA=$(bc ~/.bcrc -l <<<"pow(10,-0.6)" | awk '{printf "%.15f\n", $0}')
echo $ALPHA
KY_LTC=$(cat ~/PycharmProjects/response_functions/vectors/ltc/fermions_torus_kysym_coulomb_0.251_plus_V1_scale_0.749_n_6_2s_18_ratio_1.000000.dat | sort -k2,2g | awk 'NR == 2 { print $1 }')
GS_LTC=$(cat ~/PycharmProjects/response_functions/vectors/ltc/fermions_torus_kysym_coulomb_0.251_plus_V1_scale_0.749_n_6_2s_18_ratio_1.000000.dat | sort -k2,2g | awk 'NR == 2 { print $2 }')
printf "%.15f \t %.15f \t %.15f \n" $ALPHA $GS_LTC $KY_LTC >> gs_energy_ltc.dat
ALPHA=$(bc ~/.bcrc -l <<<"pow(10,-0.5)" | awk '{printf "%.15f\n", $0}')
echo $ALPHA
KY_LTC=$(cat ~/PycharmProjects/response_functions/vectors/ltc/fermions_torus_kysym_coulomb_0.316_plus_V1_scale_0.684_n_6_2s_18_ratio_1.000000.dat | sort -k2,2g | awk 'NR == 2 { print $1 }')
GS_LTC=$(cat ~/PycharmProjects/response_functions/vectors/ltc/fermions_torus_kysym_coulomb_0.316_plus_V1_scale_0.684_n_6_2s_18_ratio_1.000000.dat | sort -k2,2g | awk 'NR == 2 { print $2 }')
printf "%.15f \t %.15f \t %.15f \n" $ALPHA $GS_LTC $KY_LTC >> gs_energy_ltc.dat
ALPHA=$(bc ~/.bcrc -l <<<"pow(10,-0.4)" | awk '{printf "%.15f\n", $0}')
echo $ALPHA
KY_LTC=$(cat ~/PycharmProjects/response_functions/vectors/ltc/fermions_torus_kysym_coulomb_0.398_plus_V1_scale_0.602_n_6_2s_18_ratio_1.000000.dat | sort -k2,2g | awk 'NR == 2 { print $1 }')
GS_LTC=$(cat ~/PycharmProjects/response_functions/vectors/ltc/fermions_torus_kysym_coulomb_0.398_plus_V1_scale_0.602_n_6_2s_18_ratio_1.000000.dat | sort -k2,2g | awk 'NR == 2 { print $2 }')
printf "%.15f \t %.15f \t %.15f \n" $ALPHA $GS_LTC $KY_LTC >> gs_energy_ltc.dat
ALPHA=$(bc ~/.bcrc -l <<<"pow(10,-0.3)" | awk '{printf "%.15f\n", $0}')
echo $ALPHA
KY_LTC=$(cat ~/PycharmProjects/response_functions/vectors/ltc/fermions_torus_kysym_coulomb_0.501_plus_V1_scale_0.499_n_6_2s_18_ratio_1.000000.dat | sort -k2,2g | awk 'NR == 2 { print $1 }')
GS_LTC=$(cat ~/PycharmProjects/response_functions/vectors/ltc/fermions_torus_kysym_coulomb_0.501_plus_V1_scale_0.499_n_6_2s_18_ratio_1.000000.dat | sort -k2,2g | awk 'NR == 2 { print $2 }')
printf "%.15f \t %.15f \t %.15f \n" $ALPHA $GS_LTC $KY_LTC >> gs_energy_ltc.dat
ALPHA=$(bc ~/.bcrc -l <<<"pow(10,-0.2)" | awk '{printf "%.15f\n", $0}')
echo $ALPHA
KY_LTC=$(cat ~/PycharmProjects/response_functions/vectors/ltc/fermions_torus_kysym_coulomb_0.631_plus_V1_scale_0.369_n_6_2s_18_ratio_1.000000.dat | sort -k2,2g | awk 'NR == 2 { print $1 }')
GS_LTC=$(cat ~/PycharmProjects/response_functions/vectors/ltc/fermions_torus_kysym_coulomb_0.631_plus_V1_scale_0.369_n_6_2s_18_ratio_1.000000.dat | sort -k2,2g | awk 'NR == 2 { print $2 }')
printf "%.15f \t %.15f \t %.15f \n" $ALPHA $GS_LTC $KY_LTC >> gs_energy_ltc.dat
ALPHA=$(bc ~/.bcrc -l <<<"pow(10,-0.1)" | awk '{printf "%.15f\n", $0}')
echo $ALPHA
KY_LTC=$(cat ~/PycharmProjects/response_functions/vectors/ltc/fermions_torus_kysym_coulomb_0.794_plus_V1_scale_0.206_n_6_2s_18_ratio_1.000000.dat | sort -k2,2g | awk 'NR == 2 { print $1 }')
GS_LTC=$(cat ~/PycharmProjects/response_functions/vectors/ltc/fermions_torus_kysym_coulomb_0.794_plus_V1_scale_0.206_n_6_2s_18_ratio_1.000000.dat | sort -k2,2g | awk 'NR == 2 { print $2 }')
printf "%.15f \t %.15f \t %.15f \n" $ALPHA $GS_LTC $KY_LTC >> gs_energy_ltc.dat
########################################################################################################################
ALPHA=$(bc ~/.bcrc -l <<<"pow(10,0)" | awk '{printf "%.15f\n", $0}')
echo $ALPHA
KY_LTC=$(cat ~/PycharmProjects/response_functions/vectors/ltc/fermions_torus_kysym_coulomb_plus_V1_scale_0_n_6_2s_18_ratio_1.000000.dat | sort -k2,2g | awk 'NR == 2 { print $1 }')
GS_LTC=$(cat ~/PycharmProjects/response_functions/vectors/ltc/fermions_torus_kysym_coulomb_plus_V1_scale_0_n_6_2s_18_ratio_1.000000.dat | sort -k2,2g | awk 'NR == 2 { print $2 }')
printf "%.15f \t %.15f \t %.15f \n" $ALPHA $GS_LTC $KY_LTC >> gs_energy_ltc.dat