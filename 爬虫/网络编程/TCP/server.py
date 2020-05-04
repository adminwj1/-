# 服务端
import socket
import threading
def tctlink(sock, addr):
    try:
        print('服务器启动成功...')
        print("%s --链接成功" % (str(addr)))
        while True:
            data = sock.recv(1024)
            print("收到来自" + str(addr) + "的数据：" + data.decode('utf-8'))
            data = input("请输入给客户端发送的数据：")
            sock.send(data.encode('utf-8'))
    except:
        print('客户端断开链接，程序结束')
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 绑定IP地址
server.bind(('192.168.31.84', 9000))
# 监听
server.listen(5)
while True:
    sock, addr = server.accept()
    t = threading.Thread(target=tctlink, args=(sock, addr))
    t.start()
