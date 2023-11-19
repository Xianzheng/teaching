'''
#input
num = int(input())

yesterday = input()

today = input()

#analyze
# yesterday and today are string

# print(yesterday[0])
# print(today[0])

# print(yesterday[1])
# print(today[1])

# print(yesterday[2])
# print(today[2])

# print(yesterday[3])
# print(today[3])

# print(yesterday[4])
# print(today[4])
count = 0
for i in range(num):
    # print(yesterday[i])
    # print(today[i])
    if yesterday[i] == today[i] == 'C':
        count += 1

#output

print(count)

# split for string

string = '9 +'
#index    012
print(int(string[0]) * string[2])

string = '3 -'
#index    012
print(int(string[0]) * string[2])

# slice for string
string = '12 A'
#index    012
print(int(string[0]+string[1]) * string[3])


#  string can do concatation
str1 = '1'
str2 = '2'
print(str1+str2)

# string = '12 A'
# #index    012
# print(int(string[0]+string[1]) * string[3])
string = '9 +'
lst = string.split(' ')
print(lst)


string = '%A&'
lst = string.split('A')
print(lst)

string = '10 9 8 7'
print(string.split(' '))
'''

# slice

email = 'mark.ffang@gamil.com'
#index   01234
# get useful information for this email

name = email[0] + email[1] + email[2] + email[3]

name = ''
for i in range(4):
    name += email[i]
# info = email [startIndex: stopbyIndex: step]
info = email[:4:1]
# for slicing , if we start with index 0, we can ignore it

info = email[3::1]
# for slicing , if we end with string, we can ignore it

info = email[0:len(email): 2]
print(info)

'''
1.
hw:

https://www.cemc.uwaterloo.ca/contests/computing/past_ccc_contests/2019/stage%201/juniorEF.pdf

2.
use slicing to do this question:

# email ='mark.ffang@gmail.com'

# print each character of thid string

# print every odd index character

# print every even index character

#print useful information from this eamil, example,mark, fang, gamil
'''