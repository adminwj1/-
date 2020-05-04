import pymysql
import requests
from lxml import etree


headers = {
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.106 Safari/537.36'
    }
url = 'https://ishuo.cn/yulu'
# 请求url数据
request = requests.get(url, headers=headers)
urlHtml = request.text
# 匹配条件
urls = etree.HTML(urlHtml)
urlContents = urls.xpath('//div[@class="content"]/text()')
print("正在执行程序清等待....")
db = pymysql.connect('127.0.0.1', 'root', 'adminwj', 'choushibaike')
cursor = db.cursor()
try:
    for urlContent in urlContents:
        sql = 'insert into csbk values(0,"{}")'.format(urlContent)
        cursor.execute(sql)
        db.commit()
except:
    print("程序在将数据存入数据库的时候出现累异常情况！！！")
    db.rollback()
    cursor.close()
finally:
    db.close()





