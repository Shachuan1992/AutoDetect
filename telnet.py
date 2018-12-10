import telnetlib

class olt():
    def __init__(self, IP=None,Device = None):
        IP = IP
        Device = Device

    def write_command(instance,command):
        finish = '\r'
        instance.write(command.encode('ascii')+finish.encode('ascii'))

    def command_make(Device):
        user = 'lyjing'
        password = 'lyjing!@#123'

    def login(IP):
        try:
            tn = telnetlib.Telnet(host=IP, port=23, timeout=10)  # 尝试开启Telnet Socket
        except ConnectionRefusedError:
            print("错误！！！目标计算机连接超时，请检查链路是否正常！")
        else:
            print('Hello World')
