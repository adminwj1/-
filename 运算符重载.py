class Person(object):
    def __init__(self, num):
        self.num = num
    #  运算符重载
    def __add__(self, other):
        #  self相当于per1，other相当如per2
        return Person(self.num + other.num)
    def __str__(self):
        return "num = " + str(self.num)


per1 = Person(1)
per2 = Person(2)
print(per1 + per2)  #  相当于：print(per1.__add__(per2))
print(per1)
print(per2)