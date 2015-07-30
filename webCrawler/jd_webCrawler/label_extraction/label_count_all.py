#! /usr/bin
# -*- coding:utf-8 -*-
import sys, os

attrs = {}
other = set()

def processFile(fileName):
    global attrs
    global other
    output = open(fileName, 'r')
    items = output.readlines()
    for i in items[:len(items) - 1]:
        items = i.strip('\n').split('\t')
        if len(items) == 2:
            x, y = items
        elif len(items) == 3:
            x, t, y = items
            y = t if len(t) != 0 else y 
        if x == "材质":
            flag = False
            #print y,
            for (k, v) in attrs.iteritems():
                if k in y:
                    attrs[k] += 1
                    flag = True
                    #print ' -> ' + k
            if flag == False:
                attrs["其他"] +=1
                #print ' -> ' + "其他"
                other.add(y)

def processSingleDir(dirName):
    preCounter = 1
    postCounter = 1
    processFlag = False
    while True:
        postCounter = 1
        processFlag = False
        #print "item " + str(preCounter),
        if os.path.exists(dirName + '/' + str(preCounter) + '.txt'):
            curFile = dirName + '/' + str(preCounter) + '.txt'
            processFile(curFile)
            processFlag = True

        if os.path.exists(dirName + '/' + str(preCounter) + '_' + str(postCounter) + '.txt'):
            processFlag = True
            while True:
                curFile = dirName + '/' + str(preCounter) + '_' + str(postCounter) + '.txt'
                if os.path.exists(curFile):
                    processFile(curFile)
                    postCounter += 1
                else:
                    break

        if processFlag == False:
            break
        preCounter += 1
        #print "done.."

def processAllDir(dirNames):
    global attrs
    global other
    topDirName = 'Result'
    if os.path.exists(topDirName) == False:
        os.mkdir(topDirName)
    for name in dirNames:
	print name + ' loading..'
        processSingleDir(name)

    attr_file = topDirName  + '/' + 'attrs_counter_all.txt'
    output = open(attr_file, 'w')
    sortAttrsDic = sorted(attrs.iteritems(), key = lambda d:d[0], reverse = False)
    counter = 0
    for i in sortAttrsDic:
        counter += i[1]

    output.write(str(counter) + '\n')
    for i in sortAttrsDic:
        output.write(i[0] + '\t' + str(i[1]) + '\t' + str(float(i[1])/counter) + '\n')
    output.close()
    
    attr_value_file = topDirName + '/'  + 'other_all.txt'
    output = open(attr_value_file, 'wb')
    for i in other:
        output.write(i + '\n')
    output.close()

def read_label(fileName):
    global attrs
    attr_file = open(fileName, 'r')
    items = attr_file.readlines()
    for i in items:
        name = i[:len(i) - 1]
        attrs[name] = 0

if __name__ == "__main__":
    read_label("material.txt")
    dirNames = []
    dirName = raw_input()
    while dirName:
        dirNames.append(dirName)
        dirName = raw_input()
    processAllDir(dirNames)
