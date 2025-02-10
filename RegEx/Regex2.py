# Anything in the parenthesis matches the regex between them. Parenthesis indicates start and end of a group.
# If a pattern matches with a contents inside a Parenthesis, it can be extracted using group method
# 1st parenthesis - . represents any character except newline character. + Indicates the previous expression may repeat one or more time
# * indicates 0 or more repetitions of the expression before it. Both + and * are greedy. .+ will match any character until space in encountered in a greedy way. o/p will be '22.22.22.1  '
# ? - Matching in a minimal fashion. .+? will match in a non greedy way. Hence, output will be '22.22.22.1' , no space as we are terminating search once we hit a space.

import re
arp = "22.22.22.1  0   b4:a9:5a:ff:c8:45  VLAN#222    L 33.32.12.222"

b = re.search(r"(.+?) +(\d) +(.+?)\s{2,} (\w)*", arp) #re.I at the end will ignore cases

print (b.group(1))
#The next + indicates, we are expecting multiple spaces but we don't want to print it
# The second parenthesis - /d is any digit from 0 to 9 in python. Python will expect a single digit here
print (b.group(2))
#The next + indicates, we are expecting multiple spaces but we don't want to print it
#Third Parenthesis - Say you want to print b4:a9:5a:ff:c8:45  VLAN#222, First part is same as Parenthesis 1. Next \s{2,} indicates stop when you found two or more occurance of space character
# Note - /s indicates space tab or a newline character. Also, note if there is no comma inside curly brace then python will expect exactly two space.
print (b.group(3))
# \w matches 0 or more occurance of any word character (a-z,A-Z,0-9,_)
print (b.group(4))
# Also remember that b.group() and b.group(0) both return the same thing the entire string
print (b.group())

#findall method returns all patterns that were matched and returnns in form of a list
#Because . + ? * have special meanings in RegEX, if you want to actually use them, then use it as \.
a = re.findall(r"\d\d+\.\d{2}\.[0-9][0-9]\.[0-9]{1,3}", arp)  #findall method returns all the matches
c = re.search(r"\d\d+\.\d{2}\.[0-9][0-9]\.[0-9]{1,3}", arp)   #Search method returns only the first match
print (a)
print (c.group())

txt = "The rain in Spain"
x = re.search(r"([S]\w{4})", txt)
print (x.group(1))