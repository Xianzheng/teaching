'''
a = input('please type anything you want: ')
print('you type',a, type(a))


# a + b = ?

a  = input('please type your a: ')
b  = input('please type your b: ')
print('a + b is',a + b)
# when you type 12 in your keyboard you also press enter in your keyboard
# any input is String, if we want do calculate, we need to int(input())
# means transfer string to int
# if we want to transfer string to int, this string must look like a number

a  =int(input('please type number a: '))
b = int(input('please type number b: '))
print('a + b is',a + b)


scores = int(input('please type score you get\n'))

if scores >= 90:
    print('A')
elif scores >= 80: # same with >= 80 and < 90
    print('B')
elif scores >= 70:
    print('C')
else:
    print('D')
'''

# our python will generate a random number between 1 to 10
# our goal is to guess what this number is

import random

# random.randint(1,10) will generate a number between 1 to 10
rNum = random.randint(1,10)
print('our python already generate a random number between 1 to 10')
# input your guess
oGuess = int(input('what is your guess\n'))

if rNum == oGuess:
    print('you get it good luck')
else:
    print('you lose it, better luck next time')
print('random number is', rNum)
#print('random number is', rNum)

# i = 0
# while i < 5:
#     i += 1
#     rNum = random.randint(1, 10)  # random.randint(1,10) will generate a number between 1 to 10
#     print('random number is', rNum)

'''
hw:

 1: we have a format result =  a + b * c
    input a, b, c
    example1 if you type 1, 2,3
    result is 7
    example if you type 8,5,3
    result is 23
    
 2: you can make your format(example y = a(x ** 2) + b, type a,x,b you can get y)
 
 3(options): for guessing name, if we have 5 oppertunity to guess, how to change code
            (we will talk in next class)
'''