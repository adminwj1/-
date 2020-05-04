# 时钟类
import pygame
import time
pygame.init()
'''
透明图像：
png格式的图像是支持透明的，在绘制图像时，透明区域不会显示任何内容。但是如果下方已经有内容，会透过透明区域显示出来
'''
screen = pygame.display.set_mode((400, 700))
bg = pygame.image.load(".\\image\\background.png")
screen.blit(bg, (0, 0))
# 绘制英雄的飞机
hero = pygame.image.load(".\\image\\hero1.png")
screen.blit(hero,(150,500))
pygame.display.update()
time.sleep(0.07)
pygame.quit()

# 创建时钟对象
# 多少秒执行一次
clook = pygame.time.Clock()
i = 0
while True:
    # tick方法会根据上次被调用的时间、自动设置游戏循环中的延时
    clook.tick(1)   # 可以指定循环内部的代码执行的频率
    print(i)
    i += 1
