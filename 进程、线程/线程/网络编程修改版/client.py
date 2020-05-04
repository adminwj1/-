import socket
# 创建套接字
clent = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

# 发送请求
clent.connect(('192.168.31.84',9000))

while True:
    data = input("请输入给服务器发送的数据：")
    # 发数据
    clent.send(data.encode("utf-8"))
    # 接收数据
    info = clent.recv(2048)
    print("服务器说：", info.decode("utf-8"))