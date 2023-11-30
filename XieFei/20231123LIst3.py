'''
lst = ['pensil','pen','eraser','paper']
print(lst)

lst.append('ruler')
lst.insert(3, 'highlighter')
print(lst)

print(lst[3])
for item in lst:
    print(item)

lst[1] = 'book'
for index in range(len(lst)):
    if lst[index] == 'pen':
        lst[index] = 'book'

print(lst)
lst.pop(3)
lst.remove('paper')
print(lst)


#how to convert string to list

# string convert to integer
str1 = '1'
print(str1)
print(type(str1))

num1 = int(str1)
print(num1)
print(type(num1))

num2 = 2
strNum2 = str(num2)
print(type(strNum2))


# string con convert to list each other
string = '12 +'
lst = string.split()
print(lst[0],lst[1])

string1 = '1200    -'
lst1 = string1.split()
print(lst1[0],lst1[1])

string3 = 'banana'
#index    012345
lst3 = list(string3)
print(lst)

string = '100100'# ''101000
#index    012345
# string is a read only data structure, list is a CRUD strucure
# string  is only surport to read

# string can convert to list
lst = list(string)
lst[2],lst[3] = lst[3],lst[2]

print(lst)

#how to make our list to our string


# we need to remember if we want to convert list to string
string2 = ''.join(lst)
print(string2)
'''
# if we want to extract important thing from our string, but there are seperate
# by space of certain character we want do split
string = '1@2@3@4'
lst = string.split('@')
print(lst)

string = '1 2 3 4'
# split()# default in bracket is space
lst = string.split()
print(lst)

string = 'abcde' #eabcd
# convert string list
lst = list(string)
# make change in list
poped = lst.pop()
lst.insert(0,poped)
print(lst)
# convert list to string 
string = ''.join(lst)
print(string)

'''
string = 'bcdef'
# cbdef
# cdbed
# cdebf
# cdefb
'''