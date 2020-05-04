import urllib.request
import urllib.parse
import socket
import urllib.error
'''
data = bytes(urllib.parse.urlencode({'word': 'hello'}), encoding='utf8')
response = urllib.request.urlopen('http://httpbin.org/post', data=data)
print(response.read())

try:
    response = urllib.request.urlopen('http://httpbin.org/get', timeout=0.1)
except urllib.error.URLError as e:
    if isinstance(e.reason, socket.timeout):
        print('TIME OUT')


response = urllib.request.urlopen('http://httpbin.org/')
print(response.status)
print(response.getheaders())
print(response.getheader('Server')) # 获取特定信息，服务器版本
      '''
url = 'http://httpbin.org/post'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:72.0) Gecko/20100101 Firefox/72.0',
    'Host': 'httpbin.org'
}
dict = {
    'name': 'Germeny'
}
data = bytes(parse.urlencode(dict),encoding='utf8')