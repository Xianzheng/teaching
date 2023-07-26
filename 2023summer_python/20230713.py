'''
A REQUEST:
3

100
200
300

we need to count our input (100 + 200 + 300) / 3

input
2
400
800

600


num = int(input())

lst = []
# create a for loop , run num times
for _ in range(num):
    # we can input a num run num times
    # we can append our input to our list
    lst.append(int(input()))

print(lst)

# get the average for lst, average = sum of content of lst/ the length of lst
avg = sum(lst) / len(lst)
print('average is',avg)


num = int(input())

lst = []

for _ in range(num):
    lst.append(input())

print(lst)

'''
string = '9 +'
# how to convert this string to '+++++++++'
lst = string.split(" ")
print(lst)

for _ in range(int(lst[0])):
    print(lst[1], end ='')
print()
print('Hello World')
'''
hw:
finish J2 of CCC 2019:
https://www.cemc.uwaterloo.ca/contests/computing/past_ccc_contests/2019/stage%201/juniorEF.pdf
'''
