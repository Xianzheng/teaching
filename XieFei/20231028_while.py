'''
i = 0


while i < 5:

    i += 1

    # if i == 2:
    #     continue

    # if i == 5:
    #     continue

    if i == 4:
        break

    print(i)
'''

'''
input
12
3

12 + 120 +1200 + 12000

input
23
2

23 + 230 + 2300
'''

inp1 = int(input())
inp2 = int(input())
# print 12 120 1200 12000 
# how we get 12 + 120 + 1200 + 12000
i = 0

sum = 0
while i < inp2 + 1:

    num = inp1 * (10 ** i)
    
    sum += num

    i += 1

print(sum)

# practice, get sum of 1 + 2 + 3 + .... + 100

'''
hw:
1
input a number
5 
1/1 + 1 /2 + 1/3 +1/4 + 1/5 = ?

10
1/1 + 1/2 +... 1/10


2(*).

inp1: 2
inp2: 3
2 + 22 + 222


'''