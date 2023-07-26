'''
Sample Input 1
3
Ahmed
300
Suzanne
500
Ivona
450
Output for Sample Input 1
Suzanne
'''

# dic  = {'Ahmed':300,'Suzanne':500,'Ivona':400}
num = int(input())
# dynamically make dictionary
dic = {}
for _ in range(num):
    key = input()
    value = int(input())
    dic[key] = value

#retrieve
'''
for key in dic:
    print(key)
    print(dic[key])
'''

keylst = list(dic.keys()) # every key makes a list
valuelst = list(dic.values()) # every value makes a list

# find the biggest value of value list
mostBiggestValueForValuelst = max(valuelst)

# print(mostBiggestValueForValuelst )
# find the index of biggest value of value list
index = valuelst.index(mostBiggestValueForValuelst)

# find the key has the biggest value
print(keylst[index])

'''
hw:
testDic = {
    'English': 90,
    'French': 95,
    'Gym': 89,
    'python': 85
}

# use testDic to get which course you get ths highest score,
# use testDic to get which course you get ths lowest score,

max(lst): to get the max value
min(lst): to get the min value
'''

num = int(input())
name = ''
bid = 0
for _ in range(num):
    key = input()
    value = int(input())
    # if name == '' is the fist time input
    if name == '':
        name = key
        bid = value

    else:

       if value > bid:
           bid = value
           name = key

print(name)




