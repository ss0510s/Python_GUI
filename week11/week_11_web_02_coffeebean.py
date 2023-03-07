from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd
import time

# 웹 접속
def set_chrome_driver():
    chrome_options = webdriver.ChromeOptions()
    d = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
    return d

wd = set_chrome_driver()
shops = list()
coffeebean_url = 'https://www.coffeebeankorea.com/store/store.asp'

for i in range(400):
    wd.get(coffeebean_url)
    time.sleep(0.5)
    try:
        wd.execute_script(f'storePop2({i})')
        time.sleep(0.5)

        html = wd.page_source
        soup = BeautifulSoup(html, 'html.parser')
        store_name_h2 = soup.select("div.store_txt > h2")
        store_name = store_name_h2[0].string
        print(f"{store_name} : {i}")
        store_info = soup.select("div.store_txt > table.store_table > tbody > tr > td")
        store_addr_list = list(store_info[2])
        store_addr = store_addr_list[0].string
        store_phone = store_info[3].string
        shops.append([store_name]+[store_addr]+[store_phone])

    except:
        pass

cb_table = pd.DataFrame(shops, columns=['매장명', '주소', '전화번호'])
cb_table.to_csv('coffeebean.csv',encoding='utf-8',mode='w',index=True)