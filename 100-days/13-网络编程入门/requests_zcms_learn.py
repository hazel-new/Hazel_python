from requests import ConnectionError
import requests
import os
import sys
import configparser
import logging
import urllib3
urllib3.disable_warnings()

def zcms_login():
    zcms_url = 'https://zcms-demo.seli.wh.rnd.internal.ericsson.com'
    zcms_username = 'eenwdev1'
    zcms_passwd = '!F!T5D37ytySu2HRJxNQzSDTE5BY'

    login_url = '{}/loginAPI'.format(zcms_url)
    print("login_url is: {}".format(login_url))
    logging.info(login_url)

    data = {
        'username': zcms_username,
        'password': zcms_passwd
    }

    res = requests.post(login_url,data=data)
    print(res.status_code)
    login_data = res.json()
    print(login_data)
    print(res.text)
    print(res.headers)
    print(res.headers['Content-Type'])
    print(login_data['JSESSIONID'])

if __name__ == '__main__':
    zcms_login()