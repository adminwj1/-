from threading import Thread
import time
# 多线程全局变量共享
# 线程共享全局变量的原因是：多线程是在同一个进程中创建多个子线程，而多进程是在主进程之外创建多个子进程
# 应用场景：在全局数据需要共享时使用
# 线程共享全局变量可能遇到的问题：
g_num = 100
def work1():
    global g_num
    for i in range(3):
        g_num += 1
    print("----in work1, g_num is %d----" % g_num)

def work2():
    global g_num
    print("----in work2, g_num is %d----" % g_num)

print("----线程创建之前g_num is %d----" % g_num)

t1 = Thread(target=work1)
t1.start()

# 延时一会，保t1线程中的事情做完
time.sleep(1)

t2 = Thread(target=work2)
t2.start()
