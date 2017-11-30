#!/bin/bash

###1
echo "Hello, World!"

###2
cd /dev 
LICZBA=`find -type f | wc -l`

export LICZBA1=$LICZBA
echo $LICZBA1
