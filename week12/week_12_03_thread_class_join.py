import threading
import time


class Worker(threading.Thread):  # threading 모듈의 Thread 클래스를 상속
    def __init__(self, name):
        super().__init__()
        self.name = name

    def run(self):
        print(f'작업 스레드 시작 : {threading.currentThread().getName()}')
        time.sleep(3)
        print(f'작업 스레드 끝 : {threading.currentThread().getName()}')


if __name__ == "__main__":
    print('메인 스레드 시작')
    t1 = Worker('1번 스레드')
    t2 = Worker('2번 스레드')
    t3 = Worker('3번 스레드')
    t1.start()
    t2.start()
    t3.start()

    t1.join()
    t2.join()
    t3.join()
    print('메인 스레드 끝')



