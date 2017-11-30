#!/bin/bash

NUMBER_OF_WORD=`tr ' ' '\n' < file.log | grep AGH | wc -l`

echo "Number of occurrences of a word in a text:"
echo $NUMBER_OF_WORD
