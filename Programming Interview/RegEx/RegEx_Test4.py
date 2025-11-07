# or operator example i.e. |. If 1st group matches then 2nd group won't be matched
# ^ acts like negation as well as start of a line character too
# $ acts like a end of character

import re

a = "I enjoy learning programming languages such as Python 3"

result = re.search(r"\W(\w{90})\W|([A-Z]\w{5})\s\d", a)

print (result.group(2))

result1 = re.search(r"^[A-Z]\s\w{5}", a)

print (result1.group())

result2 = re.search(r"[A-Z]\w{5}\s\d$", a)

print (result2.group())