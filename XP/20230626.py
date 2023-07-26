

def rotate(table):
    rowLen = len(table)
    afterRotate = []
    for i in range(rowLen):
        row = []
        for j in range(rowLen - 1, -1,-1):
            row.append(table[j][i])
        afterRotate.append(row)
    return afterRotate
# newTable = rotate(table1)
# print(rotate(newTable)) 
# print(newTable)
# judge if table fit rules

def checkTable(table) -> bool:
    '''
    #check if this table fit rules
    # rule1 : each row from left to right follows less to bigger
    # rule2 : each column from top to bottom follows less to bigger
    # how fit rule row look like
    '''

    #check rule1
    for eachRow in table:
        followRulesRow = sorted(eachRow)
        if eachRow != followRulesRow:
            return False
        
    #check rule2
    #thinking how to make a column list(reverseTable) and check
    # [[4,3,1],[6,5,2],[9,7,3]]
    # reversed table [[4,6,9],[3,5,7],[1,2,3]]
    reversedTable = []
    for rowIndex in range(len(table)):
        # print(index)
        row = []
        for colunmIndex in range(len(table)):
            row.append(table[colunmIndex][rowIndex])
        reversedTable.append(row)
    
    for eachRow in reversedTable:
        followRulesRow = sorted(eachRow)
        if eachRow != followRulesRow:
            return False
    # if row and columns don't have any question     
    return True


# table1 = [[1,2,3],[4,5,6],[7,8,9]]
table= [[4,3,1],[6,5,2],[9,7,3]]
print('initial')
for row in table:
    print(*row)

# if table not follows rule, rotate, until follow the rule

while checkTable(table) == False :
    print('\nrotate')
    table = rotate(table)
    for row in table:
        print(*row)


print('\nfinal')

for row in table:
    print(* row)


'''
hw: try cide by your self
2018 J4

make input to 2d array
'''


'''
input 
3
3 7 9
2 5 6
1 3 4
'''

#check how to reverse Table
#after reverse
'''
3 2 1
7 5 3
9 6 4
'''

#check table follow ruls: each row follows from bigger to less, column row follows from bigger to less

# sorted(lst,reverse == True)

lst = [1,5,6,9]
print(sorted(lst,reverse=True))



