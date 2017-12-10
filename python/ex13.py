#!/usr/bin/env python

import numpy as np

def gen_matrix(x,y):
    array=np.int_(np.random.rand(x,y)*10)
    print (array)
    return array

X=gen_matrix(8,8)
Y=gen_matrix(8,8)
Z=np.int_(np.random.rand(8,8)*0)

for i in range(len(X)):
   for j in range(len(Y[0])):
       for k in range(len(Y)):
           Z[i][j] += X[i][k] * Y[k][j]

for r in Z:
   print(r)
