import tkinter

# 创建主窗口
win = tkinter.Tk()		# T是大写k是小写
win.title("窗口标题")

# win.geometry("400x200")
'''
文本控件，用于显示多行文本的
height：显示的行数
'''
# 创建滚动条
scroll = tkinter.Scrollbar()
text = tkinter.Text(win, width=40, height=20)
# 显示滚动条
# side：放到父窗体的哪一侧
# fill：填充空间
# 参数：
# x、y、both、none
scroll.pack(side=tkinter.RIGHT, fill=tkinter.Y)
text.pack(side=tkinter.LEFT,fill=tkinter.Y)

# 管理text和scroll（滚动条）
scroll.config(command=text.yview)		# scroll关联text，yview，y轴适配，x轴的话就是xview
text.config(yscrollcommand=scroll.set)	# text关联滚动条
str = '''I stand here today humbled by the task before us, grateful for the trust you have bestowed, mindful of the sacrifices borne by our ancestors. I thank President Bush for his service to our nation, as well as the generosity and cooperation he has shown throughout this transition.
Forty-four Americans have now taken the presidential oath. The words have been spoken during rising tides of prosperity and the still waters of peace. Yet, every so often the oath is taken amidst gathering clouds and raging storms. At these moments, America has carried on not simply because of the skill or vision of those in high office, but because we the people have remained faithful to the ideals of our forebears, and true to our founding documents.
That we are in the midst of crisis is now well understood. Our nation is at war, against a far-reaching network of violence and hatred. Our economy is badly weakened, a consequence of greed and irresponsibility on the part of some, but also our collective failure to make hard choices and prepare the nation for a new age. Homes have been lost; jobs shed; businesses shuttered. Our health care is too costly; our schools fail too many; and each day brings further evidence that the ways we use energy strengthen our adversaries and threaten our planet.
These are the indicators of crisis, subject to data and statistics. Less measurable but no less profound is a sapping of confidence across our land — a nagging fear that America's decline is inevitable, and that the next generation must lower its sights.
In reaffirming the greatness of our nation, we understand that greatness is never a given. It must be earned. Our journey has never been one of shortcuts or settling for less. It has not been the path for the faint-hearted — for those who prefer leisure over work, or seek only the pleasures of riches and fame. Rather, it has been the risk-takers, the doers, the makers of things — some celebrated but more often men and women obscure in their labor, who have carried us up the long, rugged path towards prosperity and freedom.
In reaffirming the greatness of our nation, we understand that greatness is never a given. It must be earned. Our journey has never been one of shortcuts or settling for less. It has not been the path for the faint-hearted — for those who prefer leisure over work, or seek only the pleasures of riches and fame. Rather, it has been the risk-takers, the doers, the makers of things — some celebrated but more often men and women obscure in their labor, who have carried us up the long, rugged path towards prosperity and freedom.
In reaffirming the greatness of our nation, we understand that greatness is never a given. It must be earned. Our journey has never been one of shortcuts or settling for less. It has not been the path for the faint-hearted — for those who prefer leisure over work, or seek only the pleasures of riches and fame. Rather, it has been the risk-takers, the doers, the makers of things — some celebrated but more often men and women obscure in their labor, who have carried us up the long, rugged path towards prosperity and freedom.
In reaffirming the greatness of our nation, we understand that greatness is never a given. It must be earned. Our journey has never been one of shortcuts or settling for less. It has not been the path for the faint-hearted — for those who prefer leisure over work, or seek only the pleasures of riches and fame. Rather, it has been the risk-takers, the doers, the makers of things — some celebrated but more often men and women obscure in their labor, who have carried us up the long, rugged path towards prosperity and freedom.
'''
# 将上面的字符串插入到text控件中
text.insert(tkinter.INSERT,str)

win.mainloop()