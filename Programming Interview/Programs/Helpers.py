'''
Easy
binary tree path
binary tree right side view

Merge Strings alternately
Palindrome Number
Remove Elements
Add two integers
search insert position
Find the Index of the First Occurrence in a String
single number

Medium
Zero array transformation 1 and 2
maximum subarray
add two numbers
next permutation
find peak element
reverse integer
longest increasing subsequence
move pieces to obtain a string
jump game
count special subsequence
subarray sum equals k
Top K Frequent Elements
Maximum Frequency of an Element After Performing Operations I
'''

"Creating a Class, Object and calling a function from a class"

class Help:
    def helper(self, a: str, b: int):
        return a
    
c = Help()
print (c.helper("a", 6))

"Convert binary to int and vice versa"
a = "1111"
x = int(a, 2)
y = bin(x)

"The zfill() method in Python pads a string with zeros on the left until it reaches a specified length"
a = "11"
x = a.zfill(5)
x = "00011"

"Addition in place"
c += 1

"Joining a list into a string --> Enter any string to join the list items"
a = ["1", "1", "1", "2"]
print ("".join(a))

"Reversing a list"
a = ["1", "1", "1", "2"]
b = a[::-1]

'''
x.append(item)
x.remove(item) --> The remove() method only removes the first occurrence of the specified element.
x.pop --> The pop() method is used to remove an element from a list at a specified index and return that element. 
If no index is provided, it will remove and return the last element by default [-1]
This method is particularly useful when we need to manipulate a list dynamically, 
as it directly modifies the original list.
The pop() method will raise an IndexError if we try to pop an element from an index that does not exist. 
IndexError: pop index out of range
'''

'''
Division/Mod Operator
5 / 2 --> Float Division
5 // 2 --> Int Division
5 % 2
'''

'''
How range function works:
range(start, stop, step)
start: (Optional) The starting value of the sequence. The default is 0.
stop: (Required) The ending value of the sequence ---->>> EXCLUSIVE
step: (Optional) The difference between each number in the sequence. The default is 1
'''

'''
char = 'A'
unicode_code = ord(char)    
The Unicode code point for 'A' is 65.
Useful to convert string to integer operations
'''

'''
SQL Query using primary key
select FirstName, LastName, City, State
from Person left join Address
on Person.PersonId = Address.PersonId
'''