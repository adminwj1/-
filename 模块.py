import time
import datetime
import os
import collections
import calendar
'''
#time模块
# 返回当前时间的时间戳，浮点形式，不需要参数
c = time.time()
print(c)
# 以元组的形式显示
t = time.gmtime(c)
print(t)
# 将时间转为本地时间元组
b = time.localtime(c)
print(b)
# 将本地时间元组转成字符串
s = time.asctime(b)
print(s)
# 将时间戳转成字符串 相当于：time.asctime(time.localtime(time.time()))
p = time.ctime(c)
print(p)
# 自己设定显示格式时间
q = time.strftime("%Y-%m-%d %H:%M:%S",b)
print(q)

# 将时间字符串转为时间元组
w = time.strptime(q, "%Y-%m-%d %X")
print(w)
'''
'''
# 延迟一个时间，值可以给整形或浮点型都可以
# time.sleep(4)
# 返回当前程序的CPU执行时间，windows从第二次开始，都是以第一个调用此函数的开始时间戳作为基数
# time.clock()
sum = 0
for i in range(100000000):
    sum += i
print(time.clock())
'''
'''
#date模块
# 获取当前时间
d1 = datetime.datetime.now()
print(d1)
# 获取指定的时间
d2 = datetime.datetime(1998, 5, 18, 12, 20)
print(d2)
# 将时间转为字符串
d3  = d1.strftime("%Y-%m-%d %X")
print(d3)
# 将格式化字符串转为datetime对象
# 注意：转换的格式要与字符串一致
d4 = datetime.datetime.strptime(d3, "%Y-%m-%d %X")
print(d4)
# 计算时间差
d5 = datetime.datetime.now()
d6 = d5 - d2
print(d6)
# 间隔的天数
print(d6.days)
# 间隔天数除外的秒数
print(d6.seconds)
'''
'''
#日历模块
# 返回指定某年某月的日历
print(calendar.month(2017,9))
# 返回指定年的日历
print(calendar.calendar(2019))
# 判断闰年返回true，否则返回False
print(calendar.isleap(2000))
# 返回某个月的周末的第一天和这个月所有的天数
print(calendar.monthrange(2019, 12))
'''
#getAllDirQU(r"D:/mis")
#
if __name__ == "__main__":
    print("这是一个模块.py")
else:
    # 队列模拟遍历目录，广度遍历
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
                    print("普通文件： ", fileName)