# write code how we can get 1 to 10 on terminal?

# using while loop and for loop to print 1 to 10 on terminal?
'''
num = 1
while num <= 10:
    print(num)
    num += 1


num = 0

while num < 10:

    num += 1
    print(num)

#recursive to print 1 to 10

# ? write a adding function

# print(adding(1,2)) # we will get 3
# print(adding(10,20)) # we will get 30


def functionName([arg1,arg2]):
    return arg1 + arg2

def adding(a, b):
    return a + b

print(adding(1,2))
print(adding(10,20))

def sayHello(name):

    print('Hello',name)

sayHello('Pascal')
sayHello('Xavier')
'''


#recursive to print 1 to 10

#recursive is function call it's self

#recursive happens function call it self, adjust argument
#recursive also need a end point

# def a(num):
#     print(num)

#     if num == 10:
#         return

#     a(num + 1)

# a(1)

# write recursive to print 10,12,14,16,18,20

# def a(num):
#     print(num)

#     if num == 20:
#         return

#     a(num + 2)

#  write a recursive code to print 100,98,96,94,92,90


# def b(num):
#     print(num)

#     if num == 90:
#         return
#     b(num - 2)

# b(100)

# write a recursive code to print 9,18,27,36,45,54
# def b(num):
#     print(num)
#     if num == 54:
#         return
#     b(num+9)
# b(9)

def r(num):
    

    if num == 1:
        return 1
    
    return r(num - 1) + num

print(r(50))

#calculate the sum of 1 + 2 + 3


# fibbonacci sequence

# 1,1,2,3,5,8,13,21

def f(n):
    if n == 1:
        return 1
    elif n == 2:
        return 1
    else:
        return f(n - 2) + f(n - 1)
    

print(f(8))

# 1. using recursive to print out 100, 200 , 300, 400 ,'''', 1000

# 2. draw fibbonacci sequence's diagram, find out how recursive work

# 3(*).
# using recursive or loop
'''
Question: The monkey picked a few peaches on the first day. He ate half of them immediately, 
but he was still not satisfied, so he ate one more. On the second day,
he ate half of the remaining peaches, but he was still not satisfied, 
so he ate one more. After that, Every day I eat more than half of the remaining peach from the previous day. 
When I want to eat more on the 10th day, there is only one peach left. How many peaches were picked on the first day?
'''