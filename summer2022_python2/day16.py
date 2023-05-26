'''
lst = [[1,2,3],[4,5,6],[7,8,9]]



# [2][0] -> [0][0]
# [1][0] -> [0][1]
# [0][0] -> [0][2]


reversedLst = [[0,0,0],[0,0,0],[0,0,0]]
for i in lst:
    print (*i)

for x in range(3):
    for y in range(3):
        reversedLst[x][y] = lst[2-y][x] 

for i in reversedLst:
    print(*i)


for i in range(3):
    for j in range(3):
        print(i, j)

# prime number

# print all prime numbers between 1 - 100

for i in range(2,101):
    for j in range(2,i):
        if i % 2 == 0:
            break
    else:
        print(i)

1
1 2
1 2 3
1 2 3 4

for i in range(1,5):
    
    for j in range(1, i+1):

        print(j, end= ' ')

    print()

'''
