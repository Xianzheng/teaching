string = '16 3 2 13'

lst = list(map(int,string.split()))

table = [[16,3,2,13],[5,10,11,8],[9,6,7,12],[4,15,14,1]]

# first row table[0][0] +  table[1][0] + table[2][0] + table[3][0]
# for row in range(len(table)):
#     colsum = 0
#     for col in range(len(table)):
#         colsum += table[col][row]
#     print(colsum)

for i in range(4):
    for j in range(4):
        print('i is',i,'j is',j)