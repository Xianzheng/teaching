'''
# a = int(input())
# b = int(input())
# c = int(input())
# d = int(input())

# print(a == 9 or a == 8)

# compare sign
# >, < , >=, <=, ==, !=

# value giving
# = 

a = 10

# print( a > 7)
# print( a > 9)

# logic sign
# or, and, not

print( a > 7 or a > 9)
print( a > 7 and a > 9)
print( not a > 11)
'''

a = int(input())
b = int(input())
c = int(input())
d = int(input())

# the first of these four digits is an 8 or 9;

cond1 = a == 8 or a == 9

# the last digit is an 8 or 9;
cond2 = d == 8 or d == 9

# the second and third digits are the same.
# (practice: make sentence to code)
cond3 = b == c

if cond1 == True and cond2 == True and cond3 == True:
    print('ignore')
else:
    print('answer')


'''
# do CCC 2018 J1 by your own:

# https://www.cemc.uwaterloo.ca/contests/computing/past_ccc_contests/2018/stage%201/juniorEF.pdf

# try to do 2017 J1:

# https://www.cemc.uwaterloo.ca/contests/computing/past_ccc_contests/2017/stage%201/juniorEF.pdf
'''