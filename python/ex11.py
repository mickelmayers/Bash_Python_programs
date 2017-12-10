#!/usr/bin/env python

a=[1,2,12,4]
b=[2,4,2,8]

print(sum([i*j for (i, j) in zip(a, b)]))
