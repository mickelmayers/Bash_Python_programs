#!/bin/bash

echo "Enter a number"
read number

if [ $number -gt 20 ]
then
   cat /proc/cpuinfo | grep -m1 "model"
fi
