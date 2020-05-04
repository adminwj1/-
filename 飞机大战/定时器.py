# pygame.time.set_timer()添加定时器
'''
定时器：每隔一段时间，去执行一些动作
set_timer(eventid, milliseconds) -->None
set_timer可以创建一个事件
可以在游戏循环的事件监听方法中捕获到该事件
第1个参数事件代号需要基于常量pygame.USEREVENT来指定
USEREVENT是一个整数，在增加的时间可以使用 USEREVENT + 1指定，依次类推...
第2个参数是事件触发间隔的毫秒值
通过pygame.event.get()可以获取当前时刻所有的事件列表
遍历列表并且判断event.type是否等于eventid，如果相等，表示定时器时间发生
'''
# 1、定义定时器常量--eventid
# 2、在初始化方法中，调用set_timer方法设置定时器时间
# 3、在游戏循环中，监听定时器事件