'''主程序区域'''
from func import *
class Interface():
    def __init__(self):
        print("======================================")
        print("     1/录入人员信息     ")
        print("     2/查询所以信息  ")
        print("     3/指定查询信息  ")
        print("     4/删除指定信息  ")
        print("     5/修改指定信息  ")

info = Interface()
choice = input("请选择：")
if choice == '1':
    Input_Info()
elif choice == '2':
    '''占时只能显示到第一行的数据'''
    Print_Info()
elif choice =='3':
    '''占时只能查询到第一行的数据'''
    Modify_Info()
elif choice == '4':
    pass
elif choice == '5':
    pass
else:
    print("违规输入！！")




