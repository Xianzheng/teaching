'''
#CCC canadian computing competition

# string, list, dictionary, set, tuples

num = int(input())# int(string) convert string to integer, it requires string must look like integer

print(num,type(num))
'''

'''
Sample Input 1
9
6
6
8
Output for Sample Input 1
ignore

Sample Input 2
5
6
6
8
Output for Sample Input 2
answer

'''

# input
num1 = int(input())
num2 = int(input())
num3 = int(input())
num4 = int(input())

#analyze

condition1 = num1 == 8 or num1 == 9

condition2 = num4 == 8 or num4 == 9

condition3 = num2 == num3

condition = condition1 and condition2 and condition3

# output
if condition:
    print('ignore')
else:
    print('answer')

# homework
# 2019 J1
# https://cemc.math.uwaterloo.ca/contests/computing/2019/stage%201/juniorEF.pdf

