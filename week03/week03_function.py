#import mymath
#import mymath as mm
#from mymath import *
from mymath import my_abs, my_power

while True:
    menu = input('1) 절대값 2) 거듭제곱 3) 종료 : ')
    if menu == '1':
        temp = int(input('정수 입력 : '))
        #print('입력된 수 {0}의 절대값은 {1}입니다'.format(temp, mymath.my_abs(temp)))
        #print('입력된 수 {0}의 절대값은 {1}입니다'.format(temp, mm.my_abs(temp)))
        print('입력된 수 {0}의 절대값은 {1}입니다'.format(temp, my_abs(temp)))
    elif menu == '2':
        b = int(input('밑 입력 : '))
        e = int(input('지수 입력 : '))
        #print('밑 {0}, 지수 {1}의 거듭제곱 값은 {2}입니다'.format(b, e, mymath.my_power(b, e)))
        #print('밑 {0}, 지수 {1}의 거듭제곱 값은 {2}입니다'.format(b, e, mm.my_power(b, e)))
        print('밑 {0}, 지수 {1}의 거듭제곱 값은 {2}입니다'.format(b, e, my_power(b, e)))
    elif menu == '3':
        break
    else:
        print('메뉴에서 골라주세요~')
