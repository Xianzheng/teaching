'''
HW:
1.

replace:

string = 'Mark Fang'

rotateStrintBack(string) =》 'ark FangM','rk FangMa' ....

get all possible change

2. string = 'Hi Justin Justin Kevin'

change first 'Justin' to 'Mark' string will be Hi Mark Justin Kevin'

change second 'Justin' to 'Pascal'string will be Hi Justin Pascal Kevin'
'''

string = 'abcde'# step1:['a','b','c','d','e']. step2:['a','b','f','d','e'] , step3 

#         01234
'''
str1 = 'ab'
str2 = 'de'
str3 = 'f'

string = str1 + str3 + str2
print(string)

string = 'abcde'
#step1: convert string to list ['a','b','c','d','e']

lst = list(string)
# print(lst)

# step2:change list to ['a','b','f','d','e']
lst[2] = 'f'
# print(lst)

# step3 : convert list to string 'abfde'
string = ''.join(lst)
print(string)


string = 'Mark Fang'

#1. convert string to list

lst = list(string)

# print(lst)

# 2. pop first element out of lst

p = lst.pop(0)

# print(p)
# print(lst)

# 3. append poped element to the tail of list

lst.append(p)

# convert list to string

string = ''.join(lst)

print(string)
'''
def rotateStrintBack(string):

    '''
     passing a string

     return 1 index back rotateString

     #1. convert string to list

     #2. pop first element out of lst

     #3. append poped element to the tail of list

     #4. convert list to string

     #5. return string

    '''
    lst = list(string)
    p = lst.pop(0)
    lst.append(p)
    string = ''.join(lst)
    return string


string = 'Mark Fang'

string = rotateStrintBack(string)
print(string)
string = rotateStrintBack(string)
print(string)
string = rotateStrintBack(string)
print(string)
string = rotateStrintBack(string)
print(string)
string = rotateStrintBack(string)
print(string)


'''
2. string = 'Hi Justin Justin Kevin'

change first 'Justin' to 'Mark' string will be Hi Mark Justin Kevin'

change second 'Justin' to 'Pascal'string will be Hi Justin Pascal Kevin'

# string = 'Hi Justin Justin Kevin'
#  #1. convert string to list
#  # lst = ['H', 'i', ' ', 'J', 'u', 's', 't', 'i', 'n', ' ', 'J', 'u', 's', 't', 'i', 'n', ' ', 'K', 'e', 'v', 'i', 'n']
#  # index   0    1    2    3    4    5    6    7    8    9
# lst = list(string)
# # 2.convert lst content from index 3 to 9 to 'Mark'
# lst[3:9] = 'Mark'

# # convert list to string
# string = ''.join(lst)
# print(string)


string = 'Hi Justin Justin Kevin' 

#  change second 'Justin' to 'Pascal'string will be Hi Justin Pascal Kevin'

#  #1. convert string to list
#  # lst = ['H', 'i', ' ', 'J', 'u', 's', 't', 'i', 'n', ' ', 'J', 'u', 's', 't', 'i', 'n', ' ', 'K', 'e', 'v', 'i', 'n']
#  # index   0    1    2    3    4    5    6    7    8    9   10    11   12   13   14  15   16

lst = list(string)

lst[10:16] = 'Pascal'

string = ''.join(lst)

print(string)

'''
def changeString(start:int,end:int,string:str,relacedPart:str):
    '''
    passing a string

    return changed string

    #1. convert string to list

    #2. change string part, start index, end index

    # convert list to string
    '''
    lst = list(string)

    lst[start:end] = relacedPart

    string = ''.join(lst)

    return string

string = string = 'Hi Justin Justin Kevin' 


string1 = changeString(3,9,string,'Mark')
print(string1)

string2 = changeString(10,16,string,'Pascal')
print(string2)

"""
HW:
1.

replace:

string = 'Mark Fang'

rotateStrintBack(string) =》 'ark FangM','rk FangMa' ....

get all possible change

2. string = 'Hi Justin Justin Kevin'

change first 'Justin' to 'Mark' string will be Hi Mark Justin Kevin'

change second 'Justin' to 'Pascal'string will be Hi Justin Pascal Kevin'

* implements two function rotateStringBack and changeString function

def rotateStrintBack(string):

    '''
     passing a string

     return 1 index back rotateString

     #1. convert string to list

     #2. pop first element out of lst

     #3. append poped element to the tail of list

     #4. convert list to string

     #5. return string

    '''
    pass
    
def changeString(start:int,end:int,string:str,relacedPart:str):
    '''
    passing a string

    return changed string

    #1. convert string to list

    #2. change string part, start index, end index

    # convert list to string
    pass
"""

