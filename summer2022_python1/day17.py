'''
#input
a3 = int(input()) # a3 is 3 points shot numbers of apple team
a2 = int(input())
a1 = int(input())

b3 = int(input()) # b3 is 3 points shot numbers of banana team
b2 = int(input())
b1 = int(input())

#analyze
apple_scores = a3 * 3 + a2 * 2 + a1 * 1

banana_scores = b3 * 3 + b2 * 2 + b1 * 1

#output
if apple_scores > banana_scores:
    print('A')
elif banana_scores > apple_scores:
    print('B')
else:
    print('T')
'''
# input
x = int(input())

y = int(input())

#analyze

c1 = x > 0 and y > 0

c2 = x < 0 and y > 0

c3 = x < 0 and y < 0

c4 = x > 0 and y < 0

#output 
if c1:

    print(1)

if c2:
    
    print(2)

if c3:
    
    print(3)

if c4:
    
    print(4)

'''
homework
choose 1 or 2
    1. pick 2 of 3 old questions
        https://cemc.math.uwaterloo.ca/contests/computing/2019/stage%201/juniorEF.pdf
        https://cemc.math.uwaterloo.ca/contests/computing/2019/stage%201/juniorEF.pdf
        https://cemc.math.uwaterloo.ca/contests/computing/2017/stage%201/juniorEF.pdf

    2 finish new  J1
        https://cemc.math.uwaterloo.ca/contests/computing/2015/stage%201/juniorEn.pdf
'''
