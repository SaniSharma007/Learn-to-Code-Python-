# Lecture 6 Data Structure
# String: Content in double or single quotes
str1='Single Quote is also string'
str2="Double Quote is a string too"
print(str1)
print(str2)
# Using backslash to add spl char
print(" This is \\n: it is used for breaking a line \n like this")
# Multiline String
print("""This 
is a 
multiline string""")
# Using raw string for addresses and locations
# Basically When the spl characters are many
path = r"C:\PythonPro\DataStr"
print(path)
# String Formatting
langname="Hindi"
print("{} is my mother tongue".format(langname))
frmtstr="{},{},{} are the positons".format("1","2","3")
print(frmtstr)
# Using the indexing in the format
idxfrmt="{0},{2},{1} are the best friends".format("sani","vaibh","varti")
print(idxfrmt)
# Using the numerical values in format
frmt="{price} is the current cost".format(price=96.67)
print(frmt)
revstr="This is my reversed string"
revstr=revstr[::-1]
print(revstr)
# Checking if a substring exist
print('py'in 'python')