'''
https://www.youtube.com/watch?v=ZDa-Z5JzLYM
Classes allow reusability of data and functions
Method is a function associated with a class
Instance variables are unique to each instance. If the variables are common all across then they can be defined in the class itself
Create special init method inside the class. When we create methods inside a class, it receives the firt argument automatically which by convention is called "self".
The self argument helps to map an instance to other variables as seen, self.first, self.last etc. maps to emp_1.first, emp_1.last etc.
first, last, email, pay are all attributes of the class

The __init__ method is similar to constructors in C++ and Java. Constructors are used to initialize the object’s state. The task of constructors is to initialize(assign values)
to the data members of the class when an object of class is created. Like methods, a constructor also contains collection of statements(i.e. instructions) that are executed at
time of Object creation. It is run as soon as an object of a class is instantiated. The method is useful to do any initialization you want to do with your object.
'''

class Employee:

    num_of_emps = 0                   #class variable
    raise_amount = 1.04               #class variable that will be used within a method. You can just update this value and will apply to all the employees

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.email = first + "." + last + "@company.com"
        self.pay = float(pay)

        Employee.num_of_emps += 1   #This will increment the value everytime a new object is initialiazed.

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)

emp_1 = Employee('rahul', 'de', '100000')
emp_2 = Employee('heena', 'agrawal', '100000')
#print (emp_1.last)

#print ('{} {}'.format(emp_1.first, emp_1.last)) #using placeholders and format. Now we can add this as a method to our class which can be used for other instance too.

print (emp_1.fullname())
print (emp_2.fullname()) # Remember the use of self. When we call this, emp_2 is passed as an argument to the fullname method in the class. That is why we need self bydefault to
                         # avoid argument mismatch
print (Employee.fullname(emp_1)) # Another way of doing this is calling the class name.method name and passing the instance as a vriable

print (emp_1.__dict__) #Returns the value of emp_1 object as a dictionary
print (Employee.num_of_emps)
emp_1.apply_raise()
print (emp_1.pay)


