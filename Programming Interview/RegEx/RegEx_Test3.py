# \D - opposite of \d, matches anyhting other than digits
# \W - Matches everything but not letters, numbers or _ character. It matches space
# \S - Anything apart from space
# \A - Match first letter. \Z - Match last letter.
# [a-z] - Will give all small characters
# [^a] - Everything except a
# [135] - This will match any of 1,3 or 5

import re

a = "I enjoy programming in Python 3"

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
