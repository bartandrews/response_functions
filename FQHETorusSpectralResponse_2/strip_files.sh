#!/bin/bash

NUMB_VALUES=10000

mkdir -p stripped_files

find . -type f -name "*.sr" -not -path "*/coulomb_scaling/n_8_qx_0/*" -print0 | while read -d $'\0' file
do
	if ! [ -e stripped_files/"$(basename "$file")".cut ]; then
	  echo "$file"
	  sort -r -g -k 2 "$file" > stripped_files/"$(basename "$file")".sorted
	  head -${NUMB_VALUES} stripped_files/"$(basename "$file")".sorted > stripped_files/"$(basename "$file")".precut
	  sort -g -k 1 stripped_files/"$(basename "$file")".precut > stripped_files/"$(basename "$file")".cut
    rm -rf stripped_files/"$(basename "$file")".sorted stripped_files/"$(basename "$file")".precut
	fi
done
