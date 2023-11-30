'''
dis = 1

s = list(map(int,input().split(':')))

t = s[0] + s[1]/60

while dis > 0:

    if 7 <= t < 10 or 15 <= t < 19:
        speed = 0.25
    else:
        speed = 0.5

    dis -= speed * 1

    t += 1

    if dis < 0:
        t -= abs(dis)/speed

    if t > 24:
        t -= 24

hr = int(t)
min = t - hr

if hr < 10:
    strhr = str(0) + str(hr)
else:
    strhr = str(hr)

if min*60 < 10:
    strmin = str(0) + str(int(min))
else:
    strmin = str(int(round(min*60,0)))

print(strhr+':'+strmin)


by = -1
bx = -1
sy = 101
sx = 101

for o in range(int(input())):
    i = list(map(int,input().split(',')))
    if i[0] > bx:
        bx = i[0]
    if i[0] < sx:
        sx = i[0]
    if i[1] > by:
        by = i[1]
    if i[1] < sy:
        sy = i[1]
print(str(sx-1)+','+str(sy-1))
print(str(bx+1)+','+str(by+1))

lst = [44,34,24,64]
print(min(lst))
print(max(lst))


def rotate(string):
    lst = [i for i in string]
    lst.append(lst[0])
    lst.pop(0)
    return ''.join(lst)

loop = []
all = input()
for i in range(len(all)):
    for j in range(i+1,len(all)+1):
        loop.append(all[i:j])
        
shift = input()

shiftlist = []
for i in range(len(shift)):
    shiftlist.append(shift)
    shift = rotate(shift)
inside = False
for i in shiftlist:
    for j in loop:
        if i == j:
            inside = True
print('yes' if inside else 'no')


# string in another

string1 = 'ABCDE'
string2 = 'CDE'

print(string2 in string1)

string = 'ABCDE'
for i in range(len(string)):
    lst = list(string)
    lst.insert(0,lst.pop())
    rotateString = ''.join(lst)
    string = rotateString
    print(rotateString)



# find , find key word: in 

# string = > list

string = 'ABC'
lst = list(string)

# list => string
print(lst)
string1 = ''.join(lst)
print(string1)

'''
#J1, j2, simple data structure knewledge, know loop

#J3, J4, COMPLICATE simple data structure knewledge, LOOP, LOGIC

#j5, argorithm: a process or set of rules to be followed in calculations or other problem-solving operations, especially by a computer.
#    make own dat structure
#    recursive
#    COMPLICATE simple data structure knewledge, LOOP, LOGIC

'''
1. AA → AB
2. AB → BB
3. B → AA

Start: AB

end: AAAB
'''

#AB => [BB,AAA]

# BB => [AAB, BAA]

# AAA => [ABA,AAB]

# write a function

dic = {
    'AA' : 'AB',
    'AB' :'BB',
    'B' :'AA'
}

def allPossibleSlice(string):
    all = []
    for i in range(len(string)):
        for j in range(i+1,len(string)+1):
            all.append([string[i:j],(i,j)])
    return all


# print(allPossibleSlice('AB')) # [['A',(0,1)],['B',(1,2)],['AB',(0:2)]]

def parse(string):
    lst = allPossibleSlice(string)
    possibleChange = []
    for item in lst:
        if change(string,item) != None:
            possibleChange.append(change(string,item))
    return possibleChange

def change(string,lst):
    '''
    receive all possible slice and it position 

    return changd string
    '''
    if lst[0] in dic:
        lstring = list(string)
        lstring[lst[1][0]:lst[1][1]] = dic[lst[0]]
        return ''.join(lstring)
    else: return None
        


# print(parse('BB')) # [BB,AAA]

class Node:

    def __init__(self,value):
        self.value = value
        self.next = []

root = Node('AB')
for i in parse('AB'):
    root.next.append(Node(i))

    
# NEXT WE WILL discuss GENERAL TREE\

'''
1.try to build a general tree, explore

2.make rule by your self, do parse again like in class

3. check J5 of 2018
    https://www.cemc.uwaterloo.ca/contests/computing/past_ccc_contests/2018/stage%201/juniorEF.pdf

   check J5 of 2020
   https://www.cemc.uwaterloo.ca/contests/computing/past_ccc_contests/2020/ccc/juniorEF.pdf


GENERAL TREE
RECURSIVE TO LOOP
'''

'''
dic = {key1:value1,key2:value2,key3:value3}

#create empty dictionary
dic = {}
# add key-value pair to dictionary
dic['a'] = 'apple'
dic['b'] = 'banana'
dic['c'] = 'cherry'

print(dic)
print(dic['a'])

print(dic['c'])

# feature of dictionary, dictionary is fast,is build by hashmap

# for i in dic:
#     print(i)

# for i in dic.items():
#     print(i)

print('a' in dic)
'''