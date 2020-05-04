from essential_information import Essential_Information
from performance import Performance
from basic_function import *
from interface import *
import time
'''
问题：
录入完信息后不能直接写入文件必须结束程序后才能执行文件写入操作，while循环的问题
'''
def main():
    """主程序"""
    EI = Essential_Information()
    PF = Performance()
    BF = Basic_Function()

    while True:
        IF = Interfac()
        option = input("请输入您的操作：")
        if option == '1':
            # 添加学生基本信息
            EI.input_info()
        elif option == '2':
            # 添加学生成绩信息
            PF.InputPerformance()
        elif option == '3':
            # 显示所有学生信息
            BF.Ess_Info()
        elif option == '4':
            # 查询指定学生信息
            BF.Assig_Ess()
        elif option == '5':
            # 显示所有学生成绩
            BF.stu_info()
        elif option == '6':
            # 查询指定学生成绩
            BF.AssignInfo()
        elif option == '7':
            # 修改学生信息
            # BF.ChangeInformation()
            pass
        elif option == '8':
            # 修改学生成绩
            pass
        elif option == '9':
            # 删除学生信息
            BF.del_info()

        elif option == 'a':
            # 删除学生成绩
            BF.del_performance()
        elif option == '0':
            # 退出系统
            print("正在退出系统，请稍等...")
            time.sleep(1)
            break
if __name__ == '__main__':
    main()