# To see where your instance of textfsm is :
# >>> import textfsm
# >>> textfsm.__file__ --> '/home/rahul/.local/lib/python3.6/site-packages/textfsm/parser.py'
# This could have been also run as - rahul@rahul-virtual-machine:~/Documents/Python_Projects/Python/TextFSM$
# python3 /home/rahul/.local/lib/python3.6/site-packages/textfsm/parser.py textfsm_test.template show_ip_int_br.txt
# This is a glue code to bind the template and the text file together
# In the template file , $ indicates a variable and so $$ will indicate end of line. Value are the Regex. Only Record will be in the op

import textfsm
from pprint import pprint

template_file = "textfsm_test.template"
template = open(template_file)

with open("show_ip_int_br.txt") as f:
    raw_text_data = f.read()

# The argument 'template' is a file handle and 'raw_text_data' is a string.
re_table = textfsm.TextFSM(template)
data = re_table.ParseText(raw_text_data)
template.close()

pprint(data)
