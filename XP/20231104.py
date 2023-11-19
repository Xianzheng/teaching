# getTwoNumberSum
"""
def getTwoNumberSum(lst,target):

    '''
    argument lst [3,4,5,6,8]
    target is 10
    require return [1,3]
    '''

    for i in range(len(lst)):

        for j in range(i + 1, len(lst)):

            if lst[i] + lst[j] == 10:

                return [i,j]
    


lst = [3,4,5,6,8]
target = 10
print(getTwoNumberSum(lst,target)) # [1,3]


# lst = [3,4,5,6,5]
# target = 11
# print(getTwoNumberSum(lst,target)) # [1,3]


Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

 

Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
Example 2:

Input: nums = [3,2,4], target = 6
Output: [1,2]
Example 3:

Input: nums = [3,3], target = 6
Output: [0,1]
'''

def advGetTwoNumberSum(lst,target):
    dic = {}

    for index in range(len(lst)):

        val = target - lst[index]

        if val in dic:

            return [dic.get(val),index]
        else:

            dic[lst[index]] = index

    return dic

lst = [3,4,5,6,8]

target = 10
print(advGetTwoNumberSum(lst,target)) # [1,3]
"""

string = 'aabbcaded'
# find out how many unique characters in string
dic = {}
for i in string:

    if i in dic:
        dic[i] += 1
    else:
        dic[i] = 1

print(dic)

# write command for your understanding of find unique characters' code

# email = 'mark.ffang@gmail.com', find how many unique characters for email

# code by your self to implement advGetTwoNumberSum(lst,target) 

def advGetTwoNumberSum(lst,target):
    pass

lst = [3,4,5,6,8]
target = 10
print(advGetTwoNumberSum(lst,target)) # [1,3]




    


