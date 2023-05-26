# lambda function
# filter()
# map()
# reduce() # web spider, data analyse
# (application: website contains backend and frontend, web spider, data analyse, intellgence)

#  basic way to go CCC contest(once one year, feburary or match each year : level 4)

#(1 - 4: use basic data structure, string, list, dictionary, set, tuple)
# 5: algorithm, and recursive

# lst = [1,2,3,4]
#
# #print(list(reversed(lst)))
# print(lst[::-1])
#
# lst = lst[::-1]
# print(lst)
'''
inp=input()

a='12'

b=a+inp
lst=[]

for i in b:
    lst.append(i)

lst1=list(map(int,lst))
lst2=list(reversed(lst1))

print(lst1)
result = []

for i in range(len(lst1) - 1, 0, -1):
    result.append(lst1[i] - lst1[i - 1])
print(result)
'''

lst = [1,2,3,4]

#index 0 1 2 3

#for i in range(0,len(lst),1):# range(len(lst))
#    print(i)

for i in range(len(lst) - 1,0,-1):
    print(i)
#https://cemc.math.uwaterloo.ca/contests/computing/2019/stage%201/juniorEF.pdf
#Problem J3: Cold Compress

#https://cemc.math.uwaterloo.ca/contests/computing/2017/stage%201/juniorEF.pdf
#Problem J4: Favourite Times
