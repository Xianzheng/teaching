num1 = int(input())
num2 = int(input())
num3 = int(input())
num4 = int(input())

cond1 = (num1 == 9 or num1 == 8)
cond2 = (num4 == 9 or num4 == 8)
cond3 = (num2 == num3)

if cond1 == True and cond2 == True and cond3 == True:
    print('ignore')
else:
    print('answer')


'''
if conditon:
    statement1
else:
    statement2

if condition is True statement1 will be excuted else statement will be excuted
'''


'''
hw:
J1
https://www.cemc.uwaterloo.ca/contests/computing/past_ccc_contests/2019/stage%201/juniorEF.pdf

a3 = int(input())
a2 = int(input())
a1 = int(input())
b3 = int(input())
b2 = int(input())
b1 = int(input())

appleScore = a3 * 3 + a2 * 2 + a1 * 1
bananaScore = b3 * 3 + b2 * 2 + b1 * 1

if appleScore > bananaScore:
    print('A')

if appleScore< bananaScore:
    print('B')

if appleScore == bananaScore:
    print('T')
'''
