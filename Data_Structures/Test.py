arp = [
    {
        "interface": "FastEthernet4",
        "mac": "00:62:EC:29:70:FE",
        "ip": "10.220.88.1",
        "age": 2.0,
    },
    {
        "interface": "FastEthernet4",
        "mac": "00:24:C4:E9:48:AE",
        "ip": "10.220.88.19",
        "age": 25.0,
    },
    {
        "interface": "FastEthernet4",
        "mac": "C8:9C:1D:EA:0E:B6",
        "ip": "10.220.88.20",
        "age": 0.0,
    },
    {
        "interface": "FastEthernet4",
        "mac": "1C:6A:7A:AF:57:6C",
        "ip": "10.220.88.21",
        "age": 6.0,
    },
    {
        "interface": "FastEthernet4",
        "mac": "A0:93:51:41:B7:80",
        "ip": "10.220.88.22",
        "age": 198.0,
    },
    {
        "interface": "FastEthernet4",
        "mac": "50:2F:A8:B1:69:00",
        "ip": "10.220.88.23",
        "age": 5.0,
    },
    {
        "interface": "FastEthernet4",
        "mac": "52:54:AB:A8:9A:EA",
        "ip": "10.220.88.28",
        "age": 238.0,
    },
    {
        "interface": "FastEthernet4",
        "mac": "52:54:AB:BE:5B:7B",
        "ip": "10.220.88.29",
        "age": 24.0,
    },
    {
        "interface": "FastEthernet4",
        "mac": "52:54:AB:71:E1:19",
        "ip": "10.220.88.30",
        "age": 224.0,
    },
    {
        "interface": "FastEthernet4",
        "mac": "52:54:AB:FB:AF:12",
        "ip": "10.220.88.35",
        "age": 239.0,
    },
    {
        "interface": "FastEthernet4",
        "mac": "00:01:00:FF:00:01",
        "ip": "10.220.88.37",
        "age": 33.0,
    },
    {
        "interface": "FastEthernet4",
        "mac": "00:02:00:FF:00:01",
        "ip": "10.220.88.38",
        "age": 6.0,
    },
    {
        "interface": "FastEthernet4",
        "mac": "64:64:9B:E8:08:C8",
        "ip": "10.220.88.39",
        "age": 9.0,
    },
    {
        "interface": "FastEthernet4",
        "mac": "EC:38:73:9E:2F:08",
        "ip": "10.220.88.42",
        "age": 7.0,
    },
]

