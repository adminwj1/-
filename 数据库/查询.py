'''
fetchone()
功能：获取下一个查询结果集，结果是一个对象



fetchall()
功能：接收全部的返回行(元组)


rowcount：是一个只读属性，返回execute()方法影响的行数，查询了多少行数
'''
import pymysql
db = pymysql.connect("localhost", "root", "adminwj", "wj")
# 创建一个cursor对象，帮助我们执行sql语句
cursor = db.cursor()
# 查询
# 钱数大于400
sql = 'select * from bandcard where money > 400'
try:
    cursor.execute(sql)
    # print("数据查询成功")
    reslist = cursor.fetchall()
    for row in reslist:
        print("%d--%d" % (row[0], row[1]))
except:
    # 如果提交失败，回滚到上一次数据
    db.rollback()

# 断开连接
cursor.close()
# 关闭数据库
db.close()









