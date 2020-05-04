from gun import gun


class Passions(object):
	"""人类设计"""
	#  人得先有把枪，才能射击
	def __init__(self, gun):
		self.gun = gun
	#  人有了枪就可以射击
	def fire(self):
		'''
		人开火一次枪设计一次，子弹少一发
		'''
		# 枪射击
		self.gun.shoot()
	#  当子弹打完后填充子弹
	def fillBulletBox(self, count):
		self.gun.bulletBox.BulletBox = count
		print("子弹以填充%d发" % count, "可以继续射击")