#!/usr/bin/python
import sys, requests, bs4, urllib, os

allCounter = 0

def getItemInfo(name, url):
    global allCounter
    response = requests.get(url)
    soup = bs4.BeautifulSoup(response.content, from_encoding='utf-8')
    app_name = (soup.select('div.left > h1'))[0].string
    print app_name,
    pic_url = soup.select('div.artwork > img')
    for i in pic_url:
        if i.attrs.get('alt') == app_name:
            pic_src = i.attrs.get('src-swap-high-dpi')
    filetype = pic_src[pic_src.rfind('.'):]
    req = requests.get(pic_src)
    if app_name.find('/') != -1:
        item = app_name.split('/')
        app_name = ''
        for i in item:
            app_name += i
    
    pic_output = open(name + '/' + app_name + filetype, 'wb')
    pic_output.write(req.content)

    output = open(name + '/' + app_name + '.txt', 'wb')
    output.write(url)
    output.close()
    allCounter += 1
    print " done..."

def getCurAllUrls(name, url):
    response = requests.get(url)
    soup = bs4.BeautifulSoup(response.content, from_encoding='utf-8')
    word = soup.select('div#selectedcontent a')
    word_urls = []
    for i in word:
        word_urls.append(i.attrs.get('href'))
    for i in word_urls:
        while(True):
            try:
                getItemInfo(name, i)
                break
            except:
                pass

def getSortAllUrlsByAlpha(name, url):
    response = requests.get(url)
    soup = bs4.BeautifulSoup(response.content, from_encoding='utf-8')
    word = soup.select('div#selectedgenre > ul li a')
    word_urls = []
    for i in word:
        if i.string.isdigit() or i.string == 'Next':
            if i.string == 'Next':
                break
            word_urls.append(i.attrs.get('href'))
    for i in word_urls:
        getCurAllUrls(name, i)

def getSortAllUrls(name, url):
    response = requests.get(url)
    soup = bs4.BeautifulSoup(response.content, from_encoding='utf-8')
    word = soup.select('div#selectedgenre > ul li a')
    # A-#
    word_url = [a.attrs.get('href') for a in word]
    for i in word_url:
        getSortAllUrlsByAlpha(name, i)

def getMainUrls(url):
    global allCounter
    response = requests.get(url)
    soup = bs4.BeautifulSoup(response.content, from_encoding='utf-8')
    word = soup.select('div#genre-nav ul li a')
    urls_set = [()]
    counter = 0
    for i in word:
        x = i.string.encode('utf-8')
        y = i.attrs.get('href')
        urls_set.append((x, y))
    length = len(urls_set)
    for i in range(1, length):
        if os.path.exists(urls_set[i][0]) == False:
            os.mkdir(urls_set[i][0])
        allCounter = 0
        getSortAllUrls(urls_set[i][0], urls_set[i][1])
        output = open('record.txt', 'ab')
        output.write(urls_set[i][0] + '\t' + allCounter + '\n')
        output.close()


if __name__ == "__main__":
    #getItemInfo('Books','https://itunes.apple.com/us/app/advance-pdfs-pro-reader/id919169075?mt=8')
    #getCurAllUrls('https://itunes.apple.com/us/genre/ios-books/id6018?mt=8&letter=A&page=1#page')
    #getSortAllUrlsByAlpha('https://itunes.apple.com/us/genre/ios-books/id6018?mt=8&letter=A')
    #getSortAllUrls('https://itunes.apple.com/us/genre/ios-books/id6018?mt=8')
    getMainUrls('https://itunes.apple.com/us/genre/ios/id36?mt=8')
    print allCounter
