#!/bin/bash
#Task 3 - While Loop (Guessing Game)

echo "enter num"

read guss

while [ $guss != 7 ];do
	echo "Wrong, try again"
	read guss
done

echo "You got it!"
 
