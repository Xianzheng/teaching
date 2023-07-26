'''
#single list
lst = [] # create a list

lst.append('apple')
lst.append(1)

for i in lst:
    print(i)


#two dimontional list

twoDlist = [[1,2,3],[4,5,6],[7,8,9]]

#index          0     1       2
row1 = twoDlist[0]

row2 = twoDlist[1]

row3 = twoDlist[2]

# print(*row1)
# print(*row2)
# print(*row3)

column2 = [row1[1],row2[1],row3[1]]
print(column2)

row1 = '16 3 2 13'
row2 = '5 10 11 8'
row3 = '9 6 7 12'
row4 = '4 15 14 1'

row1 = row1.split()
row2 = row2.split()
row3 = row3.split()
row4 = row4.split()


print(row1)
#basic method
# how to do update for list
# for index in range(len(row1)):
#     row1[index] = int(row1[index])

# print(row1)

# advanced method(python build in method) * remember -> understanding
row1 = list(map(int,row1))
row2 = list(map(int,row2))
row3 = list(map(int,row3))
row4 = list(map(int,row4))

twoD = [row1,row2,row3,row4]

print(twoD)

'''

num=int(input())
table = []
for i in range(num):
    row = input().split()
    #advanced method
    # row = list(map(int,row))
    #baic method
    for index in range(len(row)):
        row[index] = int(row[index])
    table.append(row)

print(table[2][0])

'''
[[4,3,1],[6,5,2],[9,7,3]]
[[9,6,4],[7,5,3],[3,2,1]]
'''