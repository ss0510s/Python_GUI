# 거듭제곱 프로그램을 작성하시오

import tkinter as tk
from tkinter import ttk

def power():
    try:
        b = int(name_b.get())
        e = int(name_e.get())
        result = 1
        for i in range(0, e):
            result = b * result
        lbl_result.configure(text=f"{b}의 {e}승의 결과는 {result}입니다.")

    except ValueError as e:
        lbl_result.configure(text='숫자만 입력 가능 합니다.\n에러내용: {0}'.format(e))
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

# label
    lbl_b = ttk.Label(win, text="밑")
    lbl_e = ttk.Label(win, text="지수")
    lbl_result = ttk.Label(win, text='결과')

    # name 변수
    name_b = tk.StringVar()
    name_e = tk.StringVar()

    # entry
    en_name_b = ttk.Entry(win, width=8, textvariable=name_b)
    en_name_e = ttk.Entry(win, width=8, textvariable=name_e)

    # button
    btn_result = ttk.Button(text='결과 출력', width=25, command=power)

# grid 배치
    lbl_b.grid(row=0, column=0)
    en_name_b.grid(row=0, column=1)
    lbl_e.grid(row=0, column=2)
    en_name_e.grid(row=0, column=3)
    lbl_result.grid(row=2, column=0, columnspan=4)
    btn_result.grid(row=1, column=0, columnspan=4)

# return 키
    en_name_b.bind('<Return>', shift_entry)
    # win.bind('<Return>', enter_power)
    en_name_e.bind('<Return>', enter_power)

    # 마우스 커서 위치
    en_name_b.focus()

    win.mainloop()