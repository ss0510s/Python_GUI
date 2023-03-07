# 단을 입력받아 결과를 출력하는 GUI기반 프로그램을 작성하시오.

import tkinter as tk
from tkinter import ttk

def gugu():
    ''' 버튼 클릭시 처리 '''
    try:
        # entry 글자 반환
        dan = int(en_dan.get())
        result = ''
        for i in range(1,10):
            result = result + f'{dan} x {i} = {dan*i}\n'
        # 글자 변환
        lbl_result.configure(text=result)
    #except valuerror
    # 에러처리
    except ValueError as e:
        lbl_result.configure(text='숫자만 입력 가능 합니다.\n에러내용: {0}'.format(e))
        # 값 삭제
        en_dan.delete(0, 'end')
        #print(e)

def enter_pressed(ev):
    ''' 엔터키 처리 '''
    gugu()

win = tk.Tk()
win.title("구구단 프로그램")
win.geometry('300x400')
win.resizable(False, False)

en_dan = tk.Entry(win)
lbl_result = tk.Label(win, text='구구단 출력')
btn_exe = tk.Button(win, text='실행', command=gugu)
# 디지안이 다름
# en_dan = ttk.Entry(win)
# lbl_result = ttk.Label(win, text='구구단 출력')
# btn_exe = ttk.Button(win, text='실행', command=gugu)

en_dan.bind('<Return>', enter_pressed)

en_dan.pack(fill='x')
btn_exe.pack(fill='x')
lbl_result.pack(fill='x')

win.mainloop()
