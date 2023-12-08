"""
def checkTable(table):
    '''
    parameter: table is two Dimensional list

    each row should be in order(from small to big)
    each column shoube in order(from small to big)
    if it is return True
    else return False
    '''
    # check if eachRow is inorder
    for eachRow in table:
       if eachRow != sorted(eachRow):
           return False
    
    tempTable = []
    for i in range(3):
        lst = []
        for j in range(3):
            lst.append(table[j][i])
        tempTable.append(lst)

    for eachRow in tempTable:
       if eachRow != sorted(eachRow):
           return False
    
    return True



def rotate90(table):
    # Suppose table is a square matrix (n x n)
    n = len(table)

    # Create an empty table
    newTable = [[0] * n for _ in range(n)]

    # Rotate the elements 90 degrees
    for i in range(n):
        for j in range(n):
            newTable[i][j] = table[n - j - 1][i]

    return newTable

def inputTable():

    return [list(map(int,input().split()))for i in range(int(input()))]

table = inputTable()

while not checkTable(table):

    table = rotate90(table)

for i in table:
    print(*i)


'''
(divide and conquer)
make big question to small


1.convert big question to many small questions

2. solve each small questions

3. combine solving method to conquer big question


'''
"""
# classic question

# fibnocci sequestion

#from third number, every item shoud equal the sum of previous two item

# 1   1   2    3    5      8 13 21 ....

# consider to print fibbnocci sequence to 30 items.

#[1,2,3,4,5...24]

dis = 1

s = list(map(int,input().split(':')))

t = s[0] + s[1]/60

while dis > 0:

    if 7 <= t < 10 or 15 <= t < 19:
        speed = 0.25
    else:
        speed = 0.5

    dis -= speed * 1

    t += 1

    if dis < 0:
        t -= abs(dis)/speed

    if t > 24:
        t -= 24

hr = int(t)
min = t - hr

if hr < 10:
    strhr = str(0) + str(hr)
else:
    strhr = str(hr)

if min*60 < 10:
    strmin = str(0) + str(int(min))
else:
    strmin = str(int(round(min*60,0)))

print(strhr+':'+strmin)

# redo 2016 J4 by yourself

#https://www.cemc.uwaterloo.ca/contests/computing/past_ccc_contests/2016/stage%201/juniorEn.pdf




   