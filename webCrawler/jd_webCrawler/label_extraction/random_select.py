#! /usr/bin/python
# -*- coding:utf-8 -*-
import sys, os, shutil, random

def copy(srcPath, destDir):
    pic_file_name = os.path.dirname(srcPath) + '_' + os.path.basename(srcPath)
    destPath = destDir + os.path.sep + pic_file_name
    if os.path.exists(srcPath) and not os.path.exists(destPath):
        shutil.copy(srcPath, destPath)

    txt_file_name = pic_file_name[:-3] + 'txt'
    txt_src_path = srcPath[:-3] + 'txt'
    destPath = destDir + os.path.sep + txt_file_name
    if os.path.exists(txt_src_path) and not os.path.exists(destPath):
        shutil.copy(txt_src_path, destPath)

def select(nameList, limited):
    if len(nameList) <= limited:
        return nameList
    size = len(nameList)
    newList = []
    for i in range(size):
        randomNum = random.randint(1, 10)
        if randomNum < 6:
            newList.append(nameList[i])
    return select(newList, limited)
    
if __name__ == '__main__':
    pic_num = 20
    #pic_num = raw_input('Input pic number : ')

    file = open('output.csv', 'r')
    items = [i.split('\t')[0] for i in file.readlines()]
    file.close()

    if os.path.exists('Result') == False:
        os.mkdir('Result')

    result = []
    while len(result) <= pic_num:
        result += select(items, pic_num)
    result = result[:pic_num]
    for i in result:
        print 'copying ' + i
        copy(i, 'Result')
