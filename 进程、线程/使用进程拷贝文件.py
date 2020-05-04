import os
import time
from multiprocessing import Pool
def copyFile(rPath, wPath):
    fr = open(rPath, "rb")
    fw = open(wPath, "wb")
    context = fr.read()
    fw.write(context)
    fr.close()
    fw.close()

path = r"D:\千锋python基础教程：第一章 python语言基础\千锋python基础教程：1、第一个python程序与数据存储"
toPath = "D:\\mis\\tofile"
# 多进程实现文件拷贝
#
if __name__ == "__main__":
    filesList = os.listdir(path)  # 获取当前路径下的所有文件
    start = time.time()
    pp = Pool()
    for fileName in filesList:
        pp.apply_async(copyFile, args=(os.path.join(path, fileName), os.path.join(toPath, fileName)))

    pp.close()
    pp.join()
    end = time.time()
    print("总耗时：%0.2f" %(end-start))