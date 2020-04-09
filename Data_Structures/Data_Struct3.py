# Why do we need data serialization - Because the data structure files can be transported to different machines/OS
# Thats why we serialize what's there indide of our pc to serial of bytes. This needs to be standard as any one should be able to understand
# YAML and JSON are two standardization protocol. JSON is good for pc to pc communication where humans are not involved. Payload for API (NX-API, E-API)
# Json is not that human readable, hence YAML. YAML is used for inventory in salt, Ansible. YAML file starts with ---

import yaml

filename = input("Enter Filename: ")
with open(filename) as f:
    yaml_out = yaml.load(f)
print(yaml_out)


