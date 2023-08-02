#导入socket库
import socket

# #1.TCP编程
# #创建一个socket
# s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
# #建立连接
# s.connect(('www.gaoxiaojob.com',80))
# #发送数据
# s.send(b'GET / HTTP/1.1\r\nHost: www.gaoxiaojob.com/\r\nConnection: close\r\n\r\n')
# #接收数据
# buffer = []
# while True:
#     #每次最多接受1K字节
#     d = s.recv(1024)
#     if d:
#         buffer.append(d)
#     else:
#         break
# data = b''.join(buffer)
# #关闭连接
# s.close()
# #处理接收数据
# header,html = data.split(b'\r\n\r\n',1)
# print(header.decode('utf-8'))
# #把接收的数据写入文件
# with open('gaoxiao.html','wb') as f:
#     f.write(html)


#2.UDP编程
s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
#绑定端口
s.bind(('127.0.0.1',9999))
print('Bind UDP on 9999')
while True:
    #接受数据
    data,addr = s.recvfrom(1024)
    print('Received from %s:%s.' % addr)
    s.sendto(b'Hello,%s!' % data, addr)


