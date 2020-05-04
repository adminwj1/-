import tkinter

# 创建主窗口
win = tkinter.Tk()		# T是大写k是小写
win.title("窗口标题")

win.geometry("400x200")

def updata():
	print(r.get())

#绑定一个整形变量，一组单选框要绑定同一个变量
r = tkinter.IntVar()
r = set(1)	# 设置默认选项
#绑定一个字符串形变量
# r = tkinter.StringVar() # 这里使用StringVar会出现默认两个单选框都被选中
radio1 = tkinter.Radiobutton(win, text="one", value=1,variable=r,
command=updata, )		# text="one"：rado1显示的名称，value=1：被点击后输出的值

radio1.pack()

radio2 = tkinter.Radiobutton(win, text="two", value=2,variable=r,
command=updata)		# text="one"：rado1显示的名称，value=1：被点击后输出的值

radio2.pack()

win.mainloop()