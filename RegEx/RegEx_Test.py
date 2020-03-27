import re

arp = "22.22.22.1  0   b4:a9:5a:ff:c8:45  VLAN#222    L"

a = re.match("22", arp, re.I)          #match only matches begining of the string and returns below. The flag re.I is used to ignore the case
#print (a)                             #As a is a match object, <_sre.SRE_Match object; span=(0, 7), match='Hello W'>, else we would have got none

#print (a.group())                     #The group methods is used to print a particular field of a regex

b = re.search(r"(.+?) +(\d) +(.+?)\s{2,} (\w)*", arp)            #r before the pattern means the pattern should be treated as raw string

# Anything in the parenthesis matches the regex between them. Parenthesis indicates start and end of a group.
# If a pattern matches with a contents inside a Parenthesis, it can be extracted using group method
# 1st parenthesis - . represents any character except newline character. + Indicates the previous expression may repeat one or more time
# * indicates 0 or more repetitions of the expression before it. Both + and * are greedy. .+ will match any character until space in encountered in a greedy way. o/p will be '22.22.22.1  '
# ? - Matching in a minimal fashion. .+? will match in a non greedy way. Hence, output will be '22.22.22.1' , no space as we are terminating search once we hit a space.

print (b.group(1))

#The next + indicates, we are expecting multiple spaces but we don't want to print it
# The second parenthesis - /d is any digit from 0 to 9 in python. Python will expect a single digit here

print (b.group(2))

#The next + indicates, we are expecting multiple spaces but we don't want to print it
#Third Parenthesis - Say you want to print b4:a9:5a:ff:c8:45  VLAN#222, First part is same as Parenthesis 1. Next \s{2,} indicates stop when you found two or more occurance of space character
# Note - /s indicates space tab or a newline character. Also, note if ther is no comma inside curly brace then python will expect exactly two space.

print (b.group(3))

# \w matches 0 or more occurance of any word character (a-z,A-Z,0-9,_)

print (b.group(4))

# Also remember that b.group() and b.group(0) both return the same thing the entire string
print (b.group())

