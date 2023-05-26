'''
homework:

1.use for loop to get sum for all odd numbers between 90 - 190

2. Determine how many prime numbers are between 101-200, and output all prime numbers.

3. print pattern

*****
****
***
**
*

print(100 % 101)
print(100 // 101)
s = 0
for i in range(101,201):
    for j in range(2,201):
        if i % j == 0:
            print('yes')
            break

    else:
        print(i)
        s += 1
print(s)



for i in range(5):
    for j in range(5 - i):
        print('*',end ='')
    print()


# 12
# 3

# 12 + 120 + 1200 + 12000

# 12 * 10 ** 0
# 12 * 10 ** 1
# 12 * 10 ** 2
# 12 * 10 ** 3

base = int(input())

num = int(input())

s = 0
for i in range(num + 1):
    eachNum = base * 10 ** i
    s += eachNum

print(s)



#A ball falls freely from a height of 100 meters,
# and bounces back to half of its original height
# each time it hits the ground; when it falls again,
# how many meters does it travel when it hits the ground for the 10th time?
# How high is the 10th rebound?
s = 0
k = int(input())
for i in range(0,k + 1):
    height = 100 / 2 ** i
    s += height
print(s)

'''

h = 100
s = 0

for i in range(1,11):
    s = s + h + h / 2

    h = h / 2

print(s)

print(h)
'''
print 
*****
****
***
**
*

2. Determine how many prime numbers are between 101-200, and output all prime numbers.

#A ball falls freely from a height of 100 meters,
# and bounces back to half of its original height
# each time it hits the ground; when it falls again,
# how many meters does it travel when it hits the ground for the 10th time?
# How high is the 10th rebound?
'''




