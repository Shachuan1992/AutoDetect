"""
    __author__ : shachuan
    Issue Date : 2018.12.6
    Description :OLT掉线自动检测程序，通过pingIP地址，及时发现掉线的OLT，并发送邮件。初期使用命令行的形式，后期加GUI
    History :
    Version : 1.0

"""

__author__ = 'shachuan1992'



import os
import time
import datetime
iplist = ['118.190.151.15','127.0.0.1','192.168.1.0']



if __name__ == '__main__':
    for ip in iplist:
        backinfo = os.system('ping -c 5 -W 15 %s'%ip)
        if backinfo:
            #在这里写ping不通的代码
            print('不通')
        else:
            print('OK')