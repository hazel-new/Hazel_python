# from time import time
# from threading import Thread
#
# import requests
#
# class DownloadHandler(Thread):
#
#     def __init__(self,url):
#         super().__init__()
#         self.url = url
#
#     def run(self):
#         filename = self.url[self.url.rfind('/') + 1:]
#         resp = requests.get(self.url)
#         with open('Users/Hao/' + filename, 'wb') as f:
#             f.write(resp.content)
#
# def main():
#     resp = requests.get(
#         'http://api.tianapi.com/meinv/?key=APIKey&num=10'
#     )
#     data_model = resp.json()
#     for mm_dict in data_model['newslist']:
#         url = mm_dict['picUrl']
#         DownloadHandler(url).start()
#
# if __name__ == '__main__':
#     main()

import socket
import ssl
# s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# s.connect(('www.sina.com.cn',80))
s= ssl.wrap_socket(socket.socket())
s.connect(('www.sina.com.cn', 443))
s.send(b'GET / HTTP/1.1\r\nHost: www.sina.com.cn\r\nConnection: close\r\n\r\n')
buffer = []
while True:
    d = s.recv(1024)
    if d:
        buffer.append(d)
    else:
        break
data = b''.join(buffer)
s.close()
header, html = data.split(b'\r\n\r\n',1)
print(header.decode('utf-8'))
with open('sina.html','wb') as f:
    f.write(html)