import tkinter

# 创建主窗口
win = tkinter.Tk()		# T是大写k是小写
win.title("窗口标题")

win.geometry("400x200")
def updata():
	# 判断是否选中
	message = ""
	if hobby1.get() == True:	# 返回的是True或Falsh
		message += "money\n"
	if hobby2.get() == True:
		message += "power\n"	
	if hobby3.get() == True:
		message += "people\n"
	# 清除text中的所有内容
	# 0.0：下标为0的第0行
	# END：清空到最后，如果写1的话就是清空到下标为0的第一行
	text.delete(0.0, tkinter.END)
	text.insert(tkinter.INSERT, message)
# 将选中的内容显示出来，使用绑定变量
# 声明一个变量类型为Boole类型
hobby1 = tkinter.BooleanVar()
hobby2 = tkinter.BooleanVar()
hobby3 = tkinter.BooleanVar()

# 创建checkButton
# variable：绑定一个hobby1的布尔值变量
check1 = tkinter.Checkbutton(win, text="money", variable=hobby1, command=updata)
check1.pack()
check2 = tkinter.Checkbutton(win, text="power", variable=hobby2, command=updata)
check2.pack()
check3 = tkinter.Checkbutton(win, text="people",variable=hobby3, command=updata)
check3.pack()


# 将复选框选中的内容显示到text中
text = tkinter.Text(win, width=50, height=5)
text.pack()
win.mainloop()