"""
J1
'''
9
6
6
8
'''
a1 = int(input())
a2 = int(input())
a3 = int(input())
a4 = int(input())

cond1 = a1 == 8 or a1 == 9
cond2 = a4 == 8 or a4 == 9
cond3 = a2 == a2

if cond1 and cond2 and cond3:
    print('ignore')
else:
    print('answer')

#J2
num = int(input())

yes = input()

to = input()

count = 0
for i in range(num):

    if yes[i] == to[i] == 'C':

        count += 1

print(count)
"""
#J3
inp = input() # 3 10 12 5

lst = inp.split() #['3', '10', '12', '5']

lst = list(map(int,lst)) #[3, 10, 12, 5]

first = [0] 
# explain why  this code can get first ans
sum = 0
for i in lst:
    sum += i
    first.append(sum)

# print(first)# #[0,3,13,25,30]

# explain why this code can get answer
for i in first:
    for j in first:
        dir = j - i
        if dir < 0:
            dir = 0 - dir
        print(dir, end=' ')
    print()

#CCC 2017 J1,j2,j3






