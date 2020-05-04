# -*- coding: utf-8 -*-
import string
import hashlib

file = open("hello.txt", "a")
md5input = input("请输入md5：\n")
md5input = md5input.lower()
apt = string.printable[:-6]


def dfs(s, num):
    m = hashlib.md5()
    m.update(s)
    md5temp = m.hexdigest()
    if md5temp == md5input:
        file.write("md5是：" + md5input + "    明文是：" + s + "\n")
        file.close()
        exit(-1)
    if len(s) == num:
        return
    for i in apt:
        dfs(s + i, num)


myinput = 10  # 生成字符的位数
for j in range(1, myinput):
    dfs("", j)
file.close()
