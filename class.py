#  类的基本学习
'''创建类'''

class Persion(object):
    # 定义属性（定义变量）
    # name = ""
    # age = 0
    # height = 0
    # weight = 0

    # 定义方法（定义函数）
    # 注意：方法的参数必须以self当第一个参数
    def run(self):
        # self代表类的实例（某个对象）
        print("run")
        
    def eat(self, food):
        print("I eat a " + food)

    # 构造函数
    def __init__(self, name, age, heght, weight, money):
        '''
        __init__相当于定义属性
        self当前对象'''
        self.name = name
        self.age = age
        self._height = heght
        self.weight = weight
        self.__money = money

    # 使用内部方法对私属性进去赋值
    def setMoney(self, money):
        if money < 0:
            money = 0
        self.__money = money

    # 使用内部方法对私有属性进行取值
    def getMoney(self):
        return self.__money
    # 析构函数
    # def __del__(self):
    #     print("这是一个析构函数")

    def say(self):
        print("Hello! my name is %s, I am %d years old" %
              (self.name, self.age))
    def openDoor(self):
        print("我已经打开了冰箱门")
    def fillEle(self):
        print("我已经把大象装进冰箱了")
    def closeDoor(self):
        print("我已经关掉了冰箱门")

    # 从写函数__str__()
    # def __str__(self):
    #     return "%s %d %d %d" %(self.name, self.age, self.weight, self.height)
    # # __repr__()
    # def __repr__(self):
    #     return "%s %d %d %d" %(self.name, self.age, self.weight, self.height)
'''使用类实例化对象'''
# 实例化对象

# pre1 = Persion()
# print(pre1)
# print(type(pre1))
'''
pre2 = Persion()
# print(pre2)
# print(type(pre2))
'''
'''访问对象的属性和方法'''
# 访问属性
'''
pre1.name = "tom"
pre1.age = 18
pre1.height = 160
pre1.weight = 80
print(pre1.name, pre1.age, pre1.height, pre1.weight)

# 访问方法
pre1.openDoor()
pre1.fillEle()
pre1.closeDoor()

# 传参数到方法中
pre1.eat("apple")
'''

'''构造函数'''
# __init__()
# pre1 = Persion("hanmeimei", 21, 170, 55)
# print(pre1.name, pre1.age, pre1.height, pre1.weight)
# pre2 = Persion("xiaolong", 22, 175, 70)
# print(pre2.name, pre2.age, pre2.height, pre2.weight)


'''self'''
'''
self代表类的实例，而非类
哪个对象调用方法，那么该方法中的self就代表那个对象
self.__class__ 代表类名
'''
# pre1 = Persion("tom", 20, 160, 80)
# pre1.say()
# pre2 = Persion("hanmeimei", 20, 160, 70)
# pre2.say()
#
'''重写函数'''
# 1、__str__()
# 比如我想答印Persion中的__init__()方法中的属性可以使用两种方法，第一种以前使用的
# print，第二种就是__str__()
# def __str__(self):
#     return "%s %d %d %d" % (self.name, self.age, self.weight, self.height)
# per = Persion("hanmeimei", 21, 55, 160, 100000)
# print(per)

'''访问限制'''
# per = Persion("hanmeimei", 21, 55, 160, 100000)
# print(per.name, per.age, per.weight, per.height, per.__money)

# 使用内部方法给私有属性赋值
per = Persion(1000)
per.setMoney(-100)
print(per.setMoney())
# print(per._height)
#
