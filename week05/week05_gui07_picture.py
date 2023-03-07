import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

def popup():
    # 메세지 박스
    # showinfo:정보, showerror: 에러, warnwarning: 경고문
    messagebox.showinfo("클릭", "버튼이 눌렀습니다.")

if __name__ == "__main__":
    win = tk.Tk()
    win.title("이미지 프로그램")
    win.geometry('300x800')
    win.resizable(False, False)

    btn_exit = ttk.Button(win, text='종료', command=quit)
    btn_click = ttk.Button(win, text ='클릭시 팝업', command=popup)

# 사진 이미지
    p1 = tk.PhotoImage(file='image/dog01.PNG')
    p2 = tk.PhotoImage(file='image/dog02.PNG')
    p3 = tk.PhotoImage(file='image/dog03.PNG')

# label
    lbl_disp1 = ttk.Label(win, image=p1)
    lbl_disp2 = ttk.Label(win, image=p2)
    lbl_disp3 = ttk.Label(win, image=p3)

    btn_click.pack(fill='x')
    lbl_disp1.pack()
    lbl_disp2.pack()
    lbl_disp3.pack()
    btn_exit.pack(fill='x')

    win.mainloop()