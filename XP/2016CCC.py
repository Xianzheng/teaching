'''
pascal code
inp1 = input()
inp2 = input()
inp3 = input()
inp4 = input()
inp5 = input()
inp6 = input()

# list
group = [inp1, inp2, inp3, inp4, inp5, inp6]
print(group)

W = group.count('W')

if W == 6 or W == 5:
    print('1')
elif W == 4 or W == 3:
    print('2')
elif W == 2 or W == 1:
    print('3')
elif W == 0:
    print('-1')

# Xavier
ans1=input()
ans2=input()
ans3=input()
ans4=input()
ans5=input()
ans6=input()
# tuples
tot = (ans1,ans2,ans3,ans4,ans5,ans6)
print(tot)
wins=tot.count('W')
if wins == 5 or wins == 6:
    print('1')
if wins == 3 or wins == 4:
    print('2')
if wins == 1 or wins == 2:
    print('3')
if wins < 1:
    print('-1')

group = []
for i in range(6):
    group.append(input())
W = 0
for i in group:
    if i == 'W':
        W += 1

if W == 6 or W == 5:
    print('1')
elif W == 4 or W == 3:
    print('2')
elif W == 2 or W == 1:
    print('3')
elif W == 0:
    print('-1')

'''
# input() is string'16 3 2 13'
# input().split() convert string to list, ['16','3','2','13']
# list(map(int,input().split())) convert each item from list, 
# from string to num [16,3,2,13]
row1 = list(map(int,input().split()))
row2 = list(map(int,input().split()))
row3 = list(map(int,input().split()))
row4 = list(map(int,input().split()))
# print(row1)
# print(row2)
# print(row3)
# print(row4)
row1Sum = sum(row1)
row2Sum = sum(row1)
row3Sum = sum(row1)
row4Sum = sum(row1)

col1 = [row1[0],row2[0],row3[0],row4[0]]
col2 = [row1[1],row2[1],row3[1],row4[1]]
col3 = [row1[2],row2[2],row3[2],row4[2]]
col4 = [row1[3],row2[3],row3[3],row4[3]]

col1Sum = sum(col1)
col2Sum = sum(col1)
col3Sum = sum(col1)
col4Sum = sum(col1)
