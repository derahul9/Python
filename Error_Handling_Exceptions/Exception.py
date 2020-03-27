# Two types of errors - syntax errors and exceptions. Any error which is not a syntax error is exception. Exceptions are also called runtime errors.
# Python evaluates each line of code line by line from top to bottom validating syntax of wach line

from sys import abcdef                     #ImportError: cannot import name 'abcdef' from 'sys' (unknown location)

import abcdef                              #ModuleNotFoundError: No module named 'abcdef'

var1  = 10
var2  = 0

r1 = var1/var2                             #ZeroDivisionError: divvvvvvvision by zero
print (r1)                                 #If previous line is commented, NameError: name 'r1' is not defined

r2 = var1 + "hello"                        #TypeError: unsupported operand type(s) for +: 'int' and 'str'

text = "Python"
r4 = text[20]                              #IndexError: string index out of range

while True:                                #This will be an infinite loop, printing hi which caaaaan be broken by hitting ctrl+c, python will give KeyboardINterrupt Exception
        print("hi")