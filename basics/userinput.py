'''
    Author : Martand Singh
    Date: 16 Mar 2019
    Scope : Take input from user for factorial programe
    Git: https://github.com/martandsingh/
    FB: https://www.facebook.com/codemakerz
    Youtube: https://www.youtube.com/martand89
    ## If you are feeling difficulty in any concept, let us know. We will get back to you
    with a step-by-step video tutorial for that topic.
    
    Remarks: 4! = 1 x 2 x 3 x 4 = 24, 0! = 1
'''

def factorial(num):
    if(num == 0):
        return 0
    elif(num == 1):
        return 1
    else:
        return num * factorial(num - 1)

_LONG_COMMENT = "-" * 50
print(_LONG_COMMENT) # This will print "-" 50 times.
print("Factorial")
print(_LONG_COMMENT) # This will print "-" 50 times.
# We will take num from user
num = int(input("enter the number: ")) # Type casting
fact = factorial(num)
print("> factorial of %d is %d" %(num, fact))
print(_LONG_COMMENT) # This will print "-" 50 times.