import pygame
'''
image
rect
speed
'''
# 飞机精灵类
# 屏幕大小的常量
SCREEN_RECT =pygame.Rect(0, 0, 480, 700)
# 刷新的帧率
FRAME_PER_SEC = 60
# 创建敌机的定时器常量
CREATE_ENEMY_EVENT = pygame.USEREVENT

class GameSprite(pygame.sprite.Sprite):
    """飞机大战游戏精灵"""
    def __init__(self, image_name, speed=1):
        """
        定义两个属性：
        image_name：用于存放用户传入的图像
        speed：设置移动频率
        """
        """调用父类的初始化方法"""
        super().__init__()
        # 定义对象的属性
        self.image = pygame.image.load(image_name)
        self.rect = self.image.get_rect()
        self.speed = speed  # 移动频率

    def update(self):
        """在屏幕的垂直方向上移动"""
        self.rect.y += self.speed

class Background(GameSprite):
    """背景交替滚动效果"""
    # 两张图像一起向下移动
    # self.rect.y += self.speed
    # 当任意背景精灵的rect.y >= 屏幕高度，说明已经移动到屏幕下方
    # 将移动到屏幕下方的这张图像设置到屏幕的正上方
    # rect.y = -rect.height
    """游戏背景精灵"""
    def __init__(self, is_alt=False):
        # 1.调用父类方法实现精灵的创建
        super().__init__(".//image//background.png")
        # 2.判断是否是交替图像，如果是，需要设置初始化位置
        if is_alt:
            self.rect.y = -self.rect.height
    def update(self):
        # 1、调用父类的方法实现垂直方向移动
        super().update()
        # 2、判断是否移除屏幕，如果移除屏幕，将图像设置到屏幕的上方
        if self.rect.y > SCREEN_RECT.height:
            # 将背景图像移动到界面的上方
            self.rect.y = -self.rect.height