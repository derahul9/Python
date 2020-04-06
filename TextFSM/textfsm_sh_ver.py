# remember there is an implicit 'EOF -> Record' at the end of the template (by default). i.e if don't write EOF it will record and do EOF implicitly
# If you put record in each line then you will get multiple list and in each list the other variables will be empty

import textfsm
from pprint import pprint

template_file = "sh_ver.template"
template = open(template_file)

with open("sh_ver.txt") as f:
    raw_text_data = f.read()

# The argument 'template' is a file handle and 'raw_text_data' is a string.
re_table = textfsm.TextFSM(template)
data = re_table.ParseText(raw_text_data)
template.close()

pprint(data)
