from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import pymysql
class Update(object):
    def __init__(self):
        # 模块去区
        self.root = Tk()
        self.root.title('学生管理系统')
        self.root.geometry("800x500")
        self.root.resizable(width=False, height=False)
        # 第一行数据
        self.id = Label(self.root, text='学号：')
        self.input_id = Entry(self.root, width=12)
        self.name = Label(self.root, text='姓名：')
        self.input_name = Entry(self.root, width=12)
        self.gender = Label(self.root, text='性别：')
        self.gender_a = ttk.Combobox(self.root, width=5)
        self.gender_a['value'] = ('男', '女')
        self.gender_a.current('0')
        self.age = Label(self.root, text='年龄：')
        self.input_age = Entry(self.root, width=12)
        # 第二行数据
        self.cardid = Label(self.root, text='身份证：')
        self.input_cardid = Entry(self.root, width=12)
        self.date = Label(self.root, text='出生日期：')
        self.input_date = Entry(self.root, width=12)
        self.address = Label(self.root, text='地址：')
        self.input_address = Entry(self.root, width=12)
        self.department = Label(self.root, text='系部：')
        self.input_department = Entry(self.root, width=12)
        # 第三行数据
        self.major = Label(self.root, text='专业：')
        self.input_major = Entry(self.root, width=12)
        self.Class = Label(self.root, text='班级：')
        self.input_Class = Entry(self.root, width=12)
        self.phone = Label(self.root, text='手机号：')
        self.input_phone = Entry(self.root, width=12)
        self.mail = Label(self.root, text='邮箱：')
        self.input_mail = Entry(self.root, width=12)
        self.QQ = Label(self.root, text='QQ号：')
        self.input_QQ = Entry(self.root, width=12)
        self.add = Button(self.root, text='修改', width=20, command=self.SQL)

        # 布局去
        # 第一行布局
        self.id.place(x=10, y=14)
        self.input_id.place(x=50, y=14)
        self.name.place(x=200, y=14)
        self.input_name.place(x=250, y=14)
        self.gender.place(x=400, y=14)
        self.gender_a.place(x=448, y=14)
        self.age.place(x=580, y=14)
        self.input_age.place(x=630, y=14)

        # 第二行布局
        self.cardid.place(x=10, y=100)
        self.input_cardid.place(x=60, y=100)
        self.date.place(x=200, y=100)
        self.input_date.place(x=270, y=100)
        self.address.place(x=400, y=100)
        self.input_address.place(x=450, y=100)
        self.department.place(x=580, y=100)
        self.input_department.place(x=630, y=100)

        # 第三行布局
        self.major.place(x=10, y=200)
        self.input_major.place(x=50, y=200)
        self.Class.place(x=200, y=200)
        self.input_Class.place(x=270, y=200)
        self.phone.place(x=400, y=200)
        self.input_phone.place(x=450, y=200)
        self.mail.place(x=580, y=200)
        self.input_mail.place(x=630, y=200)
        self.QQ.place(x=10, y=300)
        self.input_QQ.place(x=60, y=300)
        self.add.place(x=580, y=300, height=50)
        self.root.mainloop()

    # 连接数据库

    def SQL(self):
        # id = self.input_id.get()
        # name = self.input_name.get()
        # gender = self.gender_a.get()
        # age = self.input_age.get()
        # cardid = self.input_cardid.get()
        # date = self.input_date.get()
        # address = self.input_address.get()
        # department = self.input_department.get()
        # major = self.input_major.get()
        # Class = self.input_Class.get()
        # phone = self.input_phone.get()
        # mail = self.input_mail.get()
        # QQ = self.input_QQ.get()
        db = pymysql.connect('127.0.0.1', 'root', 'adminwj', 'studentsystem')
        cursor = db.cursor()
        try:
            sql = "select * from info where id = " + self.input_id.get()
            cursor.execute(sql)
            db.commit()  # 提交事务
            reslist = cursor.fetchall()
            if reslist:
                sql_a = "update info set name = '%s',gender = '%s',age = '%s', cardid = '%s', date = '%s', address = '%s', department = '%s', major = '%s', class = '%s', phone = '%s', mail = '%s', QQ = '%s' where id = '%s'" % \
                        (self.input_name.get(), self.gender_a.get(), self.input_age.get(), self.input_cardid.get(),
                         self.input_date.get(), self.input_date.get(), self.input_department.get(),
                         self.input_major.get(), self.input_Class, self.input_phone.get(), self.input_mail.get(),
                         self.input_QQ.get(), self.input_id.get())
                cursor.execute(sql_a)
                db.commit()
                messagebox.showinfo(title='修改', message='修加成功！')
            else:
                messagebox.showinfo(title='修改', message='未查询到数据！')
        except:
            db.rollback()
            cursor.close()
            messagebox.showinfo(title='添加', message='添加失败！')
        finally:
            db.close()





def main():
    U = Update()
    U.SQL()




if __name__ == '__main__':
    main()