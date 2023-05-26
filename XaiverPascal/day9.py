'''
string = ''
# key word is str
# a = input()

# key word is list
lst = []

#CRUD
lst.append('apple')
lst.append('banana')
lst.append('cherry')
lst.append('pear')

print(lst)

lst[1] = 'orange'
print(lst)

lst.pop(2)
print(lst)


# dictionary
#CRUD
# key word is dict

#create

# dic = dict()
# print(dic,type(dic))

dic = {}
print(dic,type(dic))

dic = {'a' : 'apple', 'b': 'banana', 'c':'cherry','p':'pear'}
print(dic)

# compare and contrast
# list and dictionary can store data, we can treat them as a container(CRUD)

#list ['apple','banana','cherry'] store element
#index    0       1         2

# dic = {'a' : 'apple', 'b': 'banana', 'c':'cherry','p':'pear'}
#        key1   value1  key2   value2   key3  value3 key4 value

# dic stores key-value pairs
# normally, dictionary does not have index under it

# print(dic['b'])
# dictionary use mapping value to get data
# print(dic['p'])

# dic = {1:5,5:1,2:3}
# print(dic[1])
# print(dic[5])
'''

# dic = {1:2,2:3,3:4}
# print(dic,type(dic))
#CRUD

#C -> create

dic = {}
# add a key-value pair to dictionary
dic['a'] = 'apple'
dic['b'] = 'banana'
dic['c'] = 'cherry'
dic['p'] = 'pear'
print(dic)

#R -> retrieve

#using key to access value

# print(dic['b'])

# we want to know how many key in dic
# for i in lst, we will get each element

# if we want to print each value, how to do it?
for key in dic:
    print('key is',key,'value is',dic[key])

# U -> update
# the key of dictionary is unique
dic['a'] = 'avocado'
# if we use same key with different value, it will replace value before
print(dic)

# D -> delete
dic.pop('a')
print(dic)

print(list(dic.keys()))
print(list(dic.values()))

'''
homework,
CRUD:
create a dictionary 7 add different fruits

retrieve all fruits, check a specific fruit if in dictionary

update a fruit key with values
 
delete 2 fruit

challange:

dic = {'math': 90, 'english':95, 'python':92,'gym':85}

in dic with subject get highest scores
'''