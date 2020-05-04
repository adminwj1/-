import re,pickle
class Essential_Information(object):
    """学生基本信息"""
    '''
    姓名
    性别
    年龄
    手机号
    邮箱
    QQ账号
    省份证
    家庭地址
    学号
    '''
    name = ""
    student_number = ""
    sex = ""
    age = ""
    idcard = ""
    phone = ""
    mail = ""
    QQid = ""
    homeaddress = ""
    def input_info(self):
        self.name = input("请输入姓名：")

        self.student_number = input("请输入学号：")
        if not self.authentication():
            print("学号输入有误！")
            return -1
        self.sex = input("请输入性别：")
        self.age = input("请输入年龄：")
        self.idcard = input("请输入身份证：")
        if not self.IdCard():
            print("省份证输入有误！")
            return -1
        self.phone = input("请输入手机号：")
        if not self.Phone():
            print("手机号输入有误！")
            return -1
        self.mail = input("请输入邮箱：")
        if not self.Mail():
            print("邮箱输入有误！")
            return -1
        self.QQid = input("请输入QQ号：")
        self.homeaddress = input("请输入家庭地址：")

        ess = {"姓名：": self.name, "学号：": self.student_number, "性别：": self.sex, "年龄：": self.age, "身份证：": self.idcard,
               "手机号：": self.phone, "邮箱：": self.mail, "QQ：": self.QQid}
        f = open("essential_information.txt", 'ab')
        pickle.dump(ess, f)
        f.close()

    # 验证输入是否满足要求
    def authentication(self):
        # 学号验证
        if len(self.student_number) == 10:
            return True
        return False

    # 身份证验证不能小于或大于18位数字，前17为不能有字母
    def IdCard(self):
        if len(self.idcard ) == 18 and self.idcard[0:17].isdigit() and self.idcard[17].isdigit() or self.idcard[17].isalpha():
                return True
        return False

    # 手机号验证
    def Phone(self):
        if len(self.phone) == 11 and self.phone[0:10].isdigit():
            return True
        return False

    # 邮箱验证
    def Mail(self):
        c = re.compile(r'^\w+@(\w+\.)+(com|cn|net)$')
        s = c.search(self.mail)
        if s:
            return True
        return False

    # QQ号验证
    def QQ(self):
        if self.QQid[0:].isdigit() and len(self.QQid) >= 4:
            return True
        return False