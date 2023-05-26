'''
T = input()
string = input()
lst = list(string)

for i in range(5):
    pE = lst.pop()
    lst.insert(0,pE)
    string = ''.join(lst)
    print(string)

# regular  expression

# slicing

# in
bigString = 'ABCCDEABAA'
smallString1 =  'EABCD'

smallString2 = 'CDEAB'

if smallString2 in bigString:
    print('yes')
else:
    print('no')

#slicing

# print(bigString[0:5])
# print(bigString[1:6])
flag = 0

for i in range(len(bigString) - 4 ):

    slice = bigString[i:i+5]

    if slice == smallString2:

        flag = 1

if flag == 1:

    print('yes')

else:

    print('no')

ABCCDEABAA
ABCDE

'''

T = input()
string = input()
lst = list(string)
container = []
for i in range(len(string)):
    pE = lst.pop()
    lst.insert(0,pE)
    string = ''.join(lst)
    container.append(string)

# print(container)
flag = 0
for string in container:
    if string in T:
        flag = 1

if flag == 1:
    print('yes')
else:
    print('no')

mj





