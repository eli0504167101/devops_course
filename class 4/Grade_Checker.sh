#!/bin/bash
#Task 5 - If + Else If (Grade Checker)

echo "enter test score"

read scure

if [ $scure -ge 90 ];then
	echo "A"

elif [ $scure -ge 80 ];then
	echo "B"

elif [ $scure -ge 70 ];then
        echo "C"

else
        echo "F"
fi



 
