'''
hw:
create lambda function:

1. judge two number which one is bigger: example 5,10, 10 bigger

2 lambda to print stars, varibal(5) *****, variable(6) *******

3 create lambda to count 10 ^ 3 = 10 * 10 * 10 , 3 ^ 4 = 3 * 3 * 3 * 3
'''
# 1.
f = lambda a , b : print(str(a) +"  is bigger") if a > b else print(str(b) + " is bigger")
f(2,1)

# 2.
varibal = lambda num : print( num * '*')
varibal(6)

#3.

f3 = lambda a,b: print(a ** b)
f3(10,3)
f3(3,4)

# create a lst, in list there are 10 random number
import random as r

#create a list
lst = []
#create a 10 times loop
for _ in range(10):
#append a random number 10 times
    lst.append(r.randint(1,10))
print(lst)

lst2 = [r.randint(1,10) for i in range(10)]

print(lst2)

#filter, map, reduce
print(list(filter(lambda x: x % 2 == 0,[1,2,3,4,5,6,7])))

print(list(map(lambda x: x * 2,[1,2,3,4,5])))
# practice lambda, filter, map
# class


