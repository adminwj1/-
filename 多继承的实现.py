#  创建一个父亲类
class Father(object):
    def __init__(self, money):
        self.money = money

    def play(self):
        print("play")

    def func(self):
        print("func1")
#  创建一个母亲类
class Mother(object):
    def __init__(self, faceValue):
        self.faceValue = faceValue

    def play(self):
        print("play")

    def eat(self):
        print("eat")

    def func(self):
        print("func2")


class Child(Father, Mother): #  子类中Father在前面，Mother在后面
    def __init__(self, money, faceValue):
        Father.__init__(self, money)
        Mother.__init__(self, faceValue )


c = Child(1000, 100)
print(c.money, c.faceValue)
c.play()
c.eat()
#  注意：父类中方法名相同，默认调用的是在括号中排前面的父类中的方法。在class Child(Father, Mother): 类中Father在前面，Mother在后面所以func输出结果为func1
c.func()
