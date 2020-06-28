import ipdb
from ncclient import manager

conn = manager.connect(
    host="192.168.1.2",
    username="junos",
    password="junos",
    device_params={"name": "junos"},
    hostkey_verify=False,
    allow_agent=False,
    look_for_keys=False,
    port=830,
    timeout=60,
)

ipdb.set_trace()
config = conn.get_config(source="running")
config_xml = config.data_xml
print(config_xml)