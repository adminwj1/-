'''
精灵和精灵组
pygame.sprite.Sprite    --存储图像数据image和位置rect的对象
精灵：（需要派生子类）
image记录图像数据
rect记录在屏幕上的位置
Update(*args)：更新精灵位置
kill()：所有组都删除

精灵组：
__init__(self, *精灵)：
add(*sprites)：向组中增加精灵
sprites()：返回所有精灵列表
update(*args)：让组中所有精灵调用update方法
draw(Surface)：将组中所有精灵的image，绘制到Surface的rect位置
pygame.display.update()：最终绘制图像

游戏流程：
游戏初始化
创建精灵
创建精灵组
游戏循环
精灵组.update()
精灵组.draw(screen)
pygame.display.update()

精灵和精灵组的职责：
精灵：
封装图像image、位置rect和速度speed
提供update()方法，根据游戏需求，更新位置rect
精灵组：
包含多个精灵对象
update方法，让精灵组中的所有精灵调用update方法更新位置
draw(screen)方法，在screen上绘制精灵组中的所有精灵
'''