import requests
import re
from lxml import etree
import os

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:73.0) Gecko/20100101 Firefox/73.0'
}
url = 'https://www.gushiwen.org/gushi/tangshi.aspx'

"""搜索诗句类别"""
request = requests.get(url, headers=headers)
html = request.text
urls = re.findall('<div class="bookMl"><strong>(.*?)</strong></div>', html)
"""搜索诗句类别下面的跳转链接"""
LianJies = re.findall('<span><a href="(.*?)" target=".*?">(.*?)</a>.*?</span>', html)
for LianJie in LianJies:
    # print(LianJie)
    """对匹配出来的链接进行处理"""
    # print(LianJie[0])   # 匹配出每个类别下面的跳转链接地址
    links = requests.get(LianJie[0], headers=headers)
    linksHtml = links.text
    # print(linksHtml)
    """匹配诗句的作者和内容"""
    countles = etree.HTML(linksHtml)
    countle = countles.xpath('//p[@class="source"]/a[@href]/text()')    #所有诗词的作者和朝代
    coun = ''.join(countle)
    print(coun)
    with open('./1.txt', 'a', encoding='utf-8') as f:
        f.write(coun + '\n')

        # 匹配具体诗句内容
    aaa = countles.xpath('//div[@class="contson"]/text()')
    for bbb in aaa:

        print(bbb)
        with open('./1.txt', 'a', encoding='utf-8') as f:
            f.write(bbb + '\n')