import socket
try:
    server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    # 绑定IP端口
    server.bind(("192.168.31.84",9000))
    # 监听
    server.listen()
    print("服务器启动成功.....")
    # 等待链接
    # clientSocket socket数据
    # clentAddress IP地址
    clientSocket, clentAddress = server.accept()

    print("%s --链接成功" % (str(clentAddress)))

    while True:
        # 接收数据
        data =clientSocket.recv(1024)
        # 输出接收到的数据内容
        print("收到" + str(clentAddress) + "的数据：" + data.decode("utf-8"))
        data = input("请输入给客户端发送的数据：")
        clientSocket.send(data.encode("utf-8"))
except:
    print("客户端断开链接，程序结束")