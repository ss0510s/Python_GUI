from bs4 import BeautifulSoup

html = """
<html>
<head>
<title>스크레이핑 실습</title>
</head>
<body>
<h1>인하대학교</h1>
<p>웹스크레이핑</p>
<p>파이썬 기본 문법, pandas, GUI, ...</p>
</body>
</html>
"""

soup = BeautifulSoup(html, 'html.parser') # html 파일 읽기
t = soup.html.head.title #html의 Head의 title만 읽기
print(t.string)

h1 = soup.html.body.h1
print(h1.string)

p1 = soup.html.body.p
print(p1.string)

p2 = p1.next_sibling.next_sibling.string
print(p2)
