from netmiko import ConnectHandler

cisco = {
    "host": "192.168.1.2",
    "username": "cisco",
    "password": "cisco",
    "device_type": "cisco_ios",
}

net_connect = ConnectHandler(**cisco)
command = "delete system:its"
output = net_connect.send_command(command, expect_string=r'Delete', strip_prompt=False, strip_command=False)
print (output)
command1 = "\n"
output += net_connect.send_command(command1, expect_string=r'confirm', strip_prompt=False, strip_command=False)
print (output)
output += net_connect.send_command(command1, expect_string=r'#', strip_prompt=False, strip_command=False)
print (output)

# The same thing can be done by timing. Where it waits for the time to complete and go to next command

net_connect = ConnectHandler(**cisco)
command = "delete system:its"
output = net_connect.send_command_timing(command, strip_prompt=False, strip_command=False)
print (output)
command1 = "\n"
output += net_connect.send_command_timing(command1, strip_prompt=False, strip_command=False)
print (output)
output += net_connect.send_command_timing(command1,  strip_prompt=False, strip_command=False)
print (output)
