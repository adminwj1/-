import pygame
import time
from plane_sprites import *
pygame.init()
'''
透明图像：
png格式的图像是支持透明的，在绘制图像时，透明区域不会显示任何内容。但是如果下方已经有内容，会透过透明区域显示出来
'''
screen = pygame.display.set_mode((400, 700))    # 组界面大小
bg = pygame.image.load(".\\image\\background.png")
print("背景大小：", bg.get_rect())
screen.blit(bg, (0, 0))
# 绘制英雄的飞机
hero = pygame.image.load(".\\image\\hero1.png")
print("背景大小：", hero.get_rect())


# 创建时钟对象
clock = pygame.time.Clock()
# 一秒执行多少次程序
# 1、定义rect记录飞机的初始位置
hero_rect = pygame.Rect(150, 500, 102, 126)


# 创建敌机的精灵
enemy =GameSprite(".//image//airplane.png")
enemy01 =GameSprite(".//image//airplane.png", 2)
# 创建敌机的精灵组
enemy_group = pygame.sprite.Group(enemy, enemy01)


while True:
    # tick方法会根据上次被调用的时间、自动设置游戏循环中的延时
    clock.tick(60)
    for event_list in pygame.event.get():
        if event_list.type == pygame.QUIT:
            pygame.quit()
        
    # 2、修改飞机的位置
    hero_rect.y -= 1
    # 判断飞机的位置
    if hero_rect.y <= 0:
        hero_rect.y = 700
    # 3、调用blit方法绘制图像
    screen.blit(bg, (0, 0))     # 每次调用Update()方法之前，需要把所有的游戏图像都重绘制一遍。而且应该最先重新绘制背景图像。
    screen.blit(hero, hero_rect)

    # 让精灵组调用两个方法
    # 1、update()方法，让精灵组中的精灵调用自身的update方法
    enemy_group.update()
    # 2、draw()方法，在screen上绘制所有的精灵
    enemy_group.draw(screen)


    # 4、调用update方法更新显示，让精灵组中所有的 精灵更新位置
    pygame.display.update()