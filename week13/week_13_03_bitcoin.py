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

# 할리스 thread
class Hollys(threading.Thread):
    def __init__(self, name, parent):
        super().__init__()
        self.name = name
        self.pb = ttk.Progressbar(parent, orient=tk.HORIZONTAL, length=300)
        self.pb.pack(fill='x')
        self.thread = threading.Thread(target=run_progress, args=(self.pb,))
        self.thread.start()

# 도움말 클릭 이벤트
def click_about():
    messagebox.showinfo('ipp', 'Copyright © 2005–2022 Inha Univ')

# 할리스 csv 파일 다운
def run_progress(pb):
    shops = list()

    for i in range(1, 55):
        # 다운 받을 url
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

# hollys thread 생성
def hollys():
    # Hollys("할리스 매장정보").start()
    h = Hollys("할리스 매장정보", fr_tab2)
    h.daemon = True # 부모 thread가 죽으면 같이 종료
    h.start()

# 슬라이더 값 변경
def change_number(ev):
    lbl_disp.configure(text=f'슬라이더 값 : {int(scaled.get())}')

# coin price
def get_coin_price():
    global coin_price
    while True:
        coin_price = pyupbit.get_current_price("KRW-BTC")
        time.sleep(1)

# 1초당 coin, date update
def get_coin_1sec():
    global coin_price
    lbl_coin.configure(text=f'{coin_price}')
    lbl_date.configure(text=f'{datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")}')
    w.after(1000, get_coin_1sec)


# global variable
coin_price = 0
t1 = threading.Thread(target=get_coin_price) # thread 생성
t1.daemon = True  # 메인 스레드 종료시 자식 스레드도 같이 종료
t1.start()


if __name__ == "__main__":
    w = tk.Tk()
    w.title("멀티 쓰레딩")
    w.geometry("300x400")

    # 메뉴 생성
    m_menubar = tk.Menu(w)

    file_menu = tk.Menu(m_menubar, tearoff=0)
    m_menubar.add_cascade(label="파일", menu=file_menu)
    file_menu.add_command(label="비트코인", command=get_coin_1sec)
    file_menu.add_separator()
    file_menu.add_command(label="종료", command=w.quit)

    help_menu = tk.Menu(m_menubar, tearoff=0)
    m_menubar.add_cascade(label="도움말", menu=help_menu)
    help_menu.add_command(label="정보", command=click_about)

    # 노트북 객체
    nb_tab = ttk.Notebook(w)

    # 프레임 객체1
    fr_tab1 = ttk.Frame(nb_tab)
    nb_tab.add(fr_tab1, text='슬라이더')

    lbl_disp = ttk.Label(fr_tab1, text="슬라이더 값 : ")
    scaled = tk.DoubleVar()
    s = ttk.Scale(fr_tab1, variable=scaled, from_=0, to=100, orient='h', command=change_number)
    lbl_disp.pack()
    s.pack(fill='x')

    # 프레임 객체2
    fr_tab2 = ttk.Frame(nb_tab)
    nb_tab.add(fr_tab2, text='커피')

    btn_hollys = ttk.Button(fr_tab2, text='할리스 정보 다운로드', command=hollys)
    btn_hollys.pack(fill='x')

    # 프레임 객체3
    fr_tab3 = ttk.Frame(nb_tab)
    nb_tab.add(fr_tab3, text='비트코인')

    lbl_coin = tk.Label(fr_tab3, fg="red", text="  ", font=("Arial", 15, "italic"))
    lbl_date = tk.Label(fr_tab3, fg="blue", text="  ", font=("맑은 고딕", 13, "bold"))
    lbl_coin.pack()
    lbl_date.pack()

    nb_tab.pack(fill='both')
    w.config(menu=m_menubar)
    w.mainloop()


