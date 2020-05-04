import tkinter

# 创建主窗口
win = tkinter.Tk()		# T是大写k是小写
win.title("窗口标题")

win.geometry("400x200")

# MULTIPLE支持多选
lb = tkinter.Listbox(win, selectmode=tkinter.MULTIPLE)
lb.pack()
for item in ["good", "nice", "handsome", "very good", "very nice","good1", "nice1", "handsome1", "very good1", "very nice1","good2", "nice2", "handsome2", "very good2", "very nice2"]:
	lb.insert(tkinter.END,item)




win.mainloop()