from tkinter import *
import threading
from multiprocessing import Pool
import requests
from lxml import etree
import re
import os
from tkinter import filedialog

fileName = ''
print(fileName)

def printItem():
    print(vLang.get())

def save():
    name = filedialog.askdirectory()
    global fileName
    fileName = name
    print(name)
    download.insert(END, '保存位置：' + fileName + '\n')
    download.update()

def download_to():
    url = 'https://www.vmgirls.com/'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:73.0) Gecko/20100101 Firefox/73.0'
    }
    request = requests.get(url, headers=headers)
    html = request.text
    urls = re.findall('<div class=".*?"> <a href="(.*?)"'
                      ' class=".*?" style=.*? data-bg=.*? data-nclazyload=".*?"> <span class=".*?"></span> </a>', html)
    # 测试urls
    for url in urls:
        download.insert(END, url + '\n')
        download.update()
        # 匹配url中的项目链接
        span = requests.get(url, headers=headers)
        spanHtml = span.text
        selector = etree.HTML(spanHtml)
        # 这里匹配所有的url地址
        links = selector.xpath('//div[@class="nav-links"]/a/@href')

        download.update()
        for link in links:
            a = str(link).split('/2')[0]
            download.insert(END, a + '\n')
            download.update()
            # 对每个页面进行图片匹配
            imag = requests.get(link, headers=headers)
            imagHtml = imag.text
            images = re.findall('<a href="(.*?)" alt=".*?" title=".*?">', imagHtml)
            for image in images:
                download.insert(END, image + '\n')
                download.update()
                file = image.split('/')[-1]
                img = requests.get(image, headers=headers)
                download.insert(END, '正在下载：' + image + '\n')
                download.update()
                with open(fileName + '/' + file, 'wb') as f:
                    f.write(img.content)
                # 单页数据

        pictures_1_imagHtml_selector = etree.HTML(spanHtml)
        pictures_1_images = pictures_1_imagHtml_selector.xpath('//p/img/@data-src')
        for pictures_1_image in pictures_1_images:
            download.insert(END, '正在下载：' + pictures_1_image + '\n')
            download.update()
            fileName_img = pictures_1_image.split('/')[-1]
            img = requests.get(pictures_1_image, headers=headers)
            with open(fileName + '/' + fileName_img, 'wb') as f:
                f.write(img.content)
    download.insert(END, '图片下载完成！！！')
    download.update()
root = Tk()
root.geometry("800x400+400+150")
root.resizable(width=FALSE, height=FALSE)
root.title("多功能图片下载器")
"""这里的顶层菜单中的内容仅用于测试使用"""
menubar = Menu(root)
vLang = StringVar()
filemenu = Menu(menubar, tearoff=0)
for k in ['设置', '帮助', '保存输出内容', '关于', '退出']:
    filemenu.add_radiobutton(label=k, variable=vLang, command=printItem)
menubar.add_cascade(label='功能', menu=filemenu)
root['menu'] = menubar
# 创建滚动条
scroll = Scrollbar()
download = Text(root, width=95, height=15, font=('楷体', 12), bg='black', fg='green')
scroll.pack(side=RIGHT, fill=Y)
download.place(x=10, y=120)
    # 管理text和scroll（滚动条）
scroll.config(command=download.yview)
download.config(yscrollcommand=scroll.set)
notarize = Button(root, text='下载', font=('楷体', 15), width=20, command=download_to)
notarize.place(x=60, y=20, height=55)
saveFile = Button(root, text='保存', font=('楷体', 15), width=20, command=save)
saveFile.place(x=530, y=20, height=55)
stop = Button(root, text='停止', font=('楷体', 15), width=10, bg='red')
stop.place(x=350, y=20, height=55)
root.mainloop()
if __name__ == '__main__':
    # save()
    pass