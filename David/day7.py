# a = input() # a will be a string

#convert string to integer int(a)
'''
a = input()
b = input()
c = input()


string = '12 3'

#[] store useful data ['12','3']

lst = string.split()

'12 -'

# print out +++

b = input()
x = b.split()
for i in range(int(x[0])):
    print(x[1], end="")

4
9 +
3 -
12 A
2 X



num = int(input())

for i in range(num):
    b = input()
    x = b.split()
    for j in range(int(x[0])):
        print(x[1], end="")
    print()

# create a lst
num = int(input())
inplst = []

for i in range(num):
    inplst.append(input())

for x in inplst:
    x = x.split()
    for j in range(int(x[0])):
        print(x[1], end="")
    print()


lst = ['1' ,'2' ,'3' ,'4','5' ,'6'] # convert once

lst = [1,2,3,4,5,6]
print(lst)

lst = list(map(int,lst))

16 3 2 13
5 10 11 8
9 6 7 12
4 15 14 1
'''

inp1 = input()
inp2 = input()
inp3 = input()
inp4 = input()

lst1 = inp1.split()
lst2 = inp2.split()
lst3 = inp3.split()
lst4 = inp4.split()

lst1 = list(map(int,lst1))
lst2 = list(map(int,lst2))
lst3 = list(map(int,lst3))
lst4 = list(map(int,lst4))

row1 = sum(lst1)
row2 = sum(lst2)
row3 = sum(lst3)
row4 = sum(lst4)

print(lst1)
print(lst2)
print(lst3)
print(lst4)

# 2019 J2 https://cemc.math.uwaterloo.ca/contests/computing/past_ccc_contests/2019/index.html
# 2016 J2 https://cemc.math.uwaterloo.ca/contests/computing/past_ccc_contests/2016/stage%201/juniorEn.pdf
