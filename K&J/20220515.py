'''
# def isUnique(string):
#     return len(string) == len(set(string))
#
# print(isUnique('aabcd'))
# print(isUnique('abcd'))

# Exercise 4
def getEvenElement(tuple):
    a = int(len(tuple))
    tuple2 = tuple[0:len(tuple):2]
    return tuple2

print(getEvenElement(('l','e','a')))
print(getEvenElement(('m','a','r','k','f','a','n','g')))

# Exercise 5
# a tuple is immutable (not modifiable) and the elements are not unique while set is mutable (modifiable) and the elements are unique
# example: tuple = ('a',1,1,'a','d') while set = set('a',1,'d')
'''
# no parameter & no return value
def myPrint():
    print('Hello World')

# myPrint()

#it has parameter and no return value

def addMethod1(a,b):
    print('result of {} + {} is {}'.format(a,b,a+b))
#
# addMethod1(1,5)

# it gets parametersand return value

def addMethod2(a,b):
    return a + b

print(addMethod2(1,2))

#anonynous function

a = lambda: print('Hello World')
a()
b = lambda a,b:print('result of {} + {} is {}'.format(a,b,a+b))
b(1,2)
b(3,4)
c = lambda a,b : a + b
print(c(1,2))

# def getEvenIndexElement(lst):
#     newlst = []
#     for i in range(len(lst)):
#         if i % 2 != 0:
#             newlst.append(lst[i])
#     return newlst
#
#
# lst = [i for i in range(1,11)]
# # print(getEvenIndexElement(lst)) # [1,3,5,7,9]
#
# f = filter(lambda x: x % 2 == 0, lst)
# print(list(f))
#
# filterContainer = []
# for i in lst:
#     if i % 2 == 0:
#         filterContainer.append(i)
# print(filterContainer)

dic = {'name1':'Mark','name2':'Lea','name3':'Kevin','name4':'Justin'}

newDic = {}

for i in dic:
    if dic[i] != 'Justin':
        newDic[i] = dic[i]

print(newDic)

f = filter(lambda i : i[1] != 'Justin',dic.items())

print(dict(f))

lst = [1,2,3,4,5] #-> [2,4,6,8,10]
print(list(map(lambda i : i * 2, lst)))