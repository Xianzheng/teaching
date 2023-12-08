
'''
# basic
lst1 = [int(i) for i in input().split()]
lst2 = [int(i) for i in input().split()]
lst3 = [int(i) for i in input().split()]
lst4 = [int(i) for i in input().split()]

sumRow1 = lst1[0] + lst2[1] + lst3[2] + lst4[3]
sumCol1 = lst1[0] + lst2[0] + lst3[0] + lst4[0]

sumRow2 = lst2[0] + lst2[1] + lst2[2] + lst2[3]
sumCol2 = lst1[1] + lst2[1] + lst3[1] + lst4[1]

sumRow3 = lst3[0] + lst3[1] + lst3[2] + lst3[3]
sumCol3 = lst1[2] + lst2[2] + lst3[2] + lst4[2]

sumRow4 = lst4[0] + lst4[1] + lst4[2] + lst4[3]
sumCol4 = lst1[3] + lst2[3] + lst3[3] + lst4[3]

print(sumCol1)
print(sumCol2)
print(sumCol3)
print(sumCol4)
print(sumRow1)
print(sumRow2)
print(sumRow3)
print(sumRow4)


if sumRow1 == sumCol1 == sumRow2 == sumCol2 == sumRow3 == sumCol3 == sumRow4 == sumCol4:
    print("magic")
else:
    print("not magic")


#build-in function

# lst = [1,2,3,4,5,6,7,8,9,10]

# build in function sum()

lst1 = [int(i) for i in input().split()]
lst2 = [int(i) for i in input().split()]
lst3 = [int(i) for i in input().split()]
lst4 = [int(i) for i in input().split()]

sumRow1 = sum(lst1)
sumCol1 = sum([lst1[0], lst2[0], lst3[0] , lst4[0]])

sumRow2 = sum(lst2)
sumCol2 = sum([lst1[1], lst2[1], lst3[1] , lst4[1]])

sumRow3 = sum(lst3)
sumCol3 = sum([lst1[2], lst2[2], lst3[2] , lst4[2]])

sumRow4 = sum(lst4)
sumCol4 = sum([lst1[3], lst2[3], lst3[3] , lst4[3]])

if sumRow1 == sumCol1 == sumRow2 == sumCol2 == sumRow3 == sumCol3 == sumRow4 == sumCol4:
    print("magic")
else:
    print("not magic")

'''
# advance (*)
#DRY (don't repeat your self)
container = []
totalInput = []

for i in range(4):
    lst = [int(i) for i in input().split()]
    container.append(sum(lst)) # get all row' s sum
    totalInput.append(lst) # store all input

for i in range(len(totalInput)):
    col = []
    for j in range(len(totalInput)):
        col.append(totalInput[j][i])
    container.append(sum(col))

if len(set(container) ) == 1:
    print('magic')
else:
    print('not magic')
'''
hw:

* PICK 2 OF 3 QUESTIONS UNDER

RE DO CCC 2016 J2:

https://www.cemc.uwaterloo.ca/contests/computing/past_ccc_contests/2016/stage%201/juniorEn.pdf

CCC: 2017 J2

https://www.cemc.uwaterloo.ca/contests/computing/past_ccc_contests/2017/stage%201/juniorEF.pdf

CCC: 2019 J3

https://www.cemc.uwaterloo.ca/contests/computing/past_ccc_contests/2019/stage%201/juniorEF.pdf
'''
                   
