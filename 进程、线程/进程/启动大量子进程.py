from multiprocessing import Pool
import os, time, random

def run(name):
    print("子进%d程启动，进程号：%s" % (name, os.getpid()))
    start = time.time()  # 开始时间
    time.sleep(random.choice([1, 2, 3]))  # random.choice在列表中随机取一个字
    end = time.time()  # 结束时间
    # print("子进%d程结束，--%s--消耗时%.2f----进程号：" % (name, os.getpid()),end-start)
    print("子进%d程结束，进程号：%s" % (name, os.getpid()), "消耗时间%.2f：" % (end-start))


if __name__ == "__main__":
    print("父进程启动")
    # 创建多个进程
    # 创建进程池
    # 第一个参数：表示可以同时执行的进程数，默认大小是CPU核心数
    pp = Pool()
    # 创建进程，放入进程池统一管理
    for i in range(4):
        pp.apply_async(run, args=(i, ))


    # 如果是用的是进程池，在调用join之前必须先调用close，调用close之后就不能再继续添加新的进程了
    pp.close()
    # 进程池对象调用join，会等待进程池中所有的子进程结束完毕再去执行父进程
    pp.join()
    print("父进程结束")