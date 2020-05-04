import tkinter

# 创建主窗口
win = tkinter.Tk()		# T是大写k是小写
win.title("窗口标题")

win.geometry("400x200")

'''
<Shift_L>：响应左shift键
<Shift_R>：响应右shift键
<F5>：响应F5
<Return>：回车键
<BackSpace>：退格按键
'''
label = tkinter.Label(win, text='sunck is a good man', bg='red')
# 设置焦点
label.focus_set()
label.pack()
def fun(event):
    # 显示被触发的哪个键
    print('event.char = ', event.char)
    # 显示触发的那个键的ASSIC码
    print('event.keycode = ', event.keycode)
label.bind("<Shift_L>",fun)

win.mainloop()