from netmiko import ConnectHandler
import inventory1

for device in (inventory1.R2,):
    net_connect = ConnectHandler(**device)
    log_output = net_connect.send_command("show log | i %OSPF-5-ADJCHG")
    print (log_output)
    if "FULL to DOWN" in log_output:
        print ("1st Pre check: OSPF is flapping - passed")
        ping_output = net_connect.send_command("ping  4.4.4.1 source fa 0/1", delay_factor =2)
        if "Success rate is 100 percent" in ping_output:
            print("2nd Pre check: Secondary circuit stable - passed")
            print("Proceeding to costing up OSPF")
            costup_config = net_connect.send_config_from_file("config_file_endpoint_fb.txt", delay_factor =2)
            print(costup_config)
            show_route = net_connect.send_command("show ip route ospf")
            print(show_route)
            print("OSPF has been costed up on the Endpoint side")
            for device1 in (inventory1.R1,):
                net_connect = ConnectHandler(**device1)
                costup_config1 = net_connect.send_config_from_file("config_file_endpoint_fb.txt", delay_factor =2)
                print (costup_config1)
                show_route1 = net_connect.send_command("show ip route ospf")
                print(show_route1)
                print("OSPF has been costed up on the tunnel Router side")
        else:
            print("2nd Pre check: Secondary circuit stable - failed")
            print("No config changes has been made")
    else:
        print("Pre check: OSPF is flapping - failed")
        print("No config changes has been made")



