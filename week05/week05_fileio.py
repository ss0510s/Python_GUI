# fp = open('week05.txt', 'w', encoding='UTF8')
# fp = open('week05.txt', 'a', encoding='UTF8')
#
# fp.write('Hello World')
# fp.write('안녕 파이썬')
# print('프린트함수 사용', file=fp)
# print('Hi', file=fp)
# fp.close()

# fp = open('week05.txt', 'r', encoding='UTF8')
# notes = fp.readlines() # list로 리턴
# # print(notes)
# for note in notes:
#     # print(note, end='')
#     print(note.rstrip('\n'))
# fp.close()

# 파일 오픈
# 'r' read 'w' write 'a' 추가
with open('week05.txt', 'r', encoding='UTF8') as fp:
    notes = fp.readlines() # list로 한 줄씩 리턴
    for note in notes:
        print(note, end='')
