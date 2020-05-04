import requests
import os
import re
from lxml import etree
import time

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:73.0) Gecko/20100101 Firefox/73.0'
}
# 匹配第一个URL
requset = requests.get('https://www.vmgirls.com/', headers=headers)
html = requset.text
urls = re.findall('<div class=".*?"> <a href="(.*?)"'
                  ' class=".*?" style=.*? data-bg=.*? data-nclazyload=".*?"> <span class=".*?"></span> </a>', html)
# 查看当前目录下是否有指定保存目录
dirName = '唯美女生全站爬取'
if not os.path.exists(dirName):
    os.mkdir(dirName)
for url in urls:
#  对每个URL进行验证是否存在多页的情况
    span = requests.get(url, headers=headers)
    spanHtml = span.text
    selector = etree.HTML(spanHtml)
    links = selector.xpath('//div[@class="nav-links"]/a/@href')     # 匹配的是URL
# 统计页数
    listNumber = len(links)
    if listNumber > 0:
        print('正在处理多页数据')
        number = len(links)     # 将新的列表赋值给number
# 对匹配出来的多页url进行处理，匹配出图片链接
        for link_num in links:
            a = str(link_num).split('/2')[0]
            # print(a)
# 对图片链接进行匹配
            imag = requests.get(a, headers=headers)
            imagHtml = imag.text
            images = re.findall('<a href="(.*?)" alt=".*?" title=".*?">', imagHtml)     # 匹配的是图片URL
            # print(images)
# 下载图片
            print('开始下载图片=====================')
            for pictures in images:
                fileName = pictures.split('/')[-1]
                picture = requests.get(pictures, headers=headers)
                print('正在下载：', pictures)
            # 保存到本地磁盘
                with open(dirName + '/' + fileName, 'wb') as f:
                    f.write(picture.content)
            print('多页数据已下载完成，接下来进行单页数据下载')
            time.sleep(1)
    elif listNumber == 0:
        print('正在处理单页数据')
        print('开始下载图片=====================')
        pictures_1 = requests.get(url, headers=headers)
        pictures_1_imagHtml = pictures_1.text
        pictures_1_imagHtml_selector = etree.HTML(pictures_1_imagHtml)
        pictures_1_images = pictures_1_imagHtml_selector.xpath('//p/img/@data-src')
        for pictures_1_image in pictures_1_images:
            fileName = pictures_1_image.split('/')[-1]
            print('正在下载：', pictures_1_image)
            image = requests.get(pictures_1_image, headers=headers)
            with open(dirName + '/' + fileName, 'wb') as f:
                f.write(image.content)


if __name__ == '__main__':
    pass