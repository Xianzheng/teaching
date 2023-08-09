# function
'''
stereotype

def [functionname]([argument]):
    pass
'''

# print('hello world')

def myPrint(str):
    print(str)

# myPrint('Hello Wold')


def add(arg1,arg2):

    return arg1 + arg2



'''

no argument, no return

'''

def sayHi():
    print('Hi')

# sayHi()
'''
have argumeng no return
'''
def add(arg1,arg2):
    print(arg1 + arg2)

# add(1,2)

'''
no argument have return
'''

def sayHi():
    return 'Hi'

# a = sayHi()
# print(a)

'''
have argument have return 
'''

def sayHi(name):

    return 'Hi '+name

print(sayHi('Jingxue'))
print(sayHi('Stephen'))
print(sayHi('Andrien'))

# create function
# adding function
# minus function
# times function
# divides function
# judge number is a even or odd
# judge a string whether have duplicated value

# ifDuplication('abcdefb') # true
# ifDuplication('abcdef') # false

#advanced function 
def adding(arg1,arg2):
    pass

print(adding(3,4)) # expect to see 7


def ifDuplication(str):
    if len(set(str)) == len(str):
        return False
    else:
        return True

print(ifDuplication('abcdefb') )
print(ifDuplication('abcdef') )