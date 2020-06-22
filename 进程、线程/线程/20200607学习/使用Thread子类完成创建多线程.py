import threading
import time
'''
父进程先结束，子进程后结束称之为：僵尸进程
父进程结束，子进程还在运行称之为：孤儿进程，孤儿进程由系统中的1号或0号进程进行处理
'''

class MyThread(threading.Thread):
    def run(self):
        for i in range(3):
            time.sleep(1)
            msg = "I'm " + self.name + ' @ ' + str(i)   # self.name 返回当前线程名
            print(msg)


def test():
    for i in range(5):
        t = MyThread()
        t.start()


if __name__ == '__main__':
    test()









