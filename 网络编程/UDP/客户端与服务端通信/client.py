import socket
client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

while True:
    # 发送数据
    data = input("请输入数据：")
    client.sendto(data.encode("utf-8"),('192.168.31.84', 8900))
    # 等待服务器回复信息
    info = client.recv(1024).decode("utf-8")
    print("服务器回复消息：",info)