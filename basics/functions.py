'''
    Author : Martand Singh
    Date: 14 Mar 2019
    Scope : functions in python
    Git: https://github.com/martandsingh/
    FB: https://www.facebook.com/codemakerz
    Youtube: https://www.youtube.com/martand89
    ## If you are feeling difficulty in any concept, let us know. We will get back to you
    with a step-by-step video tutorial for that topic.

    REMARKS: In python we defined functions with def keyword.

'''
_LONG_COMMENT = "-" * 50

print(_LONG_COMMENT) # This will print "-" 50 times.
print("Functions In Python")
print(_LONG_COMMENT) # This will print "-" 50 times

# define a basic functions with no arguements and empty functionality (pass). 
def sayHello():
    pass # this function will not do anything. but syntactically it is correct.

def sayHelloNow():
    print("Hello From Python Function... It is so cool !!!")

#calling functions
sayHello() # it will do nothing.
sayHelloNow() # it will print above mentioned text.

# function with parameter.
def printMessage(name, msg):
    print("Heya...", name, "!!!", msg)

# call function
printMessage("Stranger", "Welcome to the codemaker...!!!")

# function with default parameter. If we assign a default value to parameter then it is optional. We may or may not provide it.
def sayHelloAgain(msg, name = "Anonymous"): # here if no value for name is provide then it will take it as "anonymous"
    print("Hello ", name, "!!!", msg)

#call func
sayHelloAgain("Welcome to the codemaker") # with one arguement
sayHelloAgain("Welcome to the codemaker", "Martand") # with two arguement.

# Named arguement. Till now we were providing arguement in the exact same order as function definition.
# but we can change it using named arguement.
printMessage(msg = "I should be the second arguement but  here i am first", name = "Martand") # here we mentioned arguement with their names. So here order doesnt matter. 

# lambda functions
mylamfunc = lambda a, b : a*b # here x is a function which takes two args a, b and return a*b
print("Lambda function mylamfunc(5, 6): ", mylamfunc(5, 6))

# function with return type
def returnSum(a, b):
    return a*b

# call fucn
print("returnSum(6, 7) will give the product of given numbers: ", returnSum(6, 7))


print(_LONG_COMMENT) # This will print "-" 50 times
