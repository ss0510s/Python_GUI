import urllib.request

# url = "https://www.inha.ac.kr/sites/kr/images/logo.png"
# urllib.request.urlretrieve(url, 'inha.png') # 이미지를 보조기억장치에 저장
# print('저장완료')

url = "https://www.inha.ac.kr/sites/kr/images/logo.png"
x = urllib.request.urlopen(url).read() # 이미지를 다운받아서 메모리에 저장

with open('inha.png','wb') as fw:
    fw.write(x)
    print('저장완료')


