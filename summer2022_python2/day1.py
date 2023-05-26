# invoke command line: ctrl + shift + ~
# save : ctrl + s

print('Hello world this is day1')

# print 1 to 10 use while loop

# i = 0

# while i < 10:
    
#     i += 1
#     print(i)

# print 1 3 5 7 9 use for loop

# for i in range(1,10,2):
#     print(i)

# string

string1 = '12345678'
# use python to detect whether 'a' is in string1
# flage = 0

# for i in string1:
#     if i == 'a':
#         flage = 1

# if flage == 1:
#     print('yes')
# else:
#     print('no')

# if string1.find('a') != -1:
#     print('yes')
# else:
#     print('no')

lst = [] # add 'apple' 'banana' 'cherry' to lst

lst.append('apple')
lst.append('banana')
lst.append('cherry')

for i in range(10):
    head = lst.pop(0)
    lst.append(head)
    print(lst)

#dictionary, set , tuple