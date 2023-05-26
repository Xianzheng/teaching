#https://cemc.math.uwaterloo.ca/contests/computing/past_ccc_contests/2018/stage%201/juniorEF.pdf

'''
input
3 10 12 5

output
0 3 13 25 30
3 0 10 22 27
13 10 0 12 17
25 22 12 0 5
30 27 17 5 0
'''

inp = input()# one input is one string

# print(inp,type(inp))

# print(inp.split(),type(inp.split()))#.split use space to split and put effective character to list

lst = inp.split() # convert string to list

numlst = list(map(int,lst)) # convert all element in lst to int type

print(numlst) 
# question , how to use [3, 10, 12, 5] to make [0,3,13,25,30]
s = 0
traverlst = [0]

for i in numlst:
    s += i
    traverlst.append(s)

print(traverlst)