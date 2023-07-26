'''
QtS=int(input())
QtM=int(input())
QtL=int(input())

Qtot=(QtS*1+QtM*2+QtL*3)

if Qtot >= 10:
    print('happy')
if Qtot < 10:
    print('sad')

#ctrl + shift + ~


#pascal code
b = int(input())
p = 5 * b - 400
print(p)
if p  < 100:
    print(1)
elif p == 100:
    print(0)
else:
    print(-1)

boil=int(input())
boilatlevel=((boil*5)-400)
print(boilatlevel)
if boil == boilatlevel:
    print('1')
if boil > boilatlevel:
    print('0')
if boil < boilatlevel:
    print('-1')
'''

# item stored in dictionary is  key value pair
# dic = {'Ahmed': 300,'Suzanne': 500,'Ivona':450}

#

dic = {}

num = int(input())

# for i in range(num):
#     pass
# let loop run num times
# store all key value pair into dic
for _ in range(num):
    key = input()
    value = int(input())
    dic[key] = value

# get list includes all key
 # list(dict_keys([...])) means convert dict_keys([...]) to normallist
keylist = list(dic.keys())

# get list inclue all values
valuelist = list(dic.values())

# get the biggest value of valuelst and also gets its index
maxValue = max(valuelist)

# list.index(value) # find value's index of list
maxValueIndex = valuelist.index(maxValue)
print(keylist[maxValueIndex])

'''
hw
1.
# do your own version of CCC J2 problem of CCC 2021
# https://www.cemc.uwaterloo.ca/contests/computing/past_ccc_contests/2021/ccc/juniorEF.pdf

2.
testDic = {'English':90,'Math': 95,'Python': 89,'Gym':99 }
# using testDic to get which course get max scores and which course get min scores
# hint : max(list) to get highest value of list
#        min(list) to get lowest value of list

3. do J2 of CCC J2 problem of CCC 2019
#https://www.cemc.uwaterloo.ca/contests/computing/past_ccc_contests/2019/stage%201/juniorEF.pdf
'''



