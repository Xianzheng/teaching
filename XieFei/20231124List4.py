''''
str = 'bcdef'
lst = list(str)
print(''.join(lst))


poped = lst.pop(0)
lst.insert(1, poped)
print(''.join(lst))

poped = lst.pop(1)
lst.insert(2, poped)
print(''.join(lst))

poped = lst.pop(2)
lst.insert(3, poped)
print(''.join(lst))

poped = lst.pop(3)
lst.insert(4, poped)
print(''.join(lst))


string1 = 'ABCDEF'

string2 = 'CD'

print(string2 in string1)


# DO INPUT()

first = input()
second = input()

# make all possible cyclic shifts, depends on second string

for i in range(len(second)):
    #make string to list
    lst = list(second)

    #make chage to list, pop last element and then insert to first
    poped = lst.pop()
    lst.insert(0,poped)

    #make changed list to string
    second = ''.join(lst)

    print(second)

'''

# hw
# make one input, to get all possible cyclic shift

