# grammer suger
'''
lst = []

for i in range(1 ,11):
    lst.append(i)

print(lst)


print([i for i in range(1,11) if i % 2 == 0])

#build in function
# map()

string = '8 9 10'

print(string.split())

string = '12345'
string[0] ='f'
print(string)



def compress(string):
    count = 1

    for index in range(len(string) - 1):
        
        p1 = string[index]
        p2 = string[index + 1]
        
        if p1 == p2:

            count += 1

        if p1 != p2:
            
            print(count, p1, end = ' ')

            count = 1
        
        if index == len(string) - 2:

            print(count, p1)

            count = 1


num = int(input())
inputLst = [input() for i in range(num)]
print(inputLst)
for string in inputLst:
    compress(string)


a = 5

b = 8

# tranditionaly way,
# record = a
# a = b
# b = record

a,b = b,a

lst = ['a','b','c','d']
#        0   1   2   3

lst[0],lst[2] = lst[2],lst[0]

print(lst)
'''

'''
hw:
 1. redo CCC 2019 j3( DON'T SEE CLASS CODE AND DO IT AGAIN)

 2. Do CCC 2019 j4

 (LINK FOR CCC2019: https://www.cemc.uwaterloo.ca/contests/computing/past_ccc_contests/2019/stage%201/juniorEF.pdf)

 3. look questions of CCC 2018 see what you can do

 Link for CCC2018 https://www.cemc.uwaterloo.ca/contests/computing/past_ccc_contests/2018/stage%201/juniorEF.pdf
'''
