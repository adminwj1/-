# 想成为你喜欢的人
import requests
from lxml import etree
import os
from multiprocessing import Pool
import threading
headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.106 Safari/537.36'
    }
dir_name = '想成为你喜欢的人'   # 可以使用xpath进行主题名的匹配
if not os.path.exists(dir_name):
    os.mkdir(dir_name)

def basice(headers):
    """地址的请求与返回"""
    url = 'https://www.vmgirls.com/13679.html'  # 爬取的网页地址
    request = requests.get(url, headers=headers)
    html = request.text
    return html


def getImg(html):
    """图片下载主函数"""
    headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.106 Safari/537.36'
    }
    urlImg = etree.HTML(html)
    links = urlImg.xpath('//div[@class="nc-light-gallery"]//a/@href')  # 匹配的是图片的URL
    for link in links:
        # print(link)   # 用于显示测试
        file_name = link.split('/')[-1]     # 使用列表的分片功能进行分片取名
        print(file_name)
        img = requests.get(link, headers=headers)   # 匹配页面中的图片
        with open(dir_name + '/' + file_name, 'wb') as f:
            print("正在下载第%s张图片" % file_name)
            f.write(img.content)

def main():
    """主函数，进行多进程的下载"""
    html = basice(headers)
    po = Pool()
    for i in range(8):
        po = threading.Thread(target=getImg, args=(html, ))
        po.start()
    po.join()



if __name__ == '__main__':
    main()