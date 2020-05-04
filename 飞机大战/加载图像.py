import pygame
import time
pygame.init()
'''
要在屏幕上看到某一个图像的雷人，需要按照三个步骤：
1、使用pygame.image.load()加载图像的数据
2、使用游戏屏幕对象，调用blit方法将图像绘制到指定位置
3、调用pygame.display.update()方法跟下整个屏幕的显示
'''
while True:
	# set_mode第一个参数：resolution：指定屏幕的宽和高，默认创建的窗口大小和屏幕大小一致
	# set_mode第二个参数：flags：参数指定屏幕的附加选项，例如是否全屏等等，默认不需要传递
	# set_mode第三个参数：depth：参数表示颜色的位数，默认自动匹配

	screen = pygame.display.set_mode((400, 700))
	bg = pygame.image.load(".\\image\\background.png")
	screen.blit(bg, (0, 0))
	pygame.display.update()
	time.sleep(0.05)
	break
