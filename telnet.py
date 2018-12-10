import telnetlib

class telnet():
    def __init__(self, IP=None,Device = None):
        IP = IP
        Device = Device

    def write_command(self,instance,command):
        finish = '\r'
        instance.write(command.encode('ascii')+finish.encode('ascii'))

    def command_make(self,Device):
        user = 'lyjing'
        password = 'lyjing!@#123'

    def change(self,IP):
        try:
            tn = telnetlib.Telnet(host=IP, port=23, timeout=10)  # 尝试开启Telnet Socket
            reply = str(tn.read_very_eager(),encoding='utf-8')
            print(reply)
        except ConnectionRefusedError:
            print("错误！！！目标计算机连接超时，请检查链路是否正常！")
        else:
            print('Hello World')
