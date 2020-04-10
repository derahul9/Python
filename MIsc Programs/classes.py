# Python does OOP using classes. objects and methods. class is a data type that contains its own data type, functions (methods) and variables
# Object is instance of a class and attribute value defines that object
# Inheritance - a new class will inherit all functions from an existing class
# Class name should start with a capital letter
# There is a huge difference between a Class and a Function and it is just not only in python it is there in every Object Oriented Programming Language. So yeah,
# the difference is there even in the small programs and the property of Python to incorporate the Class is very significant in bigger projects.
# If we go literally a Class can be defined as a set or category of things having some property or attribute in common and differentiated from others by kind, type, or
# quality (copied from google definitions :P). So basically class is an encapsulation of data under a single entity and the data can be variables(called attributes) and
# functions(called methods), YES a function can be included in a class while a class can’t be a part of a function. Basically when we create classes we normally call the
# class or the functions(methods) enclosed in them using an Object. A class is basically a definition of an Object. While a function is merely a piece of code.
# To sum it up - Functions do specific things but classes are specific things.

class MyRouter(object):  # creating a class which inherts from the default "object" class
    def __init__(self, routername, model, serialno, ios):  # class constructor; initializing some variables and the method is called whenever you create a new instance of the class
        self.routername = routername  # "self" is a reference to the current instance of the class
        self.model = model
        self.serialno = serialno
        self.ios = ios

    def print_router(self, manuf_date):
        print("The router name is: ", self.routername)
        print("The router model is: ", self.model)
        print("The serial number of: ", self.serialno)
        print("The IOS version is: ", self.ios)
        print("The model and date combined: ", self.model + manuf_date)


router1 = MyRouter('R1', '2600', '123456',
                   '12.4')  # creating an object by simply calling the class name and entering the arguments required by the __init__ method in between parentheses

router1.model  # accessing the object's attributes; result is '2600'

router1.print_router("20150101")  # accessing a function (actually called method) from within the class





