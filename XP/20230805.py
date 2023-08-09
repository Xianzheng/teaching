'''
Sample Input 1
ABCCDEABAA
ABCDE

Output for Sample Input 1
yes

Sample Input 2
ABCDDEBCAB
ABA
Output for Sample Input 2
no
'''

#ABCDE
'''
options
EABCD
DEABC
CDEAB
BCDEA
ABCDE
'''

'''
inp = 'ABCDE'
#show all cyclic shift option
lst = ['A','B','C','D','E'] 

#how to convert string to list
print(list(inp))
#how to convert list to a string
# print(''.join(lst))

# print(''+'A'+'B'+'C')
string = ''
for i in lst:
    string += i
print(string)
'''



def cirlicShift(string):
    lst  = list(string)
    popedElement = lst.pop()
    lst.insert(0,popedElement)
    return ''.join(lst)
# how to make a circlic shiftW
line=input()
searchedgroup=input()
string = searchedgroup

# we want to add all circlic option to group
group = []
# don't repeat your self
for _ in range(len(string)):
    string= cirlicShift(string)
    group.append(string)


flag = False
for i in group:
    if i in line:
        flag = True
        break
#output
if flag == True:
    print('yes')
else:
    print('no')

'''
hw:
1.
['apple','banana','cherry','pear']

['pear','apple','banana','cherry']
['cherry','pear','apple','banana']
['banana','cherry','pear','apple',]

2.
string = 'pear'
lst= ['apple','banana','cherry']
# consider how to add pear to index 1
to make lst like
lst= ['apple','pear','banana','cherry']

3.
# string = 1234
#get result of 1234 + 4123 + 3412 +2341

4. do your own verson of CCC 2020 J4
'''