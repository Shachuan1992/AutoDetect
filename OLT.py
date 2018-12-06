import os
import time
import datetime
ip = '118.190.151.15'
backinfo = os.system('ping -c 5 -W 15 %s'%ip)
if backinfo:
    print('不通')
else:
    print('OK')