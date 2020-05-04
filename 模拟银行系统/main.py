from admin import Admin
from atm import ATM
import os
import pickle
import time
def main():
    # 字典写有问题，如果创建的文件中没有数据会报错
    absPath = os.getcwd()  # 获取当前程序文件所在路径
    filepath = os.path.join(absPath,"allusers.txt")  # 在当前路径下创建一个名为alluser.txt的文件
    f = open(filepath,"rb")
    allUsers = pickle.load(f)
    # print(allUsers)

    admin = Admin()
    admin.printAdminView()
    if admin.adminLong():
        return -1
    atm = ATM(allUsers)
    while True:
        print(allUsers)
        admin.printsysFunctionView()
        option = input("请输入您的操作：")
        if option == "1":   #  当用户选择选项后调用ATM类
            #  开户
            atm.createUser()
        elif option == "2":
            #  查询
            atm.searchUserInfo()
        elif option == "3":
            #  取款
            atm.getMoney()
        elif option == "4":
            #  存款
            atm.saveMoney()
        elif option == "5":
            #  转账
            atm.transferMoney()
        elif option == "6":
            #  改密码
            atm.changePasswd()
        elif option == "7":
            #  锁定
            atm.lockUser()
        elif option == "8":
            #  解锁
            atm.unlokUser()
        elif option == "9":
            #  补卡
            atm.newCard()
        elif option == "0":
            #  销户
            atm.killUser()
        elif option == "q":
            #  如果输入的账号和密码正确判定为false就结束程序，如果账号密码是错误的就判断为正确的继续循环执行程序
            if not admin.adminLong():
                f = open(filepath, "wb")
                pickle.dump(atm.allUser,f)
                f.close()
                return -1

if __name__ == '__main__':
    main()