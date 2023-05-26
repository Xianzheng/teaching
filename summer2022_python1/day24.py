'''
10
3
7
8
9
6
'''
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

if appleScore < bananaScore:
    print('B')

if appleScore == bananaScore:
    print('T')