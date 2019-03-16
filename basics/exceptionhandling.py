'''
    Author : Martand Singh
    Date: 16 Mar 2019
    Scope : Exception Handling
    Git: https://github.com/martandsingh/
    FB: https://www.facebook.com/codemakerz
    Youtube: https://www.youtube.com/martand89
    ## If you are feeling difficulty in any concept, let us know. We will get back to you
    with a step-by-step video tutorial for that topic.
   
'''
# Simple try-catch block
def divide(x, y):
    try:
        return x/y
    except Exception as err:
        print("Exception occured: ", err)

# Specific exception - If you know the exact exception
def divideSpecific(x, y):
    try:
        return x/y
    except ZeroDivisionError as err:
        print("Exception occured: ", err)

# Multiple catch block for the same try 
def divideMultiCatch(x, y):
    try:
        return x/y
    except ZeroDivisionError as err: # Specific exception
        print("Specific Exception occured: ", err)
    except Exception as err: # Generic exception
        print("Generic Exception occured: ", err)

# Multiple exceptios in same except
def divideMultiErrorSameCatch(x, y):
    try:
        return x/y
    except (RuntimeError, TypeError, NameError) as err: # multiple exception in same except
        print("Specific Exception occured: ", err)
    except ZeroDivisionError as err: # single specific exception
        print("Zero Divide Exception occured: ", err)
    except Exception as err: # Generic exception
        print("Generic Exception occured: ", err)

# Throw exception
def raiseException(n):
    if(n > 10):
        raise Exception("Value is too high.")


divide(20, 0)
divideSpecific(23, 0)
divideMultiCatch(78, 0)
divideMultiErrorSameCatch(23, 0)
raiseException(12) # This will throw the exception