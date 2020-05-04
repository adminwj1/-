import pygame
import time
import random
class HeroPlane(object):
    """用户飞机类"""
    def __init__(self, screen_temp):
        # 控制图片位置
        self.x = 200
        self.y = 580
        self.screen = screen_temp
        # 创建一个飞机图片
        self.image = pygame.image.load(".\\image\\hero1.png")
        self.bullet_list = []  # 存储发射出去的子弹对象引用
        self.direction = "right"  # 用来存储飞机默认的显示方向

    def display(self):
        """显示玩家飞机"""
        self.screen.blit(self.image, (self.x, self.y))
        """显示飞机子弹"""
        for bullet in self.bullet_list:
            bullet.display()  # 调用display方法显示子弹
            # 让子弹自动移动
            bullet.move()
            if bullet.judge():  # 判断子弹是否越界
                # 这里使用remove删除元素有bug，会出现漏删的情况，因为在for循环中删除第一个元素后第二个元素会自动顶位，这样就会造成原先的第二个元素漏删的情况。
                # 解决方法，将要删除的元素存放在另一个列表中，然后循环这个列表然后删除里面的元素即可
                """例如：
                a = [11,22,33,44,55,66,77]
                b = []
                for i in a:
                    if i == 33 or i == 44:
                        b.append(i)
                for i in b:
                    a.remove(i)
                """
                self.bullet_list.remove(bullet)


    def move_left(self):
        self.x -= 5
        if self.x < 0:  # 控制飞机的左边界
            self.x += 5

    def move_right(self):
        self.x += 5
        if self.x > 382:    # 控制飞机的右边界
            self.x -= 5

    def fire(self):
        self.bullet_list.append(Bullet(self.screen, self.x, self.y))

class Bullet(object):
    """玩家飞机子弹类"""
    def __init__(self, screen_temp, x, y):
        self.x = x + 46
        self.y = y - 25
        self.screen = screen_temp
        self.image = pygame.image.load(".\\image\\bullet.png")

    def display(self):
        self.screen.blit(self.image, (self.x, self.y))

    def move(self):
        """使子弹自动移动"""
        self.y -= 5

    def judge(self):
        """删除子弹方法"""
        if self.y < 0:
            return True
        else:
            return False



class EnemyPlane(object):
    """敌机的类"""
    def __init__(self, screen_temp):
            self.x = 0
            self.y = 0
            self.screen = screen_temp  # 填充背景
            # 创建一个飞机图片
            self.image = pygame.image.load(".\\image\\airplane.png")  # 显示敌机图片
            self.bullet_list = []  # 存储发射出去的子弹对象引用
            self.direction = "right"    # 用来存储飞机默认的显示方向

    def display(self):
        """显示敌人飞机"""
        self.screen.blit(self.image, (self.x, self.y))
        """显示飞机子弹"""
        for bullet in self.bullet_list:
            # 显示子弹
            bullet.display()
            # 让子弹自动移动
            bullet.bulletMove()
            if bullet.judge():
                self.bullet_list.remove(bullet)

    def move(self):
        # 判断方向
        if self.direction == "right":   # 如果键盘事件为右那么x轴加5
            self.x += 5
        elif self.direction == "left":
            self.x -= 5

        # 用来判断边界
        # 要飞机的右边界靠到界面的边界
        if self.x > 430:
            self.direction = "left"
        elif self.x < 0:
            self.direction = "right"

    def fire(self):
        # 降低随机值重复情况
        random_num = random.randint(1, 100)
        if random_num == 50 or random_num == 80:
            self.bullet_list.append(enemyBullet(self.screen, self.x, self.y))
class enemyBullet(object):
    """敌机飞机子弹类"""
    def __init__(self, screen_temp, x, y):
        self.x = x + 25
        self.y = y + 35
        self.screen = screen_temp
        self.image = pygame.image.load(".\\image\\bullet.png")

    def display(self):
        self.screen.blit(self.image, (self.x, self.y))

    def bulletMove(self):
        """使子弹自动移动"""
        self.y += 5

    def judge(self):
        """删除子弹方法"""
        if self.y > 700:
            return True
        else:
            return False




def key_control(hero_temp):
    """事件判断"""
    # 获取事件，比如按键等
    for event in pygame.event.get():
        # 判断是否点击了退出按钮
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w or event.key == pygame.K_LEFT:
                hero_temp.move_left()
            elif event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                hero_temp.move_right()
            elif event.key == pygame.K_SPACE:
                hero_temp.fire()
def main():
    """程序整体框架"""
    pygame.init()
    #1、 创建一个窗口，用来显示内容
    scree = pygame.display.set_mode((480, 700))
    #2、 创建一个和窗口大小的图片，用来充当背景
    background = pygame.image.load(".\\image\\background.png")
    # 创建一个飞机对象
    hero = HeroPlane(scree)
    # 创建一个敌机
    enemy = EnemyPlane(scree)
    while True:
        # 设定需要显示的背景图
        scree.blit(background, (0, 0))
        # 显示飞机
        hero.display()
        # 显示敌机
        enemy.display()
        enemy.move()    # 调用敌机移动方法
        enemy.fire()    # 第几开火
        # 更新需要显示的内容
        pygame.display.update()
        key_control(hero)
        time.sleep(0.01)


if __name__ == "__main__":
    main()
