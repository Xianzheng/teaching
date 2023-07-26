'''
dic = {
    'math':10,
    'enlish':9,
    'python':11,
    'gym': 12
}
# print(dic)
# which course have best scores
# 1. we want to sort this dictionaray, 
# 2.how to sort,
#   a.sorted by value, after sorted, result will be{'gym': 12,'python':11,'math':10, 'enlish':9,}
#   b sorted by key,   after sorted,  result be {'enlish':9,'gym': 12,'math':10,'python':11,}
# sorted by the key
# print(sorted(dic.items()))

# sorted by value
# result = list(sorted(dic.items(),key= lambda x : x[1]))
# print(result[-1][0])

print(dic.values()) # convert class dict_values to class list

lst = list(dic.values())

print(lst)

#max(lst) :max find the most biggest value of list

#lst.index(vale)# find a special value's index
biggest = max(lst)
print(biggest)
index = lst.index(biggest)

print(index)

print(list(dic.keys())[index])



string = 'abcd'
#         0123

print(string[3])
print(type(string))

lst= ['a','b','c','d']
print(lst[3])
print(type(lst))

tup = ('a','b','c','d')
print(tup[3])
print(type(tup))

# code a
print(list(filter(lambda x : x,tup)))

# code b
lst = []
for i in tup:
    lst.append(i)
print(lst)

# code a and code b in funactionality is same, but in speedy, code a is more quickly and shorter

lst = [(1,2,3),(1,3,2),(3,1,2)]

print(sorted(lst,key = lambda x: x[2]))

# result = []
# for i in lst:
#     result.append(i[0])
# print(result)
'''


tupl = [(1,2,3), (4,5,6), (7,8,9), (10,11,12)]


a = lambda x : x[0] 

print(a(tupl))


'''
homework:

Write a Python program to create a function that takes one argument, and that argument will be multiplied with an unknown given number.
Sample Output:
Double the number of 15 = 30
Triple the number of 15 = 45
Quadruple the number of 15 = 60
Quintuple the number 15 = 75

 Write a Python program to sort a list of tuples using Lambda.
Original list of tuples:
[('English', 88), ('Science', 90), ('Maths', 97), ('Social sciences', 82)]
Sorting the List of Tuples:
[('Social sciences', 82), ('English', 88), ('Science', 90), ('Maths', 97)]

Write a Python program to sort a list of dictionaries using Lambda.
Original list of dictionaries :
[{'make': 'Nokia', 'model': 216, 'color': 'Black'}, {'make': 'Mi Max', 'model': '2', 'color': 'Gold'}, {'make': 'Samsung', 'model': 7, 'color': 'Blue'}]
Sorting the List of dictionaries :
[{'make': 'Nokia', 'model': 216, 'color': 'Black'}, {'make': 'Samsung', 'model': 7, 'color': 'Blue'}, {'make': 'Mi Max', 'model': '2', 'color': 'Gold'}]

Write a Python program to square and cube every number in a given list of integers using Lambda.
Original list of integers:
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
Square every number of the said list:
[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
Cube every number of the said list:
[1, 8, 27, 64, 125, 216, 343, 512, 729, 1000]


'''