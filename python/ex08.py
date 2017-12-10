#!/usr/bin/env python

import random

array=random.sample(range(100), 30)

print("Generated list:")
print(array)
print("Sorted using built-in function")
print (sorted(array, reverse=True))

array_out = []

while array:
    minimum = array[0]  # arbitrary number in list 
    for x in array: 
        if x > minimum:
            minimum = x
    array_out.append(minimum)
    array.remove(minimum)    

print ("Sorted using our function")
print (array_out)
