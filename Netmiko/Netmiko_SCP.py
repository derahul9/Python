# This is test scp code, as the device on GNS can't have disk space, we can't copy actual files.
# scp in netmiko is idempotent i.e. it checks if file is available if not only then it will copy


from netmiko import ConnectHandler, file_transfer

cisco = {
    "host": "192.168.1.2",
    "username": "cisco",
    "password": "cisco",
    "device_type": "cisco_ios",
}

source_file = "test.txt"
dest_file = "test.txt"
direction = "put"
file_system = "system:"

# Create the Netmiko SSH connection
ssh_conn = ConnectHandler(**cisco)
transfer_dict = file_transfer(
    ssh_conn,
    source_file=source_file,
    dest_file=dest_file,
    file_system=file_system,
    direction=direction,
    overwrite_file=True,
)
print(transfer_dict)