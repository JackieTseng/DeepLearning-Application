#!/usr/bin/python
# -*- encoding:utf-8 -*-
import sys, requests, bs4, urllib, os

allCounter = 0

# Check if next button exist
def checkNext(url):
    response = requests.get(url)
    soup = bs4.BeautifulSoup(response.content, from_encoding='utf-8')
    s = soup.select('a.paginate-more')
    if len(soup.select('a.paginate-more')) == 0:
        return None
    else:
        return s[0].attrs.get('href')

# Calculate the number of pages
def calculatePage(url):
    print "========== Calculating pages =========="
    response = requests.get(url)
    soup = bs4.BeautifulSoup(response.content, from_encoding='utf-8')
    word = soup.select('ul.list.paginate li a')
    word_urls = []
    nextUrl = checkNext(url)
    # check if next button exist
    if nextUrl == None:
        for i in word:
            if i.attrs.get('href') in word_urls:
                break
            word_urls.append(i.attrs.get('href'))
    else:
        word_urls.append(url)
        i = checkNext(url)
        while i != None:
            word_urls.append(i)
            response = requests.get(i)
            soup = bs4.BeautifulSoup(response.content, from_encoding='utf-8')
            i = checkNext(i)
        # add the final page
        i = word_urls[len(word_urls) - 1]
        pos1 = i.rfind('=') + 1
        pos2 = i.rfind('#')
        word_urls.append(i[:pos1] + str(int(i[pos1:pos2])+1) + i[pos2:])
    return word_urls

# Get the Item info : Icon, Name, Url
def getItemInfo(name, url):
    global allCounter
    response = requests.get(url)
    soup = bs4.BeautifulSoup(response.content, from_encoding='utf-8')
    app_name = ((soup.select('div.left > h1'))[0].string)
    print app_name,
    pic_url = soup.select('div.artwork > img')
    # Choose the right icon
    for i in pic_url:
        if i.attrs.get('alt') == app_name:
            pic_src = i.attrs.get('src-swap-high-dpi')
    filetype = pic_src[pic_src.rfind('.'):]
    req = requests.get(pic_src)
    # Handle if name include '/'
    if app_name.find('/') != -1:
        item = app_name.split('/')
        app_name = ''
        for i in item:
            app_name += i
    
    # download the icon
    pic_output = open((name + '/' + app_name + filetype).encode('utf-8'), 'wb')
    pic_output.write(req.content)

    # download the name and url
    output = open((name + '/' + app_name + '.txt').encode('utf-8'), 'wb')
    output.write(app_name.encode('utf-8') + '\n')
    output.write(url)
    output.close()
    allCounter += 1
    print " done..."

# Get all apps urls in number page
def getCurAllUrls(name, url, page):
    response = requests.get(url)
    soup = bs4.BeautifulSoup(response.content, from_encoding='utf-8')
    word = soup.select('div#selectedcontent a')
    word_urls = []
    for i in word:
        word_urls.append(i.attrs.get('href'))
    # Handle HttpConnection
    print "========== " + name + " Page " + str(page) + " =========="
    for i in word_urls:
        curCounter = 0
        while(True):
            # try 10 times otherwise record
            if curCounter == 10:
                output = open('miss.txt', 'ab')
                output.write(name + '\t' + i + '\n')
                output.close()
                break
            try:
                getItemInfo(name, i)
                break
            except:
                print " fail..."
                curCounter += 1
                pass

# Number Page
# https://itunes.apple.com/us/genre/ios-books/id6018?mt=8&letter=A
def getSortAllUrlsByAlpha(name, url):
    response = requests.get(url)
    soup = bs4.BeautifulSoup(response.content, from_encoding='utf-8')
    word_urls = calculatePage(url)
    if len(word_urls) == 0:
        getCurAllUrls(name, url ,1)
    else:
        counter = 1
        for i in word_urls:
            getCurAllUrls(name, i, counter)
            counter += 1

# Sort Page
# https://itunes.apple.com/us/genre/ios-books/id6018?mt=8 
def getSortAllUrls(name, url):
    response = requests.get(url)
    soup = bs4.BeautifulSoup(response.content, from_encoding='utf-8')
    word = soup.select('div#selectedgenre > ul li a')
    # get A-# pages
    word_url = [a.attrs.get('href') for a in word]
    for i in word_url:
        getSortAllUrlsByAlpha(name, i)

# Main Page 
# https://itunes.apple.com/us/genre/ios/id36?mt=8
def getMainUrls(url):
    global allCounter
    while(True):
        try:
            response = requests.get(url)
            break
        except:
            pass
    soup = bs4.BeautifulSoup(response.content, from_encoding='utf-8')
    # get top labels
    word = soup.select('div#genre-nav ul li a.top-level-genre')
    urls_set = [()]
    counter = 0
    for i in word:
        x = i.string.encode('utf-8')
        y = i.attrs.get('href')
        urls_set.append((x, y))
    
    # get second labels of Games
    allWord = soup.select('ul.list.column ul.list.top-level-subgenres > li a')
    gameWord = allWord[:18]
    for i in gameWord:
        x = ('Games/' + i.string).encode('utf-8')
        y = i.attrs.get('href')
        urls_set.append((x, y))

    # get second labels of News
    newsWord = allWord[18:]
    for i in newsWord:
        x = ('Newsstand/' + i.string).encode('utf-8')
        y = i.attrs.get('href')
        urls_set.append((x, y))

    # process each sort
    length = len(urls_set)
    for i in range(1, length):
        if os.path.exists(urls_set[i][0]) == False:
            os.mkdir(urls_set[i][0])
        allCounter = 0
        getSortAllUrls(urls_set[i][0], urls_set[i][1])
        output = open('record.txt', 'ab')
        output.write(urls_set[i][0] + '\t' + str(allCounter) + '\n')
        output.close()

def getMissPage():
    temp = {} 
    output = open('miss.txt', 'rb')
    items = output.readlines()
    for i in items:
        x, y = i.split('\t')
        if os.path.exists(x) == False:
            os.mkdir(x)
        counter = 0
        while(True):
            if counter == 20:
                break
            try:
                getItemInfo(x, y)
                temp[x] = y
                break
            except:
                print " fail..."
                pass
            counter += 1
    output.close()
    newOutput = open('miss.txt', 'wb')
    for i in items:
        x, y = i.split('\t')
        if x not in temp:
            newOutput.write(x + '\t' + y + '\n')
    newOutput.close()


if __name__ == "__main__":
    getMainUrls('https://itunes.apple.com/us/genre/ios/id36?mt=8')
    getMissPage()
