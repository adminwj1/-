'''
import requests
import re
import time
import os
headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.106 Safari/537.36'
}
response = requests.get('https://www.vmgirls.com/12021.html', headers=headers)
# print(response.request.headers)     # 查看请求体】中的，user-agent
# print(response.text)       # 查看返回的html代码
html = response.text
"""解析网页"""
# <img alt="海棠花与JＫ-唯美女生" src="data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7" width="800" height="1200" class="alignnone size-full wp-image-7395" data-src="https://static.vmgirls.com/image/2018/03/2018-03-29_14-00-14.jpg" data-nclazyload="true" data-srcset="https://static.vmgirls.com/image/2018/03/2018-03-29_14-00-14.jpg 800w, https://static.vmgirls.com/image/2018/03/2018-03-29_14-00-14-683x1024.jpg 683w" data-sizes="(max-width: 800px) 100vw, 800px">
urls = re.findall('<a href="(.*?)" alt=".*?" title=".*?">', html)
# <h1 class="post-title h3">喜欢夏天也喜欢你</h1>
dir_name = re.findall('<h1 class="post-title h3">(.*?)</h1>', html)[-1]
if not os.path.exists(dir_name):
    os.mkdir(dir_name)
# print(dir_name)
# print(urls)
"""保存图片"""
for url in urls:
    time.sleep(1)
    file_name = url.split('/')[-1]
    response = requests.get(url, headers=headers)
    with open(dir_name + '/' + file_name, 'wb') as f:
        f.write(response.content)'''


import requests
import re
import os
headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.106 Safari/537.36'
}
response = requests.get('https://www.vmgirls.com/3545.html', headers=headers)
html = response.text

# urls = re.findall('<img alt="(.*?)" data-src="(.*?)" data-nclazyload="(.*?)" data-srcset="(.*?)">', html)
urls = re.findall('<a href="(.*?)" alt=".*?" title=".*?">', html)
# print(urls)
dir_name = re.findall('<h1 class="post-title h3">(.*?)</h1>', html)[-1]
if not os.path.exists(dir_name):
	os.mkdir(dir_name)
num = 1
for url in urls:
	file_name = url.split('/')[-1]
	print('正在下载第{}'.format(num))
	response = requests.get(url, headers=headers)
	with open(dir_name + '/' + file_name, 'wb') as f:
		f.write(response.content)
	num += 1