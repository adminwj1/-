from multiprocessing import Queue
q = Queue(3)

# .qsize()     # 查看队列大小
# .put()    向对列中添加数据，如果队列满了程序会自动堵塞等待队列的空闲位置
# .put_nowait()    向对列中添加数据，如果队列满了程序会自动结束程序不会等待
# .get()    在队列里取出数据（先进先出，第一次取出的数据，是第一个进入队列的数据），如果队列为空，程序会自动堵塞等待数据
#  .get_nowait()    在队列里取出数据（先进先出，第一次取出的数据，是第一个进入队列的数据），如果队列为空，程序会自动结束不会堵塞等待
# .empty()  判断队列是否为空，空位True
# .full()   判断队列是否填满，填满为True
# 进程池之间通信使用Manager().Queue()
q.put("haha-1")
q.put("haha-2")
q.put("haha-3")
# q.put("haha-4")   # 创建队列时指定了队列的大小为3，当向队列中创建第4个数据时就自动堵塞等待取值后再向队列中添加数据
print(q.qsize())
a = q.get()
print(a)
print(q.qsize())