# Need below two lines in the Switch config
# feature nxapi
# nxapi https port 8443
# If you get kvm permission denied error when running Nexus then run sudo chown /dev/kvm or sudo chmod 777 /dev/kvm

import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning
from nxapi_plumbing import Device

requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

device = Device(
    api_format="jsonrpc",                                                    #This format could also be xml instead of jsonrpc
    host="192.168.1.4",
    username="nexus",
    password="nexus",
    transport="https",
    port=8443,
    verify=False,
)

output = device.show("show ver")
print(output)

cmd = [
    "show hostname",
    "show version"
]

output1 = device.show_list(cmd, raw_text = True)

for entry in output1:
    print(entry)
    input("Hit Enter to continue: ")

cfg_cmd = [
    "logging history size 400"
]
output2 = device.config_list(cfg_cmd)
print (output2)
