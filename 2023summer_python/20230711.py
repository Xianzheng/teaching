'''
1
2
3
4
5

# USING WHILE LOOP TO PRINT 1,2,3,4,5 LINE BY LINE?
#
for i in range(1,6,1):
    print(i)

# range function contain three parameter , (start, stop, step)
print(list(range(1,11,1)))
print(list(range(3,8,1)))
print(list(range(1,11,2)))

# print all even numbers between 1 to 10
for i in range(1,11):
    if i % 2 == 0:
        print(i)

# range(1,6,1) first one in where start from, second is where stop, third one is what is step

for i in range(1, 6):
    # if i can be whole divided by 2, we are going to print(i), i will be 1,2,3,4,5, only 2, 4 can be whole divided
    if i % 2 == 0:
        print(i)
'''

# if we want to get sum of 1 to 100,5050

# sum = 0
# for i in range(1,101):
#     sum += i
# print(sum)

# we want to get the sum from (25 to 45).

# sum = 25
# for i in range(26,46):
#     sum += i
# print(sum)

# we want to get sum from 5 to 10

# sum = 0
# for i in range(5,11):
#     sum += i
# print(sum)

# print(sum(range(1,11)))# python 's syntax sugar

# get the sum of all odd number from 1 to 100

result = 0

for num in range(1, 101):

    if num % 2 != 0:
        # print(num)
        result += num

print(result)

result1 = 0

for i in range(1,101,2):

    result1 += i
print(result1)

'''
hw:
    write a program
    # print first 20 nature numbers
    # print first 10 odd numbers
    # print first 10 even numbers
    # get the factorial number 10 !, 10! = 10 * 9 * 8 * ... * 1
    # (options) print first 10 even numbers in reverse order
'''

