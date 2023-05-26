# string='+++===!!!!'
#
# lst = list(string)
#
# unique = list()
# for i in range(len(string) - 1):
#     if lst[i]!=lst[i+1]:
#         unique.append(lst[i])
# unique.append(lst[-1])
# print(unique)

# inp=int(input())
# lst=[]
# for i in range(inp):
#     tempinp=input()
#     lst.append(tempinp)
# a=()
# lst1=[]
# for i in range(inp):
#     for j in range(len(lst[i])):
#         #print(lst[i][j])
#         lst1.append(lst[i][j])
#     print(lst1)
#
#
# lst2=[]
# for i in range(len(lst1)-1):
#
#     if lst1[i]!=lst1[i+1]:
#         lst2.append(lst1[i])
# lst2.append(lst1[-1])
#
# lst3=[]
# for i in range(len(lst1)):
#     for j in lst2:
#         a = lst1.count(j)
#         lst3.append(j + ':' + str(a))
#
# keys=[]
# value=[]
# for i in range(len(lst3)):
#     keys.append(lst3[i][0])
#     value.append(lst3[i][2])
#
# dic=dict(zip(keys,value))
#
# print(dic)

def parse(string):
    #do some parse
    lst = list(string)
    count = 1
    for i in range(len(lst) - 1):
        if lst[i] != lst[i + 1]:
            print(count, end = ' ')
            print(lst[i],end=' ')
            count = 1
        else:
            count += 1

    print()

inp=int(input())
lst=[]
for i in range(inp):
    tempinp=input()
    lst.append(tempinp)

for i in lst:
    parse(i)

# 2018 j3 , j4
# https://cemc.math.uwaterloo.ca/contests/computing/2018/stage%201/juniorEF.pdf