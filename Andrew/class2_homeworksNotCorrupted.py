'''
def twoSum(nums,target):

    
    
    for i in range(len(nums)):
        # print(i)
        for j in range(i+1,len(nums)):

            if nums[i] + nums[j] == target:

                return [i,j]
            
    return 'not find it'

print(twoSum([2,7,11,15],18)) # -> [0,1]

print(twoSum([1,2,3,4,5,6,7],10)) # -> [2,6]


lst = [1,4,6,7,8,9,20]
#      0 1 2 3 4 5 6

# loop all the element in lst

# use the feature of for loop to loop all element

# for element in lst:
#     print(element)

print(lst)
# create index list for lst then access lst

length = len(lst)# count how element in lst

print(list(range(length)))

for index in list(range(length)):
    print(lst[index])
# print(list(range(len(lst))))
# for index in range(len(lst)):
#     print(index)



lst = [1,2,3,4,5]

for i in lst:
    print('i is',i)
    print()
    for j in lst:
        print('j is',j)

'''

#There are four numbers: 1, 2, 3, 4. How many different three-digit numbers can be formed without repeated numbers? What is each?
# get all possibility
# count = 0
# for i in range(1,5):
#     for j in range(1,5):
#         for z in range(1,5):
#             if i != j and i != z and j != z:
#                 print(i,j,z) 
#                 count += 1
# print(count)


# 6x + 3y = 36
# 3x + 2y = 22
# x,y becone 1-20 find  x,y = ?

# using nest loop to 


'''
1. Printing multiplication table using Python nested for loops

(advanced Output 9 * 9 multiplication formula table.)

2 * 1 = 2
2 * 2 = 4
2 * 3 = 6
2 * 4 = 8
2 * 5 = 10
2 * 6 = 12
2 * 7 = 14
2 * 8 = 16
2 * 9 = 18
2 * 10 = 20


3 * 1 = 3
3 * 2 = 6
3 * 3 = 9
3 * 4 = 12
3 * 5 = 15
3 * 6 = 18
3 * 7 = 21
3 * 8 = 24
3 * 9 = 27
3 * 10 = 30
'''

# for i in range(1, 10):
#     for j in range(1, 10):
#         product = i * j
#         print(str(i),'*',str(j),'=',product)
#     print(' ')

'''
2.

list1 = ['I am ', 'You are ']
list2 = ['healthy', 'fine', 'geek']

start outer for loop
I am  healthy
I am  fine
I am  geek

end for loop

start outer for loop

You are  healthy
You are  fine
You are  geek

end for loop
'''

# list1 = ['I am ', 'You are ']
# list2 = ['healthy', 'fine', 'geek']

# for i in range(len(list1)):
#     for j in range(len(list2)):
#         print(list1[i],list2[j])
#     print(' ')

'''
3.
Determine how many prime numbers are between 101-200, and output all prime numbers.(using nesed loop to solved)
'''

# primenumbers = []
# notPrime = []
# for i in range(101, 201):
#     for j in range(2, i):

#         if i % j == 0:
#             notPrime.append(i)
#             break

# count = 0
# for i in range(101,202):
#     if i not in notPrime:
#         print(i)
#         count += 1
# print(count)

# pi = 12.566370614359 /
from math import pi
print(pi)
format(pi,'.25f')
