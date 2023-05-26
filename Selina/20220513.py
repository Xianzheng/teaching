# str , iist, dict, set, tuple

#string = 'content'

#lst = []

#dic = {'key': 'value}

#s = {'a',} # set()

#tuple ()

t = tuple()

# immutable

# string = 'Mark'
#
# string[3] = 'c'

# t = ('Mark','Selina')
#
# t[0] = 'Ella'

# tuple is immutable

t = ('apple','banana','cherry')

#       0        1        2
lst = ['apple','banana','cherry']

#        0       1        2

# print(t[0])# be care of index out of range
# print(lst[0])# be care of index out of range

lst.append('peach') # create
# print(lst)
lst[0] = 'piapple' # update
# print(lst)
lst.pop(0) #delete
# print(lst)

# tuple is immutable, read-only , lst is CRUD data structure

# CRUD
# C: CREATE, R:READ, U:UPDATE,D:DELETE

# use index to read element of object
print(t[0]) # read
print(lst[0])#read

for item in t:
    print(item)

for item in lst:
    print(item)

# tuple gets more security, is more secure

def addTimes(a,b):

    return a + b, a * b

res = addTimes(10,19)
print(res, type(res))

# review 5 datatype str , iist, dict, set, tuple

# summerize how  to use them, give a example

# compare and contrast tuple and str, tuple and str