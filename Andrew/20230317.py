# we can only use break in loop
#break continue

# for i in range(1,11):
#
#     if i == 5:
#
#
#     print(i)


# find max value

# print(max([4,1,3,7,3]))

dic = {
    'apple' : 5,
    'banana': 6,
    'cherry' : 12,
    'pear': 1
}

m = 0
# for dictionary we use key to get value
# for i in dic:
#     print('each key is ',i)
#     print('each key is ', dic[i])
#
#     if dic[i] > m:
#
#         m = dic[i]
#
# for i in dic:
#
#     if dic[i] == m:
#         print('most expensive fruit is', i, 'value is', dic[i])
#         print('most expensive fruit is {} value is {}'.format(i, str(dic[i])))

'''
keylist = list(dic.keys())
valuelist = list(dic.values())
maxvalue = max(valuelist)
maxvalue_index = valuelist.index(maxvalue)
print(keylist)
print()
print(valuelist)
print()
# print(maxvalue)
# print(maxvalue_index )
print('most expensive fruit is {} value is {}'.format(keylist[maxvalue_index],maxvalue))
'''

lst = [3,6,9,4]
#      0 1 2 3

m = max(lst)
print(m)

print(lst.index(m))