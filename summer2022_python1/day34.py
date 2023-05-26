# today we talk about dictionary

# when we want to create a dictionary we can do 

dic = {} # we will get a empty dictionary

print(dic,type(dic))

# in dictionary we always type {'key':'value'}  

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

'''
Dictionaries are used to store data values in key:value pairs.

A dictionary is a collection which is ordered*, changeable and do not allow duplicates.

Dictionaries are written with curly brackets, and have keys and values:

Dictionary Items

Dictionary items are ordered, changeable, and does not allow duplicates.

Dictionary items are presented in key:value pairs, and can be referred to by using the key name.

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict["brand"])

When we say that dictionaries are ordered, it means that the items have a defined order, 
and that order will not change.

Unordered means that the items does not have a defined order,
you cannot refer to an item by using an index.

Changeable

Dictionaries are changeable, meaning that we can change, 
add or remove items after the dictionary has been created.

Duplicates Not Allowed
Dictionaries cannot have two items with the same key:


thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964,
  "year": 2020
}
print(thisdict)
'''

# Accessing Items
# You can access the items of a dictionary by referring to its key name, inside square brackets:

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
x = thisdict["model"]

# There is also a method called get() that will give you the same result:

x = thisdict.get("model")


