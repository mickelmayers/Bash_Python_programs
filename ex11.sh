#!/bin/bash

for i in `find photos -name '*.jpg'`
do 
   mv $i photos/converted/`basename $i .jpg`.png
done
