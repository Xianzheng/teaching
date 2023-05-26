'''
homework:
print all odd numbers between 1 - 100, 1,3,5,7,9 ....

upgrade our game,
a. we have unlimited time to guess, until we make it
b. if our number is bigger, it will say it is bigger, if smaller it will say smaller,
   if correct, it will say right and terminated
c. random number 's range will be in 1 - 100

from random import randint
randNum = randint(1,100) # binary search

i = 0

while True:
    a = int(input())
    if a != randNum:
        if a > randNum:
            print('it is bigger')
        else:
            print('it is smaller')
    else:
        print("right")
        break
    i += 1

# print('right is',randNum)



i = 0
while i < 100:

    i += 1
    print(i)

for i in range(1,101):
    print(i)


for i in range(10):  # x >= 0 and x < 10
    print(i,end= ' ')

print()

# range(start,stopby,steps) # if we only add one number argument, default start is 0, step is 1


for i in range(1,11):# we define start is 1 , stopby is 11, step default is 1
    print(i)

for i in range(1,10,2):# we define start is 1, stopby is 10, step is 2

    print(i)




# use while and for loop to get sum for 75 to 105

# 75 + 76 + 77 + ... + 104 + 105 = ?

s = 0

for i in range(75,106):
    print(i)
    s += i
print(s)



# use while and for loop to get sum for all even number between 90 to 180

for i in range(1,11):
    if i == 6:
        continue
    print(i)

for i in range(3):
    for j in range(3):
        if j == 2:
            break
        print('i is {}, j is {}'.format(i,j))


#There are four numbers: 1, 2, 3, 4. How many different three-digit numbers can be formed without repeated numbers? What is each?

total = 0

for x in range(1,5):
    for k in range(1,5):
        for j in range(1,5):
            if x != k and k != j and x != j:
                print(x,k,j)
                total += 1

*
**
***
****
*****
'''

for i in range(1,6):
    for j in range(i):
        print('*',end='')
    print()

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
'''