import requests
import re
import time
import os

num = 1
headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.106 Safari/537.36'
}

# 下载网页
for i in range(1):
    # url = 'https://www.vmgirls.com/3545.html'
    url = 'https://www.vmgirls.com/13344/page-{}.html'.format(i)
    print(url)
    response = requests.get(url, headers=headers)
    html = response.text
    dir_name = re.findall('<h1 class="post-title h3">(.*?)</h1>', html)[-1]
    if not os.path.exists(dir_name):
        os.mkdir(dir_name)
    urls = re.findall('<a href="(.*?)" alt=".*?" title=".*?">', html)
    for ur in urls:
        file_name = ur.split('/')[-1]
        print('正在爬取地{}张图片'.format(num))
        response = requests.get(ur, headers=headers)
        with open(dir_name + '/' + file_name, 'wb') as f:
            f.write(response.content)
        num += 1



