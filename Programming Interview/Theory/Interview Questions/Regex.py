# \D - opposite of \d, matches anyhting other than digits
# \W - Matches everything but not letters, numbers or _ character. It matches space
# \S - Anything apart from space
# \A - Match first letter. \Z - Match last letter.
# [a-z] - Will give all small characters
# [^a] - Everything except a
# [135] - This will match any of 1,3 or 5
# or operator example i.e. |. If 1st group matches then 2nd group won't be matched
# ^ acts like negation as well as start of a line character too
# $ acts like a end of character

import re

a = "I enjoy learning programming languages such as Python 3"

result = re.search(r"\D+", a)
print (result.group())

result1 = re.search(r"\S+", a)
print (result1.group())

result2 = re.search(r"\W+", a)
print (result2.group())

result3 = re.search(r"\AI", a)
print (result3.group())

result4 = re.search(r"3\Z", a)
print (result4.group())

result5 = re.findall(r"[a-z]", a)
print (result5)

result6 = re.findall(r"[^a]", a)
print (result6)

result = re.search(r"\W(\w{90})\W|([A-Z]\w{5})\s\d", a)
print (result.group(2))

result1 = re.search(r"^[A-Z]\s\w{5}", a)
print (result1.group())

result2 = re.search(r"[A-Z]\w{5}\s\d$", a)
print (result2.group())