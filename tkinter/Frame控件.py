import tkinter

# 创建主窗口
win = tkinter.Tk()		# T是大写k是小写
win.title("窗口标题")

win.geometry("400x200")


'''
框架控件
在屏幕上显示一个矩形区域，多作为容器控件
'''

# 创建底层frame
frm = tkinter.Frame(win)
frm.pack()


# left
# 在底层Frame上创建leftFrame
frm_l = tkinter.Frame(frm)
# frm_l = tkinter.Frame(win)    # 在win上创建
tkinter.Label(frm_l, text='左上', bg='red').pack(side=tkinter.TOP)
tkinter.Label(frm_l, text='左下', bg='yellow').pack(side=tkinter.TOP)
frm_l.pack(side=tkinter.LEFT)


# right
# frm_r = tkinter.Frame(win)   # 在win上创建
frm_r = tkinter.Frame(frm)
tkinter.Label(frm_r, text='右上', bg='pink').pack(side=tkinter.TOP)
tkinter.Label(frm_r, text='右下', bg='blue').pack(side=tkinter.TOP)
frm_r.pack(side=tkinter.RIGHT)
win.mainloop()