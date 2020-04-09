import json

filename = input("enter file: ")
with open(filename) as f:
    data = json.load(f)
print (type(data))
print (data)