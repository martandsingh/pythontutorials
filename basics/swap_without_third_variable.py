'''
    Author : Martand Singh
    Date: 16 Mar 2019
    Scope : Swap two numbers without using any third variable
    Git: https://github.com/martandsingh/
    FB: https://www.facebook.com/codemakerz
    Youtube: https://www.youtube.com/martand89
    ## If you are feeling difficulty in any concept, let us know. We will get back to you
    with a step-by-step video tutorial for that topic.
    
'''

def swap(a, b):
    print("Before Swap (a, b): ", a, b)
    a = a + b
    b = a - b
    a = a - b
    print(a)
    print(b)
    print("After Swap (a, b): ", a, b)

swap(3, 4)
