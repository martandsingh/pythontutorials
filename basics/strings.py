'''
    Author : Martand Singh
    Date: 14 Mar 2019
    Scope : Basic string operations in python.
    Git: https://github.com/martandsingh/
    FB: https://www.facebook.com/codemakerz
    Youtube: https://www.youtube.com/martand89
    ## If you are feeling difficulty in any concept, let us know. We will get back to you
    with a step-by-step video tutorial for that topic.
    REMARK: Python strings are immutable
'''
_LONG_COMMENT = "-" * 50

X = "Hello"
Y = "World"
P = "Python"

print(_LONG_COMMENT) # This will print "-" 50 times.
print("String Operations")
print(_LONG_COMMENT) # This will print "-" 50 times.

print("> Concatenation: ", X+Y) # Concatenates the string
print("> Concatenation again: ", 'Hello' ' World') # It two single quote text written continously it will concatenated
print("> Escape character: \n New Line") # Send the "New Line" text to new line.
print("> Escape character: \a Alert") # Make a system sound
print("> Escape character again: \'\' ") # Print single quotes
print('> Single quote use: ""') # Print double quotes
print(r'> C:\some\name') # Raw character, if we don put r then \name will be "New Line + ame"
print("""
> Hello
    This is multiline comment
    using double quotes
""") # Multiline comments with double quotes

print('''
> Bye
    This is multiline comment
    using single quotes
''') # Multiline comments with single quotes
print("> Repeat text: ", "#"*20) # This will print hash 20 times
print("> Index: ", P[0]) # This will print first character
print("> Index again: ", P[-1]) # this will print the last character of the string
print("> Slicing: ", P[0:3]) # this from 0(included) index to 3(excluded) index.. 0th, 1st, 2nd character
print("> Slicing again: ", P[:2]) # Character from begining to position 2 (Not index)
print("> Slicing again: ", P[:2] + P[2:]) #  s[:i] + s[i:] is always equal to s:
print("> Slicing again: ", P[-2:]) # Chracter from second last to end
print("> Length of the string: ", len(P))

print(_LONG_COMMENT) # This will print "-" 50 times.
