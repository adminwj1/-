import pygame
import time
def main():
    pygame.init()
    #1、 创建一个窗口，用来显示内容
    scree = pygame.display.set_mode((480, 852), 0, 32)
    #2、 创建一个和窗口大小的图片，用来充当背景
    background = pygame.image.load(".\\image\\background.png")
    # 3、创建一个飞机图片
    hero = pygame.image.load(".\\image\\hero1.png")
    # 把背景图片放到窗口中显示
    x = 200
    y = 700
    while True:
        # 设定需要显示的背景图
        scree.blit(background, (0, 0))
        scree.blit(hero, (x, y))
        # 更新需要显示的内容
        pygame.display.update()
        for event in pygame.event.get():
            """检测退出事件"""
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif event.type == pygame.KEYDOWN:
                """检测键盘事件"""
                if event.key == pygame.K_w or event.key == pygame.K_LEFT:
                    x -= 5
                elif event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                    x += 5
                elif event.key == pygame.K_SPACE:
                    print("暂停游戏")
if __name__ == "__main__":
    main()