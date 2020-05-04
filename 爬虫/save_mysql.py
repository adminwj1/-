# -*- coding=utf-8 -*-
import pymysql
import sys

# 读取图片文件

# fp = open("test.jpg",'rb',encoding='utf-8')
# fp = open("test.jpg", 'rb')
# img = fp.read()
# fp.close()
# 创建连接
conn = pymysql.connect(host='localhost',
                       port=3306,
                       user='root',
                       passwd='adminwj',
                       db='images')
# 创建游标
cursor = conn.cursor()

with open(r'D:\images\秋日温柔，人间理想\8FC5182A-1C7C-467C-8C5D-0618D825C1AF-1-scaled.jpeg', 'rb') as fp:
    data = fp.read()
cursor.execute("insert into images (img) values (%s)", [data])

# 提交，不然无法保存新建或者修改的数据
conn.commit()

# 关闭游标
cursor.close()
# 关闭连接
conn.close()