'''
# lambda function

a = lambda : print('Hello World')# no argument

f1 = lambda a, b: a + b# get arguments

# filter(function, iterable)# two arguments, one is function, other is iterable

lst = [45,78,23,56,90,24]

filterobj = filter(lambda num: num % 2 == 0, lst)

print(list(filterobj))


def f1(num):
    return num % 2 == 0 # compare sign will get a boolean valye

# f1 = lambda num: num % 2 == 0

lst = [45,78,23,56,90,24]


result = filter(f1,lst)

print(list(result))


string = '93675321'

def f2(a):
    numberA = int(a)
    return numberA % 2 != 0

lst = list(filter(f2, string))
print(''.join(lst)) # convert list to string
'''

# homework
lst = list(range(1,51))

print(lst)
# use filter function to get all even number in lst
# get sum of all even number





