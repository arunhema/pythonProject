"""
multiline Comments
# single line comment
shortcut cmd + /

1)  Escape character
    Data Type - Int, Str, Boolean

2)  Keyword

3)  Basic Calculation

4)  Print Statement

"""

import keyword
print(keyword.kwlist)
print(keyword.iskeyword('False'))

print('hello world')
#Hi 'Arun' Welcome to python "Day 1"

print("Hi \'Arun\' Welcome to paithon " '"Day 1"')

a = 25
b = 4
print(a + b)  # 29
print(a / b)  # 6.25
print(a // b)  # 6
print(a % b)  # 1

x = True
y = False
print(int(x))
print(int(y))

print(type(a))
a='a'
print(type(a))
a=True
print(type(a))

print ("This is a concatenation"+"of string in print satement")
print ("This is a concatenation","of string in print satement")

print ("Hema"+"Arun")
print ("Hema","Arun")

print (int(True))
print (int(False))