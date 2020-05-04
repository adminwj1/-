'''
爬虫思路：
首先确定需要爬取的网页URL地址
通过HTTP协议来获取对应的HTML页面
提取HTML页面里的有用数据

破解动态验证码：tesseract
中国常见的框架Scrapy、Pyspider
Scrapy：高定制性能（异步网络框架twisted），所以数据下载速度非常快，提供了数据存储、数据下载、提取规则等组件
分布式策略：scrapy-redis
反爬虫技术：
User-Agent：让程序模拟成浏览器
代理：
验证码：
动态数据加载：Selenium+PhantimJS(无界面浏览器)，模拟真实浏览器加载js、ajax等非静态页面数据
加密数据：

通用爬虫工作流程：
爬取网页
存储数据
内容处理
提供检索/排名服务

通用化爬虫缺点：
只能提供文本相关的内容（HTML、World、PDF）等，但是不能提供多媒体（音乐、图片、视频）和二进制文件（程序、脚本）等
提供结果千篇一律，不能针对不同人群提供不同的搜索结果
不能理解人类语义上的检索
为了解决这些缺点就有了-聚焦网络爬虫
概念：爬虫程序员写的针对某种内容的爬虫
特点：面向主体爬虫，面向需求爬虫，会针对某种特定的内容去爬取信息，而且会保证信息和需求尽可能相关
'''

from lxml import etree

text = '''
<div>
<ul>
<li class="item-0"><a href="link1.html">first item</a></li>
<li class="item-1"><a href="link2.html">second item</a></li>
<li class="item-inactive"><a href="link3.html">third item</a></li>
<li class="item-1"><a href="link4.html">fourth item</a></li>
<li class="item-0"><a href="link5.html">fifth item</a>
</ul>
</div>
'''
from lxml import etree

html = etree.parse('./test.html', etree.HTMLParser())
result = etree.tostring(html)
print(result.decode('utf-8'))
