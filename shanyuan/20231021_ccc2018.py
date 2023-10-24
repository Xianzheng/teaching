'''
lst = []
size = int(input())

for i in range(size):
    lst.append(list(map(int,input().split())))



def flip(lst1,s):
    ln = s-1
    inum = 0
    templst = []
    r = True
    tlst = []
    while r:
        tlst.append(lst1[ln][inum])
        ln -= 1
        if ln < 0:
            ln = s-1
            inum += 1
            templst.append(tlst)
            tlst = []
            if inum > s-1:
                r = False
    return templst


finallst = lst
correct = False
while not correct:
    correct = True
    for i in finallst:
        if sorted(i) != i and correct:
            correct = False
            finallst = flip(finallst,size)
    flist = flip(finallst,size)
    
    for i in flist:
        big = i[0] + 1
        for j in i:
            if j < big:
                big = j
            elif correct == True:
                correct = False
                finallst = flip(finallst,size)
for i in finallst:
    print(*i)

# add comment


#swap

a = 10
b = 20

# c = a
# a = b
# b = c
# print(a,b)

a,b = b,a
print(a,b)

# J4: Flipper
a,b,c,d = 1,2,3,4
for i in [*input()]:
    if i == 'H':
        a,b,c,d = c,d,a,b
    if i == 'V':
        a,b,c,d = b,a,d,c
print(a,b)
print(c,d)
'''
# fibbonacci sequence

# 1,1,2,3,5,8,13,21 ...
# 0 1 2 3 4 5 6 7 ....

# consider to get 30 items
# while
def getsequence(num):
    a,b = 1,1
    # Safety
    if num == 1 or num == 0:
        return a
    for i in range(num-1):
        a,b = b,a+b
    return b
print(getsequence(6))

# print(whileGetItem(6)) # we will get 13
# print(whileGetItem(7)) # we will get 21

# recursive

# recursive:
# 1  function will call itself
# 2. we need to modify the argument funtion
# 3. function needs to have a end point
# 4. understand the relation between each element

def f(i):

    if i == 0 or i == 1: return 1
    else: return f(i - 2) + f(i - 1)

print(f(6))


# using recursive to print 1 to 10

def rPrint(i):
    print(i)
    if i == 10:
        return 
    else:
        return rPrint(i + 1)
    
rPrint(1)

'''
猴子第一天摘了若干个桃子，
当即吃了一半，还不解馋，又多吃了一个；
第二天，吃剩下的桃子的一半，还不过瘾，
又多吃了一个；以后每天都吃前一天剩下的一半多一个，
到第10天想再吃时，只剩下一个桃子了。问第一天共摘了多少个桃子？
'''

# hw:
# use while loop do this question
# (*)consider using recursive way to do this question
# (*)consider to use recursive get 1 + 2 + 3 ... 10