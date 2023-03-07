import urllib.request
from bs4 import BeautifulSoup
import datetime
import sqlite3
import pandas as pd

shops = list()

for i in range(1, 55):
    # hollys url 링크
    url = f'https://www.hollys.co.kr/store/korea/korStore2.do?pageNo={i}&sido=&gugun=&store='
    # print(url)
    page = urllib.request.urlopen(url) # url 읽기
    soup = BeautifulSoup(page, 'html.parser') # html읽기
    tbody = soup.find('tbody') # tbody 만 읽기
    trs = tbody.find_all('tr') # 10개 행을 리스트로 리턴

    for shop in trs: # 맨 마지막 페이지를 제외하고 페이지당 10개 매장
        tds = shop.find_all('td')
        shop_name = tds[1].string # 매장명
        shop_address = tds[3].string # 주소
        shop_phone = tds[5].string # 전화번호
        shops.append([shop_name]+[shop_address]+[shop_phone])

# print(shops)
hollys_df = pd.DataFrame(shops, columns=('매장명','주소','전화번호'))
hollys_df.to_csv('hollys.csv', mode ='w', encoding='utf-8', index=True) # utf8