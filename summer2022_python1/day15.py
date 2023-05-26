'''
homework

string1 = 'this is homework'

# write a programe to check whether character 'a' is in string1 # False

# write a programe to check whether character 'o' is in string1 # True

if i == 'a' 

# how many basic differnet type date structure in python , print it 
'''

from numpy import character


string1 = 'this is homework'

#          0123456789012345

'''

# method 1
character = 'o'

flag = 0 

length = len(string1) # to find the length of string

for index in range(length):

    if string1[index] == character:

        flag = 1

if flag == 0:
    print(False)
else:
    print(True)

# method 2
character = 'a'
if string1.find(character) != -1:
    print(True)
else:
    print(False)

'''
'''
string1 = 'it is beautiful day'

for eachCharacter in string1:

    print(eachCharacter)

'''

'''
# string is a immutable data type

# immutable means can not change itself


string1 = 'eech'

# index    0123

# = is a value giving sign

string1[1] = 'a'

print(string) # it will give a type error
'''
'''
# any input is a string

a = input('type anything\n')

print(a, type(a))

'''
'''
b = int(input('please type a number')) # convert what we type to a number

print(b,type(b))
'''

string1 = 'test find a character in string'

# using two method 1

# find if 'c' in string1 # print True

# using method 2

# find if 'd' in string1 # print True

# use for loop to print it