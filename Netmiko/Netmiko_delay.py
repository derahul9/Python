# Use delay factor when you need to allocate more time for a command to run, eg. copy run start on nexus
# You can use delay for each command or global delay factor

from netmiko import ConnectHandler

cisco = {
    "host": "192.168.1.2",
    "username": "cisco",
    "password": "cisco",
    "device_type": "cisco_ios",
    "global_delay_factor": 2,
}

cisco1 = {
    "host": "192.168.1.3",
    "username": "cisco",
    "password": "cisco",
    "device_type": "cisco_ios",
    "global_delay_factor": 2,
}
for device in (cisco, cisco1):
    net_connect = ConnectHandler(**device)
    output = net_connect.send_command("sh ip int br", delay_factor =5) #delay factor is a multiplier to netmiko's delay.
    print (output)

# You can also use the write and read channels if you want to see all the leading and trailing prompts
# You would need a sleep code as well, so that the read is not fast enough and you can capture

for device in (cisco, cisco1):
    net_connect = ConnectHandler(**device)
    net_connect.write_channel("sh ip arp")
    output = net_connect.read_channel()
    print (output)
