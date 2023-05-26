'''
2
3

246
reason
2 + 22 + 222 = 246
'''
'''
string = input()
num = int(input())

#result of string mutiply by number is string

s = 0

for i in range(1,num + 1):

    s += int(string * i)

print(s)
'''
# how to write a function
def adding(num1,num2):
    return num1 + num2

# write a anonymous function

# lambda represents anonymoys

f = lambda num1,num2,exp1:num1+num2**exp1

print(f(1,2,3))

#filter(function, iterable)

lst = [2,5,1,8,4,7,3]

result = filter(lambda num: num % 2 == 1,lst)

print(list(result))

# J3 of https://cemc.math.uwaterloo.ca/contests/computing/2019/stage%201/juniorEF.pdf