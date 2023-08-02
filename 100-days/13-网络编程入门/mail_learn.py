# from email.mime.text import MIMEText
#
# msg = MIMEText('Hello,send by Python...','plain','utf-8')
#
# #输入Email地址和口令：
# from_addr = input('From: ')
# password = input('Password: ')
# #输入收件人地址：
# to_addr = input('To: ')
# #输入SMTP服务器地址：
# smtp_server = input('SMTP server: ')
#
# import smtplib
# server = smtplib.SMTP(smtp_server, 25) #SMTP协议默认端口是25
# server.set_debuglevel(1)
# server.login(from_addr, password)
# server.sendmail(from_addr,[to_addr], msg.string())
# server.quit()
#


import smtplib
from email.mime.text import MIMEText

# 第三方 SMTP 服务
mail_host = "smtp.163.com"  # SMTP服务器
mail_user = "hazel97@163.com"
mail_pass = "QGKCCNRXPJMUZJBW"

sender = 'hazel97@163.com'
receiver = ['hairong.liu@ericsson.com']

content = '过期教程不能用了2'
title = 'Python SMTP Mail Test2!'
message = MIMEText(content, 'plain', 'utf-8')
message['From'] = "{}".format(sender)
message['To'] = "{}".format(receiver)
message['Subject'] = title

try:
    smtpobj = smtplib.SMTP_SSL(mail_host, 465)  # 启用SSL发信, 端口一般是465
    smtpobj.login(mail_user, mail_pass)         # 登录验证
    smtpobj.sendmail(sender, receiver, message.as_string())  # 发送
    print("mail has been send successfully!")
except smtplib.SMTPException as e:
    print(e)