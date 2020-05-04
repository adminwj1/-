import lxml
from lxml import etree
import re
import requests
import os
def request(url, headers):
    urls = url
    headers = headers
    request = requests.get(urls, headers=headers)
    urlHtml = request.text
    # print(urlHtml)
    urls = re.findall('<span>(\d.*?)</span>', urlHtml)  # 匹配出最大的页数
    print(urls)
    return urlHtml
def urlImg(html):
    # print(html)
    # 拼接地址
    # https://www.mzitu.com/171649/48
    selector = etree.HTML(html)
    link = selector.xpath('//div[@class="main-image"]/p/a/@href')
    # print(links)
    return link
def links(link, headers):
    link = ''.join(link).split("/2")[0]
    # print(link)
    # 匹配地址
    # link =
    # print(link)
    for i in range(1, 50):
        urls = link + "/" + str(i)
        print(urls)
        req = requests.get(urls, headers=headers)
        reqHtml = req.text
        # selector = etree.HTML(reqHtml)
        # link = selector.xpath('//div[@class="main-image"]/p/a/img/@src')
        # print(link)
        url = re.findall('<div class=".*?"><p><a href=".*?"><img src="(.*?)" alt="(.*?)" width=".*?" height=".*?"></a></p></div>', reqHtml)
        print(url)





def main():
    url = "https://www.mzitu.com/171649"
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.106 Safari/537.36'
    }
    html = request(url, headers)
    link = urlImg(html)
    links(link, headers)


if __name__ == '__main__':
    main()