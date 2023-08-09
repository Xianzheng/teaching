# create function
  
# judge number is a even or odd
# judge a string whether have duplicated value

'''
stereotype

def [functionname]([argument]):
    pass
'''

def ifDuplication(str):
    if len(set(str)) == len(str):
        return False
    else:
        return True

# print(ifDuplication('abcdefb') )
# print(ifDuplication('abcdef') )

def ifEvenOrOdd(num):
    if num % 2 == 0:
        print('this is even number')
    else:
        print('this is odd number')
# ifEvenOrOdd(8)
# ifEvenOrOdd(3) 

def minus(num1,num2):
    return num1 - num2
print(minus(2,5))

# times function


def add(num1,num2):
    return num1 + num2

print(add(1,2))

#amoumous
a = lambda num1,num2: num1 + num2
print(a(1,2))

#filter

lst = [1,2,3,4,5,6,7,8,9,10]

def getEven(lst):
    newLst = []
    for i in lst:
        if i % 2 == 0:
            newLst.append(i)
    return newLst
print(getEven(lst))

print(list(filter(lambda x: x % 2 == 0,lst)))

# create some anonymous function

# adding function
# minus function
# times function
# divides function
# judge a string whether have duplicated value
