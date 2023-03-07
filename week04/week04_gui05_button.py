import tkinter as tk
from tkinter import ttk

def clicked():
    #btn_action.configure(text="클릭됨!")
    # lbl_a.configure(fg='red')
    # 버튼 글씨 변환
    btn_action.configure(text='안녕 {0}'.format(name.get()))
    # label 글자색 변환
    lbl_a.configure(foreground='red')
    # label text 변환
    lbl_a.configure(text='빨강 A 레이블')

win = tk.Tk()
win.title("버튼 프로그램")
win.geometry('300x200')
win.resizable(False, False)
win.configure(bg='white')

# label
lbl_a = ttk.Label(win, text="A 레이블")

# button
btn_action = ttk.Button(text="클릭하세요", command=clicked)
#btn_dummy = ttk.Button(text="그냥버튼")

# 변수 지정
name = tk.StringVar()

# entry 변수에 입력 받음
en_name = ttk.Entry(win, width=25, textvariable=name)

# 글자 위치 grid
en_name.grid(row=0, column=0, columnspan=2)

lbl_a.grid(row=1, column=0)
btn_action.grid(row=1, column=1)
#btn_dummy.grid(row=1, column=0, columnspan=2)
ttk.Button(text="그냥버튼").grid(row=2, column=0, columnspan=2)

win.mainloop()