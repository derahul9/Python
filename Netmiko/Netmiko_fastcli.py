from netmiko import ConnectHandler

cisco = {
    "host": "192.168.1.2",
    "username": "cisco",
    "password": "cisco",
    "device_type": "cisco_ios",
    "fast_cli": True,                                  #fast_cli will speed things up. underhood it will reduce global delay factor less than 1.
}

net_connect = ConnectHandler(**cisco)
print(net_connect.find_prompt())
output = net_connect.send_command("show ip bgp summ")
print (output)
net_connect.disconnect()

