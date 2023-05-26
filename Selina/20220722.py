# function
def add(a,b):
    return a + b

print(add(3,5))

#anonymous function

# lambda
lf = lambda a,b:a + b


lf1 = lambda a,b:a * b # lambda is anonymous function

#filter(function,iterable)

lst = [1,2,3,4,5,6,7,8,9,10]

for i in lst:
    if i % 2 != 0:
        print(i)

print(list(filter(lambda i: i % 2 != 0, lst)))

'''
homework:
 write normal function minus 5 - 2 = 3 
 write normal function divides 4 / 2 = 2.0 
 write anonymous minus 5 - 2 = 3 
 write anonymous  function divides 4 / 2 = 2.0
 lst = [0,1,2,3,4,5,6,7,8]
 use filter to get all number which is in even index
'''

