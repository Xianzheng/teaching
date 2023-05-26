# integer(Number), string
'''
num1 = 1
print(num1, type(num1))

num2 = 2
print(num2, type(num2))

string1 = '1'
print(string1,type(string1))


string2 = '2'
print(string2,type(string2))

print(num1 + num2) # + for numbers mean adding
print(int(string1 + string2))# + for string means concatenation(concat)

# numbers can + - * / % ...
# string can only do +
'''
'''
# * can be used between string and integer

string = 'a'

num = 3

print(string * num)
'''
'''
input
2
3

output
246

reason:
2 + 22 + 222 = 246

input
1
2

output
12

reason:
1 + 11 = 12
'''

# sum = 0
# for number in range(1,11):
#     sum += number
# print(sum)
#input
string = input()

num = int(input())

# the result of string * number is a string 
sum = 0
for number in range(1,num + 1): #range(1,3)->[1,2]
    sum += int(number * string)
print(sum)

# problem J2 of 2017
# https://cemc.math.uwaterloo.ca/contests/computing/2017/stage%201/juniorEF.pdf
