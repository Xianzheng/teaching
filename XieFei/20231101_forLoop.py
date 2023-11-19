# i = 0

# while i < 10:

#     i += 1

#     print(i)

# for i in range(1,11):
# for i in range(5):
#     print(i)
"""
for i in range(5): # same with range(0,5,1)
    print(i)

print('----another for loop----')
# if we only have one number in brucket, it starts with 0, stop by 5
for i in range(1,11): # same with range(1,11,1)
    print(i)
# if we have two argument in brucket, it starts with argument1, stop by argument2

'''
when you use for loop, you need to add indentation after for loop

'''
print('----another for loop----')
for i in range(1,11,2):
    print(i)


#practice using for loop to get sum of 3 to 15?

#
"""

# consider if you want to print all even number between 3 to 15

# num = 10

# if num % 2 == 0:
#     print('even number')
# else:
#     print('odd number')

for i in range(3,16):
    if i % 2 != 0:
        continue
    print(i)


print('----another options')

for i in range(4,16,2):
    print(i)


'''
hw:
#print 1 - 100
# get sum of 1 - 100
# get all odd numbers between 1 - 100
# *
input a number
get the factorial of this number
5
5 * 4 * 3 * 2 * 1 == 1 * 2 * 3 * 4 * 5

consider how to print 100,99,98 ..., 1
'''