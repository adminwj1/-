import re
'''
判断手机号
'''
def checkPhon(str):
    if len(str) != 11:
        return False
    elif str[0] != "1":
        return False
    elif str[1:3] !="39" and str[1:3] != "31":
        return False
    for i in range(3, 11):
        if str[i] < "0" or str[i] > "9":
            return False
        return True


def checkPhon2(str):
    pat = r"^1[34578]\d{9}$"
    res = re.findall(pat,str)
    print(res)
checkPhon2("13912345678")
checkPhon2("13912a45678")
checkPhon2("13412345678")
checkPhon2("14712345678")