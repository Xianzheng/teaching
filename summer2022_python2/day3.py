# input() always is a string
a3 = int(input())
a2 = int(input())
a1 = int(input())

b3 = int(input())
b2 = int(input())
b1 = int(input())

appleScore = a1 * 1 + a2 * 2 + a3 * 3
bananaScore = b1 * 1 + b2 * 2 + b3 * 3

if appleScore > bananaScore:
    print('A')
elif appleScore < bananaScore:
    print('B')
else:
    print('T')