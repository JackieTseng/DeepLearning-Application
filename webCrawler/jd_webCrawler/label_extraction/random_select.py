#! /usr/bin/python
# -*- coding:utf-8 -*-
import sys, os, shutil, random

label_file_names = ["sort.txt", "shape.txt", "material.txt", "color.txt"]
label_numbers = [8, 6, 7, 16]
standard_labels = []
standard_labels_string = []
data = []

def changeString(string, index):
    temp = list(string)
    temp[index] = '1'
    newString = ''.join(temp)
    return newString

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
    pic_name = fileName[:fileName.rfind('.')]
    if os.path.exists(pic_name + '.jpg'):
        data.append((pic_name + '.jpg', result_string))
    elif os.path.exists(pic_name + '.png'):
        data.append((pic_name + '.png', result_string))
    else:
        data.append((fileName, result_string))
        print fileName

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

    read_standard_labels(label_file_names)
    construct_string(label_numbers)

    result = []
    while len(result) <= pic_num:
        result += select(items, pic_num)
    result = result[:pic_num]
    for i in result:
        processFile(i[:-3]+'txt')
        print 'copying ' + i
        copy(i, 'Result')

    input = open('Result/output.csv', 'w')
    for i in data:
        input.write(i[0] + '\t' + i[1] + '\n')
    input.close()

