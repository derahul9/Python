# NAPALM - Create a standard set of operations across a range of platforms. Three Categories - Config + Getter + Validate
# Lower level connection info is hidden from you and you have uniform napalm api to use (Support - EoS, IOS, IOS-XR, NX-OS, Junos)
# Data structure returned is also uniform for different vendors. getfact() will return dictionary
# napalm getter documentation --> http://napalm.readthedocs.io/en/latest/support/index.html#getters-supportt-matrix

from napalm import get_network_driver
from inventory import cisco

device_type = cisco.pop("device_type")
driver = get_network_driver(device_type)
device = driver(**cisco)

print()
print("\n\n>>>Test device open")
device.open()

print()
output = device.get_facts()
print(output)
print()



