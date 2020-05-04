'''
特点：把参数进行打包，单独传输
优点：数量大，安全（当对服务器数据进行修改时建议使用post）
缺点：速度慢
'''
import urllib.request
# 对参数进行打包
import urllib.parse

url = "http://www.httpbin.org/post"
# 将要发送的数据合成一个字典
# 字典的键去网址里找，一般为input标签的name属性的值
data = {
    "username":"sunck",
    "passwd":"666"
}
# 对要发送的数据进行打包
postData = urllib.parse.urlencode(data)
# 创建请求体
req = urllib.request.Request(url, data=postData)
# 发送请求
response = urllib.request.urlopen(req)
print()