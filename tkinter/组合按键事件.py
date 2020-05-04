import tkinter

# 创建主窗口
win = tkinter.Tk()		# T是大写k是小写
win.title("窗口标题")

win.geometry("400x200")

'''
<Shift-Up>：组合事件
'''
# label = tkinter.Label(win, text='sunck is a good man', bg='red')
# 设置焦点
win.focus_set()
# label.pack()
def fun(event):
    # 显示被触发的哪个键
    print('event.char = ', event.char)
    # 显示触发的那个键的ASSIC码
    print('event.keycode = ', event.keycode)
win.bind("<Shift-Up>",fun)

win.mainloop()