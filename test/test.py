import tkinter as tk
from tkinter import ttk
from abc import abstractmethod, ABCMeta

from bs4 import BeautifulSoup
import urllib.request
import threading
import datetime

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

# 웹 접속
def set_chrome_driver():
    chrome_options = webdriver.ChromeOptions()
    d = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
    return d

class WebSite(threading.Thread):
    name = ''
    url = ''
    thread = None
    def __init__(self):
        super().__init__()  # 부모 클래스(Thread)의 생성자 호출
        self.thread = threading.Thread(target=self.Crawling, args=(self,))
        self.thread.start()
    @abstractmethod
    def Crawling(self):
        pass


class WebServer:
    def __init__(self, wcf):
        self.wcf = wcf

    def webConnecting(self, name):
        # 웹 객체 생성
        website = self.wcf.createWeb(name)
        # 프레임, 레이블 추가
        fr_tab = ttk.Frame(nb_tab)
        nb_tab.add(fr_tab, text=name)

        content = website.Crawling()
        lbl_content = ttk.Label(fr_tab, text=content)
        lbl_content.pack()
        return website


class WebServerFactory:
    def createWeb(self, name):
        website = None
        if name == '정보통신공학과':
            website = informNotice()
        elif name == 'ZUM':
            website = zumSearch()
        elif name == 'Google':
            website = googleSearch()
        elif name == '네이트':
            website = nateSearch()
        return website


class informNotice(WebSite):
    def __init__(self):
        self.name = '정보통신공학과'
        self.url = 'https://ice.inha.ac.kr/ice/2250/subview.do'
    def Crawling(self):
        page = urllib.request.urlopen(self.url)  # 학과 홈페이지
        soup = BeautifulSoup(page, "html.parser")

        title = soup.select_one('a > span').string  # 학과 이름
        tbody = soup.find('tbody')
        trs = tbody.find_all('tr')

        # 공지사항 변수
        content = f'{datetime.datetime.now().strftime("%Y년 %m월 %d일")} 인하대학교 {title} 공지사항 안내입니다.\n\n'

        for i, tr in enumerate(trs):
            tds_title = tr.select('a > strong')
            title_str = tds_title[0].string  # 공지사항 제목
            tds = tr.find_all('td')

            content = content + f'{i + 1}번째 공지 / 조회수 : {int(tds[5].string)}/ {title_str}\n'
        return content

class zumSearch(WebSite):
    def __init__(self):
        self.name = 'zum'
        self.url = 'https://issue.zum.com/'
    def Crawling(self):
        page = urllib.request.urlopen(self.url)
        soup = BeautifulSoup(page, "html.parser")
        content = f'{datetime.datetime.now().strftime("%Y년 %m월 %d일")} zum 실시간 검색어\n\n'

        ul = soup.select('div.cont > span.word')

        for i, k in enumerate(ul):
            content = content + f'[{i+1}위] {k.string}\n'
        return content


class googleSearch(WebSite):
    def __init__(self):
        self.name = 'Google'
        self.url = "https://trends.google.co.kr/trends/trendingsearches/daily/rss?geo=KR"
    def Crawling(self):
        page = urllib.request.urlopen(self.url)
        soup = BeautifulSoup(page, "html.parser")
        content = f'{datetime.datetime.now().strftime("%Y년 %m월 %d일")} Google 실시간 검색어\n\n'

        ul = soup.select('item > title')

        for i, k in enumerate(ul):
            content = content + f'[{i+1}위] {k.string}\n'
        return content

class nateSearch(WebSite):
    def __init__(self):
        self.name = '네이트'
        self.url = 'https://www.nate.com/?f=news'
    def Crawling(self):
        wd = set_chrome_driver()
        wd.get(self.url)
        element = wd.find_element(By.CLASS_NAME, 'ik')
        element.click()

        html = wd.page_source
        soup = BeautifulSoup(html, 'html.parser')
        keyword = f'{datetime.datetime.now().strftime("%Y년 %m월 %d일")} 네이트 실시간 검색어\n\n'
        lists = soup.select('span.kwd-list > a')

        for i, key in enumerate(lists):
            keyword = keyword + f'[{i+1}위] {key.string}\n'
        return keyword

if __name__ == "__main__":
    w = tk.Tk()
    w.title("12191754 남수진")
    w.geometry("500x500")

    # 노트북 객체
    wc = WebServer(WebServerFactory())
    wc.daemon = True
    # wc.start()
    nb_tab = ttk.Notebook(w)

    # 프레임 객체1
    wc.webConnecting('정보통신공학과')

    # 프레임 객체2
    wc.webConnecting('ZUM')

    # 프레임 객체3
    wc.webConnecting('Google')

    # 프레임 객체4
    wc.webConnecting('네이트')


    nb_tab.pack(fill='both')
    w.mainloop()
