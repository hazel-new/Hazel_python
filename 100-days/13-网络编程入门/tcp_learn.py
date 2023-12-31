import socket

#创建socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#建立连接
s.connect(('www.sina.com.cn',80))

#发送数据
s.send(b'GET / HTTP/1.1\r\nHost: www.sina.com.cn\r\nConnection: close\r\n\r\n')

#接受数据
buffer = []
while True:
    d = s.recv(1024)
    if d:
        buffer.append(d)
    else:
        break
data = b''.join(buffer)

#关闭连接
s.close()

#把HTTP头跟网页分离，打印出来
header, html = data.split(b'\r\n\r\n',1)
print(header.decode('utf-8'))
# print(html.decode('utf-8'))

#网页内容保存到文件
with open('sina.html','wb') as f:
    f.write(html)

