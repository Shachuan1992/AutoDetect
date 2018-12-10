# coding=utf-8

"""
    __author__ : shachuan
    Issue Date : 2018.12.6
    Description :OLT掉线自动检测程序，通过pingIP地址，及时发现掉线的OLT，并发送邮件。初期使用命令行的形式，后期加GUI
    History :
    Version : 1.0

"""
import os
import IPy
from telnet import *

__author__ = 'shachuan1992'

if __name__ == '__main__':
    while True:
        with open("平邑OLT地址.txt", 'r') as f:
            iplist = f.readlines()
            for ip in iplist:
                # 对IP进行预处理，得到网络位和网段
                ip_pre = ip.rstrip('\n').split('.')
                network_1 = ip_pre[0]
                network_2 = ip_pre[1]
                network_3 = ip_pre[2]
                subnet = network_1 + '.' + network_2 + '.' + network_3 + '.' + '0' + '/24'
                #Ping该IP
                info = os.system('ping -n 1 -w 10 %s' % ip)
                if info:
                    print('监测到%s不通，正在自动更换IP\n' % ip)
                    #遍历当前的IP表
                    for ip_backup in iplist:
                        #如果该备用IP与ping的IP在同一字网且不是当前的IP
                        if ((ip_backup in IPy.IP(subnet)) and (ip_backup != ip)) is True:
                            ip_backup = ip_backup.rstrip('\n')
                            olt_telnet.change(ip_backup)
                else:
                    print('%s 正常' % ip)

