# !/usr/bin/python
# -*- coding:utf-8 -*-

import os, sys
import numpy as np

# Translate string List to float
def strListToFlatList(line):
    temp = []
    for i in line:
        temp.append(float(i))
    return temp

def pca(mx):
    # Step 1 -> center data
    row, col = mx.shape
    for i in range(col):
        mx[:, i] -= mx[:, i].mean()

    # Step 2 -> scatter matrix
    cov = np.cov(mx.T)
    
    # Step 3 -> eigenvectors and eigenvalues
    val, vec = np.linalg.eig(cov)

    # Step 4 -> sort the eigenvectors together with the eigenvalues
    idx = np.argsort(-val)
    sort_val = val[idx]
    sort_vec = vec[:, idx]
    
    # Step 5 -> choose K rows of eigenvectors
    K = 100
    idx = idx[:K]
    P = sort_vec[:, idx]
    
    # return transform matrix
    Y = mx * P
    return Y

if __name__ == '__main__':
    file = open('output.csv', 'rb')
    lines = file.readlines()
    file.close()
    name = []
    data = []
    # import data
    for i in lines:
        items = i.split(',')
        name.append(items[0])
        # transform data type
        data.append(strListToFlatList(items[1:]))
    # set as matrix
    mx = np.mat(data)
    pca(mx)
