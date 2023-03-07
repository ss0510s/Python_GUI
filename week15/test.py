import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from bs4 import BeautifulSoup
import urllib.request
import pandas as pd
import threading
import pyupbit
import time
import datetime
import random
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

class Hollys(threading.Thread):
    def __init__(self, name, parent):
        super().__init__()
        self.name = name
        self.pb = ttk.Progressbar(parent, orient=tk.HORIZONTAL, length=300)
        self.pb.pack(fill='x')
        self.thread = threading.Thread(target=run_progress, args=(self.pb,))
        self.thread.start()


def click_about():
    messagebox.showinfo('ipp', '12191754 남수진')


def run_progress(pb):
    shops = list()

    for i in range(1, 55):
        url = f'https://www.hollys.co.kr/store/korea/korStore2.do?pageNo={i}&sido=&gugun=&store='
        #print(f'{i} : {url}')
        pb['value'] = pb['value'] + 2
        page = urllib.request.urlopen(url)
        soup = BeautifulSoup(page, "html.parser")
        tbody = soup.find('tbody')
        trs = tbody.find_all('tr')

        for shop in trs:
            tds = shop.find_all('td')
            shop_name = tds[1].string  # 매장명
            shop_address = tds[3].string  # 주소
            shop_phone = tds[5].string  # 전화번호
            shops.append([shop_name] + [shop_address] + [shop_phone])

    hollys_df = pd.DataFrame(shops, columns=('매장명', '주소', '전화번호'))
    hollys_df.to_csv('hollys.csv', mode='w', encoding='cp949', index=True)


def hollys():
    # Hollys("할리스 매장정보").start()
    h = Hollys("할리스 매장정보", fr_tab2)
    h.daemon = True
    h.start()


def get_coin_price():
    global coin_price
    while True:
        coin_price = pyupbit.get_current_price("KRW-BTC")
        time.sleep(1)


def get_coin_1sec():
    global coin_price
    lbl_coin.configure(text=f'{coin_price}')
    lbl_date.configure(text=f'{datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")}')
    w.after(1000, get_coin_1sec)


def notice_apsl():
    global inha_url
    messagebox.showinfo('공지사항','아태물류학부')
    inha_url = 'https://apsl.inha.ac.kr/logistics/4465/subview.do'


def notice_gps():
    global inha_url
    messagebox.showinfo('공지사항', '공간정보공학과')
    inha_url = 'https://geoinfo.inha.ac.kr/geoinfo/2678/subview.do?enc=Zm5jdDF8QEB8JTJGYmJzJTJGZ2VvaW5mbyUyRjY0NiUyRmFydGNsTGlzdC5kbyUzRg%3D%3D'


def change_number(ev):
    global inha_url
    lbl_disp.configure(text=f'조회수 : {int(scaled.get())} (이상)')
    today = datetime.datetime.now()

    req = urllib.request.Request(inha_url)
    html = urllib.request.urlopen(req)
    soup = BeautifulSoup(html.read(), 'html.parser')

    announcement = f"{today.year}년 {today.month}월 {today.day}일 인하대학교 {soup.find('span').string} 공지사항 안내입니다.\n"

    trs = soup.find('tbody').find_all('tr')
    title_count = 1

    for tr in trs:
        tds = tr.find_all('td')
        title = tds[1].find('strong').string
        hit = tds[5].string.strip()
        if int(hit) >= int(scaled.get()):
            announcement += f'{title_count}번째 공지 / 조회수 : {hit} / {title}.\n'
        title_count += 1
    lbl_notice.configure(text=announcement)

def get_number():
    number = []
    while len(number) < 6:
        a = random.randint(1, 45)
        if a not in number:
            number.append(a)
    n_con = ''
    for i in range(0, 6):
        if i == 5:
            n_con = n_con + f'{number[i]}'
        else:
            n_con = n_con + f'{number[i]},'

    return n_con

def get_lotto() :
    listbox.delete(0, 4)
    listbox.insert(0, f"1회 : {get_number()}")
    listbox.insert(1, f"2회 : {get_number()}")
    listbox.insert(2, f"3회 : {get_number()}")
    listbox.insert(3, f"4회 : {get_number()}")
    listbox.insert(4, f"5회 : {get_number()}")

