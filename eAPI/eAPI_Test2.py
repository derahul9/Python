# The eapi.conf file needs to be in the home directory with the below content. This code becomes very simple as you are not even importing the inventory.

#[connection:arista]
#host: 192.168.1.2

#[DEFAULT]
#transport: https
#username: arista
#password: arista

import pyeapi

device1 = pyeapi.connect_to("arista")
print (device1)
print (device1.model)                  #Use other functions from eAPI_Test1.py to retrieve other information

