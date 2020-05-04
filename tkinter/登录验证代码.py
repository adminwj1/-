# 这是系统的登录界面
import tkinter
from tkinter import messagebox


class Login(object):
    def __init__(self):
        # 创建主窗口,用于容纳其它组件
        self.root = tkinter.Tk()
        # 给主窗口设置标题内容
        self.root.title("测试系统")
        self.root.geometry('700x400')
        # 运行代码时记得添加一个gif图片文件，不然是会出错的
        self.canvas = tkinter.Canvas(self.root, height=400, width=700)  # 创建画布
        # self.image_file = tkinter.PhotoImage(file="test.gif")  # 加载图片文件
        # self.image = self.canvas.create_image(0, 0, anchor='nw', image=self.image_file)  # 将图片置于画布上
        self.canvas.pack(side='top')  # 放置画布（为上端）

        # 创建一个`label`名为`账户: `
        self.label_account = tkinter.Label(self.root, text='账户: ')
        # 创建一个`label`名为`密码: `
        self.label_password = tkinter.Label(self.root, text='密码: ')

        # 创建一个账号输入框,并设置尺寸
        self.input_account = tkinter.Entry(self.root, width=30)
        # 创建一个密码输入框,并设置尺寸
        self.input_password = tkinter.Entry(self.root, show='*', width=30)

        # 创建一个登录系统的按钮
        self.login_button = tkinter.Button(self.root, command=self.backstage_interface, text="登录", width=10)
        # 创建一个注册系统的按钮
        self.siginUp_button = tkinter.Button(self.root, command=self.siginUp_interface, text="注册", width=10)

    # 完成布局
    def gui_arrang(self):
        self.label_account.place(x=60, y=50)
        self.label_password.place(x=60, y=75)
        self.input_account.place(x=110, y=50)
        self.input_password.place(x=110, y=75)
        self.login_button.place(x=125, y=100)
        self.siginUp_button.place(x=220, y=100)

    # 进入注册界面
    def siginUp_interface(self):
        # self.root.destroy()
        tkinter.messagebox.showinfo(title='测试系统', message='进入注册界面')

    # 这里没有写具体逻辑，这里一般应用是链接一个数据库，插入用户信息，留做发散思维

    # 进行登录信息验证
    def backstage_interface(self):
        # account = self.input_account.get().ljust(10, " ")
        # password = self.input_password.get().ljust(10, " ")
        account = self.input_account.get().ljust(10)
        password = self.input_password.get().ljust(10)
        # 获取录入的账号以及密码
        '''
            showinfo(title='Hi', message='正常文本')            # 提示信息对话窗
            showwarning(title='Hi', message='有警告！')         # 提出警告对话窗
            showerror(title='Hi', message='出错了！')           # 提出错误对话窗
            askquestion(title='Hi', message='你好！')           # 询问选择对话窗return 'yes', 'no'
            askyesno(title='Hi', message='你好！')              # return 'True', 'False'
            askokcancel(title='Hi', message='你好！')           # return 'True', 'False'
        '''
        tkinter.messagebox.showinfo(title='测试系统', message='录入账户:{}\n密码：{}\n登录成功！'.format(account, password))
    # 这里没有写验证逻辑，读者可以发散思维，自己增加验证逻辑，例如自己设置一个固定的密码，然后判断；也可以读取数据库内容，做出各种判断


def main():
    # 初始化对象
    L = Login()
    # 进行布局
    L.gui_arrang()
    # 主程序执行
    tkinter.mainloop()


if __name__ == '__main__':
    main()

