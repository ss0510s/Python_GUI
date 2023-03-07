# (100°F − 32) × 5/9 = 37.778°C
# fahrenheit = float(input('화씨온도 입력 : '))
# celsius = (fahrenheit-32.0)*(5.0/9.0)
# print('화씨 {0}도는 섭씨 {1}도 입니다'.format(fahrenheit,round(celsius, 4)))

# widget
# 입력 : Entry
# 출력 : Label
# 실행 : Button

# layout
# pack(), grid(), place()

import tkinter

def f2c():
    '''버튼 클릭시 처리'''
    fahrenheit = float(en_fahrenheit.get())
    celsius = (fahrenheit - 32.0) * (5.0 / 9.0)
    # 글자 변환
    lbl_celsius.configure(text='화씨 {0}도는 섭씨 {1}도 입니다'.format(fahrenheit, round(celsius, 4)))

def enter_pressed(ev):
    ''' 엔터키 처리 '''
    f2c()

win = tkinter.Tk()
win.title("온도변환 프로그램")
# with, height
win.geometry('300x100')

#사이즈 변환x
win.resizable(False, False)

# entry : 입력
en_fahrenheit = tkinter.Entry(win)
# label : 출력
lbl_celsius = tkinter.Label(win, text='섭씨온도')
# button : 버튼
btn_trans = tkinter.Button(win, text='화씨->섭씨', command=f2c)

# 엔터키 작용
en_fahrenheit.bind('<Return>', enter_pressed)

# 위치
en_fahrenheit.pack(fill='x')
lbl_celsius.pack(fill='x')
btn_trans.pack(fill='x')

win.mainloop()