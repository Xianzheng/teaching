string = 'ABCDE'
lst = list(string)

print(lst)

popLastElement = lst.pop()

lst.insert(0,popLastElement)

string1 = ''.join(lst)
print(string1)

bigString = 'ADFADSASDFEABCDDASFA'

if string1 in bigString:
    print('yes')
else:
    print('no')


