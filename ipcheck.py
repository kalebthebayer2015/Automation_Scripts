import os

ip = input('Enter IP address:')

os.system('ping -c 3 ' + ip)
