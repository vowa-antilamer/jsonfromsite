import json
from collections import defaultdict

import requests
from bs4 import BeautifulSoup, element

url = "http://www.peterburg-kino.spb.ru/druzba"

response = requests.get(url)
html = response.text
d = defaultdict(list)
soup = BeautifulSoup(html, "lxml")
for element1 in soup.find_all("div", {"class": "movie-block"}):
    dateess = ''
    key = element1.find('div', {'class': 'movie-seans '}).text
    content = element1.find('div', {'class': 'movie-name trigger'}).text
    if element1:
        for ss in element1.previous_elements:
            if type(ss) is element.Tag:
                if ss.name == 'h1':
                    dateess = ss.text
                    break
    d[dateess].append([content, key])
print(json.dumps(d))
