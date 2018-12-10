import telnetlib
import time
import os

class olt_telnet():

    def __init__(self, IP=None,Device = None):
        self.IP = IP
        self.Device = Device

    def write_command(instance,command):
        finish = '\r'
        instance.write(command.encode('ascii') + finish.encode('ascii'))

    def command_make(self,Device):
        commands = []
        if Device=='C300':
            commands = ['show']
        elif Device == 'C220':
            commands = ['show']
        elif Device == 'MA5680T':
            commands = ['enable','config']
        elif Device == 'MA5683T':
            commands = ['enable','config']
        return commands

    def change(self,IP):
        user = 'lyjing'
        password = 'lyjing!@#123'
        try:
            tn = telnetlib.Telnet(host=IP, port=23, timeout=10)  # 尝试开启Telnet Socket
        except ConnectionRefusedError:
            print("错误！！！目标计算机连接超时，请检查链路是否正常！")
        else:
            #事前不知道设备是什么型号，需要用账户名密码登陆后才能判断
            time.sleep(1)
            olt_telnet.write_command(tn, user)
            time.sleep(0.5)
            olt_telnet.write_command(tn, password)
            time.sleep(1)
            reply = str(tn.read_very_eager(), encoding='utf-8')
            if 'C300' in reply:
                commands = self.command_make('C300')
            elif 'C220' in reply:
                commands = self.command_make('C220')
            elif 'MA5680T' in reply:
                commands = self.command_make('MA5680T')
            elif 'MA5683T' in reply:
                commands = self.command_make('MA5683T')
            for command in commands:
                time.sleep(0.5)
                olt_telnet.write_command(tn,command)
            #这是检测是否成功
            backinfo =os.system('ping -n 1 -w 10 %s' % IP)
            if backinfo:
                print("自动更换不成功，请手动更换，IP是%s"%IP)
            else:
                print("自动更换IP成功")
