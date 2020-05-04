import tkinter

# 创建主窗口
win = tkinter.Tk()		# T是大写k是小写
win.title("窗口标题")

win.geometry("400x200")

# 创建菜单条
menubar = tkinter.Menu(win) 
win.config(menu=menubar)	# 显示在主界面的顶部
def func():
	print("*********")
	print(v.get())
# 创建菜单选项
# 绑定变量获取值
v = tkinter.StringVar()
menu1 = tkinter.Menu(menubar, tearoff=False)
for item in ['Python', 'C', 'C++', 'shell', 'C#', 'PHP', 'Java', 'Swift']:
	menu1.add_command(label=item, command=func)
	# 添加分割线
	menu1.add_separator()

menu2 = tkinter.Menu(menubar, tearoff=False)
for item2 in ['red', 'blue']:
	menu2.add_command(label=item2)
# 显示在菜单条上
menubar.add_cascade(label='语言', menu=menu1)
menubar.add_cascade(label='颜色', menu=menu2)
win.mainloop()



