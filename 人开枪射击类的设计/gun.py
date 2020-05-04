class gun(object):
	def __init__(self, bulletBox):
		self.bulletBox = bulletBox
	def shoot(self):
		#  判断子弹是否能打出去
		if self.bulletBox.BulletBox == 0:
			print("没有子弹了")
		else:
			self.bulletBox.BulletBox -=1
			print("剩余子弹：%d发：" % (self.bulletBox.BulletBox))
