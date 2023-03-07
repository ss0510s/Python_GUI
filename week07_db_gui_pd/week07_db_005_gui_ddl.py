# 거듭제곱 프로그램을 작성하시오

import tkinter as tk
from tkinter import ttk
import datetime
import sqlite3
def table_create():
    # global lbl_result
    try:
        ddl_sql_create = 'create table if not exist power(' \
                         'id integer primary key autoincrement,' \
                         'base text not null,' \
                         'exponent text not null,' \
                         'result text not null,' \
                         'etc text);'
        conn = sqlite3.connect('mathdb.db')
        cur = conn.cursor()
        cur.execute(ddl_sql_create)
        conn.commit()
        cur.close()
        conn.close()
        # lbl_result.configure(text='테이블 생성 완료')
        print('성공')
    except:
        # lbl_result.configure(text=f'에러발생')
        print('실패')

def power():
    try:
        b = int(name_b.get())
        e = int(name_e.get())
        result = 1
        for i in range(0, e):
            result = b * result

        conn = sqlite3.connect('mathdb.db')
        cur = conn.cursor()
        cur.execute('insert into power (base, exponent, result,etc) values (?,?,?,?)',(b, e, result, str(datetime.datetime.now())))
        conn.commit()
        cur.close()
        conn.close()

        lbl_result.configure(text=f"{b}의 {e}거듭제곱은 {result}입니다.\n{datetime.datetime.now()}")

    except ValueError as e:
        error = f'[{datetime.datetime.now()}] 밑: {name_b.get()}, 지수: {name_e.get()} 에러!\n숫자만 입력 가능 합니다.\n에러 내용: {e}\n\n'
        with open('log.txt', 'a') as fp:
            # fp.write(str(datetime.datetime.now()))
            # fp.write('\n')
            fp.write(error)
        lbl_result.configure(text=error)
        en_name_b.delete(0, 'end')
        en_name_e.delete(0,'end')
        en_name_b.focus()

def db_load():
    conn = sqlite3.connect('mathdb.db')
    cur = conn.cursor()
    cur.execute('select base, exponent, result from power')
    records = cur.fetchall()
    msg = ''
    for record in records:
        msg = msg + f'{record[0]}의 {record[1]}거듭제곱은 {record[2]}. [{datetime.datetime.now()}]\n'
    lbl_result.configure(text=msg)
    conn.commit()
    cur.close()
    conn.close()

def enter_power(ev):
    power()

def shift_entry(ev):
    en_name_e.focus()

if __name__ == "__main__":
    table_create()
    win = tk.Tk()
    win.title("거듭제곱 프로그램")
    win.geometry('400x400')
    win.resizable(False, False)

    lbl_b = ttk.Label(win, text="밑")
    lbl_e = ttk.Label(win, text="지수")
    name_b = tk.StringVar()
    name_e = tk.StringVar()
    en_name_b = ttk.Entry(win, width=8, textvariable=name_b)
    en_name_e = ttk.Entry(win, width=8, textvariable=name_e)
    btn_result = ttk.Button(text='결과 출력', width=25, command=power)
    lbl_result = ttk.Label(win, text='결과')

    db_load = ttk.Button(text='데이터베이스 로딩', width=25, command=db_load)

    lbl_b.grid(row=0, column=0)
    en_name_b.grid(row=0, column=1)
    lbl_e.grid(row=0, column=2)
    en_name_e.grid(row=0, column=3)
    lbl_result.grid(row=2, column=0, columnspan=4)
    btn_result.grid(row=1, column=0, columnspan=4)

    db_load.grid(row=3, column=0, columnspan=4)

    en_name_b.bind('<Return>', shift_entry)
    # win.bind('<Return>', enter_power)
    en_name_e.bind('<Return>', enter_power)
    en_name_b.focus()

    win.mainloop()