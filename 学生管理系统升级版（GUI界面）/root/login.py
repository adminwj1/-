# —*— encoding: utf-8 _*_
import tkinter
from tkinter import ttk
from zjm import Sys
import os
import pymysql
from sel import Select
from checkpasswd import CheckPasswd
from tkinter import messagebox
class Login(object):
    def __init__(self):
        self.root = tkinter.Tk()
        self.root.title('学生信息系统-登录模块')
        self.root['width'] = 500
        self.root['height'] = 200
        self.root.resizable(width=False, height=False)
        self.label_account = tkinter.Label(self.root, text='用户名：', width=6)
        self.input_account = tkinter.Entry(self.root, width=25)
        self.label_password = tkinter.Label(self.root, text='密码：', width=6)
        self.input_password = tkinter.Entry(self.root, width=25, show='*')
        self.login_button = tkinter.Button(self.root, command=self.backstage_interface, text='登录', width=11, height=1)
        self.siginUp_button = tkinter.Button(self.root, command=self.Changepassword, text='修改密码', width=11, height=1)
        self.com = ttk.Combobox(self.root, width=10)    # 下拉列表
    def gui_arrang(self):
        self.label_account.place(x=110, y=44)
        self.input_account.place(x=170, y=40, height=30)
        self.label_password.place(x=110, y=85)
        self.input_password.place(x=170, y=80, height=30)
        self.login_button.place(x=80, y=140)
        self.siginUp_button.place(x=320, y=140)
        self.com.place(x=380, y=68)
        self.com['value'] = ('root', 'teacher', 'student')   # 控制权限
        # self.com.current(0)
    # 密码修改
    def Changepassword(self):
       C = CheckPasswd()


    # 登录验证
    def backstage_interface(self):

        # ljust()方法返回一个原字符串左对齐, 并使用空格填充至指定长度的新字符串。如果指定的长度小于原字符串的长度则返回原字符串。
        # width -- 指定字符串长度。
        # fillchar -- 填充字符，默认为空格。
        account = self.input_account.get()
        password = self.input_password.get()
        permission = self.com.get()
    
        '''
                    messagebox：
                    showinfo(title='Hi', message='正常文本')            # 提示信息对话窗
                    showwarning(title='Hi', message='有警告！')         # 提出警告对话窗
                    showerror(title='Hi', message='出错了！')           # 提出错误对话窗
                    askquestion(title='Hi', message='你好！')           # 询问选择对话窗return 'yes', 'no'
                    askyesno(title='Hi', message='你好！')              # return 'True', 'False'
                    askokcancel(title='Hi', message='你好！')           # return 'True', 'False'
                '''
        db = pymysql.connect('127.0.0.1', 'root', 'adminwj', 'studentsystem')
        cursor = db.cursor()
        if account and password and permission:
            # try:
                sql = 'select * from zc where name = "%s" and passwd = "%s" and permission = "%s";' % (account, password, permission)
                res = cursor.execute(sql)
                if res:
                    # 后期使用多线程先启动登录界面，验证通过后接受登录线程启动zjm线程
                    # tkinter.messagebox.showinfo(title="登录", message="登录成功！")
                    os.popen('taskkill.exe /pid:' + str(os.getpid()))   # 使用os模块获取当前进程号，使用os.popen强行关掉该进程
                    sys = Sys()
                else:
                    tkinter.messagebox.showinfo(title='登录失败', message="账号、密码或权限错误！")
                    self.input_account.delete(0, tkinter.END)
                    self.input_password.delete(0, tkinter.END)
            # except:
                cursor.close()

            # finally:
                db.close()
        else:
            tkinter.messagebox.showinfo(title="登录", message="请输入用户名和密码并且选择你的职务")










def main():
    # 初始化对象
    L = Login()
    # 进行布局
    L.gui_arrang()
    # 主程序执行
    tkinter.mainloop()
if __name__ == '__main__':
    main()