from threading import Thread
import time
'''
进程和线程的区别：
进程：启动一个程序就是一个进程
线程：是进程里面真正执行任务的，线程是cpu调度的单位
主线程程序结束完成后，不会立即结束会等待子线程执行完成后才会结束

如果多个线程执行的都是同一个函数的话，各自之间不会影响，各是个的
'''
def test():
    print("----昨晚喝多了，下次少喝点----")
    time.sleep(1)


for i in range(5):
    t = Thread(target=test)
    t.start()