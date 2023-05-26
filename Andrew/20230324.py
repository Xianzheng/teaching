'''
lst = [3,6,9,4]
print(max(lst))

dic = {
    'apple' : 5,
    'banana': 6,
    'cherry' : 12,
    'pear': 1
}

print(dic.items())
print(dic.keys())
print(dic.values())

keylst = list(dic.keys())# convert dictionary list to normal list
print(keylst)
valuelst = list(dic.values())
print(valuelst)

maxValue = max(valuelst)
print(maxValue)
maxIndex = valuelst.index(maxValue)
print(maxIndex)
print(keylst[maxIndex])



participants = {}
i = 0
bids = int(input())

while i < bids:
    i += 1
    person = str((input()))
    bid = int((input()))

    participants[person] = bid

print()
# print(participants)
kl = list(participants.keys())
vl = list(participants.values())
m = max(vl)
mIndex = vl.index(m)
# print(mIndex)
print(kl[mIndex])


# make sure we can store input into a dictionary
# we want to find the biggest value's index
# we want to find the key relative to biggest value
'''

'''
def functionName():
    statement
'''
# make a function
# def sayHi(arg,arg2):
#     print('Hi '+(arg * arg2))
#
# #call function/ invoke function
#
# sayHi('Andrew ',2)
# sayHi('Selina ',2)
# sayHi('Kevin ',2)

def add(arg1,arg2):
    return arg1 + arg2

print(add(1,2))


print(add(3,7))

'''

homework:

1 dic = {
    'apple' : 5,
    'banana': 6,
    'cherry' : 12,
    'pear': 1
}

find the key relative to biggest value

# 1. function have return/ does not have return/ have arg, not have arg, make a try -> send me the code

# 2. make a times function , time(3,7) -> 32, make a divide function divide(12,3) -> 4.0

'''

