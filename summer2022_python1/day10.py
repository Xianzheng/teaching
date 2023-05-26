'''
write a small program

if practice
1. at first we input two numbers and compare which number is bigger
for example we input 6 ,4 we will print 6 is bigger
hint we use int(inpuit()) for input
example 1
input:
6
4
output:
6 is bigger

example 2
input:
10
11
output:

11 is bigger

2. we input a number then it will print from 0 to this number

example 1

input:
4
output:
1
2
3
4

example 2

input:
2
output:
1
2

# syntax error, logic error, not robust
try:
    num1 = int(input())
    num2 = int(input())

    if num1 > num2:
        print(num1,'is bigger')
    elif num2 > num1:
        print(num2,'is bigger')
    else:
        print('two numbers are equal')

except:
    print('you have to input two numbers')



num = int(input())

i = 0

while i < num:

    print(i)
    i += 1
'''
import random # load a library to python program

randomNumber = random.randint(1,10) # rn means randomNumber
print('random is given')

# if we get 5 times to guess

i = 0

while i < 10:
    ourNumber= int(input('please type your guess:')) 
    #if else
    if randomNumber == ourNumber:
        print('you get me')
        break
    else:
        print('you did not get me')

    i += 1

print('correct answer is', randomNumber)


# write a small program guess number you have 7 times to guess number
# if you get right answer, loop will be terminated

# use while loop to print 1 to 10 but if i == 5, loop will be terminated// break

