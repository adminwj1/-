'''
TCP是建立可靠的连接，摈弃通信双方都可以以流的形式发送数据
相对TCP，UDP则是面向无连接的协议
使用UDP协议时，不需要建立连接，只需要知道对方的IP地址和端口号，
就可以直接发送数据包。但是能不能到达就不知道了。
虽然UDP传输数据不可靠，但他的优点是和TCP比，速度开，对于要求不高的数据可以使用UDP
'''
'''
server:
socket---->bind---->readfrom/sendto---->closecoket
client:
socket---->bind---->readfrom/sendto---->closecoket
'''
import socket
udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
udp.bind(("ipadd",'[udp端口号]'))
udp.sendto("[内容]".encode("utf-8"))