from multiprocessing import Queue, Process
import time

def write(q):
    list_a = ['a', 'b', 'c', 'd', 'e']
    for item in list_a:
        # print(os.getpid())
        # print(os.getppid())
        q.put(item)


def read(q):
    while True:
        if not q.empty():
            print('正在读取队列中的 ', q.get())
        else:
            print("队列中的数据已读取完成，程序结束")
            time.sleep(1)
            break



def main():
    queue = Queue()
    p1 = Process(target=write, args=(queue,))
    p1.start()
    p1.join()

    p2 = Process(target=read, args=(queue,))
    p2.start()
    p2.join()

if __name__ == '__main__':
    main()