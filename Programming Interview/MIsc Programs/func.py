# Remember there are local vars which can be used only in the fucntio. Global variables can be used outside the function and inside as well.

def test (a,b):                                      # Simple print function with parameters
    print (a)
    print (b)

#a = input("Enter parameter a:")
#b = input("Enter parameter b:")

#test ("hello", "hi")

def func1(x, *args):                                 # Args is an optional parameter, even if you don't pass it the functions still works
    print (x)
    print (args)

func1("hello", 100, 200)


def func2(x, *args):                                # * for positional argument and ** for keyword arguments
    print(x)
    for arg in args:
        print (arg)

func2("hello", 100, 200)

def my_sum (x, y):
    sum = x + y
    return sum

print (my_sum(x = 14, y = 5))
