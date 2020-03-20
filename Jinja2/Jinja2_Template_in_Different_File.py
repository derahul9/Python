from jinja2 import Template

filename = "bgp_config.j2"
with open(filename) as f:
    my_template =f.read()

my_vars = {
    "bgp_as": 22,
    "router_id": "1.1.1.1",
    "peer1": "20.20.20.20"
}

j2_temp = Template(my_template)
output = j2_temp.render(**my_vars)    #my_vars will render the dictinary my_vars and pass it as key value pairs
#output = j2_temp.render(bgp_as=22, router_id="1.1.1.1", peer1="2.2.2.2") #Also can be done this way
print (output)