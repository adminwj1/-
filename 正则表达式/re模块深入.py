import re
'''
字符串切割
'''
str1 = "sunck    is a good man"
print(str1.split(" "))
print(re.split(r" +", str1))

'''
re.finditer函数
原型：match(pattern, string, flases=0)
参数：
patter：匹配的正则表达式
string：要匹配的字符串
flages：标志位，用于控制正则表达式的匹配方式
功能：与findall类似，扫描整个字符串，返回到是一个迭代器
'''
str3 = "sunck is a good man! sunck is a nice man! sunck is handsome man"
d = re.finditer(r"(sunck)",str3)
# 迭代器
while True:
    try:
        l = next(d)
        print(d)
    except StopIteration as e:
        break


'''
字符串的替换和修改
sub(pattern, repl, string, count=0, flags=0)
subn(pattern, repl, string, count=0, flags=0)
参数：
pattern：正则表达式
repl：指定用来替换的字符串
string：目标字符串
count：最多替换次数
flags：
值：re.[I,L,M,S,U,X]
I：忽略大小写
L：本地化识别
M：多行匹配（影响^和$）
S：是.匹配包括换行符在内的所有字符
U：根据Unicode字符集解析字符，影响\w \W \b \B
X：使我们更灵活的格式理解正则表达式
功能：在目标字符串中以正则表达式的规则匹配字符串，再把他们替换成指定的字符串。
可以指定替换的次数，如果不指定，替换所有的匹配字符串
区别：前者返回一个被替换的字符串，后者返回一个元组，第一个元素被替换的字符串，第二个元素表示被替换的次数
'''
print("-------------字符串的替换和修改-----------------")
str5 = "sunck is a good  good good man"
print(re.sub(r"(good)","nice",str5))
print(re.sub(r"(good)","nice",str5,count=2))
print(type(re.sub(r"(good)","nice",str5)))
print(re.subn(r"(good)","nice",str5,count=1))
print(type(re.subn(r"(good)","nice",str5,count=1)))

print("-------------分组-----------------")
'''
分组：
概念：除了简单的判断是否匹配之外，正则表达式还有提取子串的功能。用()表示的分组
给组取名：?P<>
'''
str6="010-53247654"
m = re.match(r"(\d{3})-(\d{8})",str6)
# 使用序号获取对应组的信息，group（0）表示的原始字符串
print(m.group(0))
print(m.group(1))
print(m.group(2))
# 查看匹配的各组的情况
print(m.groups())

# 给组取名字
print("给组取名字")
b = re.match(r"(?P<a1>\d{3})-(?P<a2>\d{8})",str6)
print(b.group("a1"))
print(b.group("a2"))



'''
编译：当使用正则表达式时，re模块会干两件事
1、编译正则表达式，如果正则表达式本身不合法，会报错
2、用编译后的正则表达式去匹配对象
compile(pattern, flags=0)
参数：
pattern：
flags：要变异的正则表达式
'''
pat = r"^1(([34578]\d)|(47))\d{8}$"

re_telephon = re.compile(pat)
print(re_telephon.search("17608391679"))

'''
# 方法：
re.match()
re.search()
re.findall()
re.finditer()
re.sub()
re.subn()
re.split()
'''
