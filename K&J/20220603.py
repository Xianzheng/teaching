'''
inp = 'banana'
lst = []
for i in inp:
    lst.append(i)

# print(lst)

lstreversed = list(reversed(lst))
# print(lstreversed)
templst = []
dellst = []

for i in range(len(inp)):
    # print(i)
    if lst[0] != lstreversed[0]:
        lst.pop(0)
        lst.append('1')
        break

for i in range(len(lst)):

    if lst[i] == lstreversed[i]:
        templst.append(lst[i])
    else:
        lst.pop(i)
        lst.append('2')

count = 0

for i in range(len(templst)):
    count += 1
'''

#Palindrome

# ana

# banana

# b, ba ban, bana, banan, banana [0:1],[0:2],[0:3]....
# a, an, ana, anan, anana - [1:2],[1:3],[1:4]...
# n, na, nan, nana  [2:3],[2:4],[2:5]
# a, an, ana,
# n, na
# a


# abracadabra

# buuld a nested loop, slicing, toi find all the possibility for palindrome of banana

string = 'banana' # string[1:4] # [0:1] # [0:2]
# index=  012345

# range(number)
# range(start, end)
# range(start, end , steps)

def ifpal(string):#if string is palindrome return true else return false
    templst=[]
    reverselst=[]
    for i in string:
        templst.append(i)

    reverselst=list(reversed(templst))
    if templst==reverselst:
        return True
    else:
        return False


print(ifpal('banana'))# False
print(ifpal('anana'))# True

for i in range(len(string)): # i = 0 , j 12345 , i = 1, j = 2345, i = 3, j = 45
    for j in range(i + 1, len(string)):
        if ifpal(string[i:j+1]) == True:
            print(string[i:j+1])


