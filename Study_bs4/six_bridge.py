from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
import random

#-------------1 example ------------
# html = urlopen('https://en.wikipedia.org/wiki/Kevin_Bacon')
# bs = BeautifulSoup(html, 'html.parser')

# for link in bs.find('div',{'id':'bodyContent'}).findAll('a',href = re.compile('^(/wiki/)((?!:).)*$')):
#     if 'href' in link.attrs:
#         print(link.attrs['href'])

# ------------ 2 example ------------
# def getLink(articleUrl):
#     html = urlopen(f'https://en.wikipedia.org{articleUrl}')
#     bs = BeautifulSoup(html, 'html.parser')
#     return bs.find('div', {'id':'bodyContent'}).findAll('a', href=re.compile('^(/wiki/)((?!:).)*$'))

# start_link = '/wiki/Kevin_Bacon'

# links = getLink(start_link)
# while len(links)>0:
#     newArticle = links[random.randint(0, len(links)-1)].attrs['href']
#     print(newArticle)
#     links = getLink(newArticle)

#---------------3 example ------------
pages = set()

def getLinks(pageUrl):
    global pages
    html = urlopen(f'https://en.wikipedia.org{pageUrl}')
    bs = BeautifulSoup(html, 'html.parser')
    for link in bs.find_all('a', href=re.compile('^(/wiki/)')):
        if 'href' in link.attrs:
            if link.attrs['href'] not in pages:
                # 새 링크를 발견
                new_page = link.attrs['href']
                print(new_page)
                pages.add(new_page)
                getLinks(new_page)
getLinks('')