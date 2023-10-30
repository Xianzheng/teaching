# previous hw
# get factorial 10!, 10 * 9 * 8 * ... * 1
'''
i = 10

f = 1

while i > 0:
    # print(i)
    f *= i

    i -= 1

print(f)


# make a guessing game

# we want python to generate a random number between 1 to 10,
# we will input a number ,see our number is equal with random number

# ramdom is a library
import random

i = 0

while i < 10:


    r = random.randint(1,10)

    print(r)

    i += 1

# make a guessing game

# 1.we want python to generate a random number between 1 to 10,
# 2.we will input a number ,see our number is equal with random number,
# if equal we print win, else lose
# 3. how about I have 3 oppertunities to gues

import random

# r = random.randint(1,100)
r = random.randint(1,10)

print('computer already generate a random number between 1 to 10')

i = 0

while i < 5:
    print('time ', i + 1)
    inp = int(input('please type your guess:'))

    if inp == r:
        print('win')
        # when break execute , while loop will break
        break
    else: 
        print('lose')

    i += 1

print('random number is',r)

'''
# lottery, input three number, if your number is exact same with  649
# you win
#1 generate 3 random number between 1 - 9
import random
r1 = random.randint(1,9)
r2 = random.randint(1,9)
r3 = random.randint(1,9)
#2 input a number betweent 1 - 9
inp1 = int(input())
# input a number betweent 1 - 9
inp2 = int(input())
# input a number betweent 1 - 9
inp3 = int(input())

# make if statement
# see how many(r1 matches input1,r2 matches input2,r3 matches input3) number is match
print(r1,r2,r3)

count = 0

if r1 == inp1:
    count += 1
if r2 == inp2:
    count += 1
if r3 == inp3:
    count += 1

print(count)
