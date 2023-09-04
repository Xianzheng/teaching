'''
# data(variable)

a = 1 
b = 1.123
print(a)
print(b)
'''

# a is varible
# 1 is data
# 1 is int
'''

# data structure
# string is a data structure since in a string contains a lot data
# string is read only (immutable)
c = 'Hello' # c = 'H' + 'e' +'l' +'l' +'o'

#ind 01234
print(c[0])
print(c[1])
print(c[2])
print(c[3])
print(c[4])

# c[0] = 'L' #(we can not do)
# if we really want to change some character
c1 = c.replace('H','L')
print(c1)


# list, list is a powerful data structure

lst = ['H','e','l','l','o']

# lst is CRUD(create, retrieve, update, delete)

# read is part of retrieve
print(lst[0])
print(lst[1])
print(lst[2])
print(lst[3])
print(lst[4])
# function
lst[0] = 'L'
print(lst)
lst.pop() # it will delete last element of lst
print(lst)
'''
#practice(CCC 2020 J4)

str1 = 'ABCCDEABAA'
str2 = 'ABCDE'

# how do we know str2 is in str1
# slice (cut some part from string)
# print(str1[0:5])
# print(str1[1:6])
# print(str1[2:7])
'''
flag = False
for i in range(0, len(str1)-len(str2)):
    cut = (str1[i:i+len(str2)])
    if cut == str2:
        flag = True

print(flag)
'''
#(python way)
if (str2 in str1) == True:
    print('yes')
else:
    print('no')
        
#advanced function

# class
print(str1.count('A'))
print(str1.count('B'))

'''
hw:

write the code and command explain to me 

1. conpare and contrast the data structure string and list

2. do slicing for 'mark.ffang@gmail.com' to get the useful info(first name, last name)

3. str1 = 'hello world str2 = ' world', check is str2 in str1
(* try use two way, to check, demo code provided)
# flag = False
# for i in range(0, len(str1)-len(str2)):
#     cut = (str1[i:i+len(str2)])
#     if cut == str2:
#         flag = True

'''




