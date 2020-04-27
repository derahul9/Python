# Need below two lines in the Switch config
# feature nxapi
# nxapi https port 8443
# If you get kvm permission denied error when running Arista eos then run sudo chown /dev/kvm or sudo chmod 777 /dev/kvm

import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning
from nxapi_plumbing import Device

requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

device = Device(
    api_format="jsonrpc",
    host="192.168.1.4",
    username="nexus",
    password="nexus",
    transport="https",
    port=8443,
    verify=False,
)

output = device.show("show ver")
print(output)