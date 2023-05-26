'''
sample_set = {"Yellow", "Green", "Black"}


sample_list = ["Blue", "Green", "Red"]


##we can not use index to access the set, since it is unorder, it does not have a certain order you can not use index
#we can use index to access the list

# output
# {'Green', 'Yellow', 'Black', 'Red', 'Blue'}

finalset = set() # create a empty set

# we put all elements of sample_set and sample_list to final_set we can get ouput

for i in sample_set:
    finalset.add(i)
for i in sample_list:
    finalset.add(i)

print(finalset)

# finally -> try
try:
    print(10 * '10')
except:
    print('it has some error')
finally:
    print('ok')

#continue

for i in range(10):
    if i == 8 or i == 4:
        continue
    print(i)



set1 = {10, 20, 30, 40, 50}
set2 = {30, 40, 50, 60, 70}

#{70, 40, 10, 50, 20, 60, 30}

print( set1 | set2)


set1 = {1,2,3}
set2 = {3,4,5}

result1 = set1.intersection(set2)

reuslt2 = set1 & set2

sc = {'M','S','P'}

se = {'P','E','F'}

print(sc & se) # intersection

print(sc | se) # union

print(sc - se) # only in sc

print(se - sc) # only in se
'''

#Add set add 5 more your favirate fruits, Remove Two fruit,show your code
fruits = {'banana', 'avocado', 'strawberry', 'pear', 'coconut', 'cherry', 'apple', 'orange'}

# none indicated parameter, make function powerful and robustic
def removefromset(*a):
    for i in a:
        if i in fruits:
            fruits.remove(i)
    # fruits.remove(re1)
    # fruits.remove(re2)
    # fruits.remove(re3)
    
removefromset('banana','apple','avacade')
print(fruits)


