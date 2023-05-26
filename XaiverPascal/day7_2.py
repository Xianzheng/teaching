#count
'''
#point1

string = "merkfang"

num = string.count('q')

#ask if e exists in this string

if string.count('e') > 0:
    print('this character exists in this string')
else:
    print('this character does not exists in this string')

#point2

# count can find more than one character

string = ':):#:#:(:):#'

# num = string.count(':)')
#
# print(num)

num = string.count(':)')

#point3

#slicing
string = 'mark.ffang@gmail.com'
#index    012345678911234567892

print(string[6:10])
print(string[11:16])
print(string[0:4])
# if start point is header, we don't need to clarify
print(string[:4])
print(string[17:20])
# of end point is tail, we don't need to to clarify
print(string[17:])

#solidify

string = 'markpascalxavier'

# we want to know how many 'a' in this string

print(string.count('a'))

cnt = 0

#len(string) can find the length of string
for index in range(len(string)):

    if string[index] == 'a':

        cnt += 1

print(cnt)

# find if pascal in this string

flag = False

for i in range(len(string) - 5):

    slice = string[i:i+6]

    if slice == 'pascal':

        flag = True

if flag == True:
    print('yes')
else:
    print('no')

'''
#homework

string = 'today is a good day'

# use slice of string to print 'today', 'good', 'day'

# use count to find how many 'o' in string

# do not use count to find how many 'o' in string

# use count to if good in string

# do not use count to if good in string

# J2 of https://cemc.math.uwaterloo.ca/contests/computing/past_ccc_contests/2015/stage%201/juniorEn.pdf


