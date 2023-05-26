# https://cemc.math.uwaterloo.ca/contests/computing/past_ccc_contests/2017/stage%201/juniorEF.pdf
# 3 4
# 3 3
str1 = input()
str2 = input()
step = int(input())

lst1 = list(map(int,str1.split()))
lst2 = list(map(int,str2.split()))

x1 = lst1[0]
x2 = lst2[0]

y1 = lst1[1]
y2 = lst2[1]

distance = abs(x1 - x2) + abs(y1 - y2)

cond1 = distance % 2 == 1 and step % 2 == 1

cond2 = distance % 2 == 0 and step % 2 == 0

cond3 = distance == 0

if cond1 or cond2 or cond3:
    print('Y')
else:
    print('N')

#print ("Y" if (charge == abs(distance)) or (charge % 2 == 0 and abs(distance) % 2 == 0) or (charge % 2 != 0 and abs(distance) % 2 != 0) else "N")
