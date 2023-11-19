"""
hr10 = 1
hr01 = 2
mn10 = 0
mn01 = 0
for i in range(int(input())+1):
    print(str(hr10)+str(hr01)+str(mn10)+str(mn01))
    mn01 += 1
    if mn01 == 10:354
        mn10 += 1
        mn01 = 0
        if mn10 == 6:
            hr01 += 1
            mn10 = 0
            if hr01 == 10:
                hr10 += 1
                hr01 = 0
            if hr01 == 3 and hr10 == 1:
                hr01 = 1
                hr10 = 0

hr = 12
min = 0
runtime = int(input())
count = 0

for i in range(runtime):

    min += 1
    if min >= 60:
        min -= 60
        hr += 1

    if min < 10:
        showmin = '0' + str(min)
    else:
        showmin = str(min)  

    if hr >= 13:
        hr -= 12    

    showhr = str(hr)

    totalTime = showhr + showmin
    if len(totalTime) == 4:
        if int(totalTime[3]) - int(totalTime[2]) == int(totalTime[2]) - int(totalTime[1]) and int(totalTime[2]) - int(totalTime[1]) == int(totalTime[1]) - int(totalTime[0]):
            count += 1
    if len(totalTime) == 3:
        if int(totalTime[2]) - int(totalTime[1]) == int(totalTime[1]) - int(totalTime[0]):
            count += 1 

print(count)


hr10 = 1
hr01 = 2
mn10 = 0
mn01 = 0
count = 0
for i in range(int(input())+1):
    mn01 += 1
    if mn01 == 10:
        mn10 += 1
        mn01 = 0
        if mn10 == 6:
            hr01 += 1
            mn10 = 0
            if hr01 == 10:
                hr10 = 1
                hr01 = 0
            if hr01 == 3 and hr10 == 1:
                hr01 = 1
                hr10 = 0
    if hr01-mn10==mn10-mn01:
        if hr10 == 1 and hr10-hr01 == hr01-mn10:
            count += 1
        if hr10 == 0:
            count += 1
print(count)


def ifPal(string:str) -> bool:
    '''
    if string is palindrome return True, else return False
    '''
    original = []
    pal = []
    for i in string:
        original.append(i)
        pal.insert(0,i)
    if original == pal:
        return True
    else:
        return False
    

print(ifPal('ban'))# False
print(ifPal('anana')) #True


string = 'banana'
print(string[1:])

print(string[: len(string) - 1])

print(string[: : -1])


def ifPal(string:str) -> bool:
    '''
    if string is palindrome return True, else return False
    '''
    return string == string[::-1]
    

print(ifPal('ban'))# False
print(ifPal('anana')) #True
"""

def ifPal(string:str) -> bool:
    '''
    if string is palindrome return True, else return False
    '''
    return string == string[::-1]


# all possible slice 'b ba ban bana banan banana a an ana ...'

# nested loop find all possible slice
def all_Possible(string :str ) -> list:
    loop = []
    
    for i in range(len(string)):
        for j in range(i+1,len(string)+1):
            loop.append(string[i:j])
    
    return loop
string = 'abba'

lst = all_Possible(string)

newLst = list(filter(ifPal, lst))

numlst = []

for i in newLst:
    numlst.append(len(i))

print(max(numlst))

'''

hw:
CCC2016 J4 Problem J4: Arrival Time
https://www.cemc.uwaterloo.ca/contests/computing/past_ccc_contests/2016/stage%201/juniorEn.pdf

'''


