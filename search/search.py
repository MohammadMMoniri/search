from bs4 import BeautifulSoup
import requests
import re
import multiprocessing


def google(inp, llist):
    try:
        request = requests.get("https://www.google.com/search?q={}".format(inp))
    except:
        return([None])

    soup = BeautifulSoup(request.content, 'html.parser')
    for i in soup.find_all('a'):
        pattern = r"/url\?q=(.*)"
        z = re.search(pattern, i['href'])
        if z:
            llist.append(z.group(1))


def yahoo(inp, llist):
    try:
        request = requests.get("https://search.yahoo.com/search?p={}&fr=yfp-t&ei=UTF-8&fp=1".format(inp))
    except:
        return([None])
    soup = BeautifulSoup(request.content, 'html.parser')
    links = []
    for i in soup.find_all('h3', attrs={"class":"title ov-h"}):
        z = i.a['href']
        if z:
            llist.append(z)


def duckgo(inp):
    request = requests.get("https://duckduckgo.com/?q={}&t=h_&ia=web".format(inp))
    soup = BeautifulSoup(request.content, 'html.parser')
    links = []
    print(soup)
    for i in soup.find_all('h2',attrs={"class":"result__title"}):
        print(i)
        links += re.findall(pattern, i['href'])
    return links


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
    return links
    

def search_in_sites(inp):
    links_list = []
    # p1 = multiprocessing.Process(target=google, args=(inp, links_list))
    # p2 = multiprocessing.Process(target=yahoo, args=(inp, links_list))
    # p1.start()
    # p2.start()
    # p1.join()
    # p2.join()
    google(inp, links_list)
    yahoo(inp, links_list)

    return links_list
