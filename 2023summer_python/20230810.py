string = '+++===!!!!'

'''
#
pseudocode
current string compare with next string

if there are same:
    ADD COUNT  BY 1

if tere are different:
    print Count number
    print current string
    restore count = 1

if come to last string:
    print Count number
    print current string


'''

a = 1
b = 2

'''
# 记录下a的值

temp = a

#交换 a 和 b的值

a = b

b = temp
print(a,b)
'''

a,b = b,a
print(a,b)

lst = [1,2,3,4]
lst[0],lst[3] = lst[3],lst[0]
print(lst)

'''
finish J3
try J4
'''