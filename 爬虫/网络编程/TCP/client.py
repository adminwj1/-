import socket

# 创建套接字
clent = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
clent.connect(('192.168.31.84', 9000))

while True:
    data = input("请对服务器发送消息：")
    clent.send(data.encode('utf-8'))
    info = clent.recv(1024)
    print(info.decode('utf-8'))