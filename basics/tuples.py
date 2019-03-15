'''
    Author : Martand Singh
    Date: 14 Mar 2019
    Scope : Basic tuples operations in python.
    Git: https://github.com/martandsingh/
    FB: https://www.facebook.com/codemakerz
    Youtube: https://www.youtube.com/martand89
    ## If you are feeling difficulty in any concept, let us know. We will get back to you
    with a step-by-step video tutorial for that topic.
    
    REMARKS: Python tuples is immutable(You can not change an existing tuple). 
    We can save heterogeneous datatypes in lists. tuple always encloses its item in parantheses().
'''
_LONG_COMMENT = "-" * 50

print(_LONG_COMMENT) # This will print "-" 50 times.
print("Tuple Operations")
print(_LONG_COMMENT) # This will print "-" 50 times.

X = () # Empty tuple
Y = (1, 34, 23, 54, 100) # Homogeneous tuple - Same datatypes
Z = ("Hello", "World", 12, 43, 45.43, "Bye") # Heteregenous tuple - Different datatypes
P = "hello", "world", "hi", "bye" # tuple without parantheses

print("> X - Empty tuple: ", X) # Print empty tuple
print("> Y - homogenous tuple: ", Y) # Print Y - tuple with same data-type
print("> Z - heterogeneous tuple: ", Z) # Print Z - tuple with different data-type
print("> P - tuple without parantheses: ", P) # Print P - Comma seperated tuple
#immutability
#P[0] = "Martand"  # this statement is not allowed. It will give you an exception.
print("> Length of tuple Y: ", len(Y)) # Prints the length or total number of item in tuple
#Just like list tuple also support indexing and slicing
print("> First item of Y: ", Y[0]) # indexing in tuple
print("> First three item of Y using slicing: ", Y[0:2]) # Print item 0th, 1st
print("> Second last item of Y: ", Y[-2]) # Print the 2nd element from the last
#Two tuples can be added just like list
result_tuple = Y + Z
print("> Result tuple (Y + Z)", Y+Z) # It will combine two tuples
del Y # This will delete the tuple
# print("Y is deleted: ", Y) # This will throw an error - Y is undefined
A = (12,) # A - tuple with single element. To define a single element tuple you should end it with comma(,) at last
print("> A - Single element tuple: ", A)
B = ("Hello",) * 4 # This will add Hello 4 times in tuple B
print("> B - Repeated elements: ", B) 
#Memebership Check
print("> Hello exist in Z: ", 'Hello' in Z) # This will return boolean variable to show whether Z contain Hello or not?
#Iteration
for item in Z:
    print("> ", item)

Y = (12, 3, 4, 123, 9, 42)
# Minimum value
print("> Y - Minimum value: ", min(Y))
# Maximum value
print("> Y - Maximum value: ", max(Y))

print(_LONG_COMMENT) # This will print "-" 50 times.
