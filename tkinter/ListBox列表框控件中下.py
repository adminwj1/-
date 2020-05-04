import tkinter

# 创建主窗口
win = tkinter.Tk()		# T是大写k是小写
win.title("窗口标题")

win.geometry("400x200")
# EXTENDED 可以是listbox支持shift和Ctrl
lb = tkinter.Listbox(win, selectmode=tkinter.EXTENDED)

for item in ["good", "nice", "handsome", "very good", "very nice","good1", "nice1", "handsome1", "very good1", "very nice1","good2", "nice2", "handsome2", "very good2", "very nice2"]:
	lb.insert(tkinter.END,item)

# 创建滚动条
sc = tkinter.Scrollbar(win)
sc.pack(side=tkinter.RIGHT,fill=tkinter.Y)
lb.configure(yscrollcommand=sc.set)
lb.pack(side=tkinter.LEFT,fill=tkinter.BOTH)
# 额外给属性赋值
sc['command'] = lb.yview
win.mainloop()