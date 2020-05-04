import os
import collections
# 栈模拟递归遍历目录（深度遍历,一直往里走）
'''
def getAllDirDE(path):
    # 创建一个空栈
    stack = []
    # 将数据压进栈
    stack.append(path)
    # 处理栈,当栈为空的时候结束循环
    while len(stack) != 0:
        # 取出栈中的数据(取出路径)，拿到路径后再对路径进行遍历处理
        dirPath = stack.pop()
        # 对拿到的路径进行遍历处理，判断如果是目录就继续处理，如果不是目录就输出为文件
        filesList = os.listdir(dirPath)
        # 处理每一个文件，如果是普通文件就打印，如果是目录就将该目录的地址压栈继续处理
        for fileName in filesList:
            # 声明一个变量来存放处理的目录路径
            fileAbsPath = os.path.join(dirPath, fileName)
            # 判断该路径下的fileName是不是目录
            if os.path.isdir(fileAbsPath):
                # 是目录就压栈
                print("目录：",fileName)
                stack.append(fileAbsPath)
            else:
                #打印普通文件
                print("普通文件：",fileName)
getAllDirDE(r"D:/MyDjango")
'''
#队列模拟遍历目录，广度遍历
def getAllDirQU(path):
    queue = collections.deque()  # 创建一个空队列
    # 进队
    queue.append(path)
    # 循环处理队列
    while len(queue) != 0:
        # 出队数据
        dirPath = queue.popleft()
        # 找出所有的文件
        filesList = os.listdir(dirPath)
        # 是目录进队，不是目录就打印普通文件
        for fileName in filesList:
            # 绝对路径
            fileAbsPath = os.path.join(dirPath, fileName)
            # 判读是否是目录，是目录就进队，不是就打印
            if os.path.isdir(fileAbsPath):
                print()
                print("目录： ", fileName)
                # 让fileAbsPath进队，继续处理该路径下面的子目录
                queue.append(fileAbsPath)
            else:
                print("普通文件： " , fileName)

getAllDirQU(r"D:/")



# 使用递归函数遍历目录结构
'''
def getAllDir(path):
    # 查看当前目录下的所有文件
    filesList = os.listdir(path)
    # 循环处理每一个目录
    for fileName in filesList:
        # 如果是目录就就继续向下找，如果是文件就不循环遍历
        # 声明一个变量，用来存放绝对路径
        fileAbsPath = os.path.join(path, fileName)
        if os.path.isdir(fileAbsPath):  # 判断是否是路径，使用绝对路径
            print("目录： ",fileName)
            # 使用递归调用遍历目录下的子目录
            getAllDir(fileAbsPath)
        else:  # 判断是否是文件
            print("普通文件： ",fileName)
getAllDir(r"D:\MyDjango")
'''
'''
import random
def sum1(n):
    sum = 0
    # 1       1
    # 3       2
    # 6       3
    # 10      4
    # 15      5
    for x in range(1, n + 1):#n+1表示的循环结束位不包含该位数字
        print(x)
        sum += x
    return sum
# res = sum1(5)
# print(res)
'''
'''
print("递归函数")
def sum2(n):
    if n == 1: #找临界条件
        return 1 #如果满足条件就返回1
    else:
        #假设当前函数已经能用，调用自身计算上一次的结果，再求出本次的结果
        return n + sum2(n - 1)  #找这次和上一次的关系
res = sum2(5)
print(res)
'''