#  老鼠类
from animal import Animal
class Mouse(Animal):
    def __init__(self, name):
        self.name = name
    def eat(self):
        print(self.name + "吃")