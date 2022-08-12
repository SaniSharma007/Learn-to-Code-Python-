# Lecture 5 Functions and Modules
# pow abs round function
x = int(input("Enter a number:"))
# pow(): It is used to compute the exponential value.
print(pow(x,2))
# abs(): It returns the positive number value
print(abs(-11))
# round(): It is should for rounding off the value
print(round(35.5))
# Lecture 6 Module Method Function
# Module contain Pre-defined Functions
import math
# When you only import the module
# You call the function as a method
# That is using the object to call it, here it is module name
# Ceiling is the value above
print(math.ceil(44.3))
# Floor is the value below
print(math.floor(44.3))
from math import sqrt
# Calling a function does not require an object
print(sqrt(49))

