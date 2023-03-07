import urllib.request
from bs4 import BeautifulSoup
import datetime
import sqlite3

# url 읽고 저장
result = urllib.request.urlopen("https://finance.naver.com/marketindex/")
soup = BeautifulSoup(result, "html.parser")

# html에서 div가 head_info인 태그 내의 span의 value만 조회한 뒤, string으로 전환
usd = soup.select_one("div.head_info > span.value").string
now = datetime.datetime.now()

# print(usd, now)

# db 생성
conn = sqlite3.connect('naver.db')
cur = conn.cursor()
conn.execute('create table if not exists finance '
             '(id integer primary key autoincrement,'
             'exchangerate text not null,'
             'dates text not null);')

# 조회 결과 삽입
cur.execute('insert into finance(exchangerate, dates) '
            'values (?,?)', (usd, now))

conn.commit() # commit

cur.execute('select * from finance') # 조회
rows = cur.fetchall() # 모든 데이터를 가져옴
print(rows)

cur.close()
conn.close()


