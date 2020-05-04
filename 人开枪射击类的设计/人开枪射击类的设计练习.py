# 引入类
from person import Passions
from gun import gun
from bulletBox import BulletBox
'''
人
类名：passions
属性：gun
行为：fire

枪
类名：Gun
属性：bulletBox
行为：shoot

弹夹
类名：bulletBox
属性：bulletcounter
行为：
'''


# 创建一个弹夹
bulletBox = BulletBox(4)

# 创建一把枪
gun = gun(bulletBox)

# 人
per = Passions(gun)
per.fire()
per.fire()
per.fire()
per.fire()
per.fillBulletBox(4)
per.fire()
per.fire()