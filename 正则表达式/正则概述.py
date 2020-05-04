'''
python自1.5以后增加了re的模块，提供了正则表达式模式
re模块使python语言拥有了全部的正则表达式功能
'''
import re
r'''
re.match函数
原型：match(pattern, string, flases=0)
patter：匹配的正则表达式
string：要匹配的字符串
flages：标志位，用于控制正则表达式的匹配方式
值：re.[I,L,M,S,U,X]
I：忽略大小写
L：本地化识别
M：多行匹配（影响^和$）
S：是.匹配包括换行符在内的所有字符
U：根据Unicode字符集解析字符，影响\w \W \b \B
X：使我们更灵活的格式理解正则表达式
参数：
功能：尝试从字符串的起始位置匹配一个模式，如果不是起始位置配置成功的话，返回None
'''
# www.baidu.com
print(re.match("www", "www.baidu.com").span())
print(re.match("www", "Www.baidu.com"))
# 不区分大小写的
print(re.match("www", "Www.baidu.com",re.I))
print("----------------------------------------")
'''
re.search函数
原型：search(pattern, string, flases=0)
参数：
patter：匹配的正则表达式
string：要匹配的字符串
flages：标志位，用于控制正则表达式的匹配方式
功能：扫描整个字符串，并返回第一个匹配成功的
'''
print(re.search("sunck", "good man is sunck! sunck is a good man").span())
print(re.search("sunck", "good man is Sunck! sunck is a good man",re.I).span())
print("----------------------------------------")

'''
re.findall函数
原型：findall(pattern, string, flases=0)
参数：
patter：匹配的正则表达式
string：要匹配的字符串
flages：标志位，用于控制正则表达式的匹配方式
功能：扫描整个字符串，并返回结果列表
'''
print(re.findall("sunck", "good man is Sunck! sunck is a good man",re.I))


print("---------匹配单个字符与数字--------------")
r'''
.               匹配除换行符以外的任意字符
[0123456789]    []是字符集合，表示匹配方括号中所包含的任意一个字符
[sunck]         匹配's','u','n','c','k'中任意一个字符
[a-z]           匹配任意单个小写字母
[A-Z]           匹配任意单个大写字母
[0-9]           匹配任意数字
[0-9a-z-A-Z]    匹配任意的数字和字母
[0-9a-z-A-Z_]   匹配任意的数字、字母和下划线
[^sunck]        匹配除了sunck这几个字母以外的所有字符，中括号里的^称为脱字符，表示不匹配集合中的字符
[^0-9]          匹配所有的非数字字符
\d              匹配所有数字，效果同[0-9]
\D              匹配非数字的所有字符，效果同[^0-9]
\w              匹配数字，字母和下划线，效果同[0-9a-z-A-Z_]
\W              匹配非数字，字母和下划线，效果同[^0-9a-z-A-Z_]
\s              匹配任意的空白符（空格，换行，回车，换页，制表符），效果同[ \f\n\r\t]
\S              匹配任意非空白符，效果同[^ \f\n\r\t]
'''
print(re.search(".","sunck is a good man"))
print(re.search("[0123456789]","sunck is a good man 7"))
print(re.search("[sunck]","sunck is a good man 7"))
print(re.findall("[^0-9]","sunck is a good man 7"))
print(re.findall("[^\d]","sunck is a good man 7"))
print(re.findall("\D","sunck is a good man 7"))
print(re.findall("\w","sunck is a good man 7"))
print(re.findall("\W","sunck is a good@ man 7"))


print("--------------锚字符（边界字符）--------------")
r'''
^               行首匹配，和在[]里的^不是一个意思
$               行尾匹配
\A              匹配字符串开始，它和^的区别是，\A只匹配整个字符串的开头，即使在re.M模式下也不会匹配它行的行首
\Z              匹配字符串结束，它和$的区别是，\Z只匹配整个字符串的结束，即使在re.M模式下也不会匹配它行的结束
\b              匹配一个单词的边界，也就是单词和空格间的位置
                're\b'可以匹配never，不能匹配nerve。因为\b匹配的是边界也就是单词的最后
\B              匹配非单词边界
                're\B0'可以匹配nerve，不能匹配never。原因和\b相反
'''
# 开头是sunck
print(re.search("^sunck", "sunck is a good@ man 7"))

