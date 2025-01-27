'''1 binary tree path
binary tree right side view
diameter of binary tree
Invert Binary Tree
maximum depth of binary tree
same tree
subtree of another tree
symmetric tree
2 Remove Elements
Add two integers
Divisor game
Find Common Character
Find Winner on a tic tac toe game
High Five
Is subsequence
island perimeter
logger rate limiter
merge sorted array
moving average from datastream
palindrome linkedlist
pascals triangle
rectangle overlap
remove duplicates from a sorted list
remove linked list elements
reverse linked list
reverse vowels of string
summary ranges
verifying alien dictionary
3 Zero array transformation 1 and 2
maximum subarray
next permutation
find peak element
reverse integer
longest increasing subsequence
move pieces to obtain a string
jump game
count special subsequence
Maximum Frequency of an Element After Performing Operations I
binary tree zigzag level order traversal
container with most water
count complete tree node
decode ways
letter combinations of a phone number
max area of an island
meeting rooms 2
rotate image
search in rotated sorted array
spiral matrix
validate Ip address
Word Break'''

'''
27th Jan - 2nd Feb (1 Week) - Programming
3rd Feb - 9th March (5 Weeks) - Networking (4Week) + Design - Amazon+Visa (1Week) 
10th March - 16th March (1 Week) - Apply+H.R (Make it Senior Role Specific)
17th March - 31st March (2Weeks) - Screening
April/May - Onsite

Amazon Programming knowledge
Pandas
File Operations
Jinja
Global Local vars
git branch
Regex

Networking Interview
System and Behavioral Interview
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
List Sort
x = sorted(x, reverse=True)
x.sort
'''

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

Useful to convert int into char
char_code = chr(int)
'''

'''
SQL Query using primary key
select FirstName, LastName, City, State
from Person left join Address
on Person.PersonId = Address.PersonId
'''

'''
Replace and Upper Function
S = S.replace('-', '')
S = S.upper()
'''

'''
Dict Operations
for key in my_dict:
    print(key)

for key in my_dict.keys():
    print(key)

for value in my_dict.values():
    print(value)

for key, value in my_dict.items():
    print(key, value)

sorted_dict = dict(sorted(x.items(), key=lambda item: item[1]))
'''

'''
Use this to get the min value
m = float('inf')
m = min(x,y)

Use this to get the max value
m = float('-inf')

'''

'''
In Python, a defaultdict is a subclass of the built-in dict class, and it is part of the collections module. 
The main difference between a regular dictionary and a defaultdict is that the defaultdict automatically provides 
a default value for any key that does not exist in the dictionary. This eliminates the need to manually check for 
the existence of a key before accessing its value.

from collections import defaultdict
my_dict = defaultdict(int)

When you try to access or modify a key that does not exist, the defaultdict will automatically 
create an entry for that key and assign it a default value using the provided factory function (e.g., int, list, set, etc.).

If you don't use defaultdict you'll have to assign a value to non-existing keys:
student_grades = {}
grades = [
    ('elliot', 91),
    ('neelam', 98),
    ('bianca', 81),
    ('elliot', 88),
]
    for name, grade in grades:
    if name not in student_grades:
        student_grades[name] = []
        student_grades[name].append(grade)
'''

'''
Anagram = All letter should match
Panagram = The task is to check if a string is a pangram which means it includes every letter of the English alphabet at least once
Palindrome = 
'''

'''
isalnum() --> to get only alpha numeric characters
isdigit() --> to check data type if digit 
lower() --> return lower case letters
'''

'''
p = "abc"
x = defaultdict(int)
for i in range(len(p)):
    x[p[i]] += 1
return x  ### {"a":1,"b":1,"c":1}

The above function can also be achieved using x = Counter(p)
'''

'''
The strip() Function in Python 
Python’s strip() function is a built-in function that removes specific leading and trailing 
characters from the start and end of the original string. These characters to remove are given 
as an argument to strip() for removal.
'''

'''
import pdb
pdb.set_trace()
'''

'''
Get index and value of a list using enumerate function:
numbers = [45, 22, 14, 65, 97, 72]
for i, num in enumerate(numbers):
    print(i, num)
'''

'''
square root function m = i ** 0.5
square function = i ** 2
'''

'''
from itertools import permutations, combinations
perm = permutations([1, 2, 3], 2) # Get 2 permutations of [1, 2, 3] , This will also include repeat digits
comb = combinations([1, 2, 3], 2) # Get 2 combinations of [1, 2, 3] , This won't include repeat digits
'''

'''
# YAML and JSON are two standardization protocol. JSON is good for pc to pc communication where humans are not involved. Payload for API (NX-API, E-API)
# Json is not that human readable, hence YAML. YAML is used for inventory in salt, Ansible. YAML file starts with ---

