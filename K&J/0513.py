#filter(func, sequence)
#
#map(func,sequence)

# dic = {'name1':'Mark','name2':'Kevin','name3':'Sindy','name4':'Selina','name5':'Ella'}
# a=0
# a=list(filter(lambda x: x if x!= 'name3' else a+1,lst))
# print(a)

# dic = {0:'m',1:'a',2:'r',3:'k'}
#
#
#
# print(dict(filter(lambda val:val[0] != 3, dic.items())))

'''

dic = {'name1':'Mark','name2':'Kevin','name3':'Sindy','name4':'Selina','name5':'Ella'}
#[('name1', 'Mark'), ('name2', 'Kevin'), ('name3', 'Sindy'), ('name4', 'Selina'), ('name5', 'Ella')]

f = filter(lambda item: item[1] != 'Ella', dic.items())

print(dict(f))

dic = {'name1':'Mark','name2':'Kevin','name3':'Sindy','name4':'Selina','name5':'Ella'}
print(dic.items())
for i in dic.items():
    print(i[1])

'''
# string , list, dictionary, set, tuple

t = ('name1', 'Mark')

print(type(t))

print(t[0])

print(t[1])


dic = {0:1,1:2,2:3,3:4,4:5,5:

# filter all value which is even number

# filter all key which is even number