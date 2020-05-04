from tkinter import *
import requests
import re
import time
from lxml import etree
import threading

def request(url, headers):
    """爬取网页代码"""
    request = requests.get(url, headers=headers)
    html = request.text
    return html

def urls(html):
    """这里匹配图片链接"""
    urls = re.findall('<a href="(.*?)" alt="(.*?)" title=".*?">', html)
    return urls

def down(urls, headers):
    """下载图片"""
    for url in urls:
        # print(url[0])
        fileName = url[0].split('/')[-1]
        # print(fileName)
        picture = requests.get(url[0], headers=headers)
        print("正在下载%s" % url[0])
        with open('img' + '/' + fileName, 'wb') as f:
            f.write(picture.content)


def main():
    url = 'https://www.vmgirls.com/12945.html'
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.106 Safari/537.36'
    }
    html = request(url, headers)
    # print(html)
    url = urls(html)
    # for urlimg in url:
    #     print(urlimg[0])
    down(url, headers)

if __name__ == '__main__':
    main()