from urllib.request import urlopen
from bs4 import BeautifulSoup

html=urlopen('http://yle.fi')
html2=urlopen('http://hs.fi')
bs = BeautifulSoup(html.read(), 'html.parser')
bs2 = BeautifulSoup(html2.read(), 'html.parser')
print(bs.body)
print(bs2.body)