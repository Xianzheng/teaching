'''
lst = [[0 for i in range(3)] for i in range(3)]# list comprehension

lst = []
newlst = []
for i in range(3):
    lst.append(0)

for i in range(3):
    newlst.append(lst)
print(newlst)

#[0,1,2,3,4]
lst = []
for i in range(5):
    lst.append(i)
print(lst)

#lst comprehension
lst = [i for i in range(5)]
print(lst)
# filter
# map
# reduce

lst = [i * 2 for i in range(5)]
print(lst)

lst = [i * 2 for i in range(5) if i != 2]
print(lst)

lst = ['a','b','c','d']

# lst = [i for i in lst[:-1]]
print(lst[: -1])

# dictionary comprehension
dic = {'key{}'.format(i) : i * 2 + 3 for i in range(5) if i > 0}
print(dic)

# set comprehension
# unique
s = {i for i in range(5) if i > 0}
print(s)

# tuple
myTuple = tuple((i for i in range(5) if i > 0))
print(myTuple)


def check(lst) :
    condition1=0
    condition2=0
    for i in range(len(lst)-1):
        if sum(lst[i])< sum(lst[i+1]) :
            condition1+=1
    if condition1==len(lst)-1:
        for i in range(len(lst)):
            templst=()
            templst=sorted(lst[i])
            if templst==lst[i]:
                condition2+=1
    if condition2==len(lst):
        return True
    else:
        return False
'''

lst = [[1,2,3],[4,5,6],[7,8,9]]
lst1 = [[7,4,1],[8,5,2],[9,6,3]]
lst2 = [[7,8,9],[4,5,6],[1,2,3]]
def check(lst):
    for eachRow in lst:
        if eachRow != sorted(eachRow):
            return False
    for i in range(len(lst)):
        newlst = []
        for j in range(len(lst)):
            newlst.append(lst[j][i])
        if newlst != sorted(newlst):
            return False
    return True

def rotate(lst):
    pass

while check(lst) == False:
    lst = rotate(lst)

display(lst)


print(check(lst2))
# do review
# make some improvement for your code
# look j4 in 2017
# https://cemc.math.uwaterloo.ca/contests/computing/2017/stage%201/juniorEF.pdf