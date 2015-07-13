#!/usr/bin/python
# -*- coding: UTF-8 -*-
import os, sys, requests, bs4, urllib

#reload(sys)
#sys.setdefaultencoding("utf8")
FILECOUNTER = 1
ATTRS = {}
ATTRSVALUE = {}

# Test if the main pic exists
def testPicExist(url):
    response = requests.get(url)
    soup = bs4.BeautifulSoup(response.content, from_encoding="utf-8")
    pic_url = soup.select('div#preview img')
    pic_src = pic_url[0].attrs.get('src')
    if pic_src == '':
        return False
    else:
        return True

# Get the item information by sortName, colorNumber, color and url from a item
def getItemInfoWithColor(dirName, number, color, url):
    global FILECOUNTER
    global ATTRS
    global ATTRVALUE
    response = requests.get(url)
    soup = bs4.BeautifulSoup(response.content, from_encoding="utf-8")

    attrs_list = [()]
    # download img
    pic_url = soup.select('div#preview img')
    pic_src = pic_url[0].attrs.get('src')
    filetype = pic_src[pic_src.rfind('.'):]
    req = requests.get(pic_src)
    pic_output = open(dirName + '/' + str(FILECOUNTER) + '_' + str(number) + filetype, 'wb')
    pic_output.write(req.content)

    # download attrs in li
    param_list = soup.select('ul#parameter2 > li')
    # fit different pages
    if len(param_list) == 0:
        param_list = soup.select('div#product-detail ul.detail-list li')
    param_str_list = [a.string for a in param_list]
    param_output = open(dirName + '/' + str(FILECOUNTER) + '_' + str(number) + '.txt', 'wb')
    for i in param_str_list:
        # Split by the ':' in Chinese character
        if i != None:
            pos = i.find(u'\uff1a')
            key = i[:pos].encode('utf-8')
            # Store and count the key & value
            if key not in ATTRS:
                ATTRS[key] = 1
            else:
                ATTRS[key] += 1
            value = i[pos + 1:].encode('utf-8')
            # Recorige the 'color' in Chinese character and transform into different color of a sort
            if key == (u'\u989c\u8272').encode('utf-8'):
                value = color
            attrs_list.append((key, value))

    # download attrs in table
    table = soup.find('table', attrs={'class':'Ptable'})
    if table != None:
        td = table.find_all('td')
        i = 0
        counter = len(td)
        # pull the data
        while i < counter:
            key = td[i].string.encode('utf-8')
            if key not in ATTRS:
                ATTRS[key] = 1
            else:
                ATTRS[key] += 1
            value = td[i + 1].string.encode('utf-8')
            attrs_list.append((key, value))
            i += 2

    # Duplicate attributes
    temp = set()
    # write url
    length = len(attrs_list)
    for i in range(1, length):
        if attrs_list[i][0] in temp:
            continue
        temp.add(attrs_list[i][0])
        param_output.write(attrs_list[i][0] + '\t' + attrs_list[i][1] + '\n')
        key = attrs_list[i][0]
        value = attrs_list[i][1]
        # store all the attributes in one sort
        if key not in ATTRSVALUE:
            ATTRSVALUE[key] = set()
        ATTRSVALUE[key].add(value)
    param_output.write('url'.encode('utf-8') + '\t' + url.encode('utf-8'))
    param_output.close()

# Process the special item without different color
def getItemInfoWithoutColor(dirName, url):
    global FILECOUNTER
    global ATTRS
    response = requests.get(url)
    soup = bs4.BeautifulSoup(response.content, from_encoding="utf-8")

    attrs_list = [()]
    # download img
    pic_url = soup.select('div#preview img')
    pic_src = pic_url[0].attrs.get('src')
    filetype = pic_src[pic_src.rfind('.'):]
    req = requests.get(pic_src)
    pic_output = open(dirName + '/' + str(FILECOUNTER) + filetype, 'wb')
    pic_output.write(req.content)

    # download attrs in li
    param_list = soup.select('ul#parameter2 > li')
    if len(param_list) == 0:
        param_list = soup.select('div#product-detail ul.detail-list li')
    param_str_list = [a.string for a in param_list]
    param_output = open(dirName + '/' + str(FILECOUNTER) + '.txt', 'wb')
    for i in param_str_list:
        if i != None:
            pos = i.find(u'\uff1a')
            key = i[:pos].encode('utf-8')
            if key not in ATTRS:
                ATTRS[key] = 1
            else:
                ATTRS[key] += 1
            value = i[pos + 1:].encode('utf-8')
            attrs_list.append((key, value))

    # download attrs in table
    table = soup.find('table', attrs={'class':'Ptable'})
    if table != None:
        td = table.find_all('td')
        i = 0
        counter = len(td)
        while i < counter:
            key = td[i].string.encode('utf-8')
            if key not in ATTRS:
                ATTRS[key] = 1
            else:
                ATTRS[key] += 1
            value = td[i + 1].string.encode('utf-8')
            attrs_list.append((key, value))
            i += 2

    temp = set()
    # write url
    length = len(attrs_list)
    for i in range(1, length):
        if attrs_list[i][0] in temp:
            continue
        temp.add(attrs_list[i][0])
        param_output.write(attrs_list[i][0] + '\t' + attrs_list[i][1] + '\n')
    param_output.write('url'.encode('utf-8') + '\t' + url.encode('utf-8'))
    param_output.close()

