'''
*
* *
* * *
'''
# i is row indicators
# j how to print i i each Row
# for i in range(1,4):
#     for j in range(i):
#         print("*", end =' ')
#     print()


'''
* * *
* *
*
'''
# i is row indicators
# j how to print in each Row
# for i in range(3,0,-1):

#     for j in range(1,i+1):
#         print("*", end =' ')

#     print()

'''
*
* *
* * *
* *
*
'''

# for i in range(1,6):

#     if i < 4:

#         for j in range(i):

#             if i < 4:
#                 print("*", end =' ')
#         print()

#     if i >= 4:

#         print((6-i) * '* ' )

'''
1
2 2
3 3 3
4 4 4 4
5 5 5 5 5
'''



'''
1
3 3
5 5 5
7 7 7 7
9 9 9 9 9
'''
for i in range(1,6,1):
    for j in range(i):
        print(i * 2 - 1, end = ' ')
    print()

'''
1
2 1
3 2 1
4 3 2 1
5 4 3 2 1
'''
        
    

