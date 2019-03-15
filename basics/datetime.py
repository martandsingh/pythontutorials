'''
    Author : Martand Singh
    Date: 14 Mar 2019
    Scope : Basic datetime operations in python.
    Git: https://github.com/martandsingh/
    FB: https://www.facebook.com/codemakerz
    Youtube: https://www.youtube.com/martand89
    ## If you are feeling difficulty in any concept, let us know. We will get back to you
    with a step-by-step video tutorial for that topic.
    
    REMARKS: To use datetime in python we need to import time module.
    Particular instants in time are expressed in seconds since 12:00am, January 1, 1970(epoch).
'''
import time  # This is required to include time module.

_LONG_COMMENT = "-" * 50

print(_LONG_COMMENT) # This will print "-" 50 times.
print("Datetime Operations")
print(_LONG_COMMENT) # This will print "-" 50 times.

ticks = time.time()
print("> Number of ticks since 12:00am, January 1, 1970:", ticks) # Time is calculated in form of number of ticks.
localtime = time.localtime(time.time()) # This will return a structure of time.
print("> Local current time :", localtime)
#Formatted time
localtime = time.asctime( time.localtime(time.time())) # This will provide an formatted date time string
print ("> Formatted local current time :", localtime)
print(_LONG_COMMENT) # This will print "-" 50 times.