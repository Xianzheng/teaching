# CCC 2017 J3
'''
x1, y1 = map(int, input().split())
x2, y2 = map(int, input().split())
t = int(input())
distance = (x1 - x2) + (y1 - y2)
if distance <= t and (t - distance) % 2 == 0:
    print('Y')
else:
    print('N')

P = int(input())
N = int(input())
R = int(input())

infect = N
infectT = N
days = 0

while True:
    if infectT > P:
        print(days)
        break

    infect = infect * R
    infectT += infect
    days += 1


# abswer will be 
# min value of left column - 1,  min value of right column - 1
# max value of left column + 1,  max value of right column + 1, 

lc = []
rc = []

num = int(input())

for i in range(num):
    inpLst = input().split(',')
    lc.append(int(inpLst[0]))
    rc.append(int(inpLst[1]))

xmin = min(lc)
ymin = min(rc)
xmax = max(lc)
ymax = max(rc)

print(str(xmin - 1) + ',' + str(ymin - 1))
print(str(xmax + 1) + ',' + str(ymax + 1))


'''
n = 'ABCCDEABAA'
# in
string1 = 'ABCDE'
 # key word in can help check if certain character in string
print('C' in string1)

print('BCD' in string1)

print('B D' in string1)

# if we want string1 rotate

# make string1 to list fist

lst1 = list(string1)

pC = lst1.pop()
# print(pC)
# print(lst1)
lst1.insert(0,pC)
# how to convert list to string
string = ''.join(lst1)
print(string)

'''
hw: do 2020 J4, 
https://www.cemc.uwaterloo.ca/contests/computing/past_ccc_contests/2020/ccc/juniorEF.pdf
'''
