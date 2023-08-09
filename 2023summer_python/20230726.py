
# number(int, float, boolean,string,list,dictionary), set
'''
a = 1 # int
b = 1.0 # float
c = True # boolean
d = 'string' # string
e = [] # list
f = {'S':'Stephen','J':'Jingxue'} # dictionary

#store everything into a list
e.extend([a,b,c,d,f])

print(e)


s = {'1'}
print(type(set))

d = {'a':'apple'}
print(type(d))


# key point for set, every thing is unique in set

# create a empty set
s = set()
print(s)

# add some thing into set 
s.add('a') # add method of s, s'add method
s.add('b')
s.add('c')
s.add('d')
# when we print set
# every element is in set, but it is not inorder
# if ['a','b','c','d'] , {'d', 'a', 'c', 'b'}/{'c', 'a', 'd', 'b'}
print(s)
# . means some method/function of s

#compare stable/ unstable

#list have index , set does not have index
lst = ['a','b','c','d']

s = {'a','b','c','d'}# set does not have index
print(lst[0])

print('e' in s)


# list can contain repeated value, set can not
lst = [1,2,3,4,5,1,2,3]
print('list is',lst)

# s = {1,2,3,4,5,1,2,3}
# print('set is',s)

s = set()# empty set
for item in lst:
    s.add(item)

print(s)
'''
s ={'a','b','c','d'}

s.add('e')

# s.remove('c')
print(s.pop())

# 是support for CRD

'''
hw:
use code to demo what you already know 
the feature for set
# example: unstable -> use your code give me a demo
'''

