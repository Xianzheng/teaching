'''
# revolve string

#abcdef

# fabcde
# efabcd
# defabc
# cdefab
# ...

lst = ['a', 'b', 'c', 'd', 'e', 'f'] # ['f', 'a', 'b', 'c', 'd', 'e']
#index  0    1    2    3    4    5
print(lst)
for i in range(10): # generate a loop, run 10 times
    popedElement = lst.pop()
    lst.insert(0,popedElement)
    print(lst)


# convert string to lst
string = 'hello world'
lst = list(string)
print(lst)


# convert lst to string'
lst = ['h', 'e', 'l', 'l', 'o', ' ', 'w', 'o', 'r', 'l', 'd']

# string = ''.join(lst)
# +=

string = ''
for i in lst:
    string = string + i
    print(string)
'''

# make string move like revolving
#abcdef

# fabcde
# efabcd
# defabc
# cdefab

string = 'abcdef'

#convert string to lst

lst = list(string)
#let lst move
#convert lst to string

for i in range(6):
    p = lst.pop()
    lst.insert(0, p)
    # string = ''.join(lst)
    string = ''
    for j in lst:
        string = string + j
    print(string)

#https://cemc.math.uwaterloo.ca/contests/computing/past_ccc_contests/2020/ccc/juniorEF.pdf
