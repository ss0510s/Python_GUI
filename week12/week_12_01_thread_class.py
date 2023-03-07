import threading
from threading import *
import time

class Worker(Thread): # threading 모듈의 Thread 클래스를 상속
    def __init__(self, name):
        super().__init__() # 부모 클래스(Thread)의 생성자 호출
        self.name = name

    def run(self):
        print(f'작업 스레드 시작 : {threading.currentThread().getName()}')
        time.sleep(3)
        print(f'작업 스레드 끝 : {threading.currentThread().getName()}')


if __name__=="__main__":
    print('메인 스레드 시작')
    for i in range(3):
        t = Worker(f'{i}번 스레드') # 객체 생성
        t.daemon = True # 작업스레드를 데몬스레드로
        t.start() # 스레드를 runnable 상태로
    print('메인 스레드 끝')