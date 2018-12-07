import telnetlib

def write_command(instance,command):
    finish = '\r'
    instance.write(command.encode('ascii')+finish.encode('ascii'))

def command_make(Device):
    user = 'lyread'
    password = 'read1234'
    commands = []
    if Device == 'MA5680T':
        commands = ['MA5680T']
    elif Device == 'MA5683T':
        commands = ['MA5683T']
    elif Device == 'C300':
        commands = ['PON']
    elif Device == 'C220':#命令不对
        commands = ['C220']
    else:
        print("错误！！！没有这种设备，联系57591添加命令")
    return commands
