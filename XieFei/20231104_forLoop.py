'''
# prev homework


input a number
get the factorial of this number
5
5 * 4 * 3 * 2 * 1 == 1 * 2 * 3 * 4 * 5

consider how to print 100,99,98 ..., 1


num = int(input())

# print(list(range(1,num + 1)))
factorial = 1

for i in range(1,num + 1):

    factorial *= i

print(factorial)



for i in range(100 , 0 , -1):
    print(i)


# make a program, get average

# input
3 # we have 3 time input
1
2
3
#output
2

5
2
2
2
2
2
# output will be 2


num = int(input())

sum = 0

for i in range(num):

   sum += int(input())

average = sum / num

print(average)
'''



'''

redo the question:(do the code by your self)
1.
# input
3 # we have 3 time input
1
2
3
#output
2

5
2
2
2
2
2
# output will be 2

use while loop and for loop to do CCC 2017 J2

https://www.cemc.uwaterloo.ca/contests/computing/past_ccc_contests/2017/stage%201/juniorEF.pdf

next:

we will learn data structure
'''