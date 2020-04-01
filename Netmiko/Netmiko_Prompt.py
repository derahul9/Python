from netmiko import ConnectHandler

cisco = {
    "host": "192.168.1.2",
    "username": "cisco",
    "password": "cisco",
    "device_type": "cisco_ios",
}

net_connect = ConnectHandler(**cisco)
output = net_connect.send_command_timing("delete system:its")  #When we do reload command it will wait and eventually timeout. Send command timing is all about timing (not explined well)
print (output)
if 'Delete' in output:
    output += net_connect.send_command_timing("\n")
    print(output)
    if 'confirm' in output:
        output1 = net_connect.send_command_timing("\n")
        print(output1)
net_connect.disconnect()

