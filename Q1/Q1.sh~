#!/bin/bash

ORGN=$1
NEWS=$2
rm -rf replace
mkdir replace
for filenm in *.txt ; do
	new_root="${filenm%%.*}"
	new_root+=_new
	if grep -q $ORGN "$filenm"; then
		sed "s/${ORGN}/${NEWS}/g" $filenm > ./replace/$new_root.txt 
	fi
	done
