import json

my_data = {
    'device_name': 'rtr1',
    'ip_addr': '1.1.1.1'
}

some_list = list (range(10))
my_data['some_list'] = some_list
my_data['null_value'] = None
my_data['a_bool'] = False

filename = "outfile1.json"
with open(filename, "wt") as f:
    json.dump(my_data, f, indent=4)              # indent 4 will help representation. JSON doesn't like the last comma

print("Python")
print("#" * 10)
print (my_data)                                  # Null value is none and false has capital F
print ()
print ("JSON")
print("#" * 10)
print(json.dumps(my_data))                       # json.dumps writes as a string. json.dump writes in a file. Python doesn't care about single or double quotes
                                                 # Null value is null and false has small f




