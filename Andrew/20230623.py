# r0 = [1,2,3,4]
# r1 = [5,6,7,8]
# r2 = [9,10,11,12]
# r3 = [13,14,15,16]

# c0 = r0[0] + r1[0] + r2[0] +r3[0]


# if sum of r0,r1,r2,r3 and c0,c1,c2,c3 are equals this is magic sequar, else not 

# r0 = input() 
# r1 = input()
# r2 = input()
# r3 = input()

# r0 is a string('1 2 3 4'), we need to convert string to list ['1','2','3','4'] then we need to purify the list [1,2,3,4,] 

# the i does not matter
# for _ in range(1):
#     raw = input()
#     stringList = raw.split()# convert string to stringList
#     numberList = list(map(int,stringList)) # convert stringList to numberList
#     print(sum(numberList))# the problem is when


# row1 = list(map(int,input(' ').split()))
# row2 = list(map(int,input(' ').split()))
# row3 = list(map(int,input(' ').split()))
# row4 = list(map(int,input(' ').split()))
for i in range(1,5):

    globals()['row'+str(i)] = list(map(int,input(' ').split()))

sumCol = lambda x: row1[x] + row2[x] + row3[x] + row4[x]

if sum(row1) == sum(row2) == sum(row3) == sum(row4) == sumCol1 == sumCol2 == sumCol3 == sumCol4:
    print('magic')
else:
    print('not magic') 
# col2 = sumCol(1)

# print(col1)

'''

hw:
1.
# redo ccc 2016 J2 question(don't see demo, code by your self)
#https://www.cemc.uwaterloo.ca/contests/computing/past_ccc_contests/2016/stage%201/juniorEn.pdf

2. 
read ccc 2017 J3 question
input and convert input to useful information
https://www.cemc.uwaterloo.ca/contests/computing/past_ccc_contests/2017/stage%201/juniorEF.pdf

input:
3 4
3 3

Output
[3,4]
[3,3]

3.
read ccc 20176 J3 question
input and convert input to useful information
https://www.cemc.uwaterloo.ca/contests/computing/past_ccc_contests/2018/stage%201/juniorEF.pdf

input
3 10 12 5

output:
[0, 3, 13,25, 30]
'''