#!/bin/bash

FILES=~/KDevProjects/response_functions/vectors/ltc/*0.dat
for f in $FILES
do
	echo $f
	KY=$(cat $f | sort -k2,2g | awk 'NR == 2 { print $1 }')
	KY2=$(cat $f | sort -k2,2g | awk 'NR == 3 { print $1 }')
	KY3=$(cat $f | sort -k2,2g | awk 'NR == 4 { print $1 }')
	echo $KY
	echo $KY2
	echo $KY3
done