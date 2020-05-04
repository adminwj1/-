import pymysql
from select import Select
class Func(object):
    def select(self):
        self.db = pymysql.connect('127.0.0.1', 'root', 'adminwj', 'studentsystem')
        cursor = self.db.cursor()

