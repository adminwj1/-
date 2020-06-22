from multiprocessing import Pool, Manager
from lxml import etree
import os, sys, time, re, requests


# https://www.vmgirls.com/

def index(url, headers):
    request = requests.get(url, headers=headers)
    html = request.text
    return html


def matchingUrl(urls):
    url = etree.HTML(urls)
    urls = url.xpath('//ul[@class="navbar-nav main-menu d-none d-lg-flex mr-auto px-4"]//a/@href')
    return urls


def disposeUrls(urls):    # 处理过后的ursl列表，这里可能会出先相同的url地址，需要删除一个
    """处理urls列表"""
    items = []
    num = len(urls)
    for i in range(num):
        index = -i + 2
        if index <= num:
           if urls[i] == urls[index]:
                print(urls[i])
                continue
           else:
                items.append(urls[i])
    return items


def LinkedAddess(disposeurls, headers):
    downImage = []
    for item in disposeurls:
        # print(item)
        indexUrls = requests.get(item, headers=headers)
        urls = indexUrls.text
        indexUrl = etree.HTML(urls)
        html = indexUrl.xpath('//div[@class="col-6 col-md-3 d-flex py-2"]//a/@href')
        # print(html)

        for url in html:

            # 匹配的图片链接地址
            downImages = requests.get(url, headers=headers)
            images = downImages.text
            urls = etree.HTML(images)
            image = urls.xpath('//div[@class="nc-light-gallery"]//a/@href')
            print(image)
            downImage.append(image)
    print("这是最后的列表数据：==============================================")
    print(downImage)



def main():
    url = "https://www.vmgirls.com/"
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                      'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.106 Safari/537.36'
    }
    indexUrls = index(url, headers)
    urls = matchingUrl(indexUrls)   # 首行栏地址

    disposeurls = disposeUrls(urls)     # 处理过后的ursl列表，这里可能会出先相同的url地址，需要删除一个

    LinkedAddess(disposeurls, headers)
    pool = Pool(6)
    pool.apply_async(LinkedAddess, args=(disposeurls, headers))
    pool.close()
    pool.join()
if __name__ == '__main__':
    main()