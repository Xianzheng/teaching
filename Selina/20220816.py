'''
#3. Determine how many prime numbers are between 101-200, and output all prime numbers.
s = 0
for i in range(101,201):
    for j in range(2,i):
        if i % j == 0:# it is not a prime number

            break
    else:
        print(i)
        s += 1

print('total prime number is',s)
'''

def isPrime(number):
    lst = []
    for i in range(2, number):
        if number % i == 0:
            return False

    return True

s = 0
for i in range(101,201):

    if isPrime(i) == True:
        print(i)
        s += 1
print(s)

''' 
A ball falls freely from a height of 100 meters, 
and bounces back to half of its original height each time it hits the ground; 
when it falls again, how many meters does it travel when it hits the ground for the 10th time? 
How high is the 10th rebound?

#https://cemc.math.uwaterloo.ca/contests/computing/past_ccc_contests/2019/stage%201/juniorEF.pdf
lst = [1,2,3,4] # [3,2,1,4]
lst[0],lst[2] = lst[2],lst[0]
'''

