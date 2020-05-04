import pickle
def Input_Info():
    """信息录入"""
    print("请输入基本信息：")
    name = input("name：")
    StudentID = input("StudentID：")
    age = input("age：")
    gender = input("gender：")
    ID = input("ID：")
    path = 'info.txt'
    f = open(path, 'ab')
    My_Info = {"name：":name, "StudentID：":StudentID, "age":age, "gender：":gender, "ID":ID}
    pickle.dump(My_Info,f)
    f.close()



def Print_Info():
    """信息输出"""
    '''占时只能显示文件中的一条数据'''
    path = 'info.txt'
    f = open(path, 'rb')
    Temp_Info = pickle.load(f)
    print('姓名： %s 性别： %s 年龄： %s 学号： %s 省份证： %s' %
            (Temp_Info['name：'],
            Temp_Info['gender'],
            Temp_Info['age'],
            Temp_Info['StudentID：'],
            Temp_Info['ID']
            ))
    f.close()
Print_Info()

def Modify_Info():
    """指定查询"""
    path = 'info.txt'
    f = open(path, 'rb')
    Temp_Info = pickle.load(f)
    f.close()
    f_id = input("请输入学号：")
    if f_id == Temp_Info['StudentID：']:
        print('姓名： %s 性别： %s 年龄： %s 学号： %s 省份证： %s'%
              (Temp_Info['name：'],
               Temp_Info['gender'],
               Temp_Info['age'],
               Temp_Info['StudentID：'],
              Temp_Info['ID']
              ))
    f.close()
# Modify_Info()

def Del_Info():
    """通过学号查询匹配数据进行删除"""
    path = 'info.txt'
    f = open(path, 'rb')
    Temp_Info = pickle.load(f)
    f_id = input("请输入学号：")
    if f_id == Temp_Info['StudentID：']:
        del Temp_Info
        print(Temp_Info)
    f.close()


