#!/usr/bin/python
import sys, requests, bs4, urllib

#reload(sys)
#sys.setdefaultencoding("utf8")
FILECOUNTER = 1
ATTRS = {}

# Write a page in jd.com(woman-bag)
def getItemInfo(url):
    global FILECOUNTER
    global ATTRS
    response = requests.get(url)
    #output = open('womanbag.html', 'w')
    #output.write(response.content)
    #output.close()
    soup = bs4.BeautifulSoup(response.content, from_encoding="utf-8")
    # download img
    pic_url = soup.select('div#preview img')
    pic_src = pic_url[0].attrs.get('src')
    filetype = pic_src[pic_src.rfind('.'):]
    req = requests.get(pic_src)
    pic_output = open(str(FILECOUNTER) + filetype, 'wb')
    pic_output.write(req.content)

    # download attrs in li
    param_list = soup.select('ul#parameter2 > li')
    if len(param_list) == 0:
        param_list = soup.select('div#product-detail ul.detail-list li')
    param_str_list = [a.string for a in param_list]
    param_output = open(str(FILECOUNTER) + '.txt', 'wb')
    for i in param_str_list:
        if i != None:
            pos = i.find(u'\uff1a')
            key = i[:pos].encode('utf-8')
            if key not in ATTRS:
                ATTRS[key] = 1
            else:
                ATTRS[key] += 1
            value = i[pos + 1:].encode('utf-8')
            param_output.write(key + '\t' + value + '\n')

    # download attrs in table
    if soup.select('ul.m-tab-trigger li#detail-tab-param') != None:
        table = soup.select('div#product-detail-2 > table.Ptable')
        td = soup.select('td')
        i = 0
        counter = len(td)
        while i < counter:
            while td[i] == None or td[i].string is None or len((td[i].string).strip()) == 0:
                i+= 1
            key = td[i].string.encode('utf-8')
            if key not in ATTRS:
                ATTRS[key] = 1
            else:
                ATTRS[key] += 1
            value = td[i + 1].string.encode('utf-8')
            param_output.write(key + '\t' + value + '\n')
            i += 2

    # write url
    param_output.write('url'.encode('utf-8') + '\t' + url.encode('utf-8'))
    param_output.close()
    FILECOUNTER += 1

# Get all the urls in the current web page
def getCurUrls(url, page):
    response = requests.get(url)
    soup = bs4.BeautifulSoup(response.content, from_encoding="utf-8")
    urls = soup.select('div.p-img a[href]')
    urls_list = [a.attrs.get('href') for a in urls]
    itemCounter = 1
    for i in urls_list:
       print i,
       try:
           getItemInfo(i)
       except:
           errorOutput = open('error.bat', 'ab')
           errorOutput.write(str(page) + "\t" + str(itemCounter) + "\t" + i + '\n')
           errorOutput.close()
       itemCounter += 1
       print " dones.."

# store the whole sort's attributes
def storeAttrs(attrs):
    try:
        output = open("attrs.bat", 'rb')
        for line in output:
            key, value = line.split('\t')
            if key not in attrs:
                attrs[key] = 1
            else:
                attrs[key] += value
    except:
        pass
    attrsOutput = open('attrs.bat', 'wb')
    sortDic = sorted(attrs.iteritems(), key = lambda d:d[0], reverse = False)
    for i in sortDic:
        attrsOutput.write(i[0] + '\t' + str(i[1]) + '\n')
    attrsOutput.close()

if __name__ == "__main__":
    '''
    preCurUrl = 'http://list.jd.com/list.html?cat=1672,2575,12069&page='
    for pageCounter in range(1, 10):
        print "========================= " + str(pageCounter) + " ================================"
        getCurUrls(preCurUrl + str(pageCounter), pageCounter)
    storeAttrs(ATTRS)
    '''
    #getItemInfo('http://item.jd.com/1037568901.html')
    getItemInfo('http://item.jd.com/1505812327.html')
