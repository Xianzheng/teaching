'''
string = 'Python is a good programming language'
#         0123456789.....
print(string,type(string))

print(string[2:6])

print(string[7:9])


# list -> is a container
lst = [] # create a list
print(lst)

lst.append(1)
lst.append(2)
lst.append(3)

print(lst)
print(lst[1]) # use index to access the element
'''

lst = []
lst.append('apple') # add some thing to lst use .append
lst.append('banana')
lst.append('cherry')
print(lst)

lst[1] = 'peach'# update index 1
print(lst)

lastElement = lst.pop() # remove the last element of lst
print(lst)

lst.insert(0,lastElement) # add the element poped to the first
print(lst)

