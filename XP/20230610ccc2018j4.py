'''
num = int(input())
# each input is a string
twoDlst = []
for _ in range(num):
    string = input()
    lst = string.split()
    lst = list(map(int,lst))
    twoDlst.append(lst)

print(twoDlst)


lst = [1,2,3,4,5,6,7,8,9]

#index 0 1 2 3 4 5
print(lst[5])
# twoDarray =
twoDlst = [[1,2,3],[4,5,6],[7,8,9]]

#index       0         1      2 
# row        row0    row1    row2            
# 
print(twoDlst[1])# row1  
print(twoDlst[1][1]) # combination of row1 and col1

#       step1   step2     step3
inp1 = '1 3' # ['1','3'], [1,3]
inp2 = '2 9' # ['2','9'], [2,9]

#how to make step2 from step1
step2 = inp1.split()
print(step2)

#how to make step3 from step2
step3 = list(map(int,step2))
print(step3)

#step3 = list(map(int,step2))
inp2 = '2 9' #[2,9] convert string to list contains tow integer number                              

step3 = inp2.split()

print(step3[0],type(step3[0]))

print(step3[1],type(step3[1]))

step3[0] = int(step3[0])
step3[1] = int(step3[1])

print(step3[0],type(step3[0]))

print(step3[1],type(step3[1]))

for i in range(len(step3)):
    step3[i] = int(step3[i])
print(step3)
'''

# positive 90 degree rotate

table1 = [[1,3],[2,9]]

# table2 = [[2,1],[9,3]]

def rotate(table):
    rowLen = len(table)
    
    afterRotate = []
    for i in range(rowLen):
        row = []
        for j in range(rowLen - 1, -1,-1):
            row.append(table[j][i])
        afterRotate.append(row)

    return afterRotate

newTable = rotate(table1)
print(rotate(newTable)) 
#[[2,1],[9,3]]


'''
input
3
4 3 1
6 5 2
9 7 3

console:
#convert input to twoDlist
[[4,3,1],[6,5,2],[9,7,3]]

#advanced question how to rotate
#rotate once ->[[9,6,4],[7,5,3],[3,2,1]]
#rotate again -> [[3,7,9],[2,5,6],[1,3,4]]

input:
3
3 7 9
2 5 6
1 3 4

console:
#convert input to twoDlist

#advanced question how to rotate
'''




