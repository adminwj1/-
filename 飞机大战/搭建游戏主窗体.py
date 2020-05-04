import pygame
import time
pygame.init()

while True:
	# set_mode第一个参数：resolution：指定屏幕的宽和高，默认创建的窗口大小和屏幕大小一致
	# set_mode第二个参数：flags：参数指定屏幕的附加选项，例如是否全屏等等，默认不需要传递
	# set_mode第三个参数：depth：参数表示颜色的位数，默认自动匹配

	pygame.display.set_mode((400, 700))
	pygame.display.update()
	time.sleep(5)
	break
# pygame.update()