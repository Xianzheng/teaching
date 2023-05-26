# flip
# lst = [1,2,3,4]
'''
1 2
3 4

vertical flip
2 1
4 3

horizontal flip
3 4
1 2
'''

def horFlip(lst):
    lst[0],lst[2] = lst[2],lst[0]
    lst[1],lst[3] = lst[3],lst[1]


def verFlip(lst):
    lst[0], lst[1] = lst[1], lst[0]
    lst[2], lst[3] = lst[3], lst[2]


lst = [1,2,3,4]

instruction = input()
for i in instruction:
    if i == 'V':
        verFlip(lst)
        print(lst)
    if i == 'H':
        horFlip(lst)
        print(lst)
print(lst[0],lst[1])
print(lst[2],lst[3])
#vertical flip
#lst : [2,1,4,3]

'''
#index 0 1 2 3
print(lst[0],lst[1])
print(lst[2],lst[3])
#swap
print('after horizontal flip')
horFlip(lst) # invoke our function
#[3,4,1,2]
print(lst[0],lst[1])
print(lst[2],lst[3])
'''