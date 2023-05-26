# print('Hello World')

#open terminal: ctrl + shift + ~
#Save : control + s

'''
def functionName(args1,args2):
    return args1 * args2


print(functionName(3,7))


string = '123456789'
print(len(string)) # len() the length of something, len() is inner build function in python

lst = [5,3,1,8,5,0]

print(sorted(lst,reverse=False)) # sorted() tsort something, sorted is inner build function in python

print(max(lst))
print(min(lst))


def myLen(string):
    counter = 0
    for i in string:
        counter += 1
    return counter

print(myLen(string)) 
'''
# In mathematics and computer science, an algorithm is a finite sequence of rigorous instructions, 
# typically used to solve a class of specific problems or to perform a computation. 
# Algorithms are used as specifications for performing calculations and data processing.

# myLen('123456789012') # question is how we can get the length of string


# how we can build a specifications for performing calculations and data processing.  to get what we want is a algorithem

# 9 # this is a result

lst = [5,3,1,8,5,0]

# print(max(lst))
def getMax(lst):
    
    m = 0

    # loop all the number in the lst

    for num in lst:
        # if m is smaller then number , we make m to this number, else m is bigger , we do nothing
        if m < num:
            
            m = num
        else:
            pass
    return m

print(getMax(lst))

 # if m is bigger then number , we make m to this number, else m is bigger , we do nothing

'''
1. The sum of two numbers
Given an array of integers and a target value, find the two numbers in the array and the target value.
You can assume that each input corresponds to only one answer, and that the same elements cannot be reused.
Example:
Given nums = [2, 7, 11, 15], target = 9
Because nums[0] + nums[1] = 2 + 7 = 9
So return [0, 1]

2.Seeking = a + aa + aaa + aaaa + aa ... the value of a, where a is a number.
For example, 2 + 22 + 222 + 2222 + 22222 (5 numbers are added together at this time), 
and the addition of several numbers is controlled by the keyboard.

2
5
2 + 22 + 222 + 2222 + 22222 = ? 

3
2
3 +33 = ?
'''
        
def twoSum(nums,target):

    '''
    param is a lst and a number

    '''
    pass

print(twoSum([2,7,11,15],9)) # -> [0,1]

print(twoSum([1,2,3,4,5,6,7],10)) # -> [2,6]
