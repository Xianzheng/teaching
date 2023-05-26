"""
'''
    *
   **
  ***
 ****
*****
'''

rows = 5
k = 2 * rows -2
for i in range(0,rows):
    for j in range(0,k):
        print(end='')
    k = k -2
    for j in range(0,i+1):
        print("*",end="")
    print()

'''
   *
  ***
 *****
*******
'''
# numbers, string(read only), list(CRUD), dictionary(CRUD), set(CRUD), tuples(read only)

#Set

lst = [1,2,3,3,4,5,6,5,7,8,9] # we don't want duplicated element

# newlst = []
# for i in lst:
#     #filter
#     if i not in newlst:
#         newlst.append(i)

# print(newlst)
print(list(set(lst)))


# set is a sequence, it is CRUD(create, ready, update, delete) datastract, 

# elements store in our set is not in order
# all elements in set is unique

# create
s = {0,}
# create empty set, using keyword of set
s1 = set()
print(type(s))
print(type(s1))

s1.add('apple')
s1.add('banana')
s1.add('cherry')
print(s1)
print(s1)

# set does not have index, we can not use index to access the data

s1.add('apple')# apple does not enter it
s1.add('pear')# pear enter itprint()

# delete or update
s1.remove('apple')
print(s1)
"""
# judge wether string has duplicated value

#original string
#set can remove duplicated element

#if string contain duplicated value, we remove duplicated valu

#1
# we need to write funtion 
def isDuplicate(string):
    pass
    

print(isDuplicate('abcc')) # it willprint True, since this string has duplicated value
print(isDuplicate('abc')) # it willprint False, since this string does not duplicated value


"""
# 2
given
sample_set = {"Yellow", "Green", "Black"}
sample_list = ["Blue", "Green", "Red"]

output
{'Green', 'Yellow', 'Black', 'Red', 'Blue'}

# 3
set1 = {10, 20, 30, 40, 50}
set2 = {30, 40, 50, 60, 70}

Output
{70, 40, 10, 50, 20, 60, 30}

# 4
Add set add 5 more your favirate fruits, Remove Two fruit,show your code
"""

