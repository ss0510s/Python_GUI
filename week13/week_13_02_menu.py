import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

def click_about():
    messagebox.showinfo('Menubar test', 'Made by Inha Univ')

def disp_counter():
    global counter
    counter = counter + 1
    lbl_disp.configure(text=f'{counter}')
    w.after(1000, disp_counter)

# global variable
counter = 0

if __name__=='__main__':
    # 윈도우
    w = tk.Tk()
    w.title("메뉴")
    w.geometry("300x400")

    m_menubar = tk.Menu(w)

    m_file = tk.Menu(m_menubar, tearoff=0)
    m_menubar.add_cascade(label='File', menu=m_file)
    m_file.add_command(label='Exit', command=w.quit)

    m_help = tk.Menu(m_menubar, tearoff=0)
    m_menubar.add_cascade(label='Help', menu=m_help)
    m_help.add_command(label='About', command=click_about)

    w.config(menu=m_menubar)

    lbl_disp = ttk.Label(w, text='')
    lbl_disp.pack()

    # start_cycle()
    w.after(1000, disp_counter)
    w.mainloop()


