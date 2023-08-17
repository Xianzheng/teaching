'''
x = int(input())
a = []
for i in range(0, x):
    t = input()
    a.append(t)
for i in range(0, x):
    n = a[i]
    d = ""
    #
    p = 0
    for i in range(0, len(n)):
        if i != len(n) - 1 and n[i] == n[i + 1]:
            p = p + 1
        else:
            d = d + "" + str(p + 1) + "" + n[i]
            print(p+1,end=" ")
            print(n[i],end=" ")
            p = 0
    print()
            
    # print(d[1 : len(d)])


line = input()

grid = [[1, 2], [3, 4]]


def horizontal(grid):
    grid[0], grid[1] = grid[1], grid[0]


def vertical(grid):
    temp = [grid[0][1], grid[0][0]]
    temp1 = [grid[1][1], grid[1][0]]
    grid[1] = temp1
    grid[0] = temp


for i in range(len(line)):
    if line[i] == "H":
        horizontal(grid)
    else:
        vertical(grid)

for i in grid:
    for k in i:
        print(k, end=" ")
    print(" ")

'''

string = '1 24 3 41' # ['1','24','3','41'] # [1,24,3,41]

'''
lst = string.split()

#method
#update
#using index to updpate
for i in range(len(lst)):
    lst[i] = int(lst[i])

print(lst)


lst = list(map(int,string.split()))
print(lst)
print(sum(lst))

'''
#thinking
lst = [[1,2],[3,4]] # rotate to [[1,3],[2,4]]

# try to do 2016 J2
