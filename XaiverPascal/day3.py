'''
userInput = input()

if userInput == '7':
    print('Sunday')
if userInput == '1':
    print('Saturday')
'''

'''
# input
a3 = int(input())
a2 = int(input())
a1 = int(input())

b3 = int(input())
b2 = int(input())
b1 = int(input())

# analyze:
appleScores = a3 * 3 + a2 * 2 + a1 * 1

bananaScores = b3 * 3 + b2 * 2 + b1 * 1

#output
if appleScores > bananaScores:
    print('A')
elif appleScores < bananaScores:
    print('B')
else:
    print('T')

# input

d1 = int(input())
d2 = int(input())
d3 = int(input())
d4 = int(input())

c1 = d1 == 8 or d1 == 9
c2 = d4 == 8 or d4 == 9
c3 = d2 == d3

if c1 and c2 and c3:
    print('ignore')
else:
    print('answer')

'''
#control statement
# if condition

# loop: while loop and for loop

# deadly loop
# while True:
#     print('Hello World')
'''
while condition:# condition is a boolean value: True/False
    statement
    
if condition is True, statement will keep running,
if condition is False, statement will stop runing
'''
i = 0

s = 0

while i < 100:

    i += 1
    print('{} + {} = {}'.format(str(s),str(i),str(s+i)))
    s += i

print(s)
# 1 + 2 + ... + 100 = ? # 5050

'''
homework:
    1.
    option:
    a. J1 of https://cemc.math.uwaterloo.ca/contests/computing/2017/stage%201/juniorEF.pdf
    b. J1 of https://cemc.math.uwaterloo.ca/contests/computing/2016/stage%201/juniorEn.pdf
    
    2. add all numbers between 1 - 50
    
    3. print all odd number between 1 - 100
    
    4. draw table for how code go(columns include i, condition, i += 1, print)
    
        i = 0
        
        while i < 3:
            
            print(i)
            
            i += 1 
    
    any questions: connect mark.ffang@gmail.com 
'''