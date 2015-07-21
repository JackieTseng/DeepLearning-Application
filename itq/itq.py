# !/usr/bin/python
# -*- coding:utf-8 -*-

import os, sys
import numpy as np
from pca import *

# Input: 
#       V: n*c PCA-processed matrix(n is the number of sample
#          and c is the code length)
#       n: the number of iterations(50 is enough)
# Output:
#       B: n*c binary matrix
#       R: the rotation found by ITQ
def itq(V, n):
    # initialize with a orthogonal random rotation matrix R
    (number, bit) = V.shape
    # Gaussian distribution of mean 0 and variance 1
    R = np.random.randn(bit, bit)
    U, V2, S2 = np.linalg.svd(R)
    R = U[:, range(0, bit)]
    
    # Fix and Update iterations
    for i in range(n):
        print 'Iteration ' + str(i + 1) + ' loading..'
        # Fix R and update B(UX)
        Z = V * R
        (row, col) = Z.shape
        UX = np.ones((row, col)) * -1
        UX[Z >= 0] = 1
        
        # Fix B and update R
        C = UX.T * V
        UB, sigma, UA = np.linalg.svd(C)
        R = UA * UB.T
    B = UX
    # Transform into binary code
    B[B < 0] = 0
    #print B
    return (B, R)
    

def compressITQ(mx, bit, iters):
    Y = pca(mx, bit)
    itq(Y, iters)

if __name__ == '__main__':
    mx = readFile('')
    compressITQ(mx, 90, 50)
