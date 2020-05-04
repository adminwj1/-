import pymysql
class WjSql():
    def __init__(self, host, user, passwd, dbName):
        self.host = host
        self.user = user
        self.passwd = passwd
        self.dbName = dbName

    # 连接数据库
    def connet(self):
        self.db = pymysql.connect(self.host, self.user, self.passwd, self.dbName)
        self.cursor = self.db.cursor()  # 创建一个cursor对象，帮助我们执行sql语句

    # 关闭数据的连接和断开连接
    def clos(self):
        self.cursor.close()
        self.db.close()

    # 查询
    def get_all(self, sql):
        res = ()
        try:
            self.connet()  # 调用连接数据库方法
            self.cursor.execute(sql)
            res = self.cursor.fetchall()
            self.clos()  # 关闭数据的连接和断开连接方法
        except:
            print("查询失败")
        return res

    def get_one(self, sql):
        res = None
        try:
            self.connet()   # 调用连接数据库方法
            self.cursor.execute(sql)
            res = self.cursor.fetchone()
            self.clos()  # 关闭数据的连接和断开连接
        except:
            print("查询失败")
        return res

    # 插入
    def insert(self, sql):
        return self.__deit(sql)
    def update(self, sql):
        return self.__deit(sql)
    def delete(self,sql):
        return self.__deit(sql)

    def __edit(self,sql):
        count = 0
        try:
            self.connet()
            count = self.cursor.execute(sql)
            self.db.commit()
            self.clos()
        except:
            print("事务提交失败")
            self.db.rollback()
        return count