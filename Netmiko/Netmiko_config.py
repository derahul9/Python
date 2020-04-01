from netmiko import ConnectHandler

cisco = {
    "host": "192.168.1.2",
    "username": "cisco",
    "password": "cisco",
    "device_type": "cisco_ios",
}

net_connect = ConnectHandler(**cisco)
output = net_connect.send_command("show run | i logging")
print (output)

cfg_commands = ['logging buffered 5000', 'logging console']
output = net_connect.send_config_set(cfg_commands)                             #Config pushed from command line
#output = net_connect.commit() - This line will commit config on Juniper. For cisco we have similar save config
#output = net_connect.exit_config_mode() - Because commit will leave you in config mode
print (output)

output = net_connect.send_config_from_file("config_file.txt")                  #Config pushed from a file
print (output)