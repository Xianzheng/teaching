'''
last week homework
'''
# 3
# 4 3 1 -> ['4','3','1']
# 6 5 2
# 9 7 3

# console:
# #convert input to twoDlist
# [[4,3,1],[6,5,2],[9,7,3]]
#advanced question how to rotate
#rotate once ->[[9,6,4],[7,5,3],[3,2,1]]
num = int(input())
table = []
for i in range(num):
    raw = input().split()
    # print(raw)
    lst = list(map(int,raw))
    # print(lst)
    table.append(lst)

print(table)

# MAKE the original table's third row's first element , second row's first element , first row's first element to new table's first row
# MAKE the original table's third row's second element , second row's second element , first row's second element to a new table's second row
# MAKE the original table's third row's third element , second row's third element , first row's thrid element to a new table's third row

'''
def rotate(original):

    # static way: in this function, we set our original table must have three rows and three columns

    newtable = []

    newtable.append([original[2][0],original[1][0],original[0][0]])

    newtable.append([original[2][1],original[1][1],original[0][1]])

    newtable.append([original[2][2],original[1][2],original[0][2]])

    print(newtable)

rotate(table)
'''

def advancedRotate(oldTable):
    oldTablesRows = len(oldTable)
    # print(oldTablesRows)
    newTable = []
    #how many rows we want adding to new newTabel
    for i in range(oldTablesRows):
        # i  will be 0 1 2
        # defind each row
        row = []
        # define each rows' element
        # ?1
        for j in range(oldTablesRows - 1, -1, -1):
            # j shoud be 2 1 0
            #core: which element we need to add
            #row.append(oldTablesRows[rows][i])
            # ? 2
            row.append(oldTable[j][i])

        newTable.append(row)
    print(newTable)
    

advancedRotate(table)

