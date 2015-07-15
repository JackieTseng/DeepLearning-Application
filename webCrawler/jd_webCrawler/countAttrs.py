#! /usr/bin
# -*- coding:utf-8 -*-
import sys, os

ATTRSVALUE = {}
ATTRS = {}

def processFile(fileName):
    global ATTRS
    global ATTRSVALUE
    output = open(fileName, 'rb')
    items = output.readlines()
    for i in items[:len(items) - 1]:
        items = i.strip('\n').split('\t')
        if len(items) == 2:
            x, y = items
        elif len(items) == 3:
            x, t, y = items
            y = t if len(t) != 0 else y 
        if x not in ATTRS:
            ATTRS[x] = 1
        else:
            ATTRS[x] += 1
        if x not in ATTRSVALUE:
            ATTRSVALUE[x] = set()
        ATTRSVALUE[x].add(y)

def processSingleDir(dirName):
    preCounter = 1
    postCounter = 1
    while True:
        postCounter = 1
        print "item " + str(preCounter),
        if os.path.exists(dirName + '/' + str(preCounter) + '.txt'):
            curFile = dirName + '/' + str(preCounter) + '.txt'
            processFile(curFile)
        elif os.path.exists(dirName + '/' + str(preCounter) + '_' + str(postCounter) + '.txt'):
            while True:
                curFile = dirName + '/' + str(preCounter) + '_' + str(postCounter) + '.txt'
                if os.path.exists(curFile):
                    processFile(curFile)
                    postCounter += 1
                else:
                    break
        else:
            break
        preCounter += 1
        print "done.."

def processAllDir(dirNames):
    global ATTRS
    global ATTRSVALUE
    topDirName = 'Result'
    if os.path.exists(topDirName) == False:
        os.mkdir(topDirName)
    for name in dirNames:
        processSingleDir(name)

    attr_file = topDirName  + '/' + 'attributes.txt'
    output = open(attr_file, 'wb')
    sortAttrsDic = sorted(ATTRS.iteritems(), key = lambda d:d[0], reverse = False)
    for i in sortAttrsDic:
        output.write(i[0] + '\t' + str(i[1]) + '\n')
    output.close()
    
    sortAttrsValueDic = sorted(ATTRSVALUE.iteritems(), key = lambda d:d[0], reverse = False)
    for i in sortAttrsValueDic:
        k = i[0]
        v = i[1]
        attr_value_file = topDirName + '/' + k + '.txt'
        output = open(attr_value_file, 'wb')
        output.write(str(len(v)) + '\n')
        for i in v:
            output.write(i + '\n')
        output.close()

if __name__ == "__main__":
    dirNames = []
    dirName = raw_input()
    while dirName:
        dirNames.append(dirName)
        dirName = raw_input()
    processAllDir(dirNames)
