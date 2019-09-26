import os
try: 
    from googlesearch import search 
except ImportError:  
    print("No module named 'google' found") 
inp = input("Yeet smthing : ")
l =  search(inp, tld='com', lang='en', num=1, stop=1, pause= 2)
with open('links.txt', 'a+') as filee:
    for link in l:
        filee.write(link)
        filee.write(" ")
os.system('scrapy crawl quotespider')
        