# 结尾是sunck
print(re.search("sunck$", "sunck is a good@ man 7"))

# 结尾是man
print(re.search("man$", "sunck is a good@ man"))

# \A
print(re.search("\Asunck", "sunck is a good@ man"))

# \A和^的区别
print(re.findall("^sunck", "sunck is a good@ man\nsunck is a nice man", re.M))
print(re.findall("\Asunck", "sunck is a good@ man\nsunck is a nice man", re.M))


# \Z和$的区别
print(re.findall("man$", "sunck is a good@ man\nsunck is a nice man", re.M))
print(re.findall("man\Z", "sunck is a good@ man\nsunck is a nice man", re.M))

# \b
print(re.search(r"man\b", "sunck is a good@ man\nsunck is a nice man", re.M))

# \B
print(re.search(r"man\B", "sumannck is a good@ man,sunck is a nice man"))



print("--------------匹配多个字符--------------")
'''
说明：下方的x、y、z均为假设的普通字符，n、m（非负整数），不是正则表达式的元字符
(xyz)           匹配小括号内的xyz（作为一个整体去匹配）
x?              匹配0个或者1个x
x*              匹配0个或者任意多个x（.*表示匹配0个或者任意多个字符（换行符除外））
x+              匹配至少一个x
x{n}            匹配确定的n个x（n是一个非负整数）
x{n,}           匹配至少n个x
x{n,m}          匹配至少n个最多m个x。注意：n <= m
x|y             |表示或，匹配的是x或y
'''
# 匹配括号类的所有字符
print(re.findall(r"(sunck)", "sunckgood is a good@ man,sunck is a nice man"))

# 匹配x?，匹配的是单个字符，0个或1个
print(re.findall(r"(a?)", "aaaabbbb"))

# 匹配x*，匹配一个整体，0个或多个
print(re.findall(r"(a*)", "aaaaabbbb"))
print(re.findall(r"(a*)", "aabaaababa")) # 贪婪匹配（尽可能多的匹配）

# 匹配.*
print(re.findall(r"(.*)", "aabaaababa")) # 贪婪匹配（尽可能多的匹配）

# 匹配x+，至少1个
print(re.findall(r"(a+)", "aabaaababa")) # 贪婪匹配（尽可能多的匹配）

# 匹配x{n}
print(re.findall(r"(a{3})", "aaaabaaababa"))

# 匹配x{n,}
print(re.findall(r"(a{3})", "aaaabaaababa"))
print(re.findall(r"(a{3})", "aabaaababa"))

# 匹配x{n,m}
print(re.findall("a{3,6}", "aaaaaabaaaaaaa"))

# 匹配x|y
print(re.findall("((s|S)unck)", "sunck---Sunck"))

# 练习
'''
需求
提取sunck……man（……任意字符数字）
str = "sunck is a good man!sunck is a nice man!sunck is a very handsome man"
'''

str = "sunck is a good man!sunck is a nice man!sunck is a very handsome man"
print(re.findall(r"^sunck.*?man$", str))
print(re.findall(r"sunck.*?man", str))

print("---------------特殊匹配----------------")
'''
*? +? ??    最小匹配，通常都是尽可能多的匹配，可以使用这种解决贪婪匹配
(?:x)       类似(xyz),但不表示一个组
'''
# 注释：/* part1 */   /* part2 */
'''
r"/：表示：/
/*：表示：*
.*：表示：part1
/*：表示：*/
'''
print(re.findall(r"//*.*?/*/", r"/* part1 */   /* part2 */"))

# 练习：
'''
QQ          4-10(纯数字)
mail        xxxxx@.x.com
phone       xxx-xxxxxxxx
user        
passwd
ip
url
'''

# 匹配QQ号
re_QQ = re.compile(r"^[1-9]\d{5,9}$")
print(re_QQ.search("654109102"))