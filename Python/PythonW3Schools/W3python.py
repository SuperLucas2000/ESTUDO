"""
# In python, a variable is created when you assign a value to it:
x = 5
y = "Hello, World!" 
"""
#STATEMENT---------------------------------------------
"""
#A statement in python usually ends when the line ends.
#There's no need to use a semicolon.
print ("Python is fun!")
"""
#STATEMENT2---------------------------------------------
"""
#The statements are executed one by one, in the same order as they are written.
print("Hello World!")
print("Have a good day.")
print("Learning Python is fun!")
"""
#PRINT TEXT---------------------------------------------
"""
# By default, the print() function ends with a new line, to print multiple words on the same line, use the end parameter.
print("Hello World!", end=" ")
print("I will print on the same line.")
"""
#PRINT NUMBERS---------------------------------------------
"""
# To print numbers, just write them inside, without quotes.
print(3)
print(358)
print(50000)

# To mix text and numbers, separate them with a comma.
print("I am", 24, "year old.")
"""
#VARIABLES---------------------------------------------
"""
#A variable is created the moment you first assign a value to it
x = 5
y = "John"
print(x)
print(y)
"""

#CASTING
"""
#If you want to specify the data type of a variable, this can be done with casting.
x = str(3)    # x will be '3'
y = int(3)    # y will be 3
z = float(3)  # z will be 3.0
"""

#GET THE TYPE
"""
#You can get the data type of a variable with the type() function.
x = 5
y = "John"
print(type(x))
print(type(y))
"""

#It is possible to assign values to multiple variables in one line

"""
x, y, z = "Orange", "Banana", "Cherry"
print(x)
print(y)
print(z)
"""

#ONE VALUE TO MULTIPLE VARIABLES

"""
x = y = z = "Orange"
print(x)
print(y)
print(z)
"""

#UNPACK A COLLECTION

#If oyu have a collection os values in a list, tuple etc.
#Python allows you to extract the values into variables, this is called unpacking.

#Unpack a list

fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
print(x)
print(y)
print(z)







