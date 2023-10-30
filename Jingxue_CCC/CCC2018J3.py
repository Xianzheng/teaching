'''
#3 10 12 5

inp = input()

strLst = inp.split()

# print(strLst)

# strLst[0] = int(strLst[0])

l = len(strLst)

for i in range(0, l):
    strLst[i] = int(strLst[i])

print(strLst)
'''

#inp = 3 10 12 5
intLst = list(map(int,input().split()))
# intLst = [3,10,12,5]
# thinking traver in cite1 the distance between each city[0,3,13,25,30]
# how to use [3,10,12,5] to make [0,3,13,25.30]

initialLst = [0]

# 0 3 13 25 30
sum = 0
for i in intLst:
    sum += i
    initialLst.append(sum)


for i in initialLst:
    for j in initialLst:
        dis = j - i
        if dis < 0:
            dis = abs(dis)
        print(dis , end = ' ')
    print()


# summany

'''
1. CCC INPUT 3 10 15 5
USE NUMBER EFFECTIVE

a . lst = input().split()
for index in range(len(lst)):
    lst[index] = int(lst[index])

a. lst = list(map(int,input().split()))

b. undertand how nested loop run's logic


hw: do 2016 J2:
choose any way:
link: https://www.cemc.uwaterloo.ca/contests/computing/past_ccc_contests/2016/stage%201/juniorEn.pdf
'''

