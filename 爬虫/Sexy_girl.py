import requests
import re
import os
import lxml
from lxml import etree

headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.106 Safari/537.36'
}
num = 1
dir_name = '妹子自拍'
if not os.path.exists(dir_name):
    os.mkdir(dir_name)
for i in range(1, 73):
    urls = 'https://www.mzitu.com/222008/{}'.format(i)
    request = requests.get(urls, headers=headers)
    html = request.text
    # print(html)
    urs = re.findall('<p><img class=".*?" src=".*?" data-original="(.*?)" width="640" height="auto"/></p>', html)
    # urs = re.findall('<a href=".*?" ><img src="(.*?)" alt=".*?" width="700" height="1050" /></a>', html)
    print(urs)
    for uls in urs:
        file_name = uls.split('/')[-1]
        print('正在下载第{}张图片'.format(num))
        request_a = requests.get(uls, headers=headers)
        with open(dir_name + '/' + file_name, 'wb') as f:
            f.write(request_a.content)
        num +=1

