import requests, bs4, random, os, time

#get web page
print("Fetching from xvideos.com")
res = requests.get('https://www.xvideos.com/')
soup = bs4.BeautifulSoup(res.text, 'lxml')

#html parse
ti = soup.find_all(class_="title")
titles = []
for p in ti:
    title = p.string ##vid title
    url = 'https://www.xvideos.com'+p.a['href'] ##vid url
    titles.append(title)

def hm():
    #select good title
    while True:
        ran = titles[random.randint(0,len(titles)-1)]
        if len(ran) <= 40:
            ranti = ran
            break

    #setup
    tilis = []
    for i in range(len(ranti)): 
        tilis.append(ranti[i])
    print(ranti)
    ans = []
    cslis = []
    for i in range(len(tilis)): 
        uc = ord(tilis[i])
        if (uc >= 65 and uc <= 90) or (uc >= 97 and uc <= 122):
            cslis.append("_")
        else:
            cslis.append(tilis[i]) 
    hp = 7
    alis = []

    #main loop
    while True:
        #progess print  
        os.system('cls')
        print("HP:", hp)
        print("Guessed:", alis)
        for i in range(len(cslis)):
            print(cslis[i]+" ",end="")

        #if it finished
        if "_" not in cslis:
            break
        if hp == 0:
            print("\nYOU DIED...")
            print(ranti)
            break

        #get ans
        ans = input("\nGuess: ")
        
        #check ans
        tgr = 0
        if ans.lower() in alis or ans.upper() in alis:
            tgr = 1
        else: 
            alis.append(ans) 
        if tgr == 0:
            for i in range(len(tilis)):
                if tilis[i] == ans.upper() or tilis[i] == ans.lower():
                    cslis[i] = tilis[i]
                    tgr = 2
                    
        
        #ans result 
        if tgr == 0:
            hp -= 1
            print("WRONG!\nHP-1")
        elif tgr == 1:
            print("You already guessed this char!")
        elif tgr == 2:
            print("CORRECT!")
        time.sleep(1)

while True:
    os.system('cls')
    hm()
    inp = input("\nAgain?[y/n]: ")
    if inp == "y":
        continue
    break
