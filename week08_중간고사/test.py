import tkinter as tk
from random import randint
from tkinter import ttk
import sqlite3

# 수강신청 버튼 클릭시 이벤트
def insert_sugang():

    # db 연결
    conn = sqlite3.connect('test.db')
    cur = conn.cursor()

    # 인자
    sub = subject.get()
    pro = professor.get()

    # 과목이 null 값일 경우
    if sub == '':
        lbl_subject.focus()

    else:
        # 테이블이 존재하지 않을 때 테이블 생성
        ddl_sql_create = 'create table if not exists sugang(' \
                         'id integer primary key autoincrement,' \
                         'subject text not null,' \
                         'professor text);'

        cur.execute(ddl_sql_create)
        conn.commit()

        # 교수 이름이 null 값일 경우
        if pro == '':
            # 랜덤하게 삽입
            ran = randint(0, 12)
            pro_list = ['김은조','김현기','정기수','이종혁','박진영','문형석','공병학','강미선','정유진','윤지수','남수진','김규리','이예린']
            pro = pro_list[ran]

        # db에 insert
        cur.execute('insert into sugang (subject, professor) values(?,?)',(sub, pro))
        conn.commit()

        # db 조회
        cur.execute("select * from sugang")
        records = cur.fetchall()

        result = ''
        for record in records:
            result = result + f'{record[0]}. {record[1]} ({record[2]})\n'

        # 조회한 모든 값 출력
        lbl_result.configure(text=result)

    # 연결 종료
    cur.close()
    conn.close()

    en_professor.delete(0, 'end')
    en_subject.delete(0, 'end')
    en_subject.focus()

# 전체 삭제 버튼 클릭시
def delete_all():
    conn = sqlite3.connect('test.db')
    cur = conn.cursor()

    # 테이블이 없을 때, 예외처리
    try:
        cur.execute('drop table sugang;')
        lbl_result.configure(text='CLEARED!')

    except:
        lbl_result.configure(text='NO SQL TABLE EXISTS')

    cur.close()
    conn.close()
    en_professor.delete(0, 'end')
    en_subject.delete(0, 'end')
    en_subject.focus()

# 신청과목에서 엔터키 클릭시
def shift_sub(ev):
    en_professor.focus()

# 담당교수에서 엔터키 클릭시
def shift_pro(ev):
    sub = subject.get()
    # subject 입력이 없을 시
    if sub == "":
        en_subject.focus()
    # insert 클릭
    else:
        insert_sugang()

if __name__ == "__main__":
    win = tk.Tk()
    win.title("2022년 2학기 수강신청 v0.1")
    win.geometry('400x200')
    win.resizable(False, False)

    subject = tk.StringVar()
    professor = tk.StringVar()

    lbl_subject = ttk.Label(win, text='신청과목 : ')
    en_subject = ttk.Entry(win, textvariable=subject)
    lbl_professor = ttk.Label(win, text='담당교수 : ')
    en_professor = ttk.Entry(win, textvariable=professor)
    btn_insert = ttk.Button(text='입력',width=20, command=insert_sugang)
    btn_delete = ttk.Button(text='전체삭제',width=20, command=delete_all)
    lbl_result = ttk.Label(win, text='Display')

    lbl_subject.grid(row=0, column=0)
    en_subject.grid(row=0, column=1)
    lbl_professor.grid(row=1,column=0)
    en_professor.grid(row=1,column=1)
    btn_insert.grid(row=2, column=0,columnspan=2)
    btn_delete.grid(row=3, column=0,columnspan=2)
    lbl_result.grid(row=0,column=2,rowspan=4)

    en_subject.bind('<Return>', shift_sub)
    en_professor.bind('<Return>', shift_pro)

    en_subject.focus()

    win.mainloop()