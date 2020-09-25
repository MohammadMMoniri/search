from django.db import models
from bs4 import BeautifulSoup
import requests
import re
import _thread



def google(inp):
    try:
        request = requests.get("https://www.google.com/search?q={}".format(inp))
    except:
        return(None)
    soup = BeautifulSoup(request.content, 'html.parser')
    links = []
    for i in soup.find_all('a'):
        pattern = r"/url\?q=(.*)"
        links.append(re.findall(pattern, i['href']))
    return(links)




def yahoo(inp):
    try:
        request = requests.get("https://search.yahoo.com/search?p={}&fr=yfp-t&ei=UTF-8&fp=1".format(inp))
    except:
        return(None)
    soup = BeautifulSoup(request.content, 'html.parser')
    links = []
    for i in soup.find_all('h3', attrs={"class":"title ov-h"}):
        links.append(i.a['href'])
    return(links)



def duckgo(inp):
    request = requests.get("https://duckduckgo.com/?q={}&t=h_&ia=web".format(inp))
    soup = BeautifulSoup(request.content, 'html.parser')
    links = []
    print(soup)
    for i in soup.find_all('h2',attrs={"class":"result__title"}):
        print(i)
        links += re.findall(pattern, i['href'])
    return(links)

# duckgo("salam")

def bing(inp):
    try:
        request = requests.get("https://www.bing.com/search?q={}&qs=n&form=QBRE&sp=-1&pq=sa&sc=8-2&sk=&cvid=411F5953DD624F6880C26E23A5E88BA2".format(inp))
    except:
        print("network fucked up!")
    soup = BeautifulSoup(request.content, 'html.parser')
    links = []
    for i in soup.find_all('a'):
        print(i)
        i = i.find('h2')
        print(i)
        i.find('a')
        print(i.find('a')['href'])
        links += i
    print(links)
    return(links)
    


def search_in_sites(inp):
    try:
    _thread.start_new_thread(google, inp)
    _thread.start_new_thread(yahoo, inp)
    print(yahool)
    print(googlel)

search_in_sites("sex")