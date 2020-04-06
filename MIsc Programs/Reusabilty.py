#If we want to reuse a function or a piece of code then we can just copy paste it. Although as it gets complicated it becomes harder
#to figure out the mistakes. Also, if you need to enhance your block of code then you can do it only at one place. Hence, use import to reuse code

print ("Importable code")

def my_func():
    print ("Importable function")

def main():
    print("Executable code")

if __name__ == "__main__":       #__name__ is an internal variable in python that automatically gets set to __main__. This code is to execute in this program itself
    main()                       # Everything else can be imported. Advanced- You can write such codes and store it in a directory, then import entire directory as a package
                                 #For better visibilty you can just call the main function here and then define main, that works too.
