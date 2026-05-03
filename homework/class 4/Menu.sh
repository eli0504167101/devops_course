#!/bin/bash
#Task 7 - While Loop (Menu)

echo " enter / 1 / 2 / 3 "

read num

while [ $num != 3 ];do
	if [ $num = 1 ];then
		echo "Say Hello"
	elif [ $num = 2 ];then
		echo "show date"
	fi
	
        echo " enter / 1 / 2 / 3 "

        read num
	
done

echo "exit" 
 
