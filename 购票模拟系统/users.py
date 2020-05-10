import random
import pymysql
class User(object):
    def __init__(self, name, address, grender, national):
        self.name = name
        self.address = address
        self.national = national
        self.grender = grender

    def random_cardid(self):
        """随机产生18位身份证号"""
        check_code = ''
        for i in range(1, 19):
            current = random.randint(1, 9)
            check_code += str(current)
        print(check_code)
        return check_code

    def random_id(self):
        """随机产生6位数的唯一标识"""
        id = ''
        for i in range(1, 7):
            current = random.randint(1, 9)
            id += str(current)
        print(id)
        return id

    def input_user(self):
        """输入用户基本信息"""
        username = input("请输入您的名字：")
        usergrender = input("请输入您的性别：")
        address = input("请输入您的家庭住址：")
        national = input("请输入您的名族：")
        info = ['姓名：', username, '性别：',usergrender, '家庭住址：', address, '名族：', national]
        print(info)
        return info

def main():
    user = User('', '', '', '')
    check_code = user.random_cardid()
    id = user.random_id()
    info = user.input_user()
    listinfo = [info, '身份证号码：', check_code, '唯一标识码：', id]
    print(listinfo[4])
    db = pymysql.connect('127.0.0.1', 'root', 'adminwj', 'ticket_system')
    cursor = db.cursor()
    try:
        sql = 'insert into ticket_system values("{}","{}","{}","{}","{}","{}")'\
            . format(listinfo[4], listinfo[0][1], listinfo[0][3], listinfo[2], listinfo[0][5],listinfo[0][7])
        cursor.execute(sql)
        db.commit()
        print("数据插入成功")
    except:
        db.rollback()
        cursor.close()
        print("数据库插入数据失败")
    finally:
        db.close()
if __name__ == '__main__':
    main()