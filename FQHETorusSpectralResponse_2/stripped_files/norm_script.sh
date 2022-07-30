#!/bin/bash

mkdir -p norm

find . -type f -name "*.sr.cut" -print0 | while read -d $'\0' file
do
	if ! [ -e norm/"$(basename "$file")".cut ]; then
	  echo "$file"
	fi
done