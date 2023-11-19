'''
# prev homework
inp1 = int(input())
 # any pure input() is a string, if we want use integer, we can do
 # int(input())
inp2 = int(input())

if inp1 > 0  and inp2 > 0:
    print(1)

if inp1 < 0  and inp2 > 0:
    print(2)

if inp1 < 0  and inp2 < 0:
    print(3)

if inp1 > 0  and inp2 < 0:
    print(4)


# print('Hello world')

# print(123465)

a = "123465" # str type

b = 123465 # int type

print(type(a))

print(type(b))

# any thing was around by signle or double quote is string

string1 = 'hello world'
string2 = "hello world"

print(string1 == string2)

# feature of string
# any string has index under it

text = 'hello world'
#index  012345678910 
print('type of text is',type(text))

print(text[0])
print(text[4])
print(text[9])

# practice using index to print l l and r of text
print(text[2])
print(text[3])
print(text[8])
'''
text = 'hello world'
#index  012345678910 
i = 0

while i <= 10:

    print(text[i])

    i += 1

#Problem J2: Occupy parking
#https://www.cemc.uwaterloo.ca/contests/computing/past_ccc_contests/2018/stage%201/juniorEF.pdf
'''
hw:
thinking how to do Problem J2: Occupy parking

requirement, have a thinking

next:
we will continue string lecture
'''
num = int(input())

str1 = input()

str2 = input()