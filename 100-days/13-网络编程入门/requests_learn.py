import  requests
import  logging

# r = requests.get('https://baidu.com/')
# print(r.status_code)
# print(r.text)

#
# from time import time
# import requests
# from threading import Thread
#
# #继承Thread类创建自定义的线程类
# class DowndloadHandler(Thread):
#
#     def __init__(self,url):
#         super().__init__()
#         self.url = url
#
#     def run(self):
#         filename = self.url[self.url.rfind('/') + 1:]
#         resp = requests.get(self.url)
#         with open('/User/Hao/' + filename,'wb') as f:
#             f.write(resp.content)
#
# def main():
#     resp = requests.get( 'http://api.tianapi.com/meinv/?key=APIKey&num=10')
#     data_model = resp.json()
#     print(data_model)
#     for mm_dict in data_model['newlist']:
#         url = mm_dict['picUrl']
#         DowndloadHandler(url).start()
#
#
# if __name__ == '__main__':
#     main()


