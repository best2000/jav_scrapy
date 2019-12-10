import requests, re, subprocess, random
from bs4 import BeautifulSoup

def junkie_search(code): #javjunkies.com
    code = code.replace('-', '')
    url = 'http://javjunkies.com/main/search/'+code
    r = requests.get(url)

    page = BeautifulSoup(r.text, 'html.parser')
    topbardiv = page.find_all(class_="posttop")
    print(url)
    print("found: ", len(topbardiv))
    date = []
    for i in topbardiv:
        href = i.find('a').attrs.get('href')
        href = re.split('/', href)
        print(href[4], href[5])

def get_dmm_cover_img(code): #dmm.co.jp
    code = code.replace('-', '')
    code = code.lower()
    print(code)
    url = 'http://pics.dmm.co.jp/mono/movie/adult/'+code+'/'+code+'pl.jpg'
    if code[0] == 'd' and code[1] == 'v':
        code = '53'+code
    elif code[0] == 'w' and code[1] == 'a' and code[2] == 'v' and code[3] == 'r':
        code = code[:4]+'00'+code[4:]
        print(code)
        url = 'https://jp.netcdn.space/digital/video/'+code+'/'+code+'pl.jpg' 

    print(url)
    r = requests.get(url)
    with open('pic/'+code+'.jpg', 'wb') as f:
        f.write(r.content)
    subprocess.run(['start', 'pic/'+code+'.jpg'], shell=True)

def clr_picfol():
    subprocess.run(['rmdir', '/Q', '/S', 'pic'], shell=True)
    subprocess.run(['mkdir', 'pic'], shell=True)

def maxjav():
    url = 'http://maxjav.com/188339/umr/'
    r = requests.get(url)
    print(r)
    page = BeautifulSoup(r.text, 'html.parser')
    for i in page.find_all(class_='title'):
        print(i.text)

def javmost():
    pass

maxjav()

