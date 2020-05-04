from wjsql import WjSql
import pymysql
# 连接对象
db = pymysql.connect('127.0.0.1', 'root', 'adminwj', 'studentsystem')
cursor = db.cursor()
# 注册功能
def register():
    name = input("请输入用户名：")
    passwd = input("请输入密码：")
    try:
        sql = 'insert into zc values("{}","{}","{}")'.format(0, name, passwd)
        cursor.execute(sql)
        db.commit()
        print("注册成功")
    except:
        print("注册失败！")
        # 关闭
        cursor.close()
    db.close()

# register()


# 登录
def login():
    name = input("请输入用户名：")
    password = input("请输入密码：")
    sql = 'select * from zc where name = "%s" and passwd = "%s";' % (name,password)
    res = cursor.execute(sql)
    if res:
        print("登录成功！")
    else:
        print("登录失败！")
login()