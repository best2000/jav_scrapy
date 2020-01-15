import requests, bs4

res = requests.get('https://www.xvideos.com/')
soup = bs4.BeautifulSoup(res.text, 'lxml')



ti = soup.find_all(class_="title")
for p in ti:
    title = p.string ##vid title
    url = 'https://www.xvideos.com'+p.a['href'] ##vid url
    print(title)




