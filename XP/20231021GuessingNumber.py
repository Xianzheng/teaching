# generate random number


'''
rule:
you need to write code by your own
you can search in google or ask
when finishing code, send me in group chat
time is 5 minutes
'''



import random

# import random
# x=random.randint(1,10000)
# print(x)

def generateRandomNumber():

    x=random.randint(1,9)
    return x 

def getInput():
    '''
    return a value we can input in console
    '''
    x=input()
    return x
    

# write code to compare if our input is same with random number
# r = generateRandomNumber()
# i = getInput()

# if r == i:
#     print('it is same')
# else:
#     print('random number is',r)
#     print('no')

# ord() chr()
def generateRandomChar():
    '''
    generate random char from 'a - z'
    '''
  
    lst = []
    for i in range(97,123):
        lst.append(chr(i))
    
    r = random.randint(0,24)

    return lst[r]
    




def generateRandomBiggerChar():

    lst = [chr(i) for i in range(65,91)]
    r = random.randint(0, 25)
    return lst[r]

rBC = generateRandomBiggerChar()
print(rBC)


# generate 10 digit password
# it contains bigger char and smaller char and number between 1 - 9
s = ''
for i in range(10):
    
    r = random.randint(1,3)
    if r == 1:
        s += generateRandomChar()
    if r == 2:
        s += generateRandomBiggerChar()
    if r == 3:
        s += str(generateRandomNumber())
print(s)
