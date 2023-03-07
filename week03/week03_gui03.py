# 단을 입력받아 결과를 출력하는 GUI기반 프로그램을 작성하시오.

import tkinter

def gugu():
    ''' 버튼 클릭시 처리 '''
    dan = int(en_dan.get())
    result = ''
    for i in range(1,10):
        result = result + f'{dan} x {i} = {dan*i}\n'

    # text 변환
    lbl_result.configure(text=result)

def enter_pressed(ev):
    ''' 엔터키 처리 '''
    gugu()

win = tkinter.Tk()
win.title("구구단 프로그램")
win.geometry('300x400')
win.resizable(False, False)

# entry
en_dan = tkinter.Entry(win)

# label
lbl_result = tkinter.Label(win, text='구구단 출력')
# button
btn_exe = tkinter.Button(win, text='실행', command=gugu)

# 엔터키
en_dan.bind('<Return>', enter_pressed)

# pack 위치
en_dan.pack(fill='x')
btn_exe.pack(fill='x')
lbl_result.pack(fill='x')

win.mainloop()