import yaml

filename = input("Enter Filename: ")
with open(filename) as f:
    yaml_out = yaml.load(f)
print(yaml_out)
'''

'''
list = [1, 2, 4, 4, 3, 3, 3, 6, 5] #Mutable meaning changeable and so append, remove etc. operations are allowed. Also they have dynamic memory but lookup is slower than tuple
tuple = (0, 1, 2, 3) #Immutable meaning non-changeable and so append, remove etc. operations are not allowed. Also they have fixed memory and lookup is faster than list
'''

'''
import pandas
dxlsx = pandas.read_excel("Employees.xlsx", sheet_name= 0) 
#print (dxlsx)
djson = pandas.read_json("Employees.json")
'''

'''
# NAPALM - Network automation and Programmability application layer
# NAPALM - Create a standard set of operations across a range of platforms. Three Categories - Config + Getter + Validate
# Lower level connection info is hidden from you and you have uniform napalm api to use (Support - EoS, IOS, IOS-XR, NX-OS, Junos)
# Data structure returned is also uniform for different vendors. getfact() will return dictionary with the same key across plaforms
# napalm getter documentation --> http://napalm.readthedocs.io/en/latest/support/index.html#getters-supportt-matrix
# The below program can be used also for Nexus by just changing the driver and few optional paramaters and it will use NX-API under the hood.

from napalm import get_network_driver

cisco = {
    "hostname": "192.168.1.2",
    "username": "cisco",
    "password": "cisco",
    "device_type": "ios",
}

device_type = cisco.pop("device_type")
driver = get_network_driver(device_type)          #uses device_type to determine the os class from NAPALM
device = driver(**cisco)                          #create isntance of the class using the device parameter

print()
print("\n\n>>>Test device open")
device.open()                                    #As this is a cisco ios device, it will open a netmiko connection
'''

'''
for i in range(10):
    pass  # pass is the equivalent of "do nothing"; it is actually a placeholder for when you just want to write a piece of code that you will treat later
'''

'''
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
'''

'''
import sys                                #This is a system module which is used to print sys arguments

#a = input("enter test string: ")

print (sys.argv[1])                      #To see this argument run this from command line - rahul@rahul-virtual-machine:~/Documents/Python_Projects/Python/MIsc Programs$ python3 sys_argv.py hello
print (sys.argv)                         #This is a list with one element by default i.e. the path of the program itself, all the passes arguments will append to the list
'''

'''
# Try / Except / Else / Finally - handling an exception when it occurs and telling Python to keep executing the rest of the lines of code in the program
try:
    print(4 / 1)  # in the "try" clause you insert the code that you think might generate an exception at some point
except ZeroDivisionError:
    print(
        "Division Error!")  # specifying what exception types Python should expect as a consequence of running the code inside the "try" block and how to handle them
else:
    print("No exceptions raised by the try block!")  # executed if the code inside the "try" block raises NO exceptions
finally:
    print(
        "I don't care if an exception was raised or not!")  # executed whether the code inside the "try" block raises an exception or not
'''

'''
Git hub is SaaS app that is very popular on hosting online GIT repository. (Git hub uses GIT under the hood). 

mkdir git-test
cd git-test/
git init
ls -al ——> .git (Repository - Set of information stored under .git sub directory - project folder for set of related files)

git status —> will give you all  untracked files created under .git  (test1.py and test2.py) 

On branch master, there will be no commits yet

