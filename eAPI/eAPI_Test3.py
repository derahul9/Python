import pyeapi
from pprint import pprint

connection = pyeapi.client.connect(
    transport="https",
    host="192.168.1.2",
    username="arista",
    password="arista",
    port="443",
)

cfg = [
    "vlan 225",
    "name green",
]

device = pyeapi.client.Node(connection)                        #Creating node object and passing eAPI connection
output = device.config(cfg)
output1 = device.enable(["show vlan"])
pprint(output1)