# 거듭제곱 프로그램을 작성하시오

import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

def click_next():
    global idx
    idx = idx + 1
    if idx > len(photos)-1:
        idx = 0
    p = tk.PhotoImage(file=photos[idx])
    # 이미지 변환
    lbl_photo.configure(image=p)
    lbl_photo.image = p
    lbl_page_no.configure(text=f'{idx+1}/{len(photos)}')

def click_prev():
    global idx
    idx = idx - 1
    if idx < 0:
        idx = len(photos) - 1
    p = tk.PhotoImage(file=photos[idx])
    lbl_photo.configure(image=p)
    lbl_photo.image = p
    lbl_page_no.configure(text=f'{idx+1}/{len(photos)}')

def pg_up(ev):
    click_prev()

def pg_down(ev):
    click_next()

def popup(ev):
    messagebox.showinfo('클릭한 이미지 좌표', f'x : {ev.x}, y : {ev.y}')

photos = ['image/franklin.PNG', 'image/michael.PNG', 'image/trevor.PNG']
idx = 0

if __name__ == "__main__":
    win = tk.Tk()
    win.title("PhotoViewer v0.2")
    win.geometry('800x800')
    win.resizable(False, False)

    p = tk.PhotoImage(file=photos[0])
    lbl_photo = ttk.Label(win, image=p)
    lbl_page_no = ttk.Label(win, text=f'1/{len(photos)}')
    btn_next = ttk.Button(win, text='다음======>', command=click_next)
    btn_prev = ttk.Button(win, text='<======이전', command=click_prev)

    win.bind('<Prior>', pg_up)
    win.bind('<Next>', pg_down)
    lbl_photo.bind('<Button-1>',popup)

    lbl_photo.pack()
    btn_next.pack(fill='x')
    btn_prev.pack(fill='x')
    lbl_page_no.pack()

    win.mainloop()