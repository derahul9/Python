from jinja2 import Template

bgp_config = """
router bgp {{ bgp_as }}
  bgp router-id {{ router_id}}
  bgp log-neighbor-changes
  neighbor {{ peer1 }} remote-as 44
"""

my_vars = {
    "bgp_as": 22,
    "router_id": "1.1.1.1",
    "peer1": "20.20.20.20"
}

j2_temp = Template(bgp_config)
output = j2_temp.render(**my_vars)    #my_vars will render the dictinary my_vars and pass it as key value pairs
#output = j2_temp.render(bgp_as=22, router_id="1.1.1.1", peer1="2.2.2.2") #Also can be done this way
print (output)