interfaces = [
    {
        "command": "show interfaces",
        "result": {
            "interfaces": {
                "Management1": {
                    "lastStatusChangeTimestamp": 1538591522.8171098,
                    "name": "Management1",
                    "interfaceStatus": "disabled",
                    "autoNegotiate": "off",
                    "burnedInAddress": "52:54:ab:02:a1:10",
                    "loopbackMode": "loopbackNone",
                    "interfaceStatistics": {
                        "inBitsRate": 0.0,
                        "inPktsRate": 0.0,
                        "outBitsRate": 0.0,
                        "updateInterval": 300.0,
                        "outPktsRate": 0.0,
                    },
                    "mtu": 1500,
                    "hardware": "ethernet",
                    "duplex": "duplexFull",
                    "bandwidth": 1000000000,
                    "forwardingModel": "routed",
                    "lineProtocolStatus": "down",
                    "interfaceCounters": {
                        "outBroadcastPkts": 0,
                        "linkStatusChanges": 2,
                        "totalOutErrors": 0,
                        "inMulticastPkts": 0,
                        "counterRefreshTime": 1539281777.827566,
                        "inBroadcastPkts": 0,
                        "outputErrorsDetail": {
                            "deferredTransmissions": 0,
                            "txPause": 0,
                            "collisions": 0,
                            "lateCollisions": 0,
                        },
                        "inOctets": 0,
                        "outDiscards": 0,
                        "outOctets": 0,
                        "inUcastPkts": 0,
                        "inputErrorsDetail": {
                            "runtFrames": 0,
                            "rxPause": 0,
                            "fcsErrors": 0,
                            "alignmentErrors": 0,
                            "giantFrames": 0,
                            "symbolErrors": 0,
                        },
                        "outUcastPkts": 0,
                        "outMulticastPkts": 0,
                        "totalInErrors": 0,
                        "inDiscards": 0,
                    },
                    "interfaceAddress": [],
                    "physicalAddress": "52:54:ab:02:a1:10",
                    "description": "",
                },
                "Vlan1": {
                    "lastStatusChangeTimestamp": 1538591527.373837,
                    "name": "Vlan1",
                    "interfaceStatus": "connected",
                    "burnedInAddress": "52:54:ab:be:5b:7b",
                    "mtu": 1500,
                    "hardware": "vlan",
                    "bandwidth": 0,
                    "forwardingModel": "routed",
                    "lineProtocolStatus": "up",
                    "interfaceAddress": [
                        {
                            "secondaryIpsOrderedList": [],
                            "broadcastAddress": "255.255.255.255",
                            "secondaryIps": {},
                            "primaryIp": {"maskLen": 24, "address": "10.220.88.29"},
                            "virtualIp": {"maskLen": 0, "address": "0.0.0.0"},
                        }
                    ],
                    "physicalAddress": "52:54:ab:be:5b:7b",
                    "description": "",
                },
                "Ethernet2": {
                    "lastStatusChangeTimestamp": 1538591527.2428443,
                    "name": "Ethernet2",
                    "interfaceStatus": "connected",
                    "autoNegotiate": "unknown",
                    "burnedInAddress": "52:54:ab:02:a1:12",
                    "loopbackMode": "loopbackNone",
                    "interfaceStatistics": {
                        "inBitsRate": 0.0,
                        "inPktsRate": 0.0,
                        "outBitsRate": 0.0,
                        "updateInterval": 300.0,
                        "outPktsRate": 0.0,
                    },
                    "mtu": 9214,
                    "hardware": "ethernet",
                    "duplex": "duplexFull",
                    "bandwidth": 0,
                    "forwardingModel": "bridged",
                    "lineProtocolStatus": "up",
                    "interfaceCounters": {
                        "outBroadcastPkts": 0,
                        "linkStatusChanges": 1,
                        "totalOutErrors": 0,
                        "inMulticastPkts": 498763,
                        "counterRefreshTime": 1539281777.849249,
                        "inBroadcastPkts": 4171,
                        "outputErrorsDetail": {
                            "deferredTransmissions": 0,
                            "txPause": 0,
                            "collisions": 0,
                            "lateCollisions": 0,
                        },
                        "inOctets": 78083049,
                        "outDiscards": 0,
                        "outOctets": 4027630,
                        "inUcastPkts": 38214,
                        "inputErrorsDetail": {
                            "runtFrames": 0,
                            "rxPause": 0,
                            "fcsErrors": 0,
                            "alignmentErrors": 0,
                            "giantFrames": 0,
                            "symbolErrors": 0,
                        },
                        "outUcastPkts": 0,
                        "outMulticastPkts": 23018,
                        "totalInErrors": 0,
                        "inDiscards": 0,
                    },
                    "interfaceAddress": [],
                    "physicalAddress": "52:54:ab:02:a1:12",
                    "description": "",
                },
                "Ethernet3": {
                    "lastStatusChangeTimestamp": 1538591527.243047,
                    "name": "Ethernet3",
                    "interfaceStatus": "connected",
                    "autoNegotiate": "unknown",
                    "burnedInAddress": "52:54:ab:02:a1:13",
                    "loopbackMode": "loopbackNone",
                    "interfaceStatistics": {
                        "inBitsRate": 0.0,
                        "inPktsRate": 0.0,
                        "outBitsRate": 0.0,
                        "updateInterval": 300.0,
                        "outPktsRate": 0.0,
                    },
                    "mtu": 9214,
                    "hardware": "ethernet",
                    "duplex": "duplexFull",
                    "bandwidth": 0,
                    "forwardingModel": "bridged",
                    "lineProtocolStatus": "up",
                    "interfaceCounters": {
                        "outBroadcastPkts": 0,
                        "linkStatusChanges": 1,
                        "totalOutErrors": 0,
                        "inMulticastPkts": 498769,
                        "counterRefreshTime": 1539281777.875926,
                        "inBroadcastPkts": 4171,
                        "outputErrorsDetail": {
                            "deferredTransmissions": 0,
                            "txPause": 0,
                            "collisions": 0,
                            "lateCollisions": 0,
                        },
                        "inOctets": 78084075,
                        "outDiscards": 0,
                        "outOctets": 4026892,
                        "inUcastPkts": 38215,
                        "inputErrorsDetail": {
                            "runtFrames": 0,
                            "rxPause": 0,
                            "fcsErrors": 0,
                            "alignmentErrors": 0,
                            "giantFrames": 0,
                            "symbolErrors": 0,
                        },
                        "outUcastPkts": 0,
                        "outMulticastPkts": 23012,
                        "totalInErrors": 0,
                        "inDiscards": 0,
                    },
                    "interfaceAddress": [],
                    "physicalAddress": "52:54:ab:02:a1:13",
                    "description": "",
                },
                "Ethernet1": {
                    "lastStatusChangeTimestamp": 1538591527.2426362,
                    "name": "Ethernet1",
                    "interfaceStatus": "connected",
                    "autoNegotiate": "unknown",
                    "burnedInAddress": "52:54:ab:02:a1:11",
                    "loopbackMode": "loopbackNone",
                    "interfaceStatistics": {
                        "inBitsRate": 0.0,
                        "inPktsRate": 0.0,
                        "outBitsRate": 0.0,
                        "updateInterval": 300.0,
                        "outPktsRate": 0.0,
                    },
                    "mtu": 9214,
                    "hardware": "ethernet",
                    "duplex": "duplexFull",
                    "bandwidth": 0,
                    "forwardingModel": "bridged",
                    "lineProtocolStatus": "up",
                    "interfaceCounters": {
                        "outBroadcastPkts": 1,
                        "linkStatusChanges": 1,
                        "totalOutErrors": 0,
                        "inMulticastPkts": 498763,
                        "counterRefreshTime": 1539281777.867376,
                        "inBroadcastPkts": 4170,
                        "outputErrorsDetail": {
                            "deferredTransmissions": 0,
                            "txPause": 0,
                            "collisions": 0,
                            "lateCollisions": 0,
                        },
                        "inOctets": 76679169,
                        "outDiscards": 0,
                        "outOctets": 5431798,
                        "inUcastPkts": 22895,
                        "inputErrorsDetail": {
                            "runtFrames": 0,
                            "rxPause": 0,
                            "fcsErrors": 0,
                            "alignmentErrors": 0,
                            "giantFrames": 0,
                            "symbolErrors": 0,
                        },
                        "outUcastPkts": 15320,
                        "outMulticastPkts": 23018,
                        "totalInErrors": 0,
                        "inDiscards": 0,
                    },
                    "interfaceAddress": [],
                    "physicalAddress": "52:54:ab:02:a1:11",
                    "description": "",
                },
                "Ethernet6": {
                    "lastStatusChangeTimestamp": 1538591527.2436152,
                    "name": "Ethernet6",
                    "interfaceStatus": "connected",
                    "autoNegotiate": "unknown",
                    "burnedInAddress": "52:54:ab:02:a1:16",
                    "loopbackMode": "loopbackNone",
                    "interfaceStatistics": {
                        "inBitsRate": 0.0,
                        "inPktsRate": 0.0,
                        "outBitsRate": 0.0,
                        "updateInterval": 300.0,
                        "outPktsRate": 0.0,
                    },
                    "mtu": 9214,
                    "hardware": "ethernet",
                    "duplex": "duplexFull",
                    "bandwidth": 0,
                    "forwardingModel": "bridged",
                    "lineProtocolStatus": "up",
                    "interfaceCounters": {
                        "outBroadcastPkts": 0,
                        "linkStatusChanges": 1,
                        "totalOutErrors": 0,
                        "inMulticastPkts": 498768,
                        "counterRefreshTime": 1539281777.897336,
                        "inBroadcastPkts": 4171,
                        "outputErrorsDetail": {
                            "deferredTransmissions": 0,
                            "txPause": 0,
                            "collisions": 0,
                            "lateCollisions": 0,
                        },
                        "inOctets": 78083936,
                        "outDiscards": 0,
                        "outOctets": 4026892,
                        "inUcastPkts": 38215,
                        "inputErrorsDetail": {
                            "runtFrames": 0,
                            "rxPause": 0,
                            "fcsErrors": 0,
                            "alignmentErrors": 0,
                            "giantFrames": 0,
                            "symbolErrors": 0,
                        },
                        "outUcastPkts": 0,
                        "outMulticastPkts": 23012,
                        "totalInErrors": 0,
                        "inDiscards": 0,
                    },
                    "interfaceAddress": [],
                    "physicalAddress": "52:54:ab:02:a1:16",
                    "description": "",
                },
                "Ethernet7": {
                    "lastStatusChangeTimestamp": 1538591527.243805,
                    "name": "Ethernet7",
                    "interfaceStatus": "connected",
                    "autoNegotiate": "unknown",
                    "burnedInAddress": "52:54:ab:02:a1:17",
                    "loopbackMode": "loopbackNone",
                    "interfaceStatistics": {
                        "inBitsRate": 0.0,
                        "inPktsRate": 0.0,
                        "outBitsRate": 0.0,
                        "updateInterval": 300.0,
                        "outPktsRate": 0.0,
                    },
                    "mtu": 9214,
                    "hardware": "ethernet",
                    "duplex": "duplexFull",
                    "bandwidth": 0,
                    "forwardingModel": "bridged",
                    "lineProtocolStatus": "up",
                    "interfaceCounters": {
                        "outBroadcastPkts": 0,
                        "linkStatusChanges": 1,
                        "totalOutErrors": 0,
                        "inMulticastPkts": 498769,
                        "counterRefreshTime": 1539281777.837162,
                        "inBroadcastPkts": 4171,
                        "outputErrorsDetail": {
                            "deferredTransmissions": 0,
                            "txPause": 0,
                            "collisions": 0,
                            "lateCollisions": 0,
                        },
                        "inOctets": 78083771,
                        "outDiscards": 0,
                        "outOctets": 4026769,
                        "inUcastPkts": 38214,
                        "inputErrorsDetail": {
                            "runtFrames": 0,
                            "rxPause": 0,
                            "fcsErrors": 0,
                            "alignmentErrors": 0,
                            "giantFrames": 0,
                            "symbolErrors": 0,
                        },
                        "outUcastPkts": 0,
                        "outMulticastPkts": 23011,
                        "totalInErrors": 0,
                        "inDiscards": 0,
                    },
                    "interfaceAddress": [],
                    "physicalAddress": "52:54:ab:02:a1:17",
                    "description": "",
                },
                "Ethernet4": {
                    "lastStatusChangeTimestamp": 1538591527.243236,
                    "name": "Ethernet4",
                    "interfaceStatus": "connected",
                    "autoNegotiate": "unknown",
                    "burnedInAddress": "52:54:ab:02:a1:14",
                    "loopbackMode": "loopbackNone",
                    "interfaceStatistics": {
                        "inBitsRate": 0.0,
                        "inPktsRate": 0.0,
                        "outBitsRate": 0.0,
                        "updateInterval": 300.0,
                        "outPktsRate": 0.0,
                    },
                    "mtu": 9214,
                    "hardware": "ethernet",
                    "duplex": "duplexFull",
                    "bandwidth": 0,
                    "forwardingModel": "bridged",
                    "lineProtocolStatus": "up",
                    "interfaceCounters": {
                        "outBroadcastPkts": 0,
                        "linkStatusChanges": 1,
                        "lastClear": 1538591421.972857,
                        "inMulticastPkts": 498767,
                        "counterRefreshTime": 1539281777.858641,
                        "inBroadcastPkts": 4171,
                        "outputErrorsDetail": {
                            "deferredTransmissions": 0,
                            "txPause": 0,
                            "collisions": 0,
                            "lateCollisions": 0,
                        },
                        "inOctets": 78083541,
                        "outDiscards": 0,
                        "outOctets": 4027138,
                        "inUcastPkts": 38214,
                        "inputErrorsDetail": {
                            "runtFrames": 0,
                            "rxPause": 0,
                            "fcsErrors": 0,
                            "alignmentErrors": 0,
                            "giantFrames": 0,
                            "symbolErrors": 0,
                        },
                        "outUcastPkts": 0,
                        "outMulticastPkts": 23014,
                        "totalInErrors": 0,
                        "inDiscards": 0,
                        "totalOutErrors": 0,
                    },
                    "interfaceAddress": [],
                    "physicalAddress": "52:54:ab:02:a1:14",
                    "description": "",
                },
                "Ethernet5": {
                    "lastStatusChangeTimestamp": 1538591527.2434251,
                    "name": "Ethernet5",
                    "interfaceStatus": "connected",
                    "autoNegotiate": "unknown",
                    "burnedInAddress": "52:54:ab:02:a1:15",
                    "loopbackMode": "loopbackNone",
                    "interfaceStatistics": {
                        "inBitsRate": 0.0,
                        "inPktsRate": 0.0,
                        "outBitsRate": 0.0,
                        "updateInterval": 300.0,
                        "outPktsRate": 0.0,
                    },
                    "mtu": 9214,
                    "hardware": "ethernet",
                    "duplex": "duplexFull",
                    "bandwidth": 0,
                    "forwardingModel": "bridged",
                    "lineProtocolStatus": "up",
                    "interfaceCounters": {
                        "outBroadcastPkts": 0,
                        "linkStatusChanges": 1,
                        "totalOutErrors": 0,
                        "inMulticastPkts": 498770,
                        "counterRefreshTime": 1539281777.884441,
                        "inBroadcastPkts": 4171,
                        "outputErrorsDetail": {
                            "deferredTransmissions": 0,
                            "txPause": 0,
                            "collisions": 0,
                            "lateCollisions": 0,
                        },
                        "inOctets": 78084198,
                        "outDiscards": 0,
                        "outOctets": 4026769,
                        "inUcastPkts": 38215,
                        "inputErrorsDetail": {
                            "runtFrames": 0,
                            "rxPause": 0,
                            "fcsErrors": 0,
                            "alignmentErrors": 0,
                            "giantFrames": 0,
                            "symbolErrors": 0,
                        },
                        "outUcastPkts": 0,
                        "outMulticastPkts": 23011,
                        "totalInErrors": 0,
                        "inDiscards": 0,
                    },
                    "interfaceAddress": [],
                    "physicalAddress": "52:54:ab:02:a1:15",
                    "description": "",
                },
            }
        },
        "encoding": "json",
    }
]

