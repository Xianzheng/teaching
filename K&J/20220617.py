# we already talk about how this table will rotate
# newlst[x][y] <- oldlst[len(lst) - 1][x]
"""
3
4 3 1
6 5 2
9 7 3

"""
lst = [[1,3],[2,4]]# 2 2columns
lst1 = [[4,3,1],[6,5,2],[9,7,3]]

def display(lst):
    for i in lst:
        for j in i:
            print(j, end=' ')
        print()

# display(lst)

def rotate(lst):
    length = len(lst)
    # list comprehension(new )
    newtable = [[0 for i in range(length)] for i in range(length)]

    for i in range(length):
        for j in range(length):
            newtable[i][j] = lst[length - 1 - j][i]
    return newtable

print()
# newtable = rotate(lst)
# display(newtable)

display(lst)
print()
display(lst1)

# rotate
# when we need to do rotate

def check(lst):
    """
    if table is following rules we return True else return False
    """

lst2 = [3,5,7]
print(sorted(lst1))
for eachRow in lst1:
    print(sorted(eachRow))
if lst2 == sorted(lst2):
    print(True)
else:
    print(False)

"""
homework: fix your code(may be you can find problem)

finish the check function
"""

