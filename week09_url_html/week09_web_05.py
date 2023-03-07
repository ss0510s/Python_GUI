import urllib.request
import urllib.parse
from bs4 import BeautifulSoup

api ='https://www.kma.go.kr/weather/forecast/mid-term-rss3.jsp'

urls = urllib.request.urlopen(api).read() # url 읽기
soup = BeautifulSoup(urls,"html.parser")

wfs = soup.find_all("wf")
# wfs = wfs[1:]
wfs.pop(0)
cities = soup.find_all("city")

# for wf in wfs:
#     print(wf)

# for i in range(len(cities)):
#     print(f'{cities[i].string}의 날씨는 {wfs[i*13].string}입니다.')

datas = soup.find_all("data")
for i in range(len(cities)):
    print(f'{cities[i].string}의 날씨는 {datas[i*13].find("wf").string}입니다.')