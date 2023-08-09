'''
# some feature of set
# 1. all element in set is unqiue
 
s = set()
s.add('a')
s.add('b')
s.add('c')

s.add('b')

print(s)

#2. set is unorder
print(s)
#3. set does not have index
# print(s[0])
#CRD
# hash value
s = {i for i in range(10)}
for i in s:
    print(i)


# convert string
# string <=> int
# input is a atring
# convert string to integer
# num = int(input())

# string <=> list
# string convert to lst
string = "Hello EveryOne"
lst = list(string)
print(lst)

# list convert to string
lst = ['H', 'e', 'l', 'l', 'o', ' ', 'E', 'v', 'e', 'r', 'y', 'O', 'n', 'e']
str1 = ''.join(lst)
print(str1)

# when list convert to string , requires all element in lst must be a string
lst = [ '1','2','3']
str2 = ''.join(lst)
print(str2)
'''
#str convert to set
string1 = 'abc'
s1 = set(string1)
print(s1)

#str2 convert to set2
string2 = 'hello'
s2 = set(string2)
print(s2)

# do set convert, it will automatically delete repreated value
# judge whether this string has repeated value
string = 'abcdefgc'
#index    01234567

for i in range(len(string)):
    for j in string[i+1:]:
        if string[i] == j:
            print('it has repeated value')

if len(string) != len(set(string)):
    print('it has repeated value')


'''
hw
try to do demo code include:

string <=> int
string <=> lst
string <=> set
judge whether string has repeated value

'''

