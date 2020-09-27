#Netconf is a standardized API came in 2006. Juniper Netconf was the first one. It needs some sort of secured transport to run across (ssh).
#Netconf uses TCP port 830. You don't want to be dealing with Netconf directly, use NCC Client library (Python talks to Netconf). In
#Juniper terms use PyEz which will abstract the lower level mechanics from you. Netconf Layers -  Content (xml data) - Operations (edit config)
# - Messages (rpc, rpc-reply) - Secure Transport (SSH and TLS)
#NETCONF and Yang are generally tied together. YANG Is just a modelling language. YANG specifies what data should look like.
#What happens is YANG model for say an interface is converted into XML and passed into NETCONF Channel. The remote device will de-construct
#the xml data and return YANG data. Across time, we didn't want YANG data model to be tied with API. So they created REST API which could
#transport YANG data through REST Channel. (Instead of running XML data through ssh channel, we can have REST API which can transport YANG)
#Similarly we can do with GRPC instead of REST, but they are just ways of transporting YANG over...

#Juniper PYEZ was created by Juniper several years ago to help interface to thier API. They are running Netconf for thier API. THis library
#makes easier to connect to their API.

import ipdb
from ncclient import manager                     #If we are using straight netconf we need this library ncclient

conn = manager.connect(
    host="192.168.1.2",
    username="junos",
    password="junos",
    device_params={"name": "junos"},
    hostkey_verify=False,
    allow_agent=False,
    look_for_keys=False,
    port=830,
    timeout=60,
)

ipdb.set_trace()
config = conn.get_config(source="running")
config_xml = config.data_xml
print(config_xml)