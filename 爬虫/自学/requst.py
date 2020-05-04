import requests
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36'}
request = requests.get('http://www.baidu.com', headers=headers)

with open(r'D:\mis\baidu.html', 'ab') as f:
    f.write(request.content)
    f.close()
