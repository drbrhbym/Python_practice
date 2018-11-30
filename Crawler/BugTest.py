import requests

from bs4 import BeautifulSoup

page = 2721

for pg in range(0,5):

    a = requests.get('https://www.ptt.cc/bbs/Beauty/index%s.html'%(page-pg))

    soup = BeautifulSoup(a.text, 'html.parser')

    #for tag in soup.find_all('a'):
    #    print(tag)

    title = soup.select('div .title')
    href = soup.select('div .title a')

    try:
        for i in range(0, len(title)):
            print(title[i].text)
            print('https://www.ptt.cc'+href[i]['href'])
            print('----------')
    except IndexError as er:
        print('list index out of range')
