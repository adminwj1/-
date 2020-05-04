import random
import time
def get_verification_code():
    verification_code=""
    count = 60  # 用来记时
    for i in range(6):
        """随机验证码"""
        verification_code += str(random.randint(0, 9))
    show = verification_code
    while count > 1:    # 对时间进行控制
        pass
