import os
path = (r"D:\mis\数据.txt")
path_1 = (r"D:\mis\邮箱")
path_2 = (r"D:\mis\身份证")
path_3 = (r"D:\mis\手机号")
f = open(path,'r',encoding='utf-8')
flag = os.path.exists(path_1)
flag_2 = os.path.exists(path_2)
flag_3 = os.path.exists(path_3)
if flag != False:
    print('文件存在')
else:
    os.mkdir('邮箱')
if flag_2 != False:
    print('文件存在')
else:
    os.mkdir("身份证")
if flag_3 != False:
    print('文件存在')
else:
    os.mkdir('手机号')
while True:
    a = f.readline()
    if not a:
        break
    if a[0:3] == "邮箱：":
        x = a.find("省",0,len(a))
        d = a[0:x]  # 输出邮箱账号
        # 将筛选出的内容写入到指定的文件中
        with open(r'D:\mis\邮箱\邮箱账号.txt', 'a', encoding='utf-8') as e:
            e.write(d + "\n")
        z = a.find("手",0,len(a))
        # 将身份证信息存入到指定文件中。输出身份证号，x表示的是省份证中省在字符串中的第一次出现的索引位置，同理z也一样
        m = a[x:z]
        with open(r'D:\mis\身份证\身份证.txt', 'a', encoding='utf-8') as v:
            v.write(m + "\n")
        # 将手机号信息存入到指定文件中
        n = a[z:]
        with open(r'D:\mis\手机号\手机号.txt', 'a', encoding='utf-8') as q:
            q.write(n)
f.close()
