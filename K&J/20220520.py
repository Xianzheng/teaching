dic = {'name1':'Mark','name2':'Lea','name3':'Selina','name4':'Kevin'}

a=dict(filter(lambda x:x[0]=='name1' or x[0]== 'name4',dic.items()))

lst = list(dic.items())

print(type(lst[0]))

# Number

# build-in data structure
# String '', "" -> str
# lst: [] -> list
# dic: {} -> dict
# s: {'a',}, set() -> set
# t: ('a',) -> tuple

# s = set()
# print(type(s))
#
# t = ()
# print(type(t))

# string is immutable(not changeable), read-only

string = 'Mark' #'k' -> 'c'

# string[3] = 'c'
print(string[2])

# lst is mutable(it can be change),CRUD

# 'c' -> 'create'
# 'r' -> 'read'
# ’u‘ -> 'update'
# 'd' -> 'delete'

# lst = ['M' , 'a', 'r', 'k']
#
# lst[3] = 'k'
#
# print(lst)

#tuple # it is immutabable, it looks like lst

t = ('Mark','Kevin','Justin')

def math(a,b):
    return a + b, a - b, a * b, a / b




string1 = 'a'
string2 = 'b'
print(string1 + string2)

tuple1 = ('a',)
tuple2 = ('b',)
print(tuple1 + tuple2)
