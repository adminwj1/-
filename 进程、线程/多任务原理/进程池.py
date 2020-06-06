from multiprocessing import Pool
import os
import time
import random
# 费堵塞进程
def worker(num):
    for i in range(5):
        print("===pid=%d==num=%d=" % (os.getpid(), num))
        time.sleep(1)
if __name__ == '__main__':
    # 3表示进程池中最多有3个进一起执行
    pool = Pool(3)
    for i in range(10):
        print("---%d---" % i)
        # 向进程池中添加任务
        # 注意：如果添加的任务书超过了，进程翅中进程的个数的话，那么不会导致无法添加到进程中的任务中
        # 如果还没有执行的话，那么此时他们会等待进程池中的进程完成一个任务之后，会自动的去用刚刚的那个进程完成当前新的任务
        pool.apply_async(worker, (i,))
    # 关闭进程池，相当于不能够再添加新任务了
    pool.close()
    # 主进程创建/添加任务后，主进程默认不会等待进程池中的任务执行完成后才结束。而是当主进程的任务做完之后，立马结束。如果这个地方没有join，会导致进程池中的任务不会执行直接结束程序。
    pool.join()