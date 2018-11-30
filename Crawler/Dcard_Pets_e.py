import requests
from urllib.request import urlretrieve
from bs4 import BeautifulSoup
import os
import time
from urllib import error
import ssl
import urllib.request
from urllib.parse import quote
#from selenium import webdriver

# used to fix Python SSL CERTIFICATE_VERIFY_FAILED
# for MacOS
if (not os.environ.get('PYTHONHTTPSVERIFY', '') and getattr(ssl, '_create_unverified_context', None)):
    ssl._create_default_https_context = ssl._create_unverified_context

x = 0 # file name

d = str(input("Select a drive you want to download the photo.(Please enter C, D or E.)\n"))
type = str(input("Which type of article you want to download?\n"))
#type = 'pet'
#th = str(input("Enter key words you want to search.\n"))
#keyWord = quote(th)
#print(th)

print('Photos will be downloaded in %s:\\tem_py\\image_'%d+type)
print('')
print('Loading......\n')
time.sleep(5)

if not os.path.isdir('%s:\\tem_py'%d):
    os.mkdir('%s:\\tem_py'%d)
if not os.path.isdir('%s:\\tem_py\\image_'%d+type):
    os.mkdir('%s:\\tem_py\\image_'%d+type)

#url = 'https://www.dcard.tw/f/pet'
#url = 'https://www.dcard.tw/f/pet?latest=false'
url = 'https://www.dcard.tw/f/' + type + '?latest=false'
#url = 'https://www.dcard.tw/search/general?forum=pet&query=' + keyWord
'''urlTem = 'https://www.dcard.tw/search/general?forum=pet&query=' + keyWord
# opener
opener = urllib.request.build_opener()
opener.addheaders = [('User-Agent',
                      'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1941.0 Safari/537.36')]
urllib.request.install_opener(opener)
url = urllib.request.urlopen(urlTem)'''
#url = 'https://www.dcard.tw/search/general?forum=pet&query=%E6%9F%AF%E5%9F%BA'

# pretend to be a explorer
'''headers = {
    'User-Agent':'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6'
}
'''
headers={'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
   'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
   'Accept-Encoding': 'none',
   'Accept-Language': 'en-US,en;q=0.8',
   'Connection': 'keep-alive'}

'''
request_=urllib.request.Request(url,None,headers) #The assembled request
response = urllib.request.urlopen(request_)# store the response
#create a new file and write the image
f = open('00000001.jpg','wb')
f.write(response.read())
f.close()
'''

'''
browser = webdriver.Chrome()
browser.get(url)
browser.execute_script('window.scrollTo(0, document.body.scrollHeight)')
browser.execute_script('alert("To Bottom")')
'''


mainURL = requests.get(url, headers = headers)
mainSoup = BeautifulSoup(mainURL.text, 'html.parser')

#title = mainSoup.select('div .PostList_wrapper_2BLUM a')
title = mainSoup.select('h3') # title[i].text
href = mainSoup.select('div .PostList_wrapper_2BLUM a') #href[i]['href']

try:

    for i in range(0, len(href)): # get each article
        print(title[i].text)
        print('https://www.dcard.tw' + href[i]['href'])
        print('---------------')

        artURL = requests.get('https://www.dcard.tw' + href[i]['href'], headers = headers)
        artSoup = BeautifulSoup(artURL.text, 'html.parser')
        imgURL = imgURL = artSoup.select('div .Post_content_NKEl9 div div div img') # imgURL is a list

        try:

            for j in imgURL:
                target = j['src']
                local = os.path.join(d + ':\\tem_py\\image_' + type + '\\%s.jpg'% x)
                #local = os.path.join('/Users/uuboy.scy/PycharmProjects/Python/image_' + type + '/%s.jpg'% x)

                # opener
                opener = urllib.request.build_opener()
                opener.addheaders = [('User-Agent',
                                      'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1941.0 Safari/537.36')]
                urllib.request.install_opener(opener)

                try:
                    urlretrieve(target, local)
                    print('%s downloaded.' % x)
                    x += 1
                except IndexError as k:
                    print('list out of range!')

        except error.HTTPError as e:
            print('http error')
        except error.URLError as e:
            print('url error')

        print('---------------')
        time.sleep(5)

except IndexError as er:
    print('list index out of range!')

print('All done!')