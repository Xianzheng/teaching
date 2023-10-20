'''
a1 = [int(i) for i in input().split()]
a2 = [int(i) for i in input().split()]
a3 = [int(i) for i in input().split()]
a4 = [int(i) for i in input().split()]
row1 = 0
row2 = 0
row3 = 0
row4 = 0
for i in range(4):
    row1 += int(a1[i])
    row2 += int(a2[i])
    row3 += int(a3[i])
    row4 += int(a4[i])
c1=a1[0]+a2[0]+a3[0]+a4[0]
c2=a1[1]+a2[1]+a3[1]+a4[1]
c3=a1[2]+a2[2]+a3[2]+a4[2]
c4=a1[3]+a2[3]+a3[3]+a4[3]
test = {row1,row2,row3,row4,c1,c2,c3,c4}
if len(test) == 1:
    print('magic')
else:
    print('not magic')


#DRY(DON'R REPEAT YOURSELF


total = []
for i in range(4):
    total.append(list(map(int,input().split())))

columnToal = []
for i in range(4):
    lst = []
    for j in range(4):
        lst.append(total[j][i])
    columnToal.append(lst)

sumlst = []
for i , j in zip(total,columnToal):
    sumlst.append(sum(i))
    sumlst.append(sum(j))

if len(set(sumlst)) == 1:
    print('magic')
else:
    print('not magic')

#concise
'''

inp = list(map(int,input().split()))

lst = [0]

sum= 0
for i in inp:
    sum += i
    lst.append(sum)

for i in lst:
    for j in lst:
        print(j - i,end=' ')
    print()

# finish 2018 J3
#https://www.cemc.uwaterloo.ca/contests/computing/past_ccc_contests/2018/stage%201/juniorEF.pdf

# THINK 2018 J4
#https://www.cemc.uwaterloo.ca/contests/computing/past_ccc_contests/2018/stage%201/juniorEF.pdf




