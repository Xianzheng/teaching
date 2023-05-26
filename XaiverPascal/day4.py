'''
print('type a number that is between 1 and 100')
number = int(input())

# numb4 = number // 2 # // is to get number before R
numb4 = number % 2 # % is to get number after R

if numb4 == 1:
    print('its an odd number')
else:
    print('its an even number')


# 3. print all odd number between 1 - 100

i = 0

while i < 100:

    i += 1

    if i % 2 == 1:

        print(i)


# let computer generate a random number
# let us input a number to match this random number
# if they match print correct, else print wrong

from random import randint

randomNum =  randint(1,10)

number = int(input())

if number == randomNum:
    print('correct')
else:
    print('wrong')

print('random number is',randomNum)

# we have 5 oppertunities
# we have unlimited time to guess, until correct

from random import randint

randomNum =  randint(1,10)

i = 0
while True:

    i += 1

    print('life time : {}'.format(str(i)))
    number = int(input())

    if number == randomNum:
        print('correct')
        break # it will break look

    else:
        print('wrong')
        # if i == 3:
        #     print('random number is',randomNum)



from random import randint

randomNum =  randint(1,100)

i = 0
while True:

    i += 1

    print('life time : {}'.format(str(i)))
    number = int(input())

    if number == randomNum:
        print('correct')
        break # it will break look

    if number > randomNum:
        print('it is bigger')

    if number < randomNum:
        print('it is smaller')

'''
# break it will break a loop
# if condition: # condition will be boolean value or condition has boolean attribution
#     statement
#
# when condition is True or boolean attribute is True, statement will be executed,
# when condition is False or boolean attribute is False, statement will not be executed
i = 0

while i < 8:

    i += 1

    if i == 3:

        continue

    if i == 6:

        continue

    print(i)

# try key word break and continue

'''

'''