'''
num1 = 1
print(type(num1))
num2 = 1.0
print(type(num2))
boolean = True
print(type(boolean))

# data structure
string = 'abc' # it is read only

print(string[0])
# string[0] = 'f'

lst = ['a','b','c'] # # it is C(read)R(retrieve)U(update)D(delete)
print(lst[0])
lst[0] = 'f'
print(lst)

dic = {'a'  :  'apple','b':'banana'}
#      key        value

s = set() # unorder , keep items unique
s.add('apple')
s.add('banana')
s.add('cherry')
s.add('apple')
print(s)

t = ('a','b','c')
print(t[0])

var = int(input('please type a number'))
print(var)
'''

string = '3.1415555 ' # 3 + 3 = 4 !

#index    0123456789
# print(string[1] == string[2])

# print(string[2] == string[3])
# 3.1415555 # 1 3 1 . 1 1 1 4 1 1 4 5

#algorithem

length = len(string)
print(length)
count = 1

for i in range(length - 1):
    if string[i] == string[i + 1]:
        # current char and next char equals
        count += 1
    if string[i] != string[i + 1]:
        print(count,string[i],end=' ')
        count = 1
        #  current char and next char not equals

    if i == length - 2:
        print(count,string[i])
        count = 1
        pass # last element
    
