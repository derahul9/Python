#findall method returns all patterns that were matched and returnns in form of a list
import re

arp = "22.22.22.1  0   b4:a9:5a:ff:c8:45  VLAN#222    L  33.32.12.222"

#Because . + ? * have special meanings in RegEX, if you want to actually use them, then use it as \.

a = re.findall(r"\d\d+\.\d{2}\.[0-9][0-9]\.[0-9]{1,3}", arp)

print (a)

# Also can be done in this way

b = re.findall(r"(\d\d)\.(\d{2})\.([0-9][0-9])\.([0-9]{1,3})", arp)

print (b)

#sub method - This will replace a particular patter nwith another value

c = re.sub(r"\d", "7", arp)

print (c)