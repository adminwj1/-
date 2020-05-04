'''
multiprocessing 库
跨平台版本的多进程模块，提供了一个Process类来代表一个进程对象
'''
import time
import os
from multiprocessing import Process
def run(str):
    count = 0
    while count <= 5:
        # os.getpgid()获取进程号
        # os.getppid()获取当前进程的父进程id号
        print("sunck is a %s man当前进程号：%s 父进程号：%s" % (str,os.getpid(),os.getppid()))
        count += 1
        time.sleep(1.2)


if __name__ == "__main__":
    print("主进程启动---%s" % (os.getpid()))

    # 创建一个子进程
    # target：说明进程执行的任务
    # args：给子进程传递参数
    p = Process(target=run, args=("nice",))
    # 启动进程
    p.start()
    while True:
        print("sunck is a good man")
        time.sleep(1)
