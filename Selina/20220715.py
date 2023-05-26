
'''
from random import randint

randomNumber = randint(1,100)

print('random number is be generated')


while True:

    inpNumber = int(input('please type a number to match random number\n'))

    if randomNumber == inpNumber:
        print('correct')
        break
    else:
        print('false')



print('right answer is',randomNumber)

# if inpNumber is bigger than randomNumber it will say, it is bigger
# if inpNumber is smaller than randomNumber it will say, it is smaller
# if inpNumber is equal randomNumber it will say, correct, loop will break

# we have unlimited time to guess


i = 0
sum = 0
while i < 10:
     i += 1
     sum += i

print(sum)
#example 1
#input
1
4
7
8
0

#output
20

#exmple 2
#input
1
2
3
0

#output
6
'''
sum = 0
while True:
    inpNumber = int(input())

    if inpNumber == 0:
        break

    sum += inpNumber

print(sum)

# homework:

# type what you understand for while loop,
# get multiple time times
'''
#input
2
3
4
1

#output
24

#input
2
8
1

#output
16
'''
# GUI  graphic user interface

import random
import tkinter


top = tkinter.Tk()

top.mainloop()