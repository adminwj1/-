import socket
udpServer = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
udpServer.bind(('192.168.31.84', 8900))
while True:
    data, addr = udpServer.recvfrom(1024)
    print("客户端说：",data.decode("utf-8"))
    # 想客户端回复消息
    info = input("请输入消息：")
    udpServer.sendto(info.encode('utf-8'),addr)