'''单继承的实现'''
class Person(object):
    def __init__(self, name, age, money):
        self.name = name
        self.age = age
        self.__money = money

    def setMoney(self, money):
        if money < 0:
            money = 0
        self.__money = money

    def getMoney(self):
    	return self.__money

    def run(self):
        print("run")

    def eat(self, food):
        print("eat" + food)

class Shutdent(Person):
 	def __init__(self, name, age, money, stuId):
 		#  调用父类中的__init__
 		super(Shutdent, self).__init__(name, age, money)
 		self.stuId = stuId
 		#  访问父类的私有属性,会报错
 		# def stuFunc(self):
 		# 	print(self.__money)



class Woker(Person):
	def __init__(self, name, age, money):
 		#  调用父类中的__init__
 		super(Woker, self).__init__(name, age, money)
		
stu = Shutdent("tom", 21, 1212, 100)
print("钱",stu.getMoney())
print(stu.name, stu.age)
# stu.run()
print(stu.stuId)
# stu.stuFunc()



