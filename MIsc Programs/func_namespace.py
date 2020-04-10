my_var = 5

def my_var_func():
    global my_var
    print (my_var)
    my_var = 10                                           #If you don't import global variable then it will give an error as my_var is defined after print statement

my_var_func()

def my_var_func1():
    my_var = 10
    print (my_var)
    return my_var                                        #If you want to use value of my_var outside of function, return the value and store it in a variable

result = my_var_func1()

print (result * 10)

# Python Modules are nothing but set of functions defined in a file which can be imported or downloaded if not built in from the internet

import math

print (dir(math))              # This gives the functions inside of the math module
print (help(math))             # Helps find more information on  the module
print (math.pi)                # To use any of the function inside the module