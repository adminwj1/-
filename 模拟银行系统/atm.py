from card import Card
from user import User
import time
import random

class ATM(object):
    KH = int()
    CM = int()
    PW = ""
    cardLook = False
    def __init__(self,allUsers):

        self.allUser = allUsers  #  卡号-用户
    # 创建账户
    def createUser(self):
        name = input("请输入您的姓名：")
        idCard = input("请输入您的身份证号码：")
        phone = input("请输入您的手机号：")
        prestoreMone = int(input("请输入您预存金额："))
        # 控制输入预存金额的准确
        if prestoreMone < 0:
            print("预存金额输入有误！！开户失败！")
            return -1
        # 设置银行卡密码（这里控制输入为6位数）
        onePass = input("请输入6位数的银行卡密码：")
        if len(onePass) != 6:
            print("密码设置为满足要求，开户失败！！")
            return -1
        if not self.checkPasswd(onePass):
            print("密码输入错误！！开户失败....")
            return -1

        # 所有信息完成
        # 存随机出来的卡号
        cardStr = self.randomCardId()
        # 输出卡号
        # print(cardId)
        card = Card(cardStr, onePass, prestoreMone) # 创建一个Card的对象，并将这个对象给user
        user = User(name, idCard, phone, card)  # 给User创建一个对象，并且传值
        self.allUser[cardStr] = user    # 将用户存字典
        print("开户成功！！请牢记卡号...(%s)" % cardStr)

    #查询余额
    def searchUserInfo(self):
        '''
        判断卡号是否存在
        判断卡是否被锁
        判断密码是否正确
        输出余额
        '''
        self.cardid()
        # 验证卡是否被锁
        # if not self.cardLook:
        #     print("该卡被锁定！！请解锁后在进行其他操作...")
        #     return -1
        if self.cardLook == True:
            print("该卡被锁定！！请解锁后在进行其他操作...")
            return -1
        # 设置银行卡密码（这里控制输入为6位数）
        onePass = input("请输入6位数的银行卡密码：")
        if len(onePass) != 6:
            print("密码设置为满足要求，开户失败！！")
        if not self.checkPasswd(self.PW):
            print("密码输入错误！！请解锁后在进行其他操作...")
            self.cardLook = True
            return -1
        print("账号：%s 余额：%d " % (self.KH, self.CM))



    # 取款
    def getMoney(self):
        self.cardid()
        # 验证卡是否被锁
        if self.cardLook == True:
            print("该卡被锁定！！请解锁后在进行其他操作...")
            return -1
        onePass = input("请输入6位数的银行卡密码：")
        if len(onePass) != 6:
            print("密码设置为满足要求，开户失败！！")
        if not self.checkPasswd(self.PW):
            print("密码输入错误！！请解锁后在进行其他操作...")
            return -1

        # 取款验证
        money = int(input("验证成功！！请输入您的取款金额："))
        if money > self.CM:
            print("余额不足！！取款是不...")
            return -1
        if money < 0:
            print("取款金额输入有误！！取款失败...")
            return -1
        # 开始取款，用卡上的余额减去取出的余额剩下的余额将返回到类中的CM属性中
        self.CM -= money
        print("取款成功！！余额 %d" % (self.CM))

    # 存款
    def saveMoney(self):
        self.cardid()
        # 验证卡是否被锁
        if self.cardLook == True:
            print("该卡被锁定！！请解锁后在进行其他操作...")
            return -1
        onePass = input("请输入6位数的银行卡密码：")
        if len(onePass) != 6:
            print("密码设置为满足要求，开户失败！！")
        if not self.checkPasswd(self.PW):
            print("密码输入错误！！请解锁后在进行其他操作...")
            return -1
        # 验证卡是否被锁
        # 存款验证
        money = int(input("验证成功！！请输入您的存款金额："))
        if money < 0:
            print("存款金额有误！！存款失败...")
            return -1
        self.CM += money
        print("取款成功！！余额 %d" % (self.CM))

        #   转账
    def transferMoney(self):
        self.cardid()
        # 验证卡是否被锁
        if self.cardLook == True:
            print("该卡被锁定！！请解锁后在进行其他操作...")
            return -1
        onePass = input("请输入6位数的银行卡密码：")
        if len(onePass) != 6:
            print("密码设置为满足要求，开户失败！！")
        if not self.checkPasswd(self.PW):
            print("密码输入错误！！请解锁后在进行其他操作...")
            return -1
        # 验证卡是否被锁
        # 转账验证
        money = int(input("验证成功！！请输入您的转账金额："))
        if money > self.CM or money < 0:
            print("金额有误，转账失败")
            return -1
        # 开始转账
        newcard = input("请输入转入账号：")
        newcard = self.allUser.get(newcard)
        if not newcard:
            print("该卡号不存在，转账失败！")
            return -1
        self.CM -= money
        newcard.card.cardMoney += money
        time.sleep(1)
        print("转账成功，请稍后...")
        time.sleep(1)
        print("转账金额%d元，账号余额为%d元！" % (money, self.CM))


    # 改密码
    def changePasswd(self):
        cardNum = input("请输入您的卡号：")
        user = self.allUser.get(cardNum)
        if not user:
            print("卡号不存在，修改密码失败！！")
            return -1
         # 验证卡是否被锁
        if self.cardLook == True:
            print("该卡被锁定！！请解锁后在进行其他操作...")
            return -1
        # 开始修改密码
        newPasswd = input("请输入新密码：")
        if len(newPasswd) != 6:
            print("密码设置为满足要求，开户失败！！")
        if not self.checkPasswd(newPasswd):
            print("密码修改失败！！")
            return -1
        user.card.cardPass = newPasswd
        print("修改密码成功！！请稍后...")



    # 锁定
    def lockUser(self):
        self.cardid()
        # 验证卡是否被锁
        if self.cardLook == True:
            print("该卡被锁定！！请解锁后在进行其他操作...")
            return -1
        # 验证密码
        onePass = input("请输入6位数的银行卡密码：")
        if len(newPasswd) != 6:
            print("密码设置为满足要求，开户失败！！")
        if not self.checkPasswd(self.PW):
            print("密码输入错误！！请解锁后在进行其他操作...")
            return -1
        # 锁卡
        self.cardLook = True
        print("锁卡成功...")


    # 解锁
    def unlokUser(self):
        self.cardid()
        # 验证卡是否被锁
        if self.cardLook == False:
            print("该卡没有锁定！！无需解锁...")
            return -1
        # 验证密码
        onePass = input("请输入6位数的银行卡密码：")
        if len(newPasswd) != 6:
            print("密码设置为满足要求，开户失败！！")
        if not self.checkPasswd(self.PW):
            self.cardLook = True
            print("密码输入错误！！请解锁后在进行其他操作...")
            return -1
        # 解锁
        self.cardLook = False
        print("解锁成功...")


    # 补卡
    def newCard(self):
        carNum = input("请输入您的卡号：")
        user = self.allUser.get(carNum)
        if not user:
            print("该卡号不存在")
            return -1
        tempname = input("请输入您的姓名：")
        tempidcard = input("请输入您的省份证号码：")
        tempphone = input("请输入您的手机号：")
        if tempname != self.allUser[carNum].name\
            or tempidcard != self.allUser[carNum].idCard\
            or tempphone != self.allUser[carNum].phone:
            print("信息有误，补卡失败！！")
            return -1
        # newPasswd = input("请输入您的新密码：")
        # self.allUser[carNum].card.cardPass = newPasswd
        newPasswd = input("请输入新密码：")
        user.card.cardPass = newPasswd
        time.sleep(1)
        print("补卡成功，请牢记您的新密码！")

    # 销户
    def killUser(self):
        self.cardid()
        # 验证卡是否被锁
        if self.cardLook == True:
            print("该卡被锁定！！请解锁后在进行其他操作...")
            return -1
        # 验证密码
        onePass = input("请输入6位数的银行卡密码：")
        if len(onePass) != 6:
            print("密码设置为满足要求，开户失败！！")
        if not self.checkPasswd(self.PW):
            print("密码输入错误！！请解锁后在进行其他操作...")
            return -1
        #销户
        del self.allUser[self.KH]
        time.sleep(1)
        print("销户成功，请稍后！！")


    """验证方法"""

    # 验证用户


    # 验证卡号
    def cardid(self):
        cardNum = input("请输入您的卡号：")
        user = self.allUser.get(cardNum)    # 将cardNum的值拿到allUser字段中去找看看能否找到匹配的值
        if not user:    # 如果有这个卡号就不执行下面的语句，没有找到这个卡号就执行
            print("该卡号不存在！！查询失败...")

            exit(0)  # 占时使用exit(0)来结束程序的执行，等找到bug后再改
            # return -1
        # 调用类中的属性将user.card.cardId和user.card.cardMoney的值传入其中方便其他方发进行调用
        self.KH = user.card.cardId
        self.CM = user.card.cardMoney
        self.PW = user.card.cardPass


    # 验证密码
    def checkPasswd(self, realPasswd):
        for i in range(3):
            tempPasswd = input("请输入密码：")
            #  控制输入6位数密码
            if tempPasswd == realPasswd and len(tempPasswd) == 6:
                return True
        return False


    # 随机生成6位数的卡号
    def randomCardId(self):
        while True:
            str = ""
            for i in range(6):
                ch = chr(random.randrange(ord('0'), ord('9') +1)) #  chr函数将随机出来的整数转换成字符串
                str += ch
            # 判断是否重复，如果在allUser字典中没有找到随机出来的卡号就返回false，加个not为真就返回这个随机出来的卡号。如果在allUser中找到和随机出来的数字一样的返回True，加个not为假就不返回这个随机数。
            if not self.allUser.get(str):
                return str