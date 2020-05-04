import tkinter

# 创建主窗口
win = tkinter.Tk()		# T是大写k是小写
win.title("窗口标题")

win.geometry("400x200")


'''
提供用户通过拖拽指示器改变变量的值，可以水平，也可以竖直
HORIZONTAL：水平
VERTTCAL：竖直
length：水平时表示宽度，竖直时表示高度
tickinterval：选择值将会为该值的倍数
'''
scale1 = tkinter.Scale(win, from_=0, to=100, orient=tkinter.HORIZONTAL, tickinterval=10,
	length=200)
scale1.pack()

# 获取值
# print(scale1.get())
def showNum():
	print(scale1.get())
tkinter.Button(win,text='按钮', command=showNum).pack()


# 设置初始值
scale1.set(20)


win.mainloop()