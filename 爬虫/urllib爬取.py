import urllib.request
# 向指定的URL地址发起请求，并返回服务器响应的数据（文件的对象）
response = urllib.request.urlopen("http://www.baidu.com")

# .decode("utf-8")转换编码格式
# 读取网页文件的全部内容，会把读取到的内容赋值给一个字符串变量
# data = response.read()
# print(data)
# print(type(data))

# 读取一行内容
#data = response.readline()

# 读取文件的全部类容，将内容赋值给一个列表
# date = response.readlines()
# print(date)

# response属性
# 返回当前环境有关信息
print(response.info())

# 返回状态码200 请求成功，304 有缓存
print(response.getcode())

# 返回当前正在爬取的URL地址
print(response.geturl())

# 解码（将浏览器的URL中的中文解码）
url = r"https://www.baidu.com/s?ie=utf-8&f=8&rsv_bp=1&rsv_idx=1&tn=baidu&wd=%E7%99%BE%E5%BA%A6%E4%B8%80%E4%B8%8B&rsv_pq=fa596fc200084575&rsv_t=541dhTuQlz7bmiJ4fgpJ1S2hIN0s0jxpQmkmGoMcuEXHxWtrAvDQf4P35Yk&rqlang=cn&rsv_enter=1&rsv_dl=tb&rsv_sug3=18&rsv_sug1=8&rsv_sug7=101&rsv_sug2=0&inputT=4906&rsv_sug4=5435"
newUrl = urllib.request.unquote(url)
print(newUrl)
print("-------------")
# 编码
newUr2 = urllib.request.quote(newUrl)
print(newUr2)
'''
# 将爬取的网页写入文件
with open(r"D:\mis\爬虫\file\baidu.html", "wb") as f:
    f.write(data)'''