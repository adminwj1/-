from tkinter import *
import pymysql
class Select(object):
    def __init__(self):
        self.root = Tk()
        self.root.title('学生管理系统__查询模块')
        self.root.geometry("700x400")
        self.root.resizable(width=False, height=False)
        self.label = Label(self.root, text='学号：', width=10, font=('微软雅黑,10'))
        self.Entry = Entry(self.root, width=20, font=('微软雅黑,'))
        self.button = Button(self.root, text='查询', command=self.Sel, width=10)
        self.Entry_a = Entry(self.root, width=80)

        self.button_1 = Button(self.root, text='清空', width=10, command=self.lefClike)
        self.label.place(x=130, y=40)
        self.Entry.place(x=220, y=42)
        self.button.place(x=500, y=41)
        self.Entry_a.place(x=75, y=90, height=100)
        self.button_1.place(x=300, y=200)
        # 显示滚动条
        # self.scroll.pack(side=BOTTOM, fill=Y)
        self.root.mainloop()

    def lefClike(self):
        self.Entry_a.delete(0, END)     # 删除Entry_a中的数据

    def Sel(self):
        account = self.Entry.get()
        db = pymysql.connect('127.0.0.1', 'root', 'adminwj', 'studentsystem')
        cursor = db.cursor()
        try:
            sql = 'select * from info where id = ' + account
            cursor.execute(sql)
            db.commit()
            reslist = cursor.fetchall()
            if reslist:
                for reo in reslist:
                    a = ('学号：', reo[0], '姓名：', reo[1], '性别：', reo[2], '年龄：', reo[3], '省份证：', reo[4], '出生年月：', reo[5],
                              '住址：', reo[6], '系部：', reo[7], '专业：', reo[8], '班级：', reo[9], '手机号：', reo[10], '邮箱：', reo[11],
                              'QQ：', reo[12])
                    # content = StringVar()
                    # e = self.Entry_a(textvariable=content,state=DISABLED)
                    self.Entry_a.insert(0, a)   # 想Entry_a中插入从数据库匹配的数据
                    self.Entry.delete(0, END)  # 删除Entry_a中的数据
            else:
                self.Entry_a.insert(0, '未查询到数据')
                self.Entry.delete(0, END)  # 删除Entry_a中的数据
        except:
            db.rollback()
            cursor.close()
            db.close()