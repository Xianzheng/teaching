'''
lst = ['9','+']
print(int(lst[0]) * lst[1])

lst = ['3','-']
print(int(lst[0]) * lst[1])

lst = ['12','A']
print(int(lst[0]) * lst[1])

lst = ['2','x']
print(int(lst[0]) * lst[1])
'''



num = int(input())

lst1 = input()#'9 +'
#               012
lst2 = input()#3 -
#               012
# 
lst3 = input()#12 A
#               012
lst4 = input()#'2 x
#               012'
print(int(lst1[0]) * lst1[2])
print(int(lst2[0]) * lst2[2])
print(int(lst3[0]) * lst3[2])
print(int(lst4[0]) * lst4[2])
print('end')

'''

hw:
if our input should be exactlly look like
9 +
3 -
12 A
2 X

how we can get output like

+++++++++
---
AAAAAAAAAAAA
XX
'''

