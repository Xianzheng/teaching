'''
Write a Python program to sort a list of dictionaries using Lambda.
Original list of dictionaries :
[{'make': 'Nokia', 'model': 216, 'color': 'Black'}, {'make': 'Mi Max', 'model': '2', 'color': 'Gold'}, {'make': 'Samsung', 'model': 7, 'color': 'Blue'}]
Sorting the List of dictionaries :
[{'make': 'Nokia', 'model': 216, 'color': 'Black'}, {'make': 'Samsung', 'model': 7, 'color': 'Blue'}, {'make': 'Mi Max', 'model': 2, 'color': 'Gold'}]

# 【】list, {'key1':value1}dictionary,{'a','b'} set

lst = [{'make': 'Nokia', 'model': 216, 'color': 'Black'}, {'make': 'Mi Max', 'model': 2, 'color': 'Gold'}, {'make': 'Samsung', 'model': 7, 'color': 'Blue'}]

result = sorted(lst,key = lambda dic: dic['model'],reverse=True)
print(result)


# def f(a, b,c=False):
#     if c == False:
#         return None
#     else:
#         return a + b
    
# print(f(1,2,c=True))

'''

'''
(Sample1)
Input:
3
10
20
30

Output
60

(Sample2)
Input:
4
2
3
4
5

Output:
24

'''
inp = input()

#input() will give us a string
# print('input is',inp, type(inp))
lst = inp.split()
print(lst)

print(list(map(int,lst))) # change each element from list to int
#input 10 15 13 15 16
# get each specific number from string


'''
1.
redo question:
Write a Python program to sort a list of dictionaries using Lambda.
Original list of dictionaries :
[{'make': 'Nokia', 'model': 216, 'color': 'Black'}, {'make': 'Mi Max', 'model': '2', 'color': 'Gold'}, {'make': 'Samsung', 'model': 7, 'color': 'Blue'}]
Sorting the List of dictionaries :
[{'make': 'Nokia', 'model': 216, 'color': 'Black'}, {'make': 'Samsung', 'model': 7, 'color': 'Blue'}, {'make': 'Mi Max', 'model': 2, 'color': 'Gold'}]

2. get sum of number in string

input1: 12,34,56,67,89(hint split(','))
input2: 1/2/3/4/5(hint split('/'))
input3: 2 3 4 5 6(hint split( ))

3 CCC question: (do 2019 J2)
Junior 2:
link: https://www.cemc.uwaterloo.ca/contests/computing/past_ccc_contests/2019/stage%201/juniorEF.pdf
'''


