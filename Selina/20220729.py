lst = [1,2,3,4,5,6,7,8,9,10]# -> [2,4,6,8,10,12,,14,16,18,20]

'''
#index 0 1 2 3 4 5 6 7 8 9

# lst[0] = lst[0] * 2 # update lst

length = len(lst)

# print(length)

for i in range(0,10):

    lst[i] = lst[i] * 2


lst[0] = lst[0] * 2
lst[1] = lst[1] * 2
lst[2] = lst[2] * 2
lst[3] = lst[3] * 2


print(lst)
'''

#filter(function, lst)
#map（function,lst)
print(lst)

# lst = list(map(lambda i: i ** 2,lst))
#use normal function to implement map

def normalFunction(i):
    return i * 2

lst = list(map(normalFunction,lst))
print(lst)

'''
homework:

lst = [10,30,50,60,80]

1. use for loop to print each index of lst

2. use index to update lst to [100,300,500,600, 800]

3. Write a Python program to triple all numbers of a given list of integers. Use Python map, use lambda

4. Write a Python program to triple all numbers of a given list of integers. Use Python map, use normal function

'''