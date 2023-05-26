#Determine how many prime numbers are between 101-200, and output all prime numbers.
'''
from operator import mod

def isprime(n):
    for i in range(2,n):
        if mod(n,i) == 0:
            return 0
    return 1
def findprimes(min, max):
    primesfound = []
    for n in range(min,max):
        if isprime(n) == 1:
            primesfound.append(n)
        
    return primesfound



print(findprimes(101, 200))
print(len(findprimes(101, 200)))
'''

def isPrime(num:  int ) -> bool:
    '''
    parameter is a number
    return a boolean
    '''
    for i in range(2,num):
        if num % i == 0: # get reminder
            return False
    return True

def printPrimeBetween(min: int,max: int) -> int:
    counter = 0
    for i in range(min,max+1):

        if isPrime(i):
            print(i)
            counter += 1
    return counter

# print('counter numbers',printPrimeBetween(101,200))

# % get reminder

if 11 % 2 == 0:
    print('it is even number')
else:
    print('it is odd number')
