import tkinter

# 创建主窗口
win = tkinter.Tk()		# T是大写k是小写
win.title("窗口标题")

win.geometry("400x200")

# 绑定变量
lbv = tkinter.StringVar()

# 与BORWS相似，但是不支持鼠标按下后移动选中位置
lb = tkinter.Listbox(win, selectmode=tkinter.SINGLE, variable=lbv)

lb.pack()
for item in ["good", "nice", "handsome", "very good", "very nice"]:
	# 按顺序添加
	lb.insert(tkinter.END, item)
# 在开始添加（从第一位置添加）
lb.insert(tkinter.ACTIVE, "cool")


# 打印当前列表中的选项
print(lbv.get())



# 设置选项
# lbv.set(("1","2","3"))


def myPrint(abc):		# abc表示：事件参数，不需要传值
	print(lb.get(lb.curselection()))

# 绑定事件
'''
Double：双击
Button：按钮
1：鼠标左键
'''
lb.bind("<Double-Button-1>", myPrint)
win.mainloop()