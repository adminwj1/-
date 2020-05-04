from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import pymysql
class CheckPasswd(object):
    def __init__(self):
        self.root = Tk()
        self.root.title('学生信息系统-登录模块')
        self.root['width'] = 500
        self.root['height'] = 200
        self.root.resizable(width=False, height=False)
        self.label_account = Label(self.root, text='用户名：', font=('微软雅黑',11))
        self.input_account = Entry(self.root, width=25)
        self.label_password = Label(self.root, text='密码：', font=('微软雅黑',11))
        self.input_password = Entry(self.root, width=25, show='*')
        self.check_button = Button(self.root, text='修改密码', width=11, height=1, command=self.Check)
        self.com = ttk.Combobox(self.root, width=10)
        self.label_account.place(x=110, y=44)
        self.input_account.place(x=170, y=40, height=30)
        self.label_password.place(x=110, y=85)
        self.input_password.place(x=170, y=80, height=30)
        self.check_button.place(x=210, y=140)
        self.com.place(x=380, y=68)
        self.com['value'] = ('root', 'teacher', 'student')  # 控制权限
        self.com.current(0)
        self.root.mainloop()




        # 修改密码
    def Check(self):
        #
        # 验证用户是否存在--成功-->修改密码
        #              --失败-->弹出提示框“未查询到该用户信息”
        name = self.input_account.get()
        passwd = self.input_password.get()
        permission = self.com.get()
        db = pymysql.connect('127.0.0.1', 'root', 'adminwj', 'studentsystem')
        cursor = db.cursor()
        try:
            sql = 'select * from zc where name = "%s" and permission = "%s"' % (name, permission)
            res = cursor.execute(sql)   # 返回值为1、0
            db.commit()  # 提交事务
                # print(res)    # 验证返回值
            # print(type(res))
            if res:
                sql_a = 'update zc set passwd = "%s"' % (passwd)
                cursor.execute(sql_a)
                db.commit()  # 提交事务
                messagebox.showinfo(title='修改密码', message='修改密码成功！')
            else:
                messagebox.showinfo(title='修改密码', message='未查询到该用户信息！')
        except:
            db.rollback()
            cursor.close()
            messagebox.showinfo(title='修改密码', message='修改密码失败！')
        finally:
            db.close()



if __name__ == '__main__':
    CP = CheckPasswd()