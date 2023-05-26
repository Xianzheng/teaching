# lst = []

# twoDlst = [[1,2,3],[4,5,6],[7,8,9]]
twlst = []

l1 = input() # "16 3 2 13" -> [16,3,2,13]

# numlist = list(map(int,l1.split(' '))) # convert ['16', '3', '2', '13'] - > [16,3,2,13]

lst = l1.split(' ')

print(lst)

for i in range(len(lst)):
    lst[i] = int( lst[i] )

print(lst)

twlst.append(lst)

# do https://cemc.uwaterloo.ca/contests/computing/2016/stage%201/juniorEn.pdf  J2
# try to remember how we can change lst using two method

# we will talk list tomorrow in detail

for eachRow in lst:
    print(eachRow)