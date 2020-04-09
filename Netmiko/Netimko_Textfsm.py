# Normally the op is just one string. This is undesirable as we have to seperately parse using RegEx.
# Group of engineers have developed ntc-templates that can be cloned to your home directory and which will help you parse commonly used templates.
# This directory /home/ntc-templates/templates, has all the commands for which ntc-template would work
# If you need a data structure use Textfsm. Only Netmiko 2.1 and above supports TextFSM.

from netmiko import ConnectHandler
from inventory import cisco,cisco1
import os

os.environ["NET_TEXTFSM"] = "/home/ntc-templates/templates" #This variable needs to be setup , so that the templates could be found

net_connect = ConnectHandler(**cisco)
output = net_connect.send_command("show ip arp", use_textfsm=True)
#print (output)
#print (output[3].keys())
#print (output[3]['address'])

#print (len(output))
#print (type(output))

print ("IP_Address     MAC_address" )
for element in output:
    print (element['address'] ,":", element['mac'])
#   break