# Write a page in jd.com(woman-bag)
def processSingleItemInfo(dirName, url):
    global FILECOUNTER
    response = requests.get(url)
    soup = bs4.BeautifulSoup(response.content, from_encoding="utf-8")

    # download other colors
    colorUrls = [()]
    diffColor = soup.select('div.dd > div.item')
    # select different color urls
    for i in diffColor:
        cur = i.find('a')
        if cur.find('img') != None:
            colorUrls.append((cur.find('i').string.encode('utf-8'), cur.attrs.get('href')))
    
    length = len(colorUrls)
    # process different situations
    if length == 1:
        getItemInfoWithoutColor(dirName, url)
    else:
        counter = 1
        for i in range(1, length):
            if testPicExist(colorUrls[i][1]):
                getItemInfoWithColor(dirName, counter, colorUrls[i][0], colorUrls[i][1])
                counter += 1
    FILECOUNTER += 1

# Get all the urls in the current web page
def processSinglePage(dirName, secDirName, url, page):
    response = requests.get(url)
    soup = bs4.BeautifulSoup(response.content, from_encoding="utf-8")
    urls = soup.select('div.p-img a[href]')
    urls_list = [a.attrs.get('href') for a in urls]
    itemCounter = 1
    if os.path.exists(dirName + '/' + secDirName) == False:
        os.mkdir(dirName + '/' + secDirName)
    for i in urls_list:
       print i,
       try:
           processSingleItemInfo(dirName, i)
           print " dones.."
       except:
           # record the error item
           errorOutput = open(dirName + '/ATTR/error.bat', 'ab')
           errorOutput.write(str(page) + "\t" + str(itemCounter) + "\t" + i + '\n')
           errorOutput.close()
           print " fail.."
       itemCounter += 1

# store the whole sort's attributes
def storeMainSortAttrs(dirName, attrs):
    global ATTRSVALUE
    attrsOutput = open(dirName + '/ATTR/attrs.bat', 'wb')
    # sort by chinese character order
    sortDic = sorted(attrs.iteritems(), key = lambda d:d[0], reverse = False)
    for i in sortDic:
        attrsOutput.write(i[0] + '\t' + str(i[1]) + '\n')
    attrsOutput.close()
    
    for (k, v) in ATTRSVALUE.items():
        output = open(dirName + '/ATTR/' + k + '.bat', 'wb')
        output.write(str(len(v)) + '\n')
        for i in v:
            output.write(i + '\n')
        output.close()

def processMainSort(dirName, page, url):
    global ATTRS
    global FILECOUNTER
    if os.path.exists(dirName) == False:
        os.mkdir(dirName)
    ATTRS = {}
    middleStr = '&page='
    secondStr = 'ATTR'
    FILECOUNTER = 1
    for i in range(1, page):
        print "========== " + dirName + " Page " + str(i) + " =========="
        processSinglePage(dirName, secondStr, url + middleStr + str(i), i)
    storeMainSortAttrs(dirName, ATTRS)

main_name = ['DanJianBao', 'ShouTiBao', 'XieKuaBao', 'ShuangJianBao', 'QianBao', 'ShouNaBao', 'KaBao', 'YaoShiBao']
main_urls = ['http://list.jd.com/list.html?cat=1672,2575,5257', 'http://list.jd.com/list.html?cat=1672,2575,5259',
             'http://list.jd.com/list.html?cat=1672,2575,5260', 'http://list.jd.com/list.html?cat=1672,2575,5258',
             'http://list.jd.com/list.html?cat=1672,2575,2580', 'http://list.jd.com/list.html?cat=1672,2575,5256',
             'http://list.jd.com/list.html?cat=1672,2575,12070', 'http://list.jd.com/list.html?cat=1672,2575,12069']
main_page = []

def calculatePage(url):
    global main_page
    for i in url:
        response = requests.get(i)
        soup = bs4.BeautifulSoup(response.content, from_encoding="utf-8")
        page = soup.select('div#J_topPage i')
        main_page.append(int(page[0].string) + 1)

if __name__ == "__main__":
    calculatePage(main_urls)
    for i in range(9):
        processMainSort(main_name[i], main_page[i], main_urls[i])
