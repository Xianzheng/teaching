'''
def test(**kargs)
'''
{
    'chinese':98,
    'math':99,
    'english':100
}
# sorted is a build-in function, sorted(**kargs, key=None,reverse=False)
def test(**kargs):
    print(kargs,'this is a dictionary')
    # item = kargs.items()
    # print(list(item))
    print(sorted(kargs,key=lambda x: kargs[x],reverse=True))

lst = [1,2,3,4,5]
# even, odd
print(list(filter(lambda x: x % 2 == 0,lst)))

# lst1 = []
# for item in lst:

#     if item % 2 == 0:

#         lst1.append(item)

# print(lst1)

# lst1 = [2,4,6,8] # [4,8,12,16]

# print(list(map(lambda x: x * 2, lst1)))

a = lambda x, y : x + y 


b = lambda x: print(x)

#map, list are build in function
#map(function,  iterable)
#python set, list, string

lst = [4,2,5,7]

def func(x):
    
    return x ** 2

print(list(map(func,lst)))

print(list(map(lambda x: x ** 2,lst)))

# lamda function is only for the single logic


# do practice(you can choose any way)
# filter, map, lambda

lst [2,5,7,10,45,56,34,56]

# find all odd elements in lst

# power 2 for each element in lst

# we have a dictionary, sorted dictionary by key, sorted dictionary by value

#(better try to use lamda)
{
    'math':10,
    'enlish':9,
    'python':11,
    'gym': 12

}
