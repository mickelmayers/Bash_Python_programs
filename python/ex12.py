#!/usr/bin/env python

import numpy as np

def gen_matrix(x,y):
    array=np.int_(np.random.rand(x,y)*10)
    print (array)
    return array

X=gen_matrix(128,128)
Y=gen_matrix(128,128)
Z=np.int_(np.random.rand(128,128)*0)

for i in range(len(X)):
   for j in range(len(Y)):
       Z[i][j] += X[i][j] + Y[i][j]

for r in Z:
   print(r)
