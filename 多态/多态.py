# from cat import Cat
# from mouse import Mouse
from  animal import Animal
from person import Person
'''在动物类中创建了tom和Jerry两个动物'''
tom = Animal("tom")
jerry = Animal("jerry")
'''
tom.eat()
jerry.eat()
'''
'''
多态流程：
两只动物单独吃
将两个动物放在一个类中，进行吃
有个人来喂这两只动物时，只需要调用动物类就可以

'''
#   思考：再添加100中动物，也都有name和eat方法
#   定义了一个有name属性和eat方法的Animal类，让所有的动物类都继承自Animal
#   定义一个人类，可以喂猫和老鼠吃东西

'''创建了一个人来喂动物'''
per = Person()
# per.feedCat(tom)
# per.feedMouse(jerry)
per.feedAnimal(tom)