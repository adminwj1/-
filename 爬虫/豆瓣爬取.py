import requests
import re
import os
num = 1
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.106 Safari/537.36'
}

# <img src="https://img9.doubanio.com/view/photo/m/public/p2284537786.webp" width="201">
response = requests.get('https://www.douban.com/photos/album/1619036812/', headers=headers)
html = response.text
# print(html)
urls = re.findall('<img width=".*?" src="(.*?)" />', html)
dir_name = '丝绒陨的相册-梦游塞纳河'
if not os.path.exists(dir_name):
    os.mkdir(dir_name)
print(urls)
for url in urls:
    file_name = url.split('/')[-1]
    print('正在下载第{}张图片'.format(num))
    response = requests.get(url, headers=headers)
    with open(dir_name + '/' + file_name, 'wb') as f:
        f.write(response.content)
    num += 1