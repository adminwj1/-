import pickle
import time

dic = {}
with open('essential_information.txt', 'rb') as f:
    dic = pickle.load(f)
    dic["年龄："] = "29"
    with open('essential_information.txt', 'wb') as f:
        pickle.dump(dic, f)
    print(dic)