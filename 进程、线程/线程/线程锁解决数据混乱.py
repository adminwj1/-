import threading
'''
两个线程同时工作，一个存钱一个取钱
可能导致数据异常

思路：加锁
线程锁确保了这段代码只能由一个线程从头到尾的完整执行
加了线程锁后性能会变慢，因为：线程锁阻止了多线程的并发执行，包含锁的某段代码实际上只能以单线程模式执行，所以效率大大降低了
由于可以存在多个锁，不同的线程持有不同的锁，并试图获取其他的锁，这样锁来锁去，可能导致多个线程挂起。只能靠操作系统强制关闭
'''

# 锁对象
lock = threading.Lock()
num = 10

def run(n):
    global num
    for i in range(10000000):
        # 加锁
        # with lock可以自动上锁与解锁
        lock.acquire()
        try:
            num = num + n
            num = num - n
        # 修改完一定要释放锁
        finally:
            lock.release()
if __name__ == "__main__":
    t1 = threading.Thread(target=run, args=(6,))
    t2 = threading.Thread(target=run, args=(9,))
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    print("num = ",num)
