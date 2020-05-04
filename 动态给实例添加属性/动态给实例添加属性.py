from types import MethodType
#  创建一个空类
class Person(object):
    def __init__(self, age):
        self.age = age
    # __slots__ = ("name",  "spak") #  ("属性1", "属性2", ..., "属性n")，这里是元组，添加的是能设置的属性。如果动态添加元组里面没有的属性，程序会直接报错
    #  方法名为受限制的变量去掉双下划线
    #  @property
    @property
    def age(self):
        return self.__age
    @age.setter #  去掉下划线.setter
    def age(self,age):
        if age < 0:
            age = 0
            self.age = age
        self.__age = age

#  @property
per = Person(-100)   #  相当于调用setAge
print(per.age)  #  相当于调用getAge


'''
per = Person()
#  动态添加属性，这体现了动态语言的特点（灵活）
per.name = "tom"
print(per.name)

#  动态添加方法
# def say(self):
#     print("my name is " + self.name)
# per.speak = say
# per.speak(per)
def say(self):
  print("my name is " + self.name)
per.spak = MethodType(say, per)
per.spak()
'''
'''
思考：如果我们想要限制实例的属性怎么办？
比如，只允许给对象添加name，age，height，weight属性
解决：定义类的时候，定义一个特殊的属性(__slots__)，可以限制动态添加的属性
'''
'''
class Person(object):
    __slots__ = ("name", "age") #  ("属性1", "属性2", ..., "属性n")，这里是元组，添加的是能设置的属性。如果动态添加元组里面没有的属性，程序会直接报错
'''
# per.height = 170
# print(per.height) #  这里报错
#


