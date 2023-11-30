'''
lst = ['apple','banana','cherry','dragonfood'] #''dragonfood'apple','banana','cherry', ''cherry','dragonfood'apple','banana'

for i in range(4):
    popedElement = lst.pop()

    lst.insert(0 ,popedElement)

    print(lst)

'''

lst = ['apple','banana','cherry','dragonfood']
#         0        1        2        3
# feature 1, it has index 

print(lst[2])

# list is a CRUD data structure, C(create, retrieve, UPDATE, Delete)
# C
lst.append('pear')
lst.insert(2,'orange')
print(lst)

# R
'''
print(lst[4])
for item in lst:
    print(item)

# if orange in our lst
count = 0
for item in lst:
    if item == 'cube':
        count += 1

if count > 0:
    print('yes')
else:
    print('no')

# len(lst) it will tell us the length of lst

for index in range(len(lst)):
    print(lst[index])


# UPDATE, if we want to change the element with a certain index, we must use index to change

lst[3] = 'avocado'

for index in range(len(lst)):
    if lst[index] == 'dragonfood':

        lst[index] = 'blueberry'

print(lst)
# if we want to change index 4 with a fruit you like
'''

#Delete
print(lst)
lst.pop()
lst.remove('orange')
print(lst)

'''
# make a list

add some study tools pen, pencil ...

show me CRUD for the coding

you also need to rotate
'''


   