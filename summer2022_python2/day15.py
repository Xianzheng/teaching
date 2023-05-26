dic = {}

value = 1
dic['key'] = value

dic = {'Mark':89,'Kevin':100,'Jack':75,'RuoShi':100}

# dictmp = sorted(dic.items(),key  = lambda x:x[1])

lst1 = (list(dic.keys()))

lst = (list(dic.values()))


# lst = [4,4,1,2,5,5,3,2]

maxNum = 0
maxIndex = 0
for i in range(len(lst)):

    if maxNum < lst[i]:

        maxNum = lst[i]

        maxIndex = i


print(lst1[maxIndex])
print(maxNum)

'''
4
Mark
89
Kevin
100
Jack
75
RuoShi
100

RuoShi
100
'''