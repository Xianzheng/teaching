'''
inp1 = input()
inp2 = input()
inp3 = input()
inp4 = input()

str1 = inp1
lst1 = str1.split()
for i in range(len(lst1)):
    lst1[i] = int(lst1[i])


str2 = inp2
lst2 = str2.split()
for i in range(len(lst2)):
    lst2[i] = int(lst2[i])

str3 = inp3
lst3 = str3.split()
for i in range(len(lst3)):
    lst3[i] = int(lst3[i])


str4 = inp4
lst4 = str4.split()
for i in range(len(lst4)):
    lst4[i] = int(lst4[i])

def getsum(lst):
    sum = 0
    for item in lst:
        sum += item
    return sum


row1 = getsum(lst1) # lst1 = [16,3,2,13]
row2 = getsum(lst2) # lst2 = [10,4,2,3]
row3 = getsum(lst3)
row4 = getsum(lst4)
if row1 == row2 == row3 == row4:
    print('magic square')
else:
    print('not magic square')
'''

inp1 = input()
inp2 = input()
inp3 = input()
inp4 = input()

def convertEachElementToIntegeger(lst):
    for i in range(len(lst)):
        lst[i] = int(lst[i])
    return lst

def getsum(lst):
    sum = 0
    for item in lst:
        sum += item
    return sum

str1 = inp1
lst1 = convertEachElementToIntegeger(str1.split())

str2 = inp2
lst2 = convertEachElementToIntegeger(str2.split())

str3 = inp3
lst3 = convertEachElementToIntegeger(str3.split())


str4 = inp4
lst4 = convertEachElementToIntegeger(str4.split())


row1 = getsum(lst1) # lst1 = [16,3,2,13]
row2 = getsum(lst2) # lst2 = [10,4,2,3]
row3 = getsum(lst3)
row4 = getsum(lst4)

# col1 = lst1[0] + lst2[0] + lst3[0] + lst4[0]
# col2 = lst1[1] + lst2[1] + lst3[1] + lst4[1]
# col3 = lst1[2] + lst2[2] + lst3[2] + lst4[2]
# col4 = lst1[3] + lst2[3] + lst3[3] + lst4[3]


if row1 == row2 == row3 == row4:
    print('magic square')
else:
    print('not magic square')


'''
hw:

J1， j2(do it by your own code, you can refer the note)

link: 
https://www.cemc.uwaterloo.ca/contests/computing/past_ccc_contests/2016/stage%201/juniorEn.pdf
'''
