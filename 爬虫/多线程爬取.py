import requests
import re
import threading
import os
num = 1
def get_html_text_one(url, headers):
    request = requests.get(url, headers=headers)
    if request.status_code == 200:
        return request.text
    return request


def get_images_one(html, headers):
    urls = re.findall('><a href="(.*?)" alt=".*?".*?"><img src=.*? alt="" data-src=.*? data-nclazyload="true"></a>',html)
    for url in urls:
        file_name = url.split('/')[-1]
        global num
        print('正在下载p第{}'.format(num))
        request = requests.get(url, headers=headers)
        with open('你与星河,皆可收藏' + '/' + file_name, 'wb') as f:
            f.write(request.content)
        num += 1
print("=======================================================================================================")








def get_images_two():
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.106 Safari/537.36'
    }
    dir_name = '妹子自拍'
    if not os.path.exists(dir_name):
        os.mkdir(dir_name)
    global num
    for i in range(1, 3):
        urls = 'https://www.mzitu.com/jiepai/comment-page-{}/#comments'.format(i)
        request = requests.get(urls, headers=headers)
        html = request.text
        urs = re.findall('<p><img class=".*?" src=".*?" data-original="(.*?)" width="640" height="auto"/></p>', html)

        for uls in urs:
            file_name = uls.split('/')[-1]
            print('正在下载p1第{}张图片'.format(num))
            request_a = requests.get(uls, headers=headers)
            with open(dir_name + '/' + file_name, 'wb') as f:
                f.write(request_a.content)
            num += 1



def get_images_two_three():
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.106 Safari/537.36'
    }
    dir_name = '妹子自拍'
    if not os.path.exists(dir_name):
        os.mkdir(dir_name)
    global num
    for i in range(4, 6):
        urls = 'https://www.mzitu.com/jiepai/comment-page-{}/#comments'.format(i)
        request = requests.get(urls, headers=headers)
        html = request.text
        urs = re.findall('<p><img class=".*?" src=".*?" data-original="(.*?)" width="640" height="auto"/></p>', html)

        for uls in urs:
            file_name = uls.split('/')[-1]
            print('正在下载p1第{}张图片'.format(num))
            request_a = requests.get(uls, headers=headers)
            with open(dir_name + '/' + file_name, 'wb') as f:
                f.write(request_a.content)
            num += 1


def main():
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.106 Safari/537.36'
    }
    url = 'https://www.vmgirls.com/3545.html'
    html = get_html_text_one(url, headers)
    get_images_one(html, headers)

def main2():
    get_images_two()

def main3():
    get_images_two_three()

if __name__ == '__main__':
    main()