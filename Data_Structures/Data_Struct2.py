from Test import lldp
from pprint import pprint

#print (lldp.keys())            # Lets convert this datastructure into a list of dictionaries [ {}, {}, {} ]

new_list = []
for intf_name, lldp_data in lldp.items():
    lldp_data = lldp_data[0]
    new_entry = {
        "intf_name" : intf_name,
        "remote_port" : lldp_data['remote_port'],
    }
    new_list.append(new_entry)
    break

print (new_list)

