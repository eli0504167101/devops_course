#!/bin/bash
#Task 10 - For Loop (Read From File)

echo "Server-1" > servers.txt
echo "Server-2" >> servers.txt
echo "Server-3" >> servers.txt

while read line; do
    echo "Checking server: $line"
done < servers.txt