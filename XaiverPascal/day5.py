# while loop, for loop

#print 1,2,3,4,5 ... 10 use while loop

'''
i = 0

while i < 10:

    i += 1
    print(i)


# print Hello World 5 times

for i in range(5): # this loop will run 5 times
    # print('Hello World')
    print(i)

# principle for for loop
# for i in some_sequence:

# print(list(range(5)))

for i in range(10):# default start from 0, indicate stopby 10, default step is 1
    print(i)

for i in range(1,11):# indicate start from 1, indicate stopby 11, default step is 1
    print(i)
print(list(range(1,11)))

# print all odd numbers between 1 to 10

for i in range(1,11,2):# indicate start from 1, indicate stopby 11, indicate step is 2
    print(i)

print(list(range(1,11,2)))

# print all even numbers between 88 - 100

for i in range(88,102,2):
    print(i)
print(list(range(88,102,2)))


# we can use for loop to define run times
# or we can define each i

for i in range(5,10):#[5,6,7,8,9]
    # print('Hello World')# 5 times
    print(i,end = ' ') # i is different
print()

for i in range(0,5):#[0,1,2,3,4]
    # print('Hello World')# 5 times
    print(i, end = ' ') # i is different

# key words, continue, break

for i in range(1,11):

    if i == 5:
        continue

    print(i)



# nested loop, there are loop under a loop

for i in range(1,7):
    for j in range(1,3):
        for z in range(1,3):
            print('grade {} term {} bigTest {}'.format(i,j,z))


# There are four numbers: 1, 2, 3, 4.
# How many different three-digit numbers can be formed without repeated numbers?
# What is each?

# list all possible options
# filter  get our solution
sum = 0
for i in range(1,5):
    for j in range(1,5):
        for z in range(1,5):
            if i != j and j != z and i != z: # filter
                print(i,j,z)
                sum += 1
print(sum)


# *
# **
# ***
# ****
# *****

for i in range(1,6):# first loop to get how many time to run
    for j in range(i):
        print('*',end = '')
    print()

1.use for loop to print all odd numbers between 90 - 190

2.use for loop to get sum for all odd numbers between 90 - 190

3. print pattern

*****
****
***
**
*
'''

