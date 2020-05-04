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

# path = "D:\\mis\\file"
path = r"D:\千锋python基础教程：第一章 python语言基础\千锋python基础教程：1、第一个python程序与数据存储"
toPath = "D:\\mis\\tofile"

filesList = os.listdir(path)  # 获取当前路径下的所有文件
# 启动for循环处理每一个文件
start = time.time()
for fileName in filesList:
    copyFile(os.path.join(path, fileName), os.path.join(toPath, fileName))  # 组合路径
end = time.time()
print("总耗时：%0.2f" % (end - start))