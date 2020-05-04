import tkinter

# 创建主窗口
win = tkinter.Tk()		# T是大写k是小写
win.title("窗口标题")

win.geometry("400x200")
def updata():
	print(v.get())

'''
数值范围控件
increment：步长，默认为1
values 最好不要与from_与to和increment同时使用，因为：显示的内容就是values里面的值
values=(0,2,4,6,8)
command：实时获取改变的值
'''
# 绑定变量
v = tkinter.StringVar()
sp = tkinter.Spinbox(win, from_=0, to=100, increment=5, textvariable=v, command=updata)
sp.pack()

# 设置值(必须要绑定变量才能赋值和取值)
v.set(20)
# 取值
print(v.get())

win.mainloop()