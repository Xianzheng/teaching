dic = {
    'AA':'AB',
    'AB':'BB',
    'B':'AA'
}

def nextLevel(str):
    lst = []
    for i in range(len(str)):
        for j in range(0,max+1):
            if i + j <= len(str):

                lst.append(change(str,str[i:i+j],i,i+j))

    return [i for i in lst if i]

def change(str,str1,s,t):
    if str1 in dic:
        new = makeChange(str,dic[str1],s,t)
        return new

def makeChange(str,str1,s,t):
    lst = list(str)
    lst[s:t] = str1
    return ''.join(lst)


max = 0
for i in dic:
    if max < len(i):
        max = len(i)

start = 'BB' # -> BB , AAA
print(nextLevel(start))

