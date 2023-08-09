'''

Sample Input
5
44,62 
34,69
24,78
42,44
64,10
Output for Sample Input
23,9
65,79

'''
inp = '44,62'


#method1
#lst = inp.split(',')
# lst[0] = int(lst[0])
# lst[1] = int(lst[1])

# print(lst)
# lst = list(map(int,inp.split(',')))
# print(lst)

leftColumn = []
rightColum = []

for i in range(int(input())):
    lst = list(map(int,input().split(',')))

    leftColumn.append(lst[0])
    rightColum.append(lst[1])

print(min(leftColumn)-1,end=',')
print(min(rightColum)-1)

print(max(leftColumn)+1,end=',')
print(max(rightColum)+1)

'''
redo this question
and add command detailly
'''
