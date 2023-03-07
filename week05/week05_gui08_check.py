# 거듭제곱 프로그램을 작성하시오

import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

# 팝업 창
def popup():
    if checked.get() == 0:
        messagebox.showinfo('팝업', '체크버튼 OFF')
        lbl_display.configure(text='체크버튼 OFF')
    else:
        messagebox.showinfo('팝업', '체크버튼 ON')
        lbl_display.configure(text='체크버튼 ON')

if __name__ == "__main__":
    win = tk.Tk()
    win.title("체크버튼 위젯")
    win.geometry('300x400')
    win.resizable(False, False)

    lbl_display = ttk.Label(win, text='')
    checked = tk.IntVar()
    # 체크버튼
    cb_popup = ttk.Checkbutton(win, text='check', variable=checked, command=popup)

    cb_popup.pack()
    lbl_display.pack()

    win.mainloop()