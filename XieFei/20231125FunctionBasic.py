'''
first = input()
str1 = input()

count = 0
for i in range(len(str1)):
    lst = list(str1)

    poped = lst.pop()
    lst.insert(0,poped)
    str1 = ''.join(lst)

    if str1 in first:
        count += 1

if count > 0:
    print('yes')
else:
    print('no')



# function
def printSomeThing():
    print('hello world')

printSomeThing()
'''

'''
how to make a function

#efine
def functionName():

    statemnent


def sayHi():
    print('Hi')

# if you want to invoke function
#         argument
def sayHi(name):
    print('Hi,',name)

sayHi('Kevin')
sayHi('XieFie')
'''

def adding(arg1, arg2):

    '''
    argument is two number

    this function will return the adding result of these two number
    '''

    return arg1 + arg2

print(adding(1,2))

#expain why we need function, function can save code us, and make easier for us to understand logic of code


first = input()
str1 = input()

count = 0


def get_CirlicShifts(str1):
    possible = []
    for i in range(len(str1)):
        lst = list(str1)

        poped = lst.pop()
        lst.insert(0,poped)
        str1 = ''.join(lst)
        possible.append(str1)

    return possible

def check(lst,string):

    for i in lst:

        if i in string:

            return 'yes'
        
    return 'no'

print(check(get_CirlicShifts(str1),first))

'''
# make function called minus(arg1,arg2)

# print(minus(3,2))# 1

# make function called divides(arg1,arg2)

# print(minus(3,2))# 1.5

2. Write a Python function to sum all the numbers in a list.
Sample List : [8, 2, 3, 0, 7]
make function named getSum

print(getSum([8, 2, 3, 0, 7])) # 20

3. 
Write a Python program to reverse a string.
Sample String : "1234abcd"
Expected Output : "dcba4321"
# hint: print(str[::-1]) # check slicing of string
make function named reverseString
print(reverseString('1234abcd')) # "dcba4321"

'''







