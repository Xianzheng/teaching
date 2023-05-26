'''
lst = [0,0,0,0,0,0,0,0,0,0] 

flage = 1

point = lst[0]

for i in lst:
    if i != point:
        flage = 0
        break

if flage == 0:
    print('not magic')
else:
    print('magic')

lst = [0,0,0,0,0,1,0,0,0,0] 

if len(set(lst)) == 1:
    print('magic')
else:
    print('not magic')
'''

# string, list, dictionary, set, tuple

s = set() # ask all element in set are unique

s.add('a')
s.add('b')
s.add('c')
s.add('d')
s.add('c')
s.add('a')

print(s)

string = 'abcdef'

print(len(string) == len(set(string)))