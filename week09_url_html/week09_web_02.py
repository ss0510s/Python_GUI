# import urllib.request
#
# urls = urllib.request.urlopen("https://api.aoikujira.com/ip/ini").read() # 이미지를 다운받아서 메모리에 저장
# print(urls)
# texts = urls.decode('utf-8')
# print(texts)

import urllib.request
import urllib.parse

api ='https://www.kma.go.kr/weather/forecast/mid-term-rss3.jsp'

id = input('지역코드: ')
values = {'stnId': id} # 108: 전국, 109: 서울/인천/경기, 105: 강원도
parameters = urllib.parse.urlencode(values)
url = api + '?' + parameters

urls = urllib.request.urlopen(url).read()
texts = urls.decode('utf-8')
print(texts)



