#! /usr/bin/python
# -*- coding:utf-8 -*-
import sys, os

label_file_names = ["sort.txt", "shape.txt", "material.txt", "color.txt"]
label_numbers = [8, 6, 7, 16]
dir_Names = ["DanJianBao", "KaBao", "QianBao", "ShouNaBao", "ShouTiBao", "ShuangJianBao", "XieKuaBao", "YaoShiBao"]
standard_labels = []
standard_labels_string = []
data = []
total_counter = 0

def changeString(string, index):
    temp = list(string)
    temp[index] = '1'
    newString = ''.join(temp)
    return newString

def processFile(fileName):
    global standard_labels
    global label_numbers
    global standard_labels_string
    global data
    # check sort
    sort = fileName[:fileName.find('/')]
    sort_number = -1
    sort_string = standard_labels_string[0]
    for i in range(len(standard_labels[0])):
        if sort == standard_labels[0][i]:
            sort_number = i
    sort_string = changeString(sort_string, sort_number)

    # open txt file
    output = open(fileName, 'r')
    items = output.readlines()
    lines = items[:len(items) - 1]

    # check three other attributes
    color_number = []
    shape_number = -1
    material_number = -1
    for i in lines:
        items = i.strip('\n').split('\t')
        if len(items) == 2:
            x, y = items
        elif len(items) == 3:
            x, t, y = items
            y = t if len(t) != 0 else y
        if x == "外形":
            for i in range(len(standard_labels[1])):
                if standard_labels[1][i] in y:
                    shape_number = i
                    break
        if x == "材质":
            for i in range(len(standard_labels[2])):
                if standard_labels[2][i] in y:
                    material_number = i
                    break
        if x == "颜色":
            for i in range(len(standard_labels[3])):
                if standard_labels[3][i] in y:
                    color_number.append(i)
    # Fix shape info no found
    shape_string = standard_labels_string[1]
    if shape_number == -1:
        shape_number = label_numbers[1] - 1
    shape_string = changeString(shape_string, shape_number)

    # Fix material info no found
    material_string = standard_labels_string[2]
    if material_number == -1:
        material_number = label_numbers[2] - 1
    else:
        if material_number == 2 or material_number == 3 or material_number == 4 or material_number == 5:
            material_number -= 1
        elif material_number == 6 or material_number == 7 or material_number == 8:
            material_number = 5
    material_string = changeString(material_string, material_number)

    # Fix material info no found
    color_string = standard_labels_string[3]
    new_color_number = set()
    if len(color_number) == 0:
        new_color_number.add(label_numbers[3] - 1)
    else:
        for i in color_number:
            number = i
            if number == 14 or number == 15 or number == 16:
                number = 14
            new_color_number.add(number)
    for i in new_color_number:
        color_string = changeString(color_string, i)

    result_string = sort_string + shape_string + material_string + color_string
    #print result_string
    data.append((fileName, result_string))

    '''
    print fileName
    print str(sort_number) + " -> " + sort_string
    print str(shape_number) + " -> " + shape_string
    print str(material_number) + " -> " + material_string
    for i in new_color_number:
        print str(i) + " ",
    print "-> " + color_string
    '''

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
    global data
    for name in dirNames:
        print name + ' loading..'
        processSingleDir(name)
    input = open('output.csv', 'w')
    for i in data:
        input.write(i[0] + '\t' + i[1] + '\n')
    input.close()

def read_standard_labels(label_file_names):
    global standard_labels
    for name in label_file_names:
        file = open(name, 'r')
        temp_list = []
        items = file.readlines()
        for item in items:
            attr = item[:len(item) - 1]
            temp_list.append(attr)
        standard_labels.append(temp_list)

def construct_string(label_numbers):
    global standard_labels_string
    for i in label_numbers:
        temp_string = ''
        for j in range(i):
            temp_string += '0'
        standard_labels_string.append(temp_string)

if __name__ == "__main__":
    read_standard_labels(label_file_names)
    construct_string(label_numbers)
    #temp = []
    #temp.append(dir_Names[7])
    #processAllDir(temp)
    processAllDir(dir_Names)
    #processFile('YaoShiBao/2_1.txt')
    #for i in data:
    #    print i[0] + " " + i[1]
