import time
'''
单任务：有多个任务但一次只能执行一个任务，只有当前执行任务结束后下一个任务才会执行
'''

def run():

    while True:
        print("sunck is a nice man")
        time.sleep(1.2)

if __name__ == "__main__":
    while True:
        print("sunck is a good man")
        time.sleep(1)

    # 不会执行到run方法，只有上面的while循环结束才可以执行，这就是单任务
    run()