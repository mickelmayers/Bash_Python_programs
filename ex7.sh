#!/bin/bash

echo "Which operation would you like to do? Choose from + - / *"
read oper
echo "Enter first number"
read NUM1
echo "Enter second number"
read NUM2

echo "$NUM1 $oper $NUM2 = "

if [ "$oper" == "+" ]
then
   echo  $(($NUM1 + $NUM2))
elif [ "$oper" == "-" ]
then
   echo $(($NUM1 - $NUM2))
elif [ "$oper" == "/" ]
then
   echo $(($NUM1 / $NUM2))
elif [ "$oper" == "*" ]
then
   echo $(($NUM1 * $NUM2))
else
   echo "Enter correct operation sign"
fi
