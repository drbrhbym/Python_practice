import requests
from urllib.request import urlretrieve
import re
from bs4 import BeautifulSoup
import os
import time
from urllib.error import HTTPError

page = 2721
x = 0 # file name
rang = 250 # pages
'''try:
    catch = abs(int(input('How many pages do you want to download?\n')))
    rang = catch
except TypeError as typ:
    rang = 30
    print('defult(30)')
except ValueError as valero:
    rang = 30
    print('defult(30)')
'''
'''
print('Files will be downloaded in the path E:\\tem_py\\image')
print('Have fun!')
time.sleep(3)
'''
if not os.path.isdir('E:\\tem_py'):
    os.mkdir('E:\\tem_py')
if not os.path.isdir('E:\\tem_py\\image'):
    os.mkdir('E:\\tem_py\\image')

for pg in range(0,rang):

    print('**page : %s'%pg)

    a = requests.get('https://www.ptt.cc/bbs/Beauty/index%s.html'%(page-pg))

    soup = BeautifulSoup(a.text, 'html.parser')

    title = soup.select('div .title')
    href = soup.select('div .title a')

    try:
        for i in range(0, len(title)):
            print(title[i].text)
            print('https://www.ptt.cc'+href[i]['href'])

            arti = requests.get('https://www.ptt.cc'+href[i]['href'])
            artiSoup = BeautifulSoup(arti.text, 'html.parser')
            theme = artiSoup.select('a')

            try:
                for j in theme:
                    target = re.findall('https://i.imgur.com/[a-zA-Z0-9]*.[pj][np]g', j.text)
                    local = os.path.join('E:\\tem_py\\image\\%s.png' % x)
                    if len(target) != 0: # if url is not null , download the file
                        try:
                            urlretrieve(target[0], local)
                            print('%s downloaded.' % x)
                            x += 1
                        except IndexError as k:
                            print('list out of range!')

            except HTTPError as e:
                print('Done!')

            print('----------')
            time.sleep(10)
    except IndexError as er:
        print('list index out of range!')
    print('**page %s done.' % pg)

'''
print('All done!')
print('You have downloaded %s photos.'%x)
print('Good luck!')
time.sleep(10)
'''