import sys

'''
They not only help solve popular problems like race conditions but are also very useful in controlling errors in areas like loops, file handling, database communication, 
network access and so on. Hence, we’ll cover broader problems and provide solutions in this post. Please note that exception handling is an art which brings you immense 
powers to write robust and quality code. So, brace to read some keynotes on exceptions along with the best ways to handle them
'''

for i in range(3):
    print (i)
    try:
        print (sys.argv[i])
    except IndexError:
        print ("List Index out of range error in the program {}".format(sys.argv[0]))
    except ValueError:
        print ("Can't convert into integer in the program {}".format(sys.argv[0]))
    finally:
        print ("bye")

