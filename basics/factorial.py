'''
    Author : Martand Singh
    Date: 16 Mar 2019
    Scope : Factorial
    Git: https://github.com/martandsingh/
    FB: https://www.facebook.com/codemakerz
    Youtube: https://www.youtube.com/martand89
    ## If you are feeling difficulty in any concept, let us know. We will get back to you
    with a step-by-step video tutorial for that topic.
    
    Remarks: 4! = 1 x 2 x 3 x 4 = 24, 0! = 1
'''

def factorial(num):
    if(num == 1):
        return 1
    else:
        return num * factorial(num-1)

_LONG_COMMENT = "-" * 50
print(_LONG_COMMENT) # This will print "-" 50 times.
print("Fibonacci Series")
print(_LONG_COMMENT) # This will print "-" 50 times.
num = 4
facto = factorial(num)
print("> factorial of %d is %d" %(num, facto))
print(_LONG_COMMENT) # This will print "-" 50 times.