#!/bin/bash

KOD=1234

echo "Hello, what is your code?"
read code

if [ $code -eq $KOD ]
then
   echo "GOOD"
else
   echo "BAD"
fi
