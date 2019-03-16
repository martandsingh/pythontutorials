'''
    Author : Martand Singh
    Date: 16 Mar 2019
    Scope : Fibonacci Series
    Git: https://github.com/martandsingh/
    FB: https://www.facebook.com/codemakerz
    Youtube: https://www.youtube.com/martand89
    ## If you are feeling difficulty in any concept, let us know. We will get back to you
    with a step-by-step video tutorial for that topic.
    
    Remarks: 0 1 1 2 3 5 8 13.....
'''
endChar = " -> "
def fibonacci(totalCount):
    a = 0
    b = 1
    count = 1
    print (a, end = endChar)
    print (b, end = endChar)
    while(count != totalCount-1):
        c = a + b
        if(count <= totalCount - 3):
            print(c, end = endChar)
            
        else:
            print(c)
        a = b
        b = c
        count += 1

_LONG_COMMENT = "-" * 50

print(_LONG_COMMENT) # This will print "-" 50 times.
print("Fibonacci Series")
print(_LONG_COMMENT) # This will print "-" 50 times.
fibonacci(10)
print(_LONG_COMMENT) # This will print "-" 50 times.