# The following config needs to be on the device to enable eAPI -
# management api http-commands
# protocol https
# no shut
# If you get kvm permission denied error when running Arista eos then run sudo chown /dev/kvm or sudo chmod 777 /dev/kvm
import pyeapi
from pprint import pprint

connection = pyeapi.client.connect(
    transport="https",
    host="192.168.1.2",
    username="arista",
    password="arista",
    port="443",
)

device = pyeapi.client.Node(connection)                        #Creating node object and passing eAPI connection
output = device.enable(["show version", "show ip arp"])
#pprint(output)
pprint(output[0]['result']['systemMacAddress'])