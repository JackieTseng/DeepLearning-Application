# !/usr/bin/python
# -*- coding:utf-8 -*-

import os, sys
import numpy as np
from pca import *

def itq(V, n):
    (number, bit) = V.shape
    R = np.random.randn(bit, bit)
    U, V2, S2 = np.linalg.svd(R)
    R = U[:, range(0, bit)]
    for i in range(n):
        Z = V * R
        (row, col) = Z.shape
        UX = np.ones((row, col)) * -1
        UX[Z >= 0] = 1
        C = UX.T * V
        UB, sigma, UA = np.linalg.svd(C)
        R = UA * UB.T
    B = UX
    B[B < 0] = 0
    print B

if __name__ == '__main__':
    mx = readFile('')
    Y = pca(mx)
    itq(Y, 50)
