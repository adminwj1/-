import re
import requests
from lxml import etree
import os
from multiprocessing import Pool
import threading
num = 0
# 请求头
headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.106 Safari/537.36'
    }
# https://www.vmgirls.com/13804.html
# https://www.vmgirls.com/13717.html
# 需要访问的url
url = input('请输入URL地址：')

def request(url, headers):
    """页面数据的请求函数"""
    html = requests.get(url, headers=headers)
    html_url = html.text
    return html_url



def request_Images(url):
    """匹配图片地址函数"""
    urls = etree.HTML(url)
    url = urls.xpath('//div[@class="nc-light-gallery"]//a/@href')
    global num
    num = len(url)
    return url


def down_Images(urls, headers, dirName):
    """下载图片函数"""
    for url in urls:
        # print(url)  # 输出每个图片链接的地址
        # 为每张图片取个名
        fileName = url.split('/')[-1]
        img = requests.get(url, headers=headers)
        with open(dirName + '/' + fileName, 'wb') as f:
            print("正在下载第%s张图片：" % fileName)
            f.write(img.content)

def imgDirName(RQ):
    """匹配目录名称"""
    a = re.findall('<h1 class="post-title h3">(.*?)</h1>', RQ)
    # print(a)    # 测试使用显示目录名
    name = ''.join(a)
    """创建目录"""
    if not os.path.exists(name):
        os.mkdir(name)
    # print(type(name))
    return name


def main():
    """程序主函数"""
    RQ = request(url, headers)
    # print(RQ)
    urls = request_Images(RQ)
    # print(urls)
    dirName = imgDirName(RQ)
    print("目录名称为：%s" % dirName)
    po = Pool()
    for i in range(num):
        po = threading.Thread(target=down_Images, args=(urls, headers, dirName))
        po.start()
    po.join()
if __name__ == '__main__':
    main()
