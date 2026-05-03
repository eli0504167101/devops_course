#!/bin/bash
#Task 9 - If (Disk Space Check)

usage=$(df / | tail -1 | awk '{print $5}' | tr -d '%')

echo "Current disk usage: $usage%"

if [ "$usage" -gt 80 ]; then
    echo "WARNING: disk almost full"
else
    echo "Disk OK"
fi

 
