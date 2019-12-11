import requests
from bs4 import BeautifulSoup

# 1. 

url = "https://finance.naver.com/sise/"

html = requests.get(url).text

# 2. HTML 문서에서 손쉽게 데이터를 가져오기 위해 뷰티플수프 클래스 객체를 만든다

soup = BeautifulSoup(html, "html.parser")
print(type(soup))

#

# 3. 가져올 태그의 선택자를 넣고 결과물을 가져온다
# soup 
# 기본적인 사용법
# 1. .select_one(선택자) : 해당하는 태그 하나
# 2. .select(선택자) : 해당하는 모든 태그
kospi = soup.select_one("#KOSPI_now").text

print(kospi)


