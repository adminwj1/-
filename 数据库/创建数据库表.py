import pymysql
db = pymysql.connect("localhost", "root", "adminwj", "wj")
# 创建一个cursor对象，帮助我们执行sql语句
cursor = db.cursor()
# 检查表是否存在，如果存在则删除
cursor.execute("drop table if exists bandcard")
# 创建表
sql = 'create table bandcard(id int auto_increment primary key, money int not null)'
cursor.execute(sql)


# 断开连接
cursor.close()
# 关闭数据库
db.close()









