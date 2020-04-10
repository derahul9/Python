import sys                                #This is a system module which is used to print sys arguments

#a = input("enter test string: ")

print (sys.argv[1])                      #To see this argument run this from command line - rahul@rahul-virtual-machine:~/Documents/Python_Projects/Python/MIsc Programs$ python3 sys_argv.py hello
print (sys.argv)                         #This is a list with one element by default i.e. the path of the program itself, all the passes arguments will append to the list

for index, argument in enumerate(sys.argv[1:]):
    print("Argument " + str(index) + ": " + argument)

for argument in sys.argv:
    if sys.argv.index(argument) == 0:
        print ("This is the file name: " + argument)
    else:
        print ("This is an argument: " + argument)