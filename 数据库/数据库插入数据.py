import pymysql
db = pymysql.connect("localhost", "root", "adminwj", "wj")
# 创建一个cursor对象，帮助我们执行sql语句
cursor = db.cursor()
# 创建表
sql = 'insert into bandcard values(0, 400),(0, 500),(0, 600)'
try:
    cursor.execute(sql)
    db.commit()  # 提交事务
    print("数据插入成功")
except:
    # 如果提交失败，回滚到上一次数据
    db.rollback()

# 断开连接
cursor.close()
# 关闭数据库
db.close()









