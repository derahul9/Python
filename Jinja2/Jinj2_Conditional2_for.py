from __future__ import unicode_literals, print_function
from jinja2 import FileSystemLoader, StrictUndefined
from jinja2.environment import Environment

env = Environment(undefined=StrictUndefined)
env.loader = FileSystemLoader([".", './Templates/'])

my_vars = {}

template_file = 'for_example.j2'
template = env.get_template(template_file)
output = template.render(**my_vars)
print(output)

#In python, range(24) is used to generate a list of elements ranging from 0 to 24. If you want range to start from 1 then do range(1,24)
#print (list(range(1,24)))