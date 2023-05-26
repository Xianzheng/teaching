'''
# control statement

# loop statement, while loop, for loop

print('Hello World')
print('Hello World')
print('Hello World')
print('Hello World')
print('Hello World')


while condition: # condition will be a boolean value or contains boolean attribution
    statement

if condition is True, statement will keep going
if condition is False, statement will stop


# it is deadly loop
while True:
    print('Hello World')


i = 0

while i < 3:

    i += 1
    print('Hello World')


# print 1 2 3 in console

i = 0

while i < 100:

    print(i)

    i += 1

# two key words can be only used in loop, break, continue
# when loop meets break, loop will be terminated



i = 0

while i < 6:
    i += 1
    j = 0
    while j < i:
        j += 1

        if j == 3:

            break
        print(i,j)

# keyword continue
#print 1,2,3,4,5,6,8,9

i = 0

while i < 9:
    i += 1

    if i == 7:

        continue

    print(i)


# python will generate a random number(smallest, highest) let user to guess
# while if

from random import randint

randomNum = randint(1,10)

print('random number is already be created')

# input a number to match randomNumber , if did not match print wrong else print right

from random import randint
randNum = randint(1,10)
print("random number already created please type in your guess:\n")
a = int(input())
if a != randNum:
    print("wrong")
else:
    print("right")

print('right is',randNum)
'''
# suppose we have 5 times to guess,
# if we make it , program will be terminated
from random import randint
randNum = randint(1,10)

i = 0

while i < 5:
    a = int(input())
    if a != randNum:
        print("wrong")
    else:
        print("right")
        break
    i += 1
    if i == 5:
        print('right is',randNum)

'''
homework:
print all odd numbers between 1 - 100, 1,3,5,7,9 ....

upgrade our game,
a. we have unlimited time to guess, until we make it
b. if our number is bigger, it will say it is bigger, if smaller it will say smaller, 
   if correct, it will say right and terminated
c. random number 's range will be in 1 - 100
'''