# 웹 접속
def set_chrome_driver():
    chrome_options = webdriver.ChromeOptions()
    d = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
    return d

wd = set_chrome_driver()
nate_url = 'https://www.nate.com/?f=news'
wd.get(nate_url)
element = wd.find_element(By.CLASS_NAME, 'ik')
element.click()

def get_keyword():
    html = wd.page_source
    soup = BeautifulSoup(html, 'html.parser')
    keyword = ''
    lists = soup.select('span.kwd-list')

    key_list = list(lists[0])
    for key in key_list:
        keyword = keyword + f'{key.string}'
    lbl_keyword.configure(text=keyword)

# global variable
inha_url = '인하대학교'

coin_price = 0
t1 = threading.Thread(target=get_coin_price)
#t2 = threading.Thread(target=change_number)
t1.daemon = True
#t2.daemon = True
t1.start()
#t2.start()


if __name__ == "__main__":
    w = tk.Tk()
    w.title("ipp - quiz")
    w.geometry("600x400")

    m_menubar = tk.Menu(w)

    file_menu = tk.Menu(m_menubar, tearoff=0)
    m_menubar.add_cascade(label="파일", menu=file_menu)
    file_menu.add_command(label="비트코인", command=get_coin_1sec)
    file_menu.add_command(label="로또", command=get_lotto)
    file_menu.add_separator()
    file_menu.add_command(label="종료", command=w.quit)

    help_menu = tk.Menu(m_menubar, tearoff=0)
    m_menubar.add_cascade(label="도움말", menu=help_menu)
    help_menu.add_command(label="정보", command=click_about)



    nb_tab = ttk.Notebook(w)
    fr_tab1 = ttk.Frame(nb_tab)
    nb_tab.add(fr_tab1, text='공지사항')

    btn_apsl = ttk.Button(fr_tab1, text='아태물류학과', command=notice_apsl)
    btn_gps = ttk.Button(fr_tab1, text='공간정보공학과', command=notice_gps)

    lbl_notice = ttk.Label(fr_tab1, text="")
    lbl_disp = ttk.Label(fr_tab1, text="조회수 : ? (이상)")
    scaled = tk.DoubleVar()
    s = ttk.Scale(fr_tab1, variable=scaled, from_=0, to=200, orient='h', command=change_number)
    btn_apsl.pack(fill='x')
    btn_gps.pack(fill='x')
    lbl_disp.pack()
    s.pack(fill='x')
    lbl_notice.pack()

    fr_tab2 = ttk.Frame(nb_tab)
    nb_tab.add(fr_tab2, text='커피')

    btn_hollys = ttk.Button(fr_tab2, text='할리스 정보 다운로드', command=hollys)
    btn_hollys.pack(fill='x')

    fr_tab3 = ttk.Frame(nb_tab)
    nb_tab.add(fr_tab3, text='비트코인')

    lbl_coin = tk.Label(fr_tab3, fg="red", text="  ", font=("Arial", 15, "italic"))
    lbl_date = tk.Label(fr_tab3, fg="blue", text="  ", font=("맑은 고딕", 13, "bold"))
    lbl_coin.pack()
    lbl_date.pack()

    # 프레임 4
    fr_tab4 = ttk.Frame(nb_tab)
    nb_tab.add(fr_tab4, text='로또추첨')
    listbox = tk.Listbox(fr_tab4, height=0)
    listbox.insert(0, "1회")
    listbox.insert(1, "2회")
    listbox.insert(2, "3회")
    listbox.insert(3, "4회")
    listbox.insert(4, "5회")
    listbox.pack()

    # 프레임5
    fr_tab5 = ttk.Frame(nb_tab)
    nb_tab.add(fr_tab5, text='네이트')
    btn_keyword = tk.Button(fr_tab5, text="실시간 검색", command=get_keyword)
    lbl_keyword = tk.Label(fr_tab5, text="실검")
    btn_keyword.pack(fill='x')
    lbl_keyword.pack()

    nb_tab.pack(fill='both')
    w.config(menu=m_menubar)
    w.mainloop()
