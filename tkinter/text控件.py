import tkinter

# 创建主窗口
win = tkinter.Tk()		# T是大写k是小写
win.title("窗口标题")

win.geometry("400x200")
'''
文本控件，用于显示多行文本的
height：显示的行数
'''

text = tkinter.Text(win, width=30, height=4)
text.pack()
str = ";jfglrjtoirjogdflkgjfdlfjgldfnglndmdlkjgoperjgdfmgkldfmgpoerjglkgnkdjgpwekprw[etjwpmvsd;kf;skfsdfl;mfg;lfrgkrkgrle;mgl;trmg;rmglekrmgl;refmglkrtmrl;wemglekrmrl;ergmhekgtrl;mtl;hmrtl;t,';lh,mrl;rlt;mg;rlg'rttmhrte'wtglker;tkrgt'rtlek[tkt[perltl[5"
# 将上面的字符串插入到text控件中
text.insert(tkinter.INSERT,str)

win.mainloop()