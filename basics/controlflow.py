'''
    Author : Martand Singh
    Date: 14 Mar 2019
    Scope : control flow in python
    Git: https://github.com/martandsingh/
    FB: https://www.facebook.com/codemakerz
    Youtube: https://www.youtube.com/martand89
    ## If you are feeling difficulty in any concept, let us know. We will get back to you
    with a step-by-step video tutorial for that topic.

'''
_LONG_COMMENT = "-" * 50

print(_LONG_COMMENT) # This will print "-" 50 times.
print("Control Flow In Python")
print(_LONG_COMMENT) # This will print "-" 50 times.

#if else loop
P = 70

if(P < 100):
    print("P is less than 100.")
elif(P == 100): #else if condition
    print("P is equals to 100.")
else:
    print("P is greater than 100.")

# for loop - range
print("Loop within a range:")
for item in range(0, 10): # this is loop from 0 to 9
    print("Item no: ",  item)

# for loop for a list
print("\nLoop with in a list: ")
X = ["Hello", "CodeMaker", 34, 23, 45.64, "Welcome"]
for item in X:
    print("Item: ", item)

# break and continue statement
for item in range(10):
    if item == 7 :
        print("break executes.")
        break # this iwll break the loop and will execute next statement after the loop
    elif (item == 4):
        print("continue....")
        continue # this will continue loop to the next execution. Statement after this iwll not get executed.
        print("After continue") # this will not get printed.
    else:
        print("Number: ", item)

# pass statement - it does nothing. it is like empty functionality
if len(X) > 0:
    pass # it is like empty body

# while loop
P = 0
while (P != 10):
    print("X: ", P)
    P += 1


print(_LONG_COMMENT) # This will print "-" 50 times.

