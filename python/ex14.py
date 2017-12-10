#!/usr/bin/env python

import numpy as np

def gen_matrix(x,y):
    array=np.int_(np.random.rand(x,y)*10)
    print (array)
    return array

def determinant(matrix, mul):
    width = len(matrix)
    if width == 1:
        return mul * matrix[0][0]
    else:
        sign = -1
        total = 0
        for i in range(width):
            m = []
            for j in range(1, width):
                buff = []
                for k in range(width):
                    if k != i:
                        buff.append(matrix[j][k])
                m.append(buff)
            sign *= -1
            total += mul * determinant(m, sign * matrix[0][i])
        return total

print(determinant(gen_matrix(5,5), 1))
