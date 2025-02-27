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
Palindrome = a word, phrase, or sequence that reads the same backward as forward
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

'''
c = array.count(item_in_array)
'''

'''
Merge last 2 commits: git rebase -i HEAD~2
git branch: useful if you're working on multiple dev tasks and want to switch between them
git checkout: switch to a branch
sync with master: git pull --rebase
'''

'''
Local vs Global var
local can be called within the function only. if called outside it errors out vs global can be called from anywhere.
To modify a global variable inside a function, use global keyword:
global_var = 10
def mod_glo():
    global global_var
    global_var = global_var +5
'''

'''
***Jinja (Temp AND Var in Same file):
from jinja2 import Template

bgp_config = """
router bgp {{ bgp_as }}
  bgp router-id {{ router_id}}
  bgp log-neighbor-changes
  neighbor {{ peer1 }} remote-as 44
"""

my_vars = {
    "bgp_as": 22,
    "router_id": "1.1.1.1",
    "peer1": "20.20.20.20"
}

j2_temp = Template(bgp_config)
#########output = j2_temp.render(**my_vars)    #my_vars will render the dictinary my_vars and pass it as key value pairs
##########output = j2_temp.render(bgp_as=22, router_id="1.1.1.1", peer1="2.2.2.2") #Also can be done this way
print (output)

Jinja (Temp AND Var in different file using Environment):

***Jinja (Temp AND Var in diff file):
# Environment is used for the following benefits -
# if your template is in a different folder then environment can be used (file handling)
# Also, if a variable is left blank it won't throw an error but just fill that part in the template with blank value. Environment will take care of this.
# if your template has reference to other templates, environment will make that possible as well.

from __future__ import unicode_literals, print_function
from jinja2 import FileSystemLoader, StrictUndefined
from jinja2.environment import Environment

env = Environment(undefined=StrictUndefined)                  #Whenever any variable is undefined throw an error. This is useful for error handling.
env.loader = FileSystemLoader([".", './Templates/'])            #This is to take the file from a directory which is defined. It will look one at a time current directoty --> Template

my_vars = {
    "bgp_as": 22,
    "router_id": "1.1.1.1",
    "peer1": "20.20.20.20"
}

template_file = 'bgp_config.j2'
template = env.get_template(template_file)
output = template.render(**my_vars)
print(output)

****Visa Router Upgrade script
import jinja2
import csv

user_in_file = input("Please enter the variable file? ")
user_in_file1 = input("Please enter the template file? ")
local_datadir = r'/home/rahul/Documents/Python_Projects/Python/Jinja2/variables/'
local_datadir1 = r'/home/rahul/Documents/Python_Projects/Python/Jinja2/Templates/'
local_datadir_out = r'/home/rahul/Documents/Python_Projects/Python/Jinja2/variables/'

input_file = local_datadir + user_in_file + ".csv"
with open(input_file) as f:
 read_csv = csv.DictReader(f)
 for vars in read_csv:
     Change_Number = vars['Change_Number']
     Router_A = vars['Router_A']
     template_file = local_datadir1 + user_in_file1 + ".j2"
     with open(template_file) as a:
          corporate_template = a.read()

     template = jinja2.Template(corporate_template)
     output_file = local_datadir_out + Change_Number + "_" + Router_A + "_" + "Install_Backout_Script"+ ".txt"

     output = open(output_file, "a")

     with open(output_file, 'a') as f:
          output.write(template.render(vars))

     output.close()
'''

'''
from ipaddress import ip_address, IPv4Address 
  
def validIPAddress(IP: str) -> str: 
    try: 
        return "IPv4" if type(ip_address(IP)) is IPv4Address else "IPv6"
    except ValueError: 
        return "Invalid"
'''

'''
opening a file and reading:

with open('file.txt', 'r+') as file: #with open makes sure file is closed. r+ means read plus write
    content = file.read() 
print(content)

    for line in file:   #reading line by line
        print(line)

Another way:
file = open('file.txt', 'r') 
content = file.read()
print(content)
file.close() # If file is opened this way then will have to explicitly close it

# Write new content (this will overwrite the content from the start)
    file.write("This is the new content!")

The file pointer moves as you read or write, so you may need to use seek() to move it to the position you want (e.g., to overwrite content).
r+ does not append; it will overwrite content starting from the current file pointer position.

'a+': Opens the file for both appending and reading. If the file doesn't exist, it will create a new file.
Using 'a' or 'a+' mode does not overwrite the existing content, it just adds to it.
'''

'''
Big-O(n)
- n is the input, helps us determine algorithms worst case efficiency
- Ignores Constant, For example 5n --> O(n)
- X = 5 + (15*2) --> O(1)
- For loop, O(N)
- Qudaratic time, O(n**2)
- Binary Tree, O(log n)
'''

'''
Sorting Algorithms:

Bubble Sort is a simple comparison-based algorithm where adjacent elements are repeatedly swapped if they are in the wrong order.
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
Time Complexity: O(n**2)
Space Complexity: O(1)

Selection Sort works by repeatedly finding the minimum element and moving it to the sorted part of the array.
Insertion Sort builds the sorted array one element at a time, by inserting each element into its correct position.
Time Complexity: O(n**2)
Space Complexity: O(1)

Quick Sort is another divide-and-conquer algorithm that selects a pivot element and partitions 
the array into two sub-arrays, then sorts them recursively.
Time Complexity: O(n**2)
Space Complexity: O(logn)

Merge Sort is a divide-and-conquer algorithm that splits the array into halves, sorts each half recursively, and then merges them back together.
Tim Sort is a hybrid sorting algorithm derived from Merge Sort and Insertion Sort. It is the default sorting 
algorithm in Python's sorted() function and list.sort() method.
Time Complexity: O(nlogn)
Space Complexity: O(n)

def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]

        merge_sort(left_half)
        merge_sort(right_half)

        i = j = k = 0
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1

Heap Sort is based on a binary heap data structure. It transforms the array into a heap and then repeatedly 
extracts the maximum element (for ascending order) and places it in its correct position.
Time Complexity: O(nlogn)
Space Complexity: O(1)
'''

'''
Regex
# \D - opposite of \d, matches anyhting other than digits
# \W - Matches everything but not letters, numbers or _ character. It matches space
# \S - Anything apart from space
# \A - Match first letter. \Z - Match last letter.
# [a-z] - Will give all small characters
# [^a] - Everything except a
# [135] - This will match any of 1,3 or 5
# or operator example i.e. |. If 1st group matches then 2nd group won't be matched
# ^ acts like negation as well as start of a line character too
# $ acts like a end of character

arp = "22.22.22.1  0   b4:a9:5a:ff:c8:45  VLAN#222    L 33.32.12.222"
a = re.findall(r"\d\d+\.\d{2}\.[0-9][0-9]\.[0-9]{1,3}", arp)  #findall method returns all the matches in form of list
print (a)
b = re.search(r"(.+?) +(\d) +(.+?)\s{2,} (\w)*", arp) 
print (b.group(1))
c = re.search(r"\d\d+\.\d{2}\.[0-9][0-9]\.[0-9]{1,3}", arp)   #Search method returns only the first match
print (c.group())
'''

'''
17th Feb - 16th March (4 Weeks) - Networking(1/2) + MPLS/Behavioral/Resume(3) + Amazon&Visa Network/Tools/Code/Projects/Planning/Sys Design(4)
17th March - Apply+Interview
'''
