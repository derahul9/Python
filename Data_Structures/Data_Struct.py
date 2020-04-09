from Test import arp, interfaces

# When dealing with complex data structure ask yourself if its a list or a dictionary.
# arp is a list. so check the length of the list. If the length had been 1, simply grab the 0th element of the list
# If there are multiple entries then loop through it

#print (type(arp))
#print (len(arp))
#print (arp[0])

for elements in arp:
    #print ('#' * 12)
    #print (elements['mac'])
    #print (elements['ip'])
    #print('#' * 12)
    break

#print (type(interfaces))
#print (len(interfaces))
#new_interfaces = interfaces[0]

#print (new_interfaces.keys())                   # Important to know the keys of a dictionary
#print (new_interfaces['result'])                # Important to know the values of a key in a dictionary. Once you know how to extract, use a function to do this

#new_inter = new_interfaces['result']
#new_int = new_inter['interfaces']

#print (new_int.keys())                           #This gives you all the interfaces
#one_interface = new_int['Vlan1']                 #Pick one of the keys

#for k, v in new_int.items():                      #Loop through the dictionary and print only the values that you're interested in
    #print (k)
    #print (v['interfaceStatus'])
    #print ()

# Building a function to do accomplish the above task as below.

def complex_data():
    #new_interfaces = interfaces[0]
    #new_interfaces = new_interfaces['result']
    #new_interfaces = new_interfaces['interfaces']
    new_interfaces = interfaces[0]['result']['interfaces']  # The above three lines could be further consoloidated into one

    for k, v in new_interfaces.items():                     # Loop through the dictionary and print only the values that you're interested in
        print (k)
        print (v['interfaceStatus'])
        print ()

complex_data()










