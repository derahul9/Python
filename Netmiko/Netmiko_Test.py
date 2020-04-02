#Paramiko is for servers. Netmiko is based on Paramiko but does away some of the complexities in Paramiko.
#If you set an invalid device type, then you'll get an error listing all the netmiko listed device types.

from netmiko import ConnectHandler

import logging                                     #importing netmiko logging
logging.basicConfig(filename='test.log', level=logging.DEBUG)
logger = logging.getLogger("netmiko")

cisco = {
    "host": "192.168.1.2",
    "username": "cisco",
    "password": "cisco",
    "device_type": "cisco_ios",
}

cisco1 = {
    "host": "192.168.1.3",
    "username": "cisco",
    "password": "cisco",
    "device_type": "cisco_ios",
}
for device in (cisco, cisco1):
    net_connect = ConnectHandler(**device)
    output = net_connect.send_command("show ip int br", expect_string=r'#') #This is the message you should get on the last line #
    print (output)

