from netmiko import ConnectHandler

cisco = {
    "host": "192.168.1.2",
    "username": "cisco",
    "password": "cisco",
    "device_type": "cisco_ios",
}
cisco1 = {
    "host": "192.168.1.3",
    "username": "cisco",
    "password": "cisco",
    "device_type": "cisco_ios",

}

net_connect = ConnectHandler(**cisco)
output = net_connect.send_command("show ip arp")

net_connect = ConnectHandler(**cisco1)
output1 = net_connect.send_command("show ip arp")

print (output)
print (output1)

net_connect.disconnect()
