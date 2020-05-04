import pickle
import time
class Basic_Function(object):
    """基本功能实现（正删改查）"""

    # 查询所有学生基本信息
    def Ess_Info(self):
        with open('essential_information.txt', 'rb') as f:
            while True:
                try:
                    TempInfo = pickle.load(f)
                    print("姓名：%s 学号：%s 性别：%s 年龄：%s 身份证：%s 手机号：%s 邮箱：%s QQ：%s" %
                          (TempInfo['姓名：'],
                           TempInfo['学号：'],
                           TempInfo['性别：'],
                           TempInfo['年龄：'],
                           TempInfo['身份证：'],
                           TempInfo['手机号：'],
                           TempInfo['邮箱：'],
                           TempInfo['QQ：']))
                    time.sleep(1)
                except EOFError:
                    time.sleep(1)
                    break

    # 查询指定学生基本信息
    def Assig_Ess(self):
        with open('essential_information.txt', 'rb') as f:
            info = input("请输入要查寻学生的学号：")
            while True:
                try:
                    TempInfo = pickle.load(f)
                    if info == TempInfo['学号：']:
                        print("姓名：%s 学号：%s 性别：%s 年龄：%s 身份证：%s 手机号：%s 邮箱：%s QQ：%s" %
                              (TempInfo['姓名：'],
                               TempInfo['学号：'],
                               TempInfo['性别：'],
                               TempInfo['年龄：'],
                               TempInfo['身份证：'],
                               TempInfo['手机号：'],
                               TempInfo['邮箱：'],
                               TempInfo['QQ：']))
                        time.sleep(1)
                        break
                except EOFError:
                    print("未查询到信息")
                    time.sleep(1)
                    break

    # 查询所有学生成绩信息
    def stu_info(self):
        with open('performance.txt', 'rb') as f:
            while True:
                try:
                    TempInfo = pickle.load(f)
                    print("姓名：%s 学号：%s 语文：%d 数学：%s 英语：%s"
                          % (TempInfo['姓名：'],
                             TempInfo['学号：'],
                             TempInfo['语文：'],
                             TempInfo['数学：'],
                             TempInfo['英语：']))
                    time.sleep(1)
                    break
                except EOFError:
                    print("未查询到信息")
                    time.sleep(1)
                    break

    # 查询指定学生成绩
    def AssignInfo(self):
        with open("performance.txt", 'rb') as f:
            TempInfo = pickle.load(f)
            f_id = input("请输入要查询学生的学号：")
            while True:
                try:
                    if len(f_id) != 10 and f_id[0:9].isdigit():
                        print("学号输入有误！")
                        time.sleep(1)
                        return -1

                    if f_id == TempInfo['学号：']:
                        print("姓名：%s 学号：%s 语文：%d 数学：%s 英语：%s"
                                % (TempInfo['姓名：'],
                                    TempInfo['学号：'],
                                    TempInfo['语文：'],
                                    TempInfo['数学：'],
                                    TempInfo['英语：']))
                        time.sleep(1)
                        break
                except EOFError:
                    print("未查询到信息")
                    time.sleep(1)
                    break

    # 修改学生基本信息
    # def ChangeInformation (self):
    #     dic = {}
    #     with open('essential_information.txt', 'rb') as f:
    #         f_id = input("请输入您要修改学生的学号：")
    #         while True:
    #             try:
    #                 dic = pickle.load(f)
    #
    #                 if dic['学号：'] == f_id:
    #                     info = input("请输入要修改的内别：")
    #                     r = input("请输入要修改的类容：")
    #                     dic[info] = r
    #             except:
    #                 break
    #         with open('essential_information.txt', 'ab') as f:
    #
    #             pickle.dump(dic, f)
    #         print(dic)

    # 修改成绩
    def ModifiedGrades(self):
        pass

    dic = {}
    # 删除学生基本信息
    def del_info(self):
        """这个方法有个问题：在文件最后一组数据时就无效了"""
        with open('essential_information.txt', 'rb+') as f:
            f_id = input("请输入学号：")
            while True:
                try:
                    TempInfo = pickle.load(f)
                    if TempInfo['学号：'] != f_id:
                        print(TempInfo)
                        print(f.tell())
                        a = open('essential_information.txt', 'wb')
                        x = f.seek(0)
                        pickle.dump(TempInfo, f)
                        a.close()
                        print('删除信息成功！！')
                except EOFError:
                    break

    # 删除成绩
    def del_performance(self):
        """这个方法有个问题：在文件最后一组数据时就无效了"""
        with open('performance.txt', 'rb+') as f:
            f_id = input("请输入学号：")
            while True:
                try:
                    TempInfo = pickle.load(f)
                    if TempInfo['学号：'] != f_id:
                        print(TempInfo)
                        print(f.tell())
                        a = open('performance.txt', 'wb')
                        x = f.seek(0)
                        pickle.dump(TempInfo, f)
                        a.close()
                        print('删除信息成功！！')
                except EOFError:
                    break

if __name__ == '__main__':

    A =Basic_Function()
    A.del_info()