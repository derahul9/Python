# Environment is used for the following benefits -
# if your template is in a different folder then environment can be used (file handling)
# Also, if a variable is left blank it won't throw an error but just fill that part in the template with blank value. Environment will take care of this.
# if your template has reference to other templates, environment will make that possible as well.

from __future__ import unicode_literals, print_function
from jinja2 import FileSystemLoader, StrictUndefined
from jinja2.environment import Environment

env = Environment(undefined=StrictUndefined)                  #Whenever any variable is undefined throw an error. This is useful for error handling.
env.loader = FileSystemLoader([".", './Templates/'])            #This is to take the file from a directory which is defined. It will look one at a time current directoty --> Template

my_vars = {
    "bgp_as": 22,
    "router_id": "1.1.1.1",
    "peer1": "20.20.20.20"
}

template_file = 'bgp_config.j2'
template = env.get_template(template_file)
output = template.render(**my_vars)
print(output)

