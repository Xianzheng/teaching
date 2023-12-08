'''
# 3 10 12 5

lst = list(map(int,input().split()))

print(lst)

tempRow = [0]

sum = 0

for i in lst:

    sum += i

    tempRow.append(sum)
    
#print(tempRow)

for i in tempRow:

    for j in tempRow:

        print(j - i, end = ' ')
    
    print()

'''

x1,y1 = map(int,input().split())

x2,y2 = map(int,input().split())

t = int(input())

distance = abs(x1 -x2) + abs(y1 - y2)

if distance <= t and (t - distance) % 2 == 0:
    print('Y')
else:
    print('N')

'''

redo CCC 2018 J3
https://www.cemc.uwaterloo.ca/contests/computing/past_ccc_contests/2018/stage%201/juniorEF.pdf

redo CCC 2017 j3
https://www.cemc.uwaterloo.ca/contests/computing/past_ccc_contests/2017/stage%201/juniorEF.pdf

think CCC 2016 J3
https://www.cemc.uwaterloo.ca/contests/computing/past_ccc_contests/2016/stage%201/juniorEn.pdf
'''



