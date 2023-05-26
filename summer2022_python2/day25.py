'''
# 1 + 2 + 3 + ... + 10?

n = 0
lst = []
for i in range(1,11):
    n += i
    lst.append(n)
print(n)
print(lst)

#[3,10,12,5] =>  [0,3,13,25,30]
[0,3,13,25,30]


#[3,10,12,5] =>  [0,3,13,25,30]
string = input()

lst = string.split()
for i in range(len(lst)): # i will be each index of lst
    lst[i] = int(lst[i]) # if we want to update list we must use index to update
#print(lst)

newlst = [0]
s = 0
for i in lst:
    s += i
    newlst.append(s)
#print(newlst)



for i in newlst:
    for j in newlst:
        print(abs(j - i), end = ' ')
    print()
'''

# {} , [], set()

lst = [5,3,2,6,1] # sorted(lst)

print(sorted(lst)) # how to sort

# algorithm bubble sort ?

lst = [4,5]

# lst[0],lst[1] = lst[1],lst[0] # python swapping way
# print(lst)
'''
# traditional way
tmp = lst[1]

lst[1] = lst[0]

lst[0] = tmp

print(lst)
'''