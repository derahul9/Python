#Paramiko is for servers. Netmiko is based on Paramiko but does away some of the complexities in Paramiko.
#If you set an invalid device type, then you'll get an error listing all the netmiko listed device types.

from netmiko import ConnectHandler
import inventory
#import inventory import *                   #This line imports all line space
from inventory import cisco                 #Importing a code that you have written, reusability of a python program, Can be done in two ways as shown

import logging                                     #importing netmiko logging
logging.basicConfig(filename='test.log', level=logging.DEBUG)
logger = logging.getLogger("netmiko")

for device in (cisco, inventory.cisco1):
    net_connect = ConnectHandler(**device)
    output = net_connect.send_command("show ver", expect_string=r'#') #This is the message you should get on the last line #
    print (output)




