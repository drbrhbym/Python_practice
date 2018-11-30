import requests
from urllib.request import urlretrieve
import re
from bs4 import BeautifulSoup
import os
import time
from urllib.error import HTTPError

x = 0 # used for file name

a = requests.get('https://www.ptt.cc/bbs/Beauty/M.1542282992.A.B37.html')
soup = BeautifulSoup(a.text, 'html.parser')
theme = soup.select('a')

try:
    for i in theme:
        target = re.findall('https://i.imgur.com/[a-zA-Z0-9]*.png', i.text)
        local = os.path.join('E:\\python\\img\\%s.png' % x)
        try:
            urlretrieve(target[0], local)
            print('%s.png done.' % x)
            x += 1
        except IndexError as k:
            print('out of range!')
        #time.sleep(10)
except HTTPError as e:
    print('Done!')
print('Done!')

