# # 进程之间的通信
# # multiprocessing对多核CPU的利用率会比threading好得多
# from multiprocessing import Process, Queue
# import os, time, random
#
#
# # 写数据进程执行的代码
# def proc_write(q,urls):
#     print('Process is wrinting...')
#     for url in urls:
#         q.put(url) #写入Queue
#         print('put %s to queue...' % url) # %号
#         time.sleep(random.random())
#
#
# # 读数据进程的代码
# def proc_read(q):
#     print('Process is reading...')
#     while True:
#         url = q.get(True)
#         print('get %s from queue...' %url)
#
#
# if __name__ == '__main__':
#     # 父进程创建Queue，并传给各个子进程
#     q = Queue()
#     proc_write1 = Process(target=proc_write,args=(q,['url1','url2','url3']))
#     proc_write2 = Process(target=proc_write,args=(q,['url4','url5','url6']))
#     proc_reader = Process(target=proc_read,args=(q,))
#     # 启动子进程，写入
#     proc_write1.start()
#     proc_write2.start()
#     proc_reader.start()
#
#     # 等待proc_write1结束
#     proc_write1.join()
#     proc_write2.join()
#     # proc_reader进程是死循环，强制结束
#     proc_reader.terminate()


# subprocess 包主要功能是执行外部的命令和程序
# 进程的练习
# 先在同一个目录创建一个try.py
# 再运行
# import subprocess
# # 执行命令，并返回执行状态
# subprocess.call(['python','try.py'])
# print('-'*50)
# print('call():',subprocess.call(['python','try.py'])) # 当返回值不为0时，抛出异常
# print('-'*50)
# print('check_call():',subprocess.check_call(['python','try.py'])) #如果返回值不为0，直接抛出异常
# print('-'*50)
# print('check_output():',subprocess.check_output(['python','try.py'])) #二进制 b'Hello python\r\n'

# # Popen
# import subprocess
# child = subprocess.Popen(['python','try.py'])
# child.wait()
# print('进程1结束') #主进程不等待child，直接结束


# 正则表达式
# import re
# txt = 'he,she,that,hat,wolf,the，attention,hen'
# #有he的单词抓出来
# p = '\w*he\w*' # \w代表一个字母或数字，*：从0开始有任意个。+：从1开始有任意个。
# result = re.findall(p,txt)
# print(result)
# # p2 = '\w*at'
# p2 = '[st]h\w*' # []多个选项，[0-9],[a-z],[A-Z]都可以
# result2 = re.findall(p2,txt)
# print(result2)

import re
# 括号的作用
# # 中括号 替换的意思
# txt = "<div>test1</div><div>test2</div>test3,test4"
# result= re.findall('test[13579]', txt)
# print(result)
#
# # 大括号 倍数的意思
# # '{m}'   匹配前一个字符m次
# txt='2019-10-31 08:52' #取得年月日
# # result=re.findall('\d\d\d\d-\d\d-\d\d',txt)
# result
# print(result)

# re.sub  批量替换
#phone = "2004-959-559 # 这是一个电话号码"

# # 删除注释
# num = re.sub(r'#.*$', "", phone)
# print("电话号码 : ", num)


# # 处理爬虫下来的信息
# txt = '一是咱cc @cc三百首 做得属实真心（😢我大概一辈子都没这么大的耐心做一件事情）二是大概他想更加明确地告诉咱'
# p1 = re.findall('\w+',txt)
# p = '@\w*:' #
# print(p1)