lldp = {
    "Eth2/1": [
        {
            "remote_chassis_id": "2C:C2:60:54:DC:2C",
            "parent_interface": "",
            "remote_port": "Ethernet2/1",
            "remote_port_description": "Ethernet2/1",
            "remote_system_name": "nxos2.twb-tech.com",
            "remote_system_description": (
                "Cisco NX-OS(tm) titanium, Software (titanium-d1), Version 7.3(1)D1(1), Interim"
                " version 7.3(1)D1(0.10), RELEASE SOFTWARE Copyright (c) 2002-2013, 2015 by Cisco"
                " Systems, Inc. Compiled 1/11/2016 16:00:00"
            ),
            "remote_system_capab": "B, R",
            "remote_system_enable_capab": "B, R",
        }
    ],
    "Eth2/2": [
        {
            "remote_chassis_id": "2C:C2:60:64:E1:5F",
            "parent_interface": "",
            "remote_port": "Ethernet2/2",
            "remote_port_description": "Ethernet2/2",
            "remote_system_name": "nxos2.twb-tech.com",
            "remote_system_description": (
                "Cisco NX-OS(tm) titanium, Software (titanium-d1), Version 7.3(1)D1(1), Interim"
                " version 7.3(1)D1(0.10), RELEASE SOFTWARE Copyright (c) 2002-2013, 2015 by Cisco"
                " Systems, Inc. Compiled 1/11/2016 16:00:00"
            ),
            "remote_system_capab": "B, R",
            "remote_system_enable_capab": "B, R",
        }
    ],
    "Eth2/3": [
        {
            "remote_chassis_id": "2C:C2:60:72:61:7B",
            "parent_interface": "",
            "remote_port": "Ethernet2/3",
            "remote_port_description": "Ethernet2/3",
            "remote_system_name": "nxos2.twb-tech.com",
            "remote_system_description": (
                "Cisco NX-OS(tm) titanium, Software (titanium-d1), Version 7.3(1)D1(1), Interim"
                " version 7.3(1)D1(0.10), RELEASE SOFTWARE Copyright (c) 2002-2013, 2015 by Cisco"
                " Systems, Inc. Compiled 1/11/2016 16:00:00"
            ),
            "remote_system_capab": "B, R",
            "remote_system_enable_capab": "B, R",
        }
    ],
    "Eth2/4": [
        {
            "remote_chassis_id": "2C:C2:60:70:69:DA",
            "parent_interface": "",
            "remote_port": "Ethernet2/4",
            "remote_port_description": "Ethernet2/4",
            "remote_system_name": "nxos2.twb-tech.com",
            "remote_system_description": (
                "Cisco NX-OS(tm) titanium, Software (titanium-d1), Version 7.3(1)D1(1), Interim"
                " version 7.3(1)D1(0.10), RELEASE SOFTWARE Copyright (c) 2002-2013, 2015 by Cisco"
                " Systems, Inc. Compiled 1/11/2016 16:00:00"
            ),
            "remote_system_capab": "B, R",
            "remote_system_enable_capab": "B, R",
        }
    ],
}