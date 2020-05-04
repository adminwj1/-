import tkinter

# 创建主窗口
win = tkinter.Tk()		# T是大写k是小写
win.title("窗口标题")

win.geometry("400x200")

'''
<ButtonRelease-1>	释放鼠标左键
<ButtonRelease-3>	释放鼠标右键
<ButtonRelease-2>	释放鼠标中键
'''
label = tkinter.Label(win, text='sunck is a good man', bg='red')
label.pack()
def fun(event):
    print(event.x, event.y)
label.bind("<ButtonRelease-1>",fun)

win.mainloop()