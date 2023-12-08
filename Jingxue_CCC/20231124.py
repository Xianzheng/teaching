'''
T = input()
S = input()
sLen = len(S)
tLen = len(T)
c = 0
DS = S + S
for i in range(sLen):
    c += ord(T[i]) - ord(S[i])

def cycle(str):
    if str in DS:
        return True
    return False


if c == 0 and cycle(T[0:sLen]):
    print("yes")
else:
    findone = False
    for i in range(sLen, tLen):
        c -= ord(T[i-sLen])
        c += ord(T[i])
        if c == 0 and cycle(T[i-sLen+1:i+1]):
            findone = True
            print("yes")
            break
    if not findone:
        print("no")



num = int(input())
table = []
for i in range(3):
    lst = input().split()
    table.append(lst)

print(table)



tLst = [[1,2,3],[4,5,6],[7,8,9]]

row0 = tLst[0]

row1 = tLst[1]

row2 = tLst[2]

# print(tLst[0][0])
# print(tLst[0][1])
# print(tLst[0][2])
# print(tLst[1][0])
# print(tLst[1][1])

# for i in range(3):
#     for j in range(3):
#         print(tLst[i][j])

for i in range(3):
    for j in range(3):
        print(tLst[j][i])




num = int(input())
table = []
for i in range(3):
    lst = input().split()
    lst = list(map(int,lst))
    table.append(lst)

print(table)
'''
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


table1 = [[1,2,3],[4,5,6],[7,8,9]]
print(checkTable(table1)) # True

table2 = [[3, 7, 9], [2, 5, 6], [1, 3, 4]]
print(checkTable(table2)) # False

# lst = [2,2,4]
# print(lst)
# print(sorted(lst))

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


def convertRowToColumn(table):
    # Use zip to transpose the table
    transposedTable = list(map(list, zip(*table)))
    return transposedTable


def checkRowinOrder(table):
    # Check each row for order
    for row in table:
        if row != sorted(row):
            return False
    return True

originalTable = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

rotatedTable = rotate90(originalTable)
print("Rotated Table:")
print(rotatedTable)

transposedTable = convertRowToColumn(originalTable)
print("\nTransposed Table:")
print(transposedTable)

inOrder = checkRowinOrder(originalTable)
print("\nRows in Order:", inOrder)

'''
# implement 3 function
    1.rotate90(table)
    2.convertRowToColumn(table)
    3. checkRowInOrder(table)
'''




