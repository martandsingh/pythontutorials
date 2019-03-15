'''
    Author : Martand Singh
    Date: 14 Mar 2019
    Scope : Basic dictionary operations in python.
    Git: https://github.com/martandsingh/
    FB: https://www.facebook.com/codemakerz
    Youtube: https://www.youtube.com/martand89
    ## If you are feeling difficulty in any concept, let us know. We will get back to you
    with a step-by-step video tutorial for that topic.
    
    REMARKS: Python dictionary is immutable(You can not change an existing tuple). 
    A dictionary is a collection which is unordered, changeable and indexed. 
    In Python dictionaries are written with curly brackets, and they have keys and values.
    Keys are unique within a dictionary while values may not be. The values of a dictionary 
    can be of any type, but the keys must be of an immutable data type such as strings, numbers, or tuples.
'''
_LONG_COMMENT = "-" * 50

print(_LONG_COMMENT) # This will print "-" 50 times.
print("Dictionary Operations")
print(_LONG_COMMENT) # This will print "-" 50 times.

dict = {"name" : "Martand Singh", "tech" : "python 3.0"} # Dictionary with two keys name & tech
newdict = {"project" : "project war", "designation" : "Tech Architect"}
print("> Original dictionary: ", dict) # Print the origial dictionary
print("> Name key: ", dict['name']) # Print the value associate with the name key
dict['name'] = "CodeMaker" # This will update the value of name key
print("> Updated dictionary - name value changed: ", dict)
# Add a new key to dictionary
dict['address']  = "New Delhi, India" # It will update or add(if there is no key named address) to the dictionary
print("> Dictionary after adding one more key: ", dict)
del dict['address'] # Delete the address key from the dictionary
print("Dictionary after deleting address key: ", dict)
A = len(dict) # It will calculate th length of the dictionary
print("> Length of dictionary: ", A)
B = str(dict) # It will provide a printable string of dictionary
print("> Dictionary string: ", B)
print("> Dictionary items: ", dict.items()) # Will give the list of all the key value tuples
all_keys = dict.keys() # It provides all the keys of the dictionary
all_values = dict.values() # It provides all the value of the dictionary
print("> All keys: ", all_keys)
print("> All values: ", all_values)
print("> Is name key exists: ", 'name' in dict) # It will print boolean value whether key exists or not
dict.update(newdict) # It will add newdict to dict as key-val pair
print("> Dictionary after updating: ", dict)
print("> Getting dict key value: ", dict.get('name')) # It will also get the keyvalue
# If there is no key present then it will provide you the default value XXX. You can use any.
print("> Getting dict key value with default value if it doesn't exists: ", dict.get('name2', "XXX")) # It will also get the keyvalue

dict.clear() #  It will clear the all the key-value pairs from the dictionary
print("> Dictionary after clearing all the key-val pair: ", dict)
del dict # It will delete the complete dictionary object
#print(dict['name']) # It will throw error as we have already delete the entir dictionary

print(_LONG_COMMENT) # This will print "-" 50 times.