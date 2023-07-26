'''
hw:

 1: we have a format result =  a + b * c
    input a, b, c
    example1 if you type 1, 2,3
    result is 7
    example if you type 8,5,3
    result is 23

 2: you can make your format(example y = a * (x ** 2) + b, type a,x,b you can get y)

 3(options): for guessing name, if we have 5 oppertunity to guess, how to change code
            (we will talk in next class)

a = int(input())
b = int(input())
c = int(input())

result = a + b * c

print(result)

#start question 2

a = int(input('a = '))
x = int(input('x = '))
b = int(input('b = '))

y = a * (x ** 2) + b
print(y)
'''
# guessing computer generated random number
import random

# random.randint(1,10) will generate a number between 1 to 10
rNum = random.randint(1,100)
print('our python already generate a random number between 1 to 100')
# input your guess

time = 0
while True:
    time += 1
    oGuess = int(input('what is your guess\n'))

    if rNum == oGuess:
        print('you get it')
        break # break all loop

    elif rNum > oGuess:
        print('smaller')
    elif rNum < oGuess:
        print('bigger')

    # print('random number is', rNum)
    #print('random number is', rNum)

print('random number is', rNum)
# we have unlimited time to guess until we make it

'''
hw:
    1.  explain what is for break base on your understanding, use the code to demo
    2.  try to change the rule for guessing name, you can make your rule, and code it.
        explain your rule and send me your code

'''
