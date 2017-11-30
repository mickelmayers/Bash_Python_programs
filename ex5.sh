#!/bin/bash

CODE=1234
VAR=0

for i in 0 1 2
do
echo "Password:"
read password
if [ $password -eq $CODE ]
then
   echo "Correct password"
   cd ..
   ls
   exit 0
else
   echo "Wrong password!"
fi
done
