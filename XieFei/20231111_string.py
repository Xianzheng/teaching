string1 = 'hello wrold'
#index     012345678910
'''
string1 = 'hello world'
string2 = "hello world"

print(string1,type(string1))
print(string2,type(string2))


string1 = 'hello wrold'

#index     012345678920

# index starts from 0
print(string1[4])
print(string1[5])

length = len(string1)
for i in range(length):
    print(string1[i])

length = len(string1)
for i in range(length):
    if i % 2 == 0:
        print(string1[i])

length = len(string1)
for i in range(0,length,2):
    print(string1[i])


# any input() is a string , no matter what you input1

# inp = input()

# print(inp, type(inp))

# use string times number

for i in range(1,6):
    print('* ' * i)
'''

# ccc 2018 j2

num = int(input())
today = input()
yesterday = input()

count = 0

for i in range(num):
    # print(i)
    if today[i] == yesterday[i] == 'C':

        count += 1

print(count)

# HW

# email ='mark.ffang@gmail.com'

# print each character of thid string

# print every odd index character

# print every even index character

#print useful information from this eamil, example,mark, fang, gamil

# try to do CCC 2017 J2 

#https://www.cemc.uwaterloo.ca/contests/computing/past_ccc_contests/2018/stage%201/juniorEF.pdf
