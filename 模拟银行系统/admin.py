import time
class Admin(object):
    #  管理员账号
    admin = 1

    passwd = 1
    def printAdminView(self):
        print("*************************************************")
        print("*                                               *")
        print("*                                               *")
        print("*                  欢迎光临                      *")
        print("*                                               *")
        print("*                                               *")
        print("*************************************************")

    # 用户登录系统
    def adminLong(self):
        inputAdmin = int(input("请输入管理员账号："))
        if self.admin != inputAdmin:
            print("管理员账号输入错误！！")
            return -1
        inputPasswd = int(input("请输入管理员密码："))
        if self.passwd != inputPasswd:
            print("管理员密码输入错误！！")
            return -1
        # 能执行到这里管理员账户密码是没有问题的
        print("操作成功！！请稍等...")
        time.sleep(0.5)
        return 0





    def printsysFunctionView(self):
        print("*************************************************")
        print("*    开户（1）               查询（2）           *")
        print("*    取款（3）               存款（4）           *")
        print("*    转账（5）               改密（6）           *")
        print("*    锁定（7）               解锁（8）           *")
        print("*    补卡（9）               销户（0）           *")
        print("*               退出（q）                       *")
        print("*************************************************")