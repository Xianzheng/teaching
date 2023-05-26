#nested loop
'''
for i in range(1,5): # loop
    for j in range(1,5):
        for z in range(1,5):
            print(i,j,z)
'''

#There are four numbers: 1, 2, 3, 4.
# How many different three-digit numbers can be formed without repeated numbers?
# What is each?
s = 0
for i in range(1,5):#first digit
    for j in range(1,5):#second digit:
        for z in range(1,5): #third digit
            if i != j and j != z and i != z:
                print(i, j, z)
                s += 1
print(s)
'''
*
**
***
****
*****
'''

for i in range(1,6): # run time
    for j in range(i):# each time print start
        print('*',end = '') # print stars in one row
    print()# change to next line

'''
homework
1.use for loop to get sum for all odd numbers between 90 - 190(one loop)

2. print pattern(nested loop)

*****
****
***
**
*

3. Determine how many prime numbers are between 101-200, and output all prime numbers.
'''
