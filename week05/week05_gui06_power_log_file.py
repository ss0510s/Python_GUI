# 거듭제곱 프로그램을 작성하시오

import tkinter as tk
from tkinter import ttk
import datetime

def power():
    try:
        # 변수 반환
        b = int(name_b.get())
        e = int(name_e.get())
        result = 1
        for i in range(0, e):
            result = b * result
        # text 출력
        lbl_result.configure(text=f"{b}의 {e}승의 결과는 {result}입니다.")

    # 에러 처리
    except ValueError as e:
        error = f'[{datetime.datetime.now()}] 밑: {name_b.get()}, 지수: {name_e.get()} 에러!\n숫자만 입력 가능 합니다.\n에러 내용: {e}\n\n'
        # 파일 open
        with open('log.txt', 'a') as fp:
            # fp.write(str(datetime.datetime.now()))
            # fp.write('\n')
            fp.write(error) # 파일 write
        lbl_result.configure(text=error)
        en_name_b.delete(0, 'end')
        en_name_e.delete(0,'end')
        en_name_b.focus()

def enter_power(ev):
    power()

def shift_entry(ev):
    en_name_e.focus()

if __name__ == "__main__":
    win = tk.Tk()
    win.title("거듭제곱 프로그램")
    win.geometry('300x200')
    win.resizable(False, False)

    lbl_b = ttk.Label(win, text="밑")
    lbl_e = ttk.Label(win, text="지수")
    name_b = tk.StringVar()
    name_e = tk.StringVar()
    en_name_b = ttk.Entry(win, width=8, textvariable=name_b)
    en_name_e = ttk.Entry(win, width=8, textvariable=name_e)
    btn_result = ttk.Button(text='결과 출력', width=25, command=power)
    lbl_result = ttk.Label(win, text='결과')

    lbl_b.grid(row=0, column=0)
    en_name_b.grid(row=0, column=1)
    lbl_e.grid(row=0, column=2)
    en_name_e.grid(row=0, column=3)
    lbl_result.grid(row=2, column=0, columnspan=4)
    btn_result.grid(row=1, column=0, columnspan=4)

    en_name_b.bind('<Return>', shift_entry)
    # win.bind('<Return>', enter_power)
    en_name_e.bind('<Return>', enter_power)
    en_name_b.focus()

    win.mainloop()