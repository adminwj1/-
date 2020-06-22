'''
0、获取用户要copy的文件夹的名字
1、创建一个文件夹
2、获取源文件叫中的所有的文件名
3、使用多进程的方式copy源文件夹中的所有文件到新的文件夹中

'''
import os
from multiprocessing import Pool, Manager
def coypFileTask(filename, oldFileName, newFileName, queue):
    for item in filename:
        fr = open(oldFileName + "/" + item, mode='r', encoding='UTF-8')
        content = fr.read()
        fw = open(newFileName + "/" + item, mode='w')
        fw.write(content)
        fw.close()
        fr.close()
        queue.put(item)

def main():
    oldFileName = input("请输入要复制的文件夹名:")
    newFileName = input("请输入一个新的文件夹名：")
    # 判当前目录下是否存在该文件
    os.mkdir(newFileName)
    # 获取源文件夹中所有的文件名
    fileNames = os.listdir(oldFileName)
    pool = Pool(5)
    queue = Manager().Queue()
    for i in range(5):
        pool.apply_async(coypFileTask, args=(fileNames, oldFileName, newFileName,queue))
    num = 0
    allNum = len(fileNames)
    while num < allNum:
        queue.get()
        num += 1
        copyRate = int((num / allNum)*100)
        print("%d%%" % copyRate)





if __name__ == '__main__':
    main()

