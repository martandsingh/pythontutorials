'''
    Author : Martand Singh
    Date: 14 Mar 2019
    Scope : Basic list operations in python.
    Git: https://github.com/martandsingh/
    FB: https://www.facebook.com/codemakerz
    Youtube: https://www.youtube.com/martand89
    ## If you are feeling difficulty in any concept, let us know. We will get back to you
    with a step-by-step video tutorial for that topic.
    
    REMARKS: Python list is mutable. We can save heterogeneous datatypes in lists. List always enclose
    its item in SQUARE BRACKETS([]).
'''
_LONG_COMMENT = "-" * 50

print(_LONG_COMMENT) # This will print "-" 50 times.
print("List Operations")
print(_LONG_COMMENT) # This will print "-" 50 times.

X = [0, 13, 43, 654, 12] # Homogeneous datatype list
Y = [23, 'Hello', 4.5, "World", 45, 67.45] # Heterogeneous datatype list

print("> Original list X: ", X) # Print the whole list
print("> Indexing(3rd element): ", X[2]) # Print second index(3rd item.. 0, 1, 2th)
print("> Indexing again(Second last element):", X[-2]) # Print Second last item
print("> Slicing: ", X[1: 3]) # Print 1st(include) index to 3rd(excluded) index.
print("> Slicing again(second last to end): ", X[-2:]) # Print from second last to end.
print("> List concatenation: ", X + Y) # Append two lists
print("> List concatenation again: ", X + [34, 45, 67, 1000]) # Append two lists
print("> Scalar multiplication: ", X * 2) # append the same list to original list
print("> Original List Y: ", Y)
Y[0] = "New Value" #  Mutable Example : We are changing the 0th index value to "New Value"
print("> List Y after 0th element value reassigned: ", Y)
Z = [X, Y] # This will create a nested list. List of list. Length of Z will be 2.
print("> Nested list Z: ", Z)
print("> Length of list: ", len(X)) # Calculate the length or total number of element in list
X.append(999) # Append a new item to the end of the list X
print("> New item 999 is added at last: ", X)
X.insert(2, 1909090) # 1909090 added to 2nd index(3rd item)
print("> X - after adding 1909090 as 3rd item: ", X)
X[2:4] = [8888, 9999] # Slice assignment. Slice will give you 2nd, 3rd element(2 values) which u can assign by a new list
print("> New values assigned to 2nd, 3rd elementi in X: ", X) 
X[2:4] = [] # this will delete the 2nd & 3rd value from the list X
print("> 2nd and 3rd value removed from the list X: ", X)
#Sorting
X.sort()
print("> Sorted X: ", X)
#Reverse
X.reverse()
print("> List reveresed: ", X)
X.remove(999) # Removes 999 from the list
print("> 999 item removed from X: ", X)
# Minimum value
print("> X - Minimum value: ", min(X))
# Maximum value
print("> X - Maximum value: ", max(X))
(_LONG_COMMENT) # This will print "-" 50 times.