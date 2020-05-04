import requests
import os
import re
headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.106 Safari/537.36'
}

url = 'http://www.xiachufang.com/category/40076/'
request = requests.get(url, headers=headers)
html = request.text
urls = re.compile('<img src=.*? data-src="(.*?)" width="215" height="136" alt="(.*?)"'
                  '.*? <p class=.*?>.*?<span class=.*?>(.*?)</span>', re.S)
url = re.findall(urls, html)
for ur in url:
    a = ''.join(ur)
    with open('下厨房.txt', 'a', encoding='utf-8') as f:
        f.write(a + '\n')

