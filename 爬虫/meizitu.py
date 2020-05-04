import urllib.request
import random
url = "https://www.mzitu.com/jiepai/"
agentList =[
"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.117 Safari/537.36"
"Mozilla/5.0 (Macintosh; Intel Mac OS X 10.6; rv:2.0.1) Gecko/20100101 Firefox/4.0.1"
"Opera/9.80 (Macintosh; Intel Mac OS X 10.6.8; U; en) Presto/2.8.131 Version/11.11"
"Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko"
]
# random.choice从字符串中随机取
agentStr = random.choice(agentList)
# 设置一个请求体
req = urllib.request.Request(url)
# 向请求体添加了User-Agent
req.add_header("User-Agent",agentStr)
# 发起请求
response = urllib.request.urlopen(req)
# 输出结果
print(response.read().decode("utf-8"))
data = response.read()
# print(data)
# # 保存文件
# # with open(r"D:\mis\爬虫\file\xg.html","wb") as f:
# #     f.write(data)
#
# # response = urllib.request.urlopen("https://www.mzitu.com/jiepai/")
# # data = response.read()
# # print(data)