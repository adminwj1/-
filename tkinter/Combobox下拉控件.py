import tkinter
from tkinter import ttk
# 创建主窗口
win = tkinter.Tk()		# T是大写k是小写
win.title("窗口标题")

win.geometry("400x200")


# 创建下拉列表
# 绑定变量
cv = tkinter.StringVar()

com = ttk.Combobox(win, textvariable=cv)
com.pack()

# 设置下拉数据
com['value'] = ('黑龙江', '吉林', '辽宁')


# 设置默认值
com.current(0)




# 绑定事件
def func(event):
    print(com.get())
    print("sunck is a good man")
    print(cv.get())
com.bind("<<ComboboxSelected>>", func)
win.mainloop()