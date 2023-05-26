'''
ask user to type a password

if this password is 1234567, then it will print yes
else print out no


print('type password')
a=input()
if a=='1234567':
    print('yes')
else:
    print('no')


print('type password')
a = input()
if a=='1234567':# robust
    print('yes')
else:
    print('no')

# difference between 1234567

# 1234567 is a number
# '1234567' is a string

# int (condition, statement, for loop, while loop)

# five data type ,'string', 'dictionary', 'list', 'tuples', 'set'

a = 1234567

print(a, type(a))

b = '1234567'

print(b, type(b))

# int('1234567')
# int('a1234567')

inp = input() # what is the type of ino
print(type(inp)) # inp is a string

# string '123456' , 123456 can be converted with each other

print(int('123456') == 123456) # convert string to int

print(str(123456) == '123456') # convert int to string

# if we want string to int, this string must look like int

print(int('1234'))

a = 'Hello World'
print(a)# '1234567'
print(type(a))

# any content between '', "" will be a string
#'123456'
#'#@%^&'
#      'PascalXavierMark', there are string
#index: 012345678901
#cons:
string = 'PascalXavierMark'
print(string,type(string))
print(string[0]+string[1]+string[2]+string[3]+string[4]+string[5])
# feature 2, string get index under it, index starts from 0

# feature 3, string can only concatenate to str
'''
# condition statement, for loop / while loop

# judge a string ,if 'd' exist in 'abcdef'
#                                  012345


'''
# for looo to do it 
for index in range(6):
    if string[index] == 'd':
        print('it exists')
    #print(string[index]) # use index to access each element of this index on string

# while loop to do it:
string = 'abceeeeeeef'

index = 0

flag = False

while index < 11:

    if string[index] == 'd':
        flag = True

    index += 1

if flag == True:
    print('it exists')
else:
    print('it not exits')

'''

#2018 J2

'''
input
5
CC..C
.CC..

7
CCCCCCC
C.C.C.C
4
'''

number = int(input())
yesterday = input()
today = input()
ans = 0
for i in range(number):
    if yesterday[i] == today[i] == 'C':
        ans += 1

print(ans)
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


'''