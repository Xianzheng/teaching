inp=int(input())
lst=[]
templst=[]
for i in range(inp):
    a = input().split(' ')
    lst.append(a)
    templst.append(a)
print(lst)
print('templst',templst)
b=False

'''
templst[0][0]=lst[0][2]
templst[0][1]=lst[1][2]
templst[0][2]=lst[2][2]
templst[1][0]=lst[0][1] 
templst[1][1]=lst[1][1]
templst[1][2]=lst[2][1]
templst[2][0]=lst[0][0]
templst[2][1]=lst[1][0]
templst[2][2]=lst[2][0]
print(templst)
'''
[['4', '3', '1'], ['6', '5', '2'], ['9', '7', '3']]
templst = [[0,0,0],[0,0,0],[0,0,0]]
test1=[]
for i in range(len(lst)):

    for j in range(len(lst[i])):
        templst[i][j]=lst[j][2-i]



print(templst)

