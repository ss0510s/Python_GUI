from threading import Thread
import time

def work(name, vector):
    for i in vector:
        print(f'{name} : {i}')
        time.sleep(0.5)


# a = [1, 2, 3]
# b = [4, 5, 6]
m = [[1, 2, 3], [4, 5, 6]]

if __name__ =="__main__":
    print('main thread')
    # thread 생성
    t1 = Thread(target=work, args=('Thread A', m[0]))
    t2 = Thread(target=work, args=('Thread B', m[1]))

    t1.start()
    t2.start()