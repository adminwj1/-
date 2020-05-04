from lxml import etree
import re
html_doc = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title"><b>The Dormouse's story</b></p>

<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>

<p class="story">...</p>
"""


# 创建选择器对象
selector = etree.HTML(html_doc)
# 取所有的链接
links = selector.xpath('//p[@class="story"]/a/@href')
# links = selector.xpath('//p[@class="title"]')
for link in links:
    print(link)

'''
概念：
节点：
    元素、属性、文本、命名空间、文档（根）节点
    
节点关系（Node）
父（parent）
子（children）
同胞（sibling）
先辈（ancestor）
后代（descendant）

xpath语法
nodename        选取此节点的所有子节点
http://iguye.com/books.xml

'''
url = 'https://www.vmgirls.com/13344.html'
span = re.findall('<a href="(.*?)" class=.*?>(/d+)</a>', url)
print(span)