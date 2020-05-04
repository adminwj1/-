import random
verification_code = "".join(list(map(str, random.sample(range(0, 10), 6))))     # 将随机出来的内容通过map函数转换成字符串，再使用list方法将字符串转成列表
print("接收到的验证码为：" + verification_code)
while True:
    code_str = input("请输入验证码：").strip()
    if not code_str.isdigit():
        print("必须输入为数字，请重新输入！")
    elif len(code_str) != 6:
        print("输入必须为六位数，请重新输入！")
    elif code_str == verification_code:
        print("输入正确，您可以修改用户信息了！")
        break
    else:
        print("输入错误，请重新输入！")