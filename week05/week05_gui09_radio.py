# 거듭제곱 프로그램을 작성하시오

import tkinter as tk
from tkinter import ttk

def disp():
    global lbl_display
    if selected.get() == 1:
        p1 = tk.PhotoImage(file='image/dog01.PNG')
        lbl_display.configure(image=p1)
        lbl_display.image = p1
    elif selected.get() == 2:
        p2 = tk.PhotoImage(file='image/dog02.PNG')
        lbl_display.configure(image=p2)
        lbl_display.image = p2
    elif selected.get() == 3:
        p3 = tk.PhotoImage(file='image/dog03.PNG')
        lbl_display.configure(image=p3)
        lbl_display.image = p3

if __name__ == "__main__":
    win = tk.Tk()
    win.title("체크버튼 위젯")
    win.geometry('300x600')
    win.resizable(False, False)

    lbl_display = ttk.Label(win, text='')
    selected = tk.IntVar()
    # 라디오 버튼
    rb_r = ttk.Radiobutton(win, text='리트리버', variable=selected, value=1, command=disp)
    rb_h = ttk.Radiobutton(win, text='허스키', variable=selected, value=2, command=disp)
    rb_w = ttk.Radiobutton(win, text='웰시코기', variable=selected, value=3, command=disp)

    lbl_display.pack()
    rb_r.pack(side='left')
    rb_h.pack(side='left')
    rb_w.pack(side='left')

    win.mainloop()