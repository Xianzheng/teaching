'''
# string(keyword:str) , lst(keyword:list), dic(keyword: dict)

string = 'StephenJingxueAdrien'
#index    01234 ...
print(string[0:7])

lst = ['Stephen','Jingxue','Adrien']
#index   0           1          2
print(lst[0])

dic = {'S':'Stephen','J':'Jingxue','A':'Adrien'}
# key-value pair we stored in dictionary
#dic = {key1:value1,key2:value2,key3:value3}
# dictionary does not have index
# we use key to access the value
print(dic['S'])
'''
#treat dictionary like a container

# create a dictionary
# 1 use sign
dic = {}

print(dic,type(dic))

# 2 use keyword
# dic1 = dict()
#
# print(dic1,type(dic1))

# put some items(key-value pair) to dictionary
# a : apple , b: banana, c: cherry
dic['a'] = 'apple'
dic['b'] = 'banana'
dic['c'] = 'cherry'
print(dic)
print(dic['b'])


'''
# compare contrast
lst = []
lst.append('apple')
lst.append('banana')
lst.append('cherry')

dic = {}
dic['a'] = 'apple'
dic['b'] = 'banana'
dic['c'] = 'cherry'
# lst does not have key, it uses index to access value
# dic does not have index, it uses key to access value
'''
# key feature for dictionary
# in our dictionary,key should be unique
# ['apple', 'banana', 'cherry']
# {'a': 'apple', 'b': 'banana', 'c': 'cherry'}
dic['a'] = 'apple'
print(dic)

dic['a'] = 'avocado'
print(dic)

dic.pop('b')
print(dic)

dic.popitem()
print(dic)

# CRUD # C:create, R: retrieve, U: update, d: delete
dic = {'a': 'avocado', 'b': 'banana', 'c': 'cherry','d':'dragonFruit'}

for i in dic:
    print(dic[i])

'''
hw: 

    implement the CRUD for dictionary
    
    -create dictionary
    (how dic looks like depend on you)
    -add some item
    -retrieve it
    -do update
    -do delete
'''

