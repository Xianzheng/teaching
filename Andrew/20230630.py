#3 10 12 5
#[0,3,13,25,30]

'''
'5 9'
['5','9']

# int() convert string to number, it works only string exactly lools like number
inp = '5 9'.split()
print(inp)

number = ''
for i in inp:
    number += i

print(number)

inp = '3 10 12 5'
inplist = inp.split()
print(inplist)

result = [0]
sum = 0
for i in inplist:
    sum += int(i)
    result.append(sum)

print(result)


demolst = [1,2,3,4,5,6,7,8]
#lst       0 1 2 3 4 5 6 7

#two way to loop the list

#one way use index to loop

for index in range(len(demolst)):
   #len(demolst) is let python knows how many elements have demost 
   # for this case, len(demolst) is 8
   print(demolst[index])

# this is anther way
for element in demolst:
    print(element)

lst = ['1','2','3','4','5']

# convert each element in lst to integer
print('before update')
print(lst)
# error code
#one way
# if we want to use index to update list, we want use index to update lst
for index in range(len(lst)):
    lst[index] = int(lst[index])
# newlst = []

# for i in lst:
#     newlst.append(int(i))
# print(newlst)

# convert each element in lst to integer
print(list(map(int,lst))) 

print(list(filter(lambda x: int(x),lst)))
'''
import time
lst = []

for i in range(100000):
    lst.append(str(i))

startTime = time.perf_counter()

# for index in range(len(lst)):
#     lst[index] = int(lst[index]) # 0.027832600000000006 seconds need

# list(map(int,lst)) # 0.013982399999999999 seconds need

list(filter(lambda x: int(x),lst)) # 0.022561800000000007 secondes I need to run code 

endTime = time.perf_counter()
print(endTime - startTime,'secondes I need to run code ')


'''

show me you understand today' content
input:
3 5 7 8 9 10

get the cumlative result [8,17 ....]

try to do 2018 J3

try to do 2017 J3

try to do 2017 J2
'''


