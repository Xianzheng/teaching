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


string = '12 A'
#index    0123


a = input()
lst2 = input()
lst3 = input()
lst4 = input()

print(int(a[0]) * a[2])
print(int(lst2[0]) * lst2[2])
print(int(lst3[0:2]) * lst3[3])
print(int(lst4[0]) * lst4[2])

# variableName      value    
name = 'mark'

a = 'mark'

# second data structure list

# create empty list
lst1 = []
lst2 = list()

print(lst1,lst2)

lst1.append('Mark')
print(lst1)
lst1.append('XieFei')
print(lst1)
lst1.append('Andrew')
print(lst1)

print(lst1[0])
print(lst1[1])
print(lst1[2])


lst1 = []
lst1.append(9)
lst1.append('X')
print(lst1)
print(lst1[0] * lst1[1])

lst1 = [12,'A']
print(lst1[0] * lst1[1])
'''

lst = []
#add some thing to container
lst.append('apple')

lst.append('banana')

lst.append('cherry')

print(lst)

# how to take out some value from list

lst.pop(0)
print(lst)

lst.pop(1)
print(lst)

'''
home work:

1. make an empty list

2. put 5 your favorite food in to this lst

3. take out two of it

4. add two more.
'''