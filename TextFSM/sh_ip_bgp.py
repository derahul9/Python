# As * is a regex operation, We use [*>] the square brackets to represent *>
# The filldown option will fill the values going down until it finds a new value in that position. Test by removing FIlldown and adding to see behaviour

import textfsm
from pprint import pprint

template_file = "sh_ip_bgp.template"
template = open(template_file)

with open("sh_ip_bgp.txt") as f:
    raw_text_data = f.read()

# The argument 'template' is a file handle and 'raw_text_data' is a string.
re_table = textfsm.TextFSM(template)
data = re_table.ParseText(raw_text_data)
template.close()

pprint(data)