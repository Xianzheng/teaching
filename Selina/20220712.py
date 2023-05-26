'''
while condition:
    statement

when condition is True, statement will keep going

#print 1 to 10
i = 0

condition = i < 10

while i < 3:

    print(i)# statement
    i += 1
'''

# let computer generate a random number

from random import randint

randomNumber = randint(1,10)

print('random number is be generated')

i = 0
while i < 3:

    inpNumber = int(input('please type a number to match random number\n'))

    if randomNumber == inpNumber:
        print('correct')
    else:
        print('false')

    i += 1

print('right answer is',randomNumber)

# make a update, we have 3 oppertunities to guess

# homework
# practice wile loop
# use while loop to print1 to 100
# use while loop to print1 3 5 7 to 99
# upgrade code to we have 5 oppertunities to guess random number