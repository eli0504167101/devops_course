#!/bin/bash
#Task 6 - For Loop (Rename Files)

for file in *.txt;do
	new_name=${file%.txt}.bak

	mv "$file" "$new_name"

	echo "$file renamed to $new_name"
	sleep 0.2
done


 
