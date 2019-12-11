import urllib.request
from bs4 import BeautifulSoup
import re
import urllib.parse
def menu():
    links=[]
    who=input("Registrant Name or Email Address: ")
    whois=urllib.parse.quote(who)
    headers={'User-Agent' : "Mozilla/5.0 (X11; Linux x86_64; rv:24.0) Gecko/20100101 Firefox/24.0"}
    req=urllib.request.Request("https://viewdns.info/reversewhois/?q="+whois,headers=headers)
    resp=urllib.request.urlopen(req).read()
    soup=BeautifulSoup(resp,"html.parser")
    font= soup.findAll('font',face="Courier")
    for i in font:
        x=re.sub('<.*?>','\n',i.text)
        links.append(x)
    links="\n".join(links)
    print(links)
menu()
