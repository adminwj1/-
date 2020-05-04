import os
import threading
import pickle
class Performance(object):
    """学生成绩信息"""
    name = ""
    student_number = ""
    Chinese = None
    Mathematics = None
    English = None




    def InputPerformance(self):
        self.name = input("请输入姓名：")
        self.student_number = input("请输入学号：")
        if not self.authentication():
            print("学号输入有误！")
            return -1
            
        """成绩录入"""
        self.Chinese = int(input("请输入语文成绩："))
        if self.Chinese < 0:
            print("成绩录入有误！")
            return -1
            
        self.Mathematics = int(input("请输入数学成绩："))
        if self.Chinese < 0:
            print("成绩录入有误！")
            return -1
            
        self.English = int(input("请输入英语成绩："))
        if self.Chinese < 0:
            print("成绩录入有误！")
            return -1
        per = {"姓名：": self.name, "学号：": self.student_number, "语文：": self.Chinese, "数学：": self.Mathematics,
                   "英语：": self.English}
        """将内容写入到文件中"""
        with open("performance.txt", 'ab') as f:
                pickle.dump(per, f)




            
            
            
            
            
            
            
    # 验证输入是否满足要求
    def authentication(self):
        # 学号验证
        if len(self.student_number) == 10:
            return True
        return False