git add test*.py (After this command it will show as changes to be committed) (after git add status will change from untracked to staging.

git commit -m “Making first commit of files”  (-m is for comments)  —> This will give warning that below fields need to be filled

git config —global user.email
git config —global user.name ——> Only have to set this up once

cat ~/.gitconfig —> this file will store the email and username details

After above is done then you can do git commit

git status —> On branch master and nothing to commit

git branch —> will show the branches that we have

To clone github to your pc do —> git clone url

GIT Flow —
————————
Working Directory —> (Use git add/rm) to stage or go to staging stage —> (use git commit) to add it to the repository (.git)

Now if you edit test2.py and create a new one test3.py and do git status —> test2.py will show under untracked files and test3.py will show under modified.

git diff gives you the config that is differing from the old one

git log —> will show us history of commits

4 - Push and Pull-
———————————

git clone url (typing this command in your commandprompt of pc will clone everything on github to your pc)

now create a file and push it to github using —> git push origin master (origin - when we initially did the clone request, the url of github became the origin), so origin is the remote machine.

git remote -v (Will give you all the remotes you have)

git pull origin master (you can pull from master branch)

5 - GIT branches- (The working directory is further divided into branches)
———————————

if a file is not added to repo then do rm to remove the file. If its already in stging area then do git reset head file name and then do rm to remove it

to discard a change made on a file do —> git checkout — ./test2.py

to discard a change made on multiple file do —> git stash

git checkout -b devel master (checkout a developer branch which is based on master branch)

git branch feature1 (creates feature1 branch, git checkout will go into the branch)

git push origin develop (This will create a new branch on github called develop). The files on develop (except for one) and master will be same as they are different views of same files

Now if you want to merge the changes made in develop branch into the master branch, then click on merge request in github. 
Whenever that request is accepted then the changes in develop branch will be merged into master branch. 
Now this can be pulled into your machine using git pull origin master.

Rebase-
——————
In Github, you can fork nornir into nornir which is basically making a copy. 
Later you make commits and changes to the original one, the updates might not be in the copy. 
You can do git rebase to update the copy with all the updates.

git fetch origin ( give me all the things that change in the origin) then go to the branch (2.0) that you want to update and  —>
git rebase origin/2.0

Useful links -
https://github.github.com/training-kit/downloads/github-git-cheat-sheet/
https://tutorialzine.com/2016/06/learn-git-in-30-minutes?__s=fem5hxy3xmx66jfao5wv
https://help.github.com/en/github/collaborating-with-issues-and-pull-requests/resolving-a-merge-conflict-using-the-command-line

'''

'''
#Concurrency vs Parallelism - Chcek out the graph from Kirk. Concurrency means over a short time multiple things are getting executed. It may
#or may not imply that they are executed in parallel.

#Ways to achieve to concurrency - Threads/Processes/Asynchronous (Threads and Processes in this course)

# Threads
#In a single process there could be multiple threads which job scheduler can pick which will allow us achieve concurrency.
#Eg. Multiple SSH sessions to different device. There could be potential race condition, also we need locks to gain access to a resource
#which can also lead to deadlock condition. Eg. Thread 1 gains a lock on some resource, thread 5 is then waiting and can reach deadlock.
#Global interpreter lock  - GIL - IF we have a single process, 50 threads, we can only run 1 thread at a time. (This would have been big deal if we
#were CPU bound but in network automation we are always IO bound. We are always waiting for remote device to respond. Hence, GIL Doesn't cause problem.

# Processes
# (50 individual processes as 50 ssh connections and say if we have 10 cpu's then 10/50 process will run at same time : Parallelism)
# In both Process/Threads the way to exchange info between them is difficult.
'''

'''
import os
import getpass
import requests                                                                       #Python requests library to do http get request
from requests.auth import HTTPBasicAuth
from pprint import pprint

from urllib3.exceptions import InsecureRequestWarning                                  #This is to ignore SSL Certificates for unsecured sites

requests.packages.urllib3.disable_warnings(category=InsecureRequestWarning)            #This is to ignore SSL Certificates for unsecured sites


if __name__ == "__main__":                                                             #Enter main part of the code

    username = "derahul9@gmail.com"
    password = getpass.getpass()                                                       #Getpass only works from terminal as pycharm and getpass have a different terminal window
    url = f"https://api.github.com/user"
    http_headers = {"accept": "Accept: application/vnd.github.v3+json"}                #Read the documentation to understand how to generate these values

    response = requests.get(url, headers=http_headers, auth=HTTPBasicAuth(username, password), verify=False)                   #verify false is to not verify SSL certificate
    response = response.json()

    print()
    pprint(response)
    print()

    response = requests.put(
        url, headers=http_headers, data=json.dumps(arista6), verify=False
    )

if __name__ == "__main__":                                                             #Enter main part of the code

    token = "63aa375e2590159ca3171c5269931043b85d33cf"                                 #Read the documentation to understand how to generate token
    url = "https://netbox.lasthop.io/api/dcim/devices/"
    http_headers = {"accept": "application/json; version=2.4;"}                        #Read the documentation to understand how to generate these values
    if token:
        http_headers["authorization"] = "Token {}".format(token)

    response = requests.get(url, headers=http_headers, verify=False)                  #verify false is to not verify SSL certificate
    response = response.json()

    print()
    pprint(response)
    print()
'''

'''
Intersection of two arrays
set.intersection(set1, set2 ... etc.)
'''