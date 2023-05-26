'''

homework
1.
ask user to create a password,  this password must include 'a', 'u', 'e'

if this password is valid , print successful created
else print  it is not valid

2.
do #2018 J2 without see answers
https://cemc.math.uwaterloo.ca/contests/computing/past_ccc_contests/2018/stage%201/juniorEF.pdf

3.Input three integers x, y, z, please output these three numbers from small to large./




print('conditions:')
print('create your password by typing your new password')
print('must contain the letters a, u, e ')
password=input()
# if password.find('a') + password.find('u') + password.find('e'):
#     print('good')
# else:
#     print('bad')

'qwea'
#0123
if password.find('a') != -1 and password.find('u') != -1 and password.find('e') != -1:
    print('good')
else:
    print('bad')

#
print(password.find('a')) # find the specific character's index, if there is no character appears in string return -1



a = int(input())
if a == 1234:
     print('yes')
else:
     print('no')

# string provides us a lot of method
a = 'he{}llo wo{}rld'
print(a, type(a))
print(a.upper())
print(a.capitalize())
print(a.format(1,2))

inp = input()

# find if 'a','u' and 'e' exits in string

# print(len(inp)) #find the length of string

#
# flag = ''
# for i in range(len(inp)):#[0,1,2]
#
#     if inp[i] == 'a':
#
#         flag +=  'a'
#
#     if inp[i] == 'u':
#         flag += 'u'
#
#     if inp[i] == 'e':
#         flag += 'e'

if ('a' in inp) and ('u' in inp) and ('e' in inp):
    print('good')
else:
    print('bad')


# 3.Input three integers x, y, z, please output these three numbers from small to large.
print('the higher the number the bigger it is')
print('type your first number')
ets1=int(input())
print('type your second number')
ets2=int(input())
print('type your third number')
ets3=int(input())
if ets1>ets2>ets3:
    print(ets1)
    print(ets2)
    print(ets3)
if ets1>ets3>ets2:
    print(ets1)
    print(ets3)
    print(ets2)
if ets2>ets3>ets1:
    print(ets2)
    print(ets3)
    print(ets1)
if ets2>ets1>ets3:
    print(ets2)
    print(ets1)
    print(ets3)
if ets3>ets1>ets2:
    print(ets3)
    print(ets1)
    print(ets2)
if ets3>ets2>ets1:
    print(ets3)
    print(ets2)
    print(ets1)


'''
string = 'mark.ffang@gmail.com'

#use string to print 'mark','fang'

# find if @ and 'gmail' is in string

# print all elements of string

# send me email to mark.ffang@gmail.com