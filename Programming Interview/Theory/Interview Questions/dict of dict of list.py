from collections import defaultdict

devices = defaultdict(lambda: defaultdict(list))

a = ["sw1.dal", "sw2.dal", "sw2.col", "sw3.nyc", "rt5.col", "rt6.nyc"]

for elem in a:
    b = elem.split(".")
    c = b[1]
    e = b[0][0:2]
    devices[c][e].append(elem)

for k, v in devices.items():
    for i, n in v.items():
        print (n)