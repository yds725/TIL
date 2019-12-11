# 0. 관련 모듈 

import requests
from bs4 import BeautifulSoup

# 1. 문자열형태

url = "https://finance.naver.com/marketindex/"

html = requests.get(url).text

soup = BeautifulSoup(html, "html.parser")

print(type(soup))

# Selector
exchange_rate = soup.select(".value")

for e in exchange_rate:
    print(e.text)

#print(exchange_rate)