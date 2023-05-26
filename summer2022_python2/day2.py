# string: ''
# lst: []
# dictionary: {}
# set: {0,}
'''
string = 'abcdef'

setString = set(string)

if len(string) == len(setString):
    print('no repetition')
else:
    print('get repetition')

# tuple
lst = ['apple','banana','cherry']
#index   0         1        2
tup = ('apple','banana','cherry')
#index   0         1        2
# lsit is mutable -> can be changed
# tuple is immutable -> can not be changed(read-only)
print(lst[2])
lst[2] = 'pear'# change content of index 2
print(lst) # print lst after change

print(tup[2])
tup[2] = 'pear'
print(tup)


# input()

a = input('please type a: ')# \n is next line
b = input('please type b: ')
try:
    a = int(a)
    b = int(b)
    print('the result of a * b',a * b)
except:
    print('a and b must be number')
'''
#canadian computing competition

string = '5432256235' # get the sum of there numbers
sum = 0
for i in string:
    sum += int(i)
print(sum)


# how to convert string to integer
# homework, J1
# https://cemc.math.uwaterloo.ca/contests/computing/2019/stage%201/juniorEF.pdf
# review today' content
# 
