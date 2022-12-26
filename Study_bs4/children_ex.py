from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

# html = urlopen('https://pythonscraping.com/pages/page3.html')
html = urlopen('https://pythonscraping.com/pages/warandpeace.html')
bs = BeautifulSoup(html, 'html.parser')

child = bs.findAll(text='the prince')
# for i in child:
#     print('\n\n')
#     print(i)
print(len(child))