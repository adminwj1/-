import tkinter

# 创建主窗口
win = tkinter.Tk()		# T是大写k是小写
win.title("窗口标题")

win.geometry("400x200")
'''
输入控件
用于显示简单的文本内容
show：输入文本显示方式
textvariable：绑定变量
'''
# 绑定变量（获取输入框的值）
e = tkinter.Variable()
entry = tkinter.Entry(win,textvariable=e).pack()
# e就代表输入这个对象
# 给输入框设置值（想输入框写入内容）
e.set("sunck is a good man")

# 获取值
print(e.get())

win.mainloop()