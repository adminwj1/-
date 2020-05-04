import pygame
import time
pygame.init()
'''
透明图像：
png格式的图像是支持透明的，在绘制图像时，透明区域不会显示任何内容。但是如果下方已经有内容，会透过透明区域显示出来
'''
while True:
	screen = pygame.display.set_mode((400, 700))
	bg = pygame.image.load(".\\image\\background.png")
	screen.blit(bg, (0, 0))
	# 绘制英雄的飞机
	hero = pygame.image.load(".\\image\\hero1.png")
	screen.blit(hero,(150,500))
	pygame.display.update()
	time.sleep(5)
	break
