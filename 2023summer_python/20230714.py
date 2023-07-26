'''
# what is String

# string is like a structure to store data

# python has 5 different data structure, string, list, dictionary, tuple, set
# number, string, char, are datas

a = 1
b = 2
a + b

# string
# Hello World is a data
# "" is string type
# print("Hello World") make string with data shows in console


a = 'Hi'
b = 'how are you'
#in  012345678910
print(a,b )
print(b[6])
# discues
# we can use index to access each character of string
print(b[0]) # h
print(b[9]) # 0
print(b[10])# u
# if we access the index does not in the string, we will have out of range error
# print(b[11])
#b[index start: index end: index step]
print(b[0:11:3])


myEmail = 'mark.ffang@gmail.com'
# the length for myEmail
print(len(myEmail))
#posindex  0123...
#negindex                   -3-2-1
print(myEmail[1])
print(myEmail[-1])

print(myEmail[0:-4])
print(myEmail[-20])
print(myEmail[0])
print(myEmail[-1:-4:-1])
'''

# how to loop for each content of string
string = 'hello word'

# for loop string
for item in string:
    print(item)

# use the index to loop each character
for index in range(len(string)):
    print(string[index])

'''
hw:
email = "mark.ffang@gmail.com"
#index   012345...
# 1. loop all item from eamil

# 2. get useful information, first name, last name, which email used

# 3. get all odd item letter # akf ...

# 4. get all even  item letter # mr. ...
'''