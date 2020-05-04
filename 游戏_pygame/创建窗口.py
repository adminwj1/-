import pygame
import time
def main():
    pygame.init()
    # 创建一个窗口，用来显示内容
    scree = pygame.display.set_mode((480,852))
    # 创建一个和窗口大小的图片，用来充当背景
    background = pygame.image.load(".\\image\\background.png")
    # 把背景图片放到窗口中显示

    while True:
        # 设定需要显示的背景图
        scree.blit(background, (0, 0))
        # 更新需要显示的内容
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
if __name__ == "__main__":
    main()