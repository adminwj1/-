import pymysql
#连接数据库
db_user = 'root'
db_passwd = 'root'
#db_addr = "192.168.190.100"
db_addr = "127.0.0.1"
db_data = "test"
'''连接数据库'''
try:
    conn = pymysql.connect(host=db_addr, user=db_user, password=db_passwd, database=db_data)
    print("数据库连接成功")
except pymysql.Error as e:
    print(e)
'''创建表'''
'''
#使用cursor()方法创建一个游标对象cur
cur = conn.cursor()
# 使用execute()方法执行SQL，如果表存在则删除
cur.execute("DROP TABLE IF EXISTS USER1")
try:
    #定义要执行的SQL语句
    sql = """
        CREATE TABLE USER1 (
         NAME  CHAR(20) NOT NULL,
         AGE INT(100),
         gender CHAR(2) NOT NULL,
         ID VARCHAR(19) NOT NULL )"""
    #执行SQL语句
    cur.execute(sql)
    print("数据表创建成功")
except pymysql.Error as e:
    print(e)
    '''
'''插入数据'''
'''
try:
    cur = conn.cursor()
    # SQL插入语句
    sql = """
        INSERT INTO USER1(NAME, AGE, gender, ID)
        VALUES ('小明', 22, '女', 510802199805183018)
    """
    # 执行SQL语句
    cur.execute(sql)
    # 提交到数据库执行
    conn.commit()
    print("插入语句成功")
except pymysql.Error as e:
    print(e)
finally:
    # 关闭游标
    cur.close()
    #关闭数据库
    conn.close()
'''

'''数据看查询'''
# 使用cursor()方法获取操作游标
cur = conn.cursor()
# SQL 查询语句
sql = "SELECT * FROM User1 > %s"
try:
    # 执行SQL语句
    cur.execute(sql)
    # 获取所有记录列表
    results = cur.fetchall()
    for row in results:
        name = row[0]
        age = row[1]
        gender = row[2]
        ID = row[3]
        # 打印结果
        print("name=%s, age = %s, gender = %s, ID=%s" % (name, age, gender, ID))
except pymysql.Error as e:
    print(e)
finally:
    # 关闭数据库
    conn.close()

'''数据库更新'''







'''删库操作'''








# #关闭数据库
# conn.close()