# from bs4 import BeautifulSoup
#
# html = """
# <html>
# <head>
# <title>스크레이핑 실습</title>
# </head>
# <body>
# <h1 id="univ">인하대학교</h1>
# <p>ipp ncs</p>
# <p id="contents">파이썬 기본 문법, pandas, GUI, ...</p>
# </body>
# </html>
# """
#
# soup = BeautifulSoup(html, 'html.parser')
# university = soup.find(id='univ')
# contents = soup.find(id='contents')
#
# print(university.string)
# print(contents.string)

from bs4 import BeautifulSoup

html = """
<html>
<head>
<title>스크레이핑 실습</title>
</head>
<body>
<a href="https://www.inha.ac.kr">인하대학교</a><br>
<a href="https://www.harvard.edu">하버드대학교</a>
</body>
</html>
"""

soup = BeautifulSoup(html, 'html.parser')
urls = soup.find_all("a") # find_all 함수는 결과를 리스트에 담아 리턴

# print(urls)

for url in urls:
    univ = url.string
    link = url.attrs["href"] # href 속성만 읽기
    print(f'{univ}의 url주소는 {link}입니다.')