import pygame
import time
class HeroPlane(object):
    def __init__(self, screen_temp):
        self.x = 200
        self.y = 700
        self.screen = screen_temp
        # 创建一个飞机图片
        self.image = pygame.image.load(".\\image\\hero1.png")
        self.bullet_list = []  # 存储发射出去的子弹对象引用

    def display(self):
        """显示玩家飞机"""
        self.screen.blit(self.image, (self.x, self.y))
        """显示飞机子弹"""
        for bullet in self.bullet_list:
            bullet.display()  # 调用display方法显示子弹
            # 让子弹自动移动
            bullet.move()

    def move_left(self):
        self.x -= 5

    def move_right(self):
        self.x += 5

    def fire(self):
        self.bullet_list.append(Bullet(self.screen, self.x, self.y))
class Bullet(object):
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

def key_control(hero_temp):
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
    pygame.init()
    #1、 创建一个窗口，用来显示内容
    scree = pygame.display.set_mode((480, 852), 0, 32)
    #2、 创建一个和窗口大小的图片，用来充当背景
    background = pygame.image.load(".\\image\\background.png")
    # 创建一个飞机对象
    hero = HeroPlane(scree)
    while True:
        # 设定需要显示的背景图
        scree.blit(background, (0, 0))
        # 显示飞机
        hero.display()
        # 更新需要显示的内容
        pygame.display.update()
        key_control(hero)


if __name__ == "__main__":
    main()