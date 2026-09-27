"""
#Create a variable inside a function, with the same name as the global variable
x = "awesome"

def myfunc():
    x = "fantastic"
    print("Python is " + x)

myfunc()

print("Python is " + x)
"""

#THE GLOBAL KEYWORD
"""
#To create a global variable inside a function, use the global keyword.

def myfunc():
    global x
    x = "fantastic"

myfunc()

print("Python is " + x)
"""

#To n




