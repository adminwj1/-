import pygame
from pygame.locals import *
import time
import random

"""飞机和子弹基类"""
class Base(object):
    def __init__(self, screnn_temp, x, y, image_name):
        self.x = x
        self.y = y
        self.screen = screnn_temp   # 主界面信息
        self.image = pygame.image.load(image_name)

class BasePlane(Base):
    """飞机基类"""
    def __init__(self, screen_temp, x, y, image_name):
        Base.__init__(self, screen_temp, x, y, image_name)
        self.bullet_list = []   # 用于存放发射的子弹

    def display(self):
        self.screen.blit(self.image, (self.x, self.y))
        for bullet in self.bullet_list:     # 循环子弹列表
            bullet.display()    # 子弹显示方法
            bullet.move()   # 子弹移动方法
            if bullet.judge():  # 判断子弹是否越界
                self.bullet_list.remove(bullet)

class BaseBullet(Base):
    """子弹基类"""
    def display(self):
        self.screen.blit(self.image, (self.x, self.y))


class HeroPlan(BasePlane):
    """玩家飞机类"""
    def __init__(self, screnn_temp):
        BasePlane.__init__(self, screnn_temp, 196, 580, ".//image//hero1.png")
        self.key_up_status = False
        self.key_right_status = False
        self.key_left_status = False
        self.key_down_status = False

    def move(self):
        """玩家飞机移动"""
        if self.key_left_status:
            self.x -= 3
        if self.key_right_status:
            self.x += 3
        if self.key_down_status:
            self.y += 3
        if self.key_up_status:
            self.y -= 3

        # 飞机越界
        if self.x > 382:
            self.x -= 5

        if self.x < 0:
            self.x += 5

        if self.y > 580:
            self.y -= 5

        if self.y < 0:
            self.y += 5

    def fire(self):
        """发射子弹"""
        self.bullet_list.append(Bullet(self.screen, self.x, self.y))

class Bullet(BaseBullet):
    """玩家子弹类"""
    def __init__(self, screen_temp, x, y):  # 显示主界面
        BaseBullet.__init__(self, screen_temp, x+40, y-20, ".//image/bullet.png")   # 在主界面中显示玩家飞机发射的子弹
    def move(self):
        self.y -= 10

    def judge(self):
        """判断子弹越界"""
        if self.y < 0:
            return True
        else:
            return False

class EnemyPlane(BasePlane):
    """敌机类"""
    def __init__(self, screen_temp):
        BasePlane.__init__(self, screen_temp, 0, 0, ".//image//airplane.png")
        self.direction = "right"    # 控制敌机默认显示方向

    def move(self):
        """敌机的移动"""
        if self.direction == "right":
            self.x += 5
        elif self.direction == "left":
            self.x -= 5
        if self.x > 420:
            self.direction = "left"
        elif self.x < 0:
            self.direction = "right"
    def fire(self):
        bullte = random.randint(1, 100)
        if bullte == 20 or bullte == 50 or bullte == 100:
            self.bullet_list.append(EnemyBullet(self.screen, self.x, self.y))

class EnemyBullet(BaseBullet):
    """敌机子弹类"""
    def __init__(self, screen_temp, x, y):
        BaseBullet.__init__(self, screen_temp, x + 0, y + 0, ".//image//bullet.png")
    def move(self):
        self.y += 5

    def judge(self):
        """判断子弹越界"""
        if self.y > 680:
            return True
        else:
            return False
def key_control(hero_temp):

    """键盘控制函数"""
    for event in pygame.event.get():
        # 判断是否点击了退出按钮
        if event.type == QUIT:
            exit()
            # 判断是否是按下了键
        elif event.type == KEYDOWN:
            # 检测按键是否是a或者left
            if event.key == K_a or event.key == K_LEFT:
                hero_temp.key_left_status = True
            # 检测按键是否是d或者right
            elif event.key == K_d or event.key == K_RIGHT:
                hero_temp.key_right_status = True
            # 检测按键是否是w或者up
            elif event.key == K_w or event.key == K_UP:
                hero_temp.key_up_status = True
            # 检测按键是否是s或者down
            elif event.key == K_s or event.key == K_DOWN:
                hero_temp.key_down_status = True
            # 检测按键是否是空格键
            elif event.key == K_SPACE:
                hero_temp.fire()
        # 判断是否是松了键
        elif event.type == KEYUP:
            if event.key == K_a or event.key == K_LEFT:
                hero_temp.key_left_status = False
            elif event.key == K_d or event.key == K_RIGHT:
                hero_temp.key_right_status = False
            elif event.key == K_w or event.key == K_UP:
                hero_temp.key_up_status = False
            elif event.key == K_s or event.key == K_DOWN:
                hero_temp.key_down_status = False


def main():
    pygame.init()
    screen = pygame.display.set_mode((480, 700), 0, 32)
    background = pygame.image.load(".//image//background.png")
    # 创建一个飞机对象
    hero = HeroPlan(screen)

    # 创建一个敌机对象
    enemy = EnemyPlane(screen)
    while True:
        screen.blit(background, (0, 0))
        # 显示玩家飞机
        hero.display()
        # 玩家飞机移动
        hero.move()
        # 显示敌机
        enemy.display()
        # 敌机移动
        enemy.move()
        enemy.fire()

        pygame.display.update()
        # 调用键盘监控方法
        key_control(hero)
        time.sleep(0.01)



if __name__ == '__main__':
    main()