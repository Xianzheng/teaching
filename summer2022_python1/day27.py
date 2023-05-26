'''
#input part
num1 = int(input())
num2 = int(input())
num3 = int(input())
num4 = int(input())



c1 = num1 == 8 or num1 == 9
c2 = num4 == 8 or num4 == 9
c3 = num2 = num3

if c1 and c2 and c3:
    print('ignore')
else:
    print('answer')
'''

num = int(input())
today = input()
yesterday = input()
counter = 0
for i in range(num):
    if today[i] == yesterday[i] == 'C':
        counter = counter + 1
print(counter)
