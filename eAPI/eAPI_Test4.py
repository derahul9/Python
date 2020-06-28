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

vlan_cfg = device.api("vlans")
print (vlan_cfg.getall())
print (vlan_cfg.get(1))
print (vlan_cfg.create(227))
print (vlan_cfg.set_name(227, "red"))
print (vlan_cfg.getall())