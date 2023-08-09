
def ifDuplication(str):
    if len(set(str)) == len(str):
        return False
    else:
        return True

# if we want to create a variable function,
#  we need to use key word lambda   
# a is a variable
a = lambda str: len(set(str)) == len(str)

# if we don't call(invoke) this function
# this function won't be execited

def run():
    string = '123'
    print(string[3])

# run()

# print(a('12341'))
# print(a('1234'))

'''
sterotype: anonymous function(lambda)

lambda function defaultly have return 
lambda arg1, arg2: print('hello')

if we want to run lambda function 
we have to assign lamba function to a variable
and use variable like function
'''
a = lambda arg1, arg2: print('hello')

# print(a(1,2))

b = lambda arg1, arg2: arg1 + arg2
# print(b(1,2))


# create some anonymous function

# 1.adding function # already finished
# 2.minus function
# 3.times function
# 4.divides function
# 5.judge a string whether have duplicated value

a = lambda str: len(set(str)) == len(str)

# judge number is a even or odd

# thinking how to use if statement in lambda

def evenOrodd(num):
    if num % 2 == 0:
        return 'Even'
    else:
        return 'Odd'

print(evenOrodd(8))
print(evenOrodd(3))

evenOrodd1 = lambda num: 'Even' if num % 2 == 0 else 'Odd'

print(evenOrodd1(8))
print(evenOrodd1(3))

'''
hw:
create lambda function:

1. judge two number which one is bigger: example 5,10, 10 bigger

2 lambda to print stars, varibal(5) *****, variable(6) *******

3 create lambda to count 10 ^ 3 = 10 * 10 * 10 , 3 ^ 4 = 3 * 3 * 4 * 3
'''
