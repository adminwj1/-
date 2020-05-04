# rect类
import pygame
# rect第一个参数：x轴位置
# rect第二个参数：y轴位置
# rect第三个参数：矩形的宽
# rect第四个参数：矩形的高
hero_rect = pygame.Rect(100, 500, 125, 200)
print("%d %d %d %d" % (hero_rect.x, hero_rect.y, hero_rect.width, hero_rect.height))
print(hero_rect.size)