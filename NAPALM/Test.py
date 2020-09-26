# NAPALM - Network automation and Programmability application layer
# NAPALM - Create a standard set of operations across a range of platforms. Three Categories - Config + Getter + Validate
# Lower level connection info is hidden from you and you have uniform napalm api to use (Support - EoS, IOS, IOS-XR, NX-OS, Junos)
# Data structure returned is also uniform for different vendors. getfact() will return dictionary with the same key across plaforms
# napalm getter documentation --> http://napalm.readthedocs.io/en/latest/support/index.html#getters-supportt-matrix
# The below program can be used also for Nexus by just changing the driver and few optional paramaters and it will use NX-API under the hood.

from napalm import get_network_driver

cisco = {
    "hostname": "192.168.1.2",
    "username": "cisco",
    "password": "cisco",
    "device_type": "ios",
}

device_type = cisco.pop("device_type")
driver = get_network_driver(device_type)          #uses device_type to determine the os class from NAPALM
device = driver(**cisco)                          #create isntance of the class using the device parameter

print()
print("\n\n>>>Test device open")
device.open()                                    #As this is a cisco ios device, it will open a netmiko connection

print(device)
output = device.get_facts()
output1 = device.get_lldp_neighbors()
print(output)
print(output1)
print(driver)



