import pymysql

# 连接数据库
'''
参数1：mysql服务器地址
参数2：mysql用户名
参数3：mysql用户密码
参数4：连接的数据库名
'''

db = pymysql.connect("localhost", "root", "adminwj", "wj")
# 创建一个cursor对象，帮助我们执行sql语句
cursor = db.cursor()
sql = 'select * from students'    # 要执行的SQL语句
# 执行SQL语句
cursor.execute(sql)

# 获取返回的信息
data = cursor.fetchall()
print(data)

# 断开连接
cursor.close()
# 关闭数据库
db.close()









