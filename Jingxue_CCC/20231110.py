
'''
n = int(input())
k = int(input())

sum = 0
sum += n

for i in range(1, k + 1):
    sum += n * 10**i

print(sum)


2
5

2+22+222+2222+22222



#   '*' is a string

result = 3 * '2'

print(type(result))

print(int('22') + int('222'))


a = input()

k = int(input())

sum = 0

for i in range(1,k+1):

    addingValue = a * i

    sum += int(addingValue)

print(sum)

2    == 2 * 10 ** 0 + 0
22   == 2 * 10 ** 1 + 2
222  == 2 * 10 ** 2 + 22
2222 == 2 * 10 ** 3+ 222


# loop record

a = int(input())

k = int(input())

record = 0
sum = 0
for i in range(k):

    addingValue = a * 10 ** i + record

    record = addingValue

    sum += addingValue

print(sum)
'''

inp = int(input())

hr = 12
min = 0

count = 0

for i in range(inp):
    min += 1

    if min == 60:
        min -= 60
        hr += 1

    if hr > 12:
        hr -= 12
    
    if min < 10:
        showMin = '0' + str(min)
    else:
        showMin = str(min)

    
    showHr = str(hr)

    showTotal = showHr+showMin
    if len(showTotal) == 4:
        if int(showTotal[3]) - int(showTotal[2]) ==  int(showTotal[2]) - int(showTotal[1]) and int(showTotal[2]) - int(showTotal[1]) ==  int(showTotal[1]) - int(showTotal[0]):
            count += 1

    if len(showTotal) == 3:
        if int(showTotal[2]) - int(showTotal[1]) ==  int(showTotal[1]) - int(showTotal[0]):
            count += 1

print(count)

'''
homework:
1
    try to do CCC2017 J4 by our own:

    https://www.cemc.uwaterloo.ca/contests/computing/past_ccc_contests/2017/stage%201/juniorEF.pdf

2
    pick 1 of 2:

    J3 OF CCC 2017

     https://www.cemc.uwaterloo.ca/contests/computing/past_ccc_contests/2017/stage%201/juniorEF.pdf

    j2 of CCC 2020

     https://www.cemc.uwaterloo.ca/contests/computing/past_ccc_contests/2020/ccc/juniorEF.pdf





'''
P = int(input())
N = int(input())
R = int(input())

infect = N
infectT = N
days = 0

for i in range(1000000000): 
    if infectT > P:
        print(days)
        break

    infect = infect * R
    infectT += infect
    days += 1



