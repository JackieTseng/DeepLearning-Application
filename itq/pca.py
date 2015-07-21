# !/usr/bin/python
# -*- coding:utf-8 -*-

import os, sys
import numpy as np

def strListToFlatList(line):
    temp = []
    for i in line:
        #print i 
        temp.append(float(i))
    return temp

def readFile(fileStr):
    file = open('C1.txt', 'r')
    lines = file.readlines()
    file.close()
    #name = []
    data = []
    # import data
    for i in lines:
        items = i.split(',')
        #name.append(items[0])
        #data.append(strListToFlatList(items[1:]))
        data.append(strListToFlatList(items))
    mx = np.mat(data)
    return mx

def PCA(dataMat, topNfeat=5):
    meanVals = mean(dataMat, axis = 0)
    # 减去均值
    meanRemoved = dataMat - meanVals
    # 用标准差归一化
    stded = meanRemoved / std(dataMat)
    # 求协方差方阵
    covMat = cov(stded, rowvar = 0)
    # 求特征值和特征向量
    eigVals, eigVects = linalg.eig(mat(covMat))
    # 对特征值进行排序
    eigValInd = argsort(eigVals)
    eigValInd = eigValInd[:-(topNfeat + 1):-1]  
    # 除去不需要的特征向量
    redEigVects = eigVects[:, eigValInd]
    # 求新的数据矩阵
    lowDDataMat = stded * redEigVects
    reconMat = (lowDDataMat * redEigVects.T) * std(dataMat) + meanVals
    return lowDDataMat, reconMat

def pca(mx):
    # Step 1 -> center data
    row, col = mx.shape
    for i in range(col):
        mx[:, i] -= mx[:, i].mean()

    # Step 2 -> scatter matrix
    cov = np.cov(mx, rowvar = 0)

    # Step 3 -> eigenvectors and eigenvalues
    val, vec = np.linalg.eig(cov)

    # Step 4 -> sort the eigenvectors together with the eigenvalues
    idx = np.argsort(-val)
    sort_val = val[idx]
    sort_vec = vec[:, idx]
    
    # Step 5 -> choose K rows of eigenvectors
    K = 90 #128
    idx = idx[:K]
    P = sort_vec[:, idx]
    
    # return transform matrix
    Y = mx * P
    return Y

if __name__ == '__main__':
    mx = readFile('C1.txt')
    pca(mx)
