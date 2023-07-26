'''
# LIST []
lst = []
print(type(lst))
print(lst)
# lst.append('something') add something to the tail of lst
lst.append('pen')
lst.append('pencil')
lst.append('apple')
lst.append('banana')

print(lst)

# how to remove app, pop(index)
lst.pop(0) # we will remove pen from list
print(lst)

lst.pop(0) # we will remove pencil
print(lst)

# add cherry and pear in list
lst.append('cherry')
lst.append('pear')
print(lst)

# change position for banana and cherry
#first way
lst[1],lst[2] = lst[2],lst[1]
print(lst)

#change apple to pineapple, update content for list
lst[0] = 'pineapple'
print(lst)
'''
# implements circular flow
lst = ['a','b','c','d']
print(*lst)
# index 0   1   2   3
for _ in range(5):
    #we want the loop run 5 times
    popItem = lst.pop(3)
    # print(popItem)
    #          where what
    lst.insert(0,popItem)
    print(* lst)

'''
create a lst put what ever you like
 - show me how to append
 - show me how to remove
 - show me how to do swap
 - show me how to do update
 - show me how to do insert
 '''



# index always start from 0, index of third item is 2
# print(lst[2])
#
# print(lst[3])

# tuple = ('apple','banana')
# print(tuple,type(tuple))

# print((1 + 2) * 4)