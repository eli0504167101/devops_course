#!bin/bash
# Task 1: File existence check script

echo "enter file name "

read filename

if [ -f "$filename" ];then
    echo "File found"
else
    echo "File not found"
fi


 
