from multiprocessing import Process, Queue
import os
def write(q):
    print("启动写子进程%s：" % (os.getpid()))
    for chr in ['A','B','C','D']:
        q.put(chr)  # 向队列里面写数据
    print("结束写子进程%s：" % (os.getpid()))



def read(q):
    print("启动读子进程%s：" % (os.getpid()))
    while True:
        value = q.get(True)  # 读取队列里面的数据
        print("value = ", value)




if __name__ == "__main__":
    '''
    流程：
    write将数据写到队列里面，然后read在从队列里面读出数据
    '''
    # 父进程创建队列，并传递给子进程
    q = Queue()
    # 创建两个子进程，并将队列传递进去
    pr = Process(target=read, args=(q,))
    pw = Process(target=write, args=(q,))
    # 启动子进程
    pw.start()
    pr.start()

    pw.join()
    # pr进程里是个死循环，无法等待其结束，只能强行结束
    pr.terminate()  # 强制停止读进程
    print("结束读子进程%s" %(os.getpid()))
    print("父进程